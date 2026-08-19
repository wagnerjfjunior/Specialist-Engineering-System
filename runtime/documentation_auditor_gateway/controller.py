from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple

class EnforcementError(RuntimeError): pass
class State(str, Enum):
    TASK_RECEIVED='TASK_RECEIVED'; TARGET_CLASSIFIED='TARGET_CLASSIFIED'; TARGET_ENTRY_VALIDATED='TARGET_ENTRY_VALIDATED'; PROJECT_IDENTIFIERS_RESOLVED='PROJECT_IDENTIFIERS_RESOLVED'; TRUSTED_EVIDENCE_BOUND='TRUSTED_EVIDENCE_BOUND'; READINESS_VALIDATED='READINESS_VALIDATED'; SUBSTANTIVE_ANALYSIS_ALLOWED='SUBSTANTIVE_ANALYSIS_ALLOWED'; OUTPUT_SCOPE_VALIDATED='OUTPUT_SCOPE_VALIDATED'; OUTPUT_RELEASED='OUTPUT_RELEASED'; FAIL_CLOSED_TARGET='FAIL_CLOSED_TARGET'; FAIL_CLOSED_PROJECT='FAIL_CLOSED_PROJECT'; FAIL_CLOSED_ENUMERATION='FAIL_CLOSED_ENUMERATION'; FAIL_CLOSED_READINESS='FAIL_CLOSED_READINESS'; FAIL_CLOSED_EFFECTIVE_SCOPE='FAIL_CLOSED_EFFECTIVE_SCOPE'
class TargetClass(str, Enum):
    AMBIGUOUS='AMBIGUOUS'; SES_SELF='SES_SELF'; CONSUMER_PROJECT='CONSUMER_PROJECT'; MULTI_PROJECT='MULTI_PROJECT'; INFORMATIONAL_PROJECT_LIST='INFORMATIONAL_PROJECT_LIST'
class ContextStatus(str, Enum): READY='READY'; LIMITED='LIMITED'; BLOCKED='BLOCKED'
REQUIRED_READINESS_FIELDS=(
'PROOF_LEVEL','TASK_SCOPE','EFFECTIVE_SCOPE','TARGET_REF_OR_OBJECT','ENVIRONMENT','SES_CANONICAL_MAIN_REF','SES_CANDIDATE_REF','SES_EFFECTIVE_REF','SES_ARCHETYPE_RESOLUTION_STATUS','SES_ARCHETYPE_ID','SES_ARCHETYPE_SOURCE_REF','PROJECT_RESOLUTION_STATUS','PROJECT_ID','PROJECT_ADAPTER_STATUS','PROJECT_ADAPTER_REF','CANONICAL_PROJECT_SOURCE','PROJECT_LIVE_REF','PROJECT_BOOTSTRAP_STATUS','PROJECT_BOOTSTRAP_REF','SPECIALIST_RESOLUTION_STATUS','SPECIALIST_SOURCE_REF','PROJECT_CONTINUITY_STATUS','PROJECT_CONTINUITY_REF','MATERIAL_EVIDENCE_STATUS','AUTHORITY_MODEL_STATUS','MUTATION_AUTHORIZATION_STATUS','CONTEXT_STATUS','RECEIPT_VALIDITY','GAPS')
EVIDENCE_BOUND_FIELDS=('SES_CANONICAL_MAIN_REF','SES_EFFECTIVE_REF','SES_ARCHETYPE_ID','SES_ARCHETYPE_SOURCE_REF','PROJECT_RESOLUTION_STATUS','PROJECT_ID','PROJECT_ADAPTER_STATUS','PROJECT_ADAPTER_REF','CANONICAL_PROJECT_SOURCE','PROJECT_LIVE_REF','PROJECT_BOOTSTRAP_STATUS','PROJECT_BOOTSTRAP_REF','SPECIALIST_RESOLUTION_STATUS','SPECIALIST_SOURCE_REF','PROJECT_CONTINUITY_STATUS','PROJECT_CONTINUITY_REF','MATERIAL_EVIDENCE_STATUS','AUTHORITY_MODEL_STATUS')

@dataclass(frozen=True)
class ScopeGraph:
    units:frozenset[str]
    def require_nonempty(self):
        if not self.units: raise EnforcementError('TASK_SCOPE_EMPTY')
@dataclass(frozen=True)
class TrustedEvidenceHandle:
    evidence_id:str; field:str; value:str; authority_status:str; source_locator:str; resolved_ref:str; coverage:str='INTEGRAL_READ'; freshness:str='CURRENT'
    def attest(self, field, value): return self.field==field and self.value==value and self.authority_status=='TRUSTED' and self.coverage not in {'NOT_READ','RETRIEVAL_FAILED'} and self.freshness!='STALE'
@dataclass(frozen=True)
class ReadinessEnvelope:
    fields:Mapping[str,str]; task_scope:ScopeGraph; effective_scope:ScopeGraph; evidence_ids_by_field:Mapping[str,Tuple[str,...]]
    @property
    def status(self):
        try: return ContextStatus(self.fields['CONTEXT_STATUS'])
        except Exception as e: raise EnforcementError('CONTEXT_STATUS_INVALID') from e
