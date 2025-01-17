from aws_cdk import core as cdk
from enterprise_sso.enterprise_aws_sso_stack import EnterpriseAwsSsoExecStack


class EnterpriseAwsSsoExecStage(cdk.Stage):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        enterprise_aws_sso_exec = EnterpriseAwsSsoExecStack(self, "EnterpriseAWSSSOExec")
