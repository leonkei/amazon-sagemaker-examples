# S3 prefix
from sagemaker import get_execution_role
import pandas as pd
import numpy as np
import os
import re
import boto3
prefix = "sagemaker-images-test"

# Define IAM role


role = get_execution_role()
