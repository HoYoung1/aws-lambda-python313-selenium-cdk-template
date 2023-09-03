from aws_cdk import Duration, Stack, aws_lambda
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk.aws_events_targets import LambdaFunction
from constructs import Construct


class ScraperStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        scraper_function = aws_lambda.DockerImageFunction(
            scope=self,
            id="SeleniumScraperFunctionTest",
            code=aws_lambda.DockerImageCode.from_image_asset("lambda/scraper"),
            memory_size=2048,
            timeout=Duration.minutes(5),
        )

        # Add event to trigger Lambda
        rule = Rule(
            scope=self,
            id="SeleniumScraperScheduleRule",
            schedule=Schedule.cron(minute="0", hour="20")
        )
        rule.add_target(target=LambdaFunction(scraper_function))
