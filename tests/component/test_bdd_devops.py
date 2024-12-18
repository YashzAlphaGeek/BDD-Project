from pytest_bdd import scenarios, given, when, then
from step_defs.devops_pipeline_steps import *

# Reference the feature file(s)
scenarios('features/devops_pipeline.feature')