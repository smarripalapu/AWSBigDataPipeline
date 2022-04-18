FROM amazon/aws-lambda-python:3.8

COPY app.py ${LAMBDA_TASK_ROOT}
COPY s3_access.py ${LAMBDA_TASK_ROOT}
COPY dynamoDB_accessor.py ${LAMBDA_TASK_ROOT}


RUN pip install pandas --target "${LAMBDA_TASK_ROOT}"



CMD ["app.handler"]
