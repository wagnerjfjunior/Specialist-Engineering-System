import unittest
from runtime.documentation_auditor_gateway.controller import *

def fields(status='READY',task=('audit',),effective=('audit',),gaps='NONE'):
    return {'PROOF_LEVEL':'ORDINARY_TASK_WORK','TASK_SCOPE':','.join(sorted(task)),'EFFECTIVE_SCOPE':(','.join(sorted(effective)) if effective else 'NONE'),'TARGET_REF_OR_OBJECT':'repo@sha','ENVIRONMENT':'github','SES_CANONICAL_MAIN_REF':'ses-main','SES_CANDIDATE_REF':'NOT_APPLICABLE','SES_EFFECTIVE_REF':'ses-main','SES_ARCHETYPE_RESOLUTION_STATUS':'RESOLVED_ACTIVE','SES_ARCHETYPE_ID':'documentation-auditor','SES_ARCHETYPE_SOURCE_REF':'archetype@sha','PROJECT_RESOLUTION_STATUS':'RESOLVED_UNIQUE_ACTIVE','PROJECT_ID':'fechai','PROJECT_ADAPTER_STATUS':'RESOLVED','PROJECT_ADAPTER_REF':'adapter@sha','CANONICAL_PROJECT_SOURCE':'owner/repo','PROJECT_LIVE_REF':'project-main','PROJECT_BOOTSTRAP_STATUS':'RESOLVED','PROJECT_BOOTSTRAP_REF':'bootstrap@sha','SPECIALIST_RESOLUTION_STATUS':'RESOLVED','SPECIALIST_SOURCE_REF':'specialist@sha','PROJECT_CONTINUITY_STATUS':'RESOLVED','PROJECT_CONTINUITY_REF':'handoff@sha','MATERIAL_EVIDENCE_STATUS':'SUFFICIENT','AUTHORITY_MODEL_STATUS':'RESOLVED_READ_ONLY','MUTATION_AUTHORIZATION_STATUS':'NOT_REQUESTED','CONTEXT_STATUS':status,'RECEIPT_VALIDITY':'VALID','GAPS':gaps}
def evidence(f):
    hs=[]; mp={}
    for n,name in enumerate(EVIDENCE_BOUND_FIELDS,1):
        eid=f'e{n}'; hs.append(TrustedEvidenceHandle(eid,name,f[name],'TRUSTED',f'source/{name}','ref')); mp[name]=(eid,)
    return hs,mp
class Tests(unittest.TestCase):
    def c(self,task=('audit',),target=TargetClass.CONSUMER_PROJECT,ids=('fechai',)):
        c=GatewayController(ScopeGraph(frozenset(task)),target,ids); c.classify_and_validate_target();
        if target in {TargetClass.CONSUMER_PROJECT,TargetClass.MULTI_PROJECT}: c.resolve_projects({'fechai':'fechai','blogs':'blogs-sites-portais-seo'})
        return c
    def ready(self,c,status='READY',task=('audit',),effective=('audit',),gaps='NONE'):
        f=fields(status,task,effective,gaps); hs,mp=evidence(f); c.bind_evidence(hs); e=ReadinessEnvelope(f,ScopeGraph(frozenset(task)),ScopeGraph(frozenset(effective)),mp); c.validate_readiness(e); return e
    def test_r03a_early_output_blocked(self):
        c=self.c()
        with self.assertRaisesRegex(EnforcementError,'SUBSTANTIVE_OUTPUT_BEFORE_VALID_READINESS'): c.validate_and_authorize_output(CandidateBundle((Claim('C1','early',frozenset({'audit'}),frozenset({'e1'})),)))
    def test_r05_zero_match_then_enumeration_blocked(self):
        c=GatewayController(ScopeGraph(frozenset({'audit'})),TargetClass.CONSUMER_PROJECT,('missing',)); c.classify_and_validate_target()
        with self.assertRaisesRegex(EnforcementError,'PROJECT_NOT_REGISTERED'): c.resolve_projects({'fechai':'fechai'})
        with self.assertRaisesRegex(EnforcementError,'UNSOLICITED_PROJECT_ENUMERATION'): c.release_informational_project_list(('fechai','blogs'))
    def test_list_then_bare_number_no_binding(self):
        c=GatewayController(ScopeGraph(frozenset({'list'})),TargetClass.INFORMATIONAL_PROJECT_LIST); c.classify_and_validate_target(); self.assertEqual(c.release_informational_project_list(('fechai','blogs')),('fechai','blogs'))
        with self.assertRaisesRegex(EnforcementError,'BARE_LIST_POSITION_NOT_PROJECT_IDENTIFIER'): c.bind_list_position_as_project('1',{'fechai','blogs'})
    def test_r06_incomplete_receipt_rejected(self):
        c=self.c(target=TargetClass.MULTI_PROJECT,ids=('fechai','blogs')); f=fields(); hs,mp=evidence(f); c.bind_evidence(hs); del f['PROJECT_CONTINUITY_REF']; e=ReadinessEnvelope(f,ScopeGraph(frozenset({'audit'})),ScopeGraph(frozenset({'audit'})),mp)
        with self.assertRaisesRegex(EnforcementError,'READINESS_INCOMPLETE'): c.validate_readiness(e)
    def test_unsupported_receipt_rejected(self):
        c=self.c(); f=fields(); hs,mp=evidence(f); c.bind_evidence(hs); f['PROJECT_LIVE_REF']='invented'; e=ReadinessEnvelope(f,ScopeGraph(frozenset({'audit'})),ScopeGraph(frozenset({'audit'})),mp)
        with self.assertRaisesRegex(EnforcementError,'READINESS_FIELD_UNSUPPORTED:PROJECT_LIVE_REF'): c.validate_readiness(e)
    def test_limited_strict_subset(self):
        c=self.c(task=('a','b')); self.ready(c,'LIMITED',('a','b'),('a',),'b missing'); self.assertEqual(c.readiness.status,ContextStatus.LIMITED)
    def test_blocked_no_output(self):
        c=self.c(); self.ready(c,'BLOCKED',('audit',),(), 'missing')
        with self.assertRaisesRegex(EnforcementError,'SUBSTANTIVE_OUTPUT_BEFORE_VALID_READINESS'): c.validate_and_authorize_output(CandidateBundle((Claim('C1','x',frozenset({'audit'}),frozenset({'e1'})),)))
    def test_out_of_scope_rejected(self):
        c=self.c(task=('a','b')); self.ready(c,'LIMITED',('a','b'),('a',),'b missing')
        with self.assertRaisesRegex(EnforcementError,'OUT_OF_EFFECTIVE_SCOPE_OUTPUT'): c.validate_and_authorize_output(CandidateBundle((Claim('C1','b',frozenset({'b'}),frozenset({'e1'})),)))
    def test_valid_digest_bound_release(self):
        c=self.c(); self.ready(c); b=CandidateBundle((Claim('C1','ok',frozenset({'audit'}),frozenset({'e1'})),)); self.assertEqual(c.validate_and_authorize_output(b),b.digest); self.assertIn('ok',c.render_and_release(b)); c.assert_append_only_trace()
    def test_digest_tamper_rejected(self):
        c=self.c(); self.ready(c); good=CandidateBundle((Claim('C1','ok',frozenset({'audit'}),frozenset({'e1'})),)); c.validate_and_authorize_output(good); bad=CandidateBundle((Claim('C1','tampered',frozenset({'audit'}),frozenset({'e1'})),))
        with self.assertRaisesRegex(EnforcementError,'DIGEST_MISMATCH'): c.render_and_release(bad)
if __name__=='__main__': unittest.main()
