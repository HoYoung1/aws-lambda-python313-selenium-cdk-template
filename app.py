#!/usr/bin/env python3
import aws_cdk as cdk
from dotenv import find_dotenv, dotenv_values
from scraper.stack import ScraperStack

config = dotenv_values(find_dotenv())
app = cdk.App()
ScraperStack(app, "SeleniumScraperTestApp",
             env=cdk.Environment(account=config['ACCOUNT_ID'],
                                 region=config['REGION']),
             )

app.synth()