@dataclass(frozen=True)
class Claim:
    claim_id:str; text:str; scope_units:frozenset[str]; evidence_ids:frozenset[str]
@dataclass(frozen=True)
class CandidateBundle:
    claims:Tuple[Claim,...]
    @property
    def digest(self):
        s='\n'.join(f'{c.claim_id}|{c.text}|{sorted(c.scope_units)}|{sorted(c.evidence_ids)}' for c in self.claims)
        return sha256(s.encode()).hexdigest()
@dataclass(frozen=True)
class TraceEvent:
    seq:int; state:State; action:str; accepted:bool; reason:str
@dataclass
class GatewayController:
    task_scope:ScopeGraph; target_class:TargetClass; explicit_project_ids:Tuple[str,...]=(); state:State=State.TASK_RECEIVED; trace:List[TraceEvent]=field(default_factory=list); evidence:Dict[str,TrustedEvidenceHandle]=field(default_factory=dict); readiness:Optional[ReadinessEnvelope]=None; authorized_digest:Optional[str]=None; project_resolution:Dict[str,str]=field(default_factory=dict)
    def __post_init__(self): self.task_scope.require_nonempty(); self._record(State.TASK_RECEIVED,'init',True,'task accepted')
    def _record(self,state,action,accepted,reason): self.trace.append(TraceEvent(len(self.trace)+1,state,action,accepted,reason)); self.state=state if accepted else self.state
    def classify_and_validate_target(self):
        self._record(State.TARGET_CLASSIFIED,'classify_target',True,self.target_class.value)
        if self.target_class is TargetClass.AMBIGUOUS: self._record(State.FAIL_CLOSED_TARGET,'validate_target',True,'clarification required'); return
        if self.target_class is TargetClass.INFORMATIONAL_PROJECT_LIST: self._record(State.TARGET_ENTRY_VALIDATED,'validate_target',True,'informational enumeration allowed'); return
        if self.target_class in {TargetClass.CONSUMER_PROJECT,TargetClass.MULTI_PROJECT} and not self.explicit_project_ids: self._record(State.FAIL_CLOSED_TARGET,'validate_target',True,'project identifier required'); return
        self._record(State.TARGET_ENTRY_VALIDATED,'validate_target',True,'target valid')
    def release_informational_project_list(self,projects:Sequence[str]):
        if self.target_class is not TargetClass.INFORMATIONAL_PROJECT_LIST: self._record(State.FAIL_CLOSED_ENUMERATION,'project_list',True,'unsolicited enumeration blocked'); raise EnforcementError('UNSOLICITED_PROJECT_ENUMERATION')
        if self.state is not State.TARGET_ENTRY_VALIDATED: raise EnforcementError('TARGET_ENTRY_NOT_VALIDATED')
        return tuple(projects)
    def bind_list_position_as_project(self,value:str,canonical:Set[str]):
        if value not in canonical: self._record(State.FAIL_CLOSED_ENUMERATION,'numeric_binding',True,'list position is not project identity'); raise EnforcementError('BARE_LIST_POSITION_NOT_PROJECT_IDENTIFIER')
        return value
    def resolve_projects(self,registry:Mapping[str,str]):
        if self.state is not State.TARGET_ENTRY_VALIDATED: raise EnforcementError('TARGET_ENTRY_NOT_VALIDATED')
        for supplied in self.explicit_project_ids:
            resolved=registry.get(supplied.casefold())
            if not resolved: self._record(State.FAIL_CLOSED_PROJECT,'resolve_project',True,f'{supplied}:PROJECT_NOT_REGISTERED'); raise EnforcementError('PROJECT_NOT_REGISTERED')
            self.project_resolution[supplied]=resolved
        self._record(State.PROJECT_IDENTIFIERS_RESOLVED,'resolve_project',True,'all explicit projects resolved')
    def bind_evidence(self,handles:Iterable[TrustedEvidenceHandle]):
        if self.state not in {State.PROJECT_IDENTIFIERS_RESOLVED,State.TARGET_ENTRY_VALIDATED}: raise EnforcementError('PROJECT_RESOLUTION_REQUIRED')
        for h in handles:
            if h.evidence_id in self.evidence: raise EnforcementError('DUPLICATE_EVIDENCE_ID')
            self.evidence[h.evidence_id]=h
        self._record(State.TRUSTED_EVIDENCE_BOUND,'bind_evidence',True,f'{len(self.evidence)} handles')
    def validate_readiness(self,e:ReadinessEnvelope):
        if self.state is not State.TRUSTED_EVIDENCE_BOUND: self._record(State.FAIL_CLOSED_READINESS,'validate_readiness',True,'trusted evidence not bound'); raise EnforcementError('TRUSTED_EVIDENCE_REQUIRED')
        missing=[f for f in REQUIRED_READINESS_FIELDS if not str(e.fields.get(f,'')).strip()]
        if missing: self._record(State.FAIL_CLOSED_READINESS,'validate_readiness',True,'missing fields:'+','.join(missing)); raise EnforcementError('READINESS_INCOMPLETE')
        if e.fields['TASK_SCOPE']!=','.join(sorted(e.task_scope.units)): raise EnforcementError('TASK_SCOPE_BINDING_MISMATCH')
        expected_effective=','.join(sorted(e.effective_scope.units)) if e.effective_scope.units else 'NONE'
        if e.fields['EFFECTIVE_SCOPE']!=expected_effective: raise EnforcementError('EFFECTIVE_SCOPE_BINDING_MISMATCH')
        st=e.status; task=e.task_scope.units; eff=e.effective_scope.units
        if not eff.issubset(task): self._record(State.FAIL_CLOSED_EFFECTIVE_SCOPE,'validate_scope',True,'scope laundering'); raise EnforcementError('EFFECTIVE_SCOPE_NOT_SUBSET')
        if st is ContextStatus.READY and eff!=task: raise EnforcementError('READY_REQUIRES_FULL_SCOPE')
        if st is ContextStatus.LIMITED and (not eff or eff==task): raise EnforcementError('LIMITED_REQUIRES_STRICT_SUBSET')
        if st is ContextStatus.LIMITED and e.fields['GAPS'] in {'NONE','NOT_APPLICABLE',''}: raise EnforcementError('LIMITED_REQUIRES_GAPS')
        if st is ContextStatus.BLOCKED and eff: raise EnforcementError('BLOCKED_REQUIRES_EMPTY_EFFECTIVE_SCOPE')
        proof=e.fields['PROOF_LEVEL']; cand=e.fields['SES_CANDIDATE_REF']; canon=e.fields['SES_CANONICAL_MAIN_REF']; eref=e.fields['SES_EFFECTIVE_REF']
        if proof=='ORDINARY_TASK_WORK' and (cand!='NOT_APPLICABLE' or eref!=canon): raise EnforcementError('SES_REF_RELATIONSHIP_INVALID')
        if proof=='CANDIDATE_HEAD_PROTOCOL_PROOF' and (cand in {'','NOT_APPLICABLE'} or eref!=cand): raise EnforcementError('SES_REF_RELATIONSHIP_INVALID')
        for name in EVIDENCE_BOUND_FIELDS:
            val=e.fields[name]; ids=e.evidence_ids_by_field.get(name,())
            if not ids: raise EnforcementError('EVIDENCE_BINDING_MISSING:'+name)
            if not any(i in self.evidence and self.evidence[i].attest(name,val) for i in ids): self._record(State.FAIL_CLOSED_READINESS,'attest_field',True,'unsupported:'+name); raise EnforcementError('READINESS_FIELD_UNSUPPORTED:'+name)
        self.readiness=e; self._record(State.READINESS_VALIDATED,'validate_readiness',True,st.value)
        if st is not ContextStatus.BLOCKED: self._record(State.SUBSTANTIVE_ANALYSIS_ALLOWED,'authorize_analysis',True,st.value)
    def validate_and_authorize_output(self,b:CandidateBundle):
        if self.state is not State.SUBSTANTIVE_ANALYSIS_ALLOWED or self.readiness is None: self._record(State.FAIL_CLOSED_READINESS,'release_attempt',True,'readiness not valid'); raise EnforcementError('SUBSTANTIVE_OUTPUT_BEFORE_VALID_READINESS')
        allowed=self.readiness.effective_scope.units
        for c in b.claims:
            if not c.scope_units or not c.scope_units.issubset(allowed): self._record(State.FAIL_CLOSED_EFFECTIVE_SCOPE,'validate_claim_scope',True,c.claim_id); raise EnforcementError('OUT_OF_EFFECTIVE_SCOPE_OUTPUT')
            if not c.evidence_ids: raise EnforcementError('CLAIM_WITHOUT_EVIDENCE')
            if any(i not in self.evidence for i in c.evidence_ids): raise EnforcementError('CLAIM_EVIDENCE_UNTRUSTED')
        self._record(State.OUTPUT_SCOPE_VALIDATED,'validate_output',True,'all claims in scope'); self.authorized_digest=b.digest; return b.digest
    def render_and_release(self,b:CandidateBundle):
        if self.state is not State.OUTPUT_SCOPE_VALIDATED: raise EnforcementError('OUTPUT_NOT_AUTHORIZED')
        if b.digest!=self.authorized_digest: raise EnforcementError('DIGEST_MISMATCH')
        out='\n'.join(f'[{c.claim_id}] {c.text}' for c in b.claims); self._record(State.OUTPUT_RELEASED,'release',True,b.digest); return out
    def assert_append_only_trace(self):
        if [e.seq for e in self.trace]!=list(range(1,len(self.trace)+1)): raise EnforcementError('TRACE_SEQUENCE_INVALID')
