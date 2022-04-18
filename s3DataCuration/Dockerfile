FROM public.ecr.aws/lambda/python:3.8

COPY app.py ${LAMBDA_TASK_ROOT}

RUN pip install numpy --target "${LAMBDA_TASK_ROOT}"
RUN pip install pandas --target "${LAMBDA_TASK_ROOT}"
RUN pip install shapely --target "${LAMBDA_TASK_ROOT}"


CMD ["app.handler"]
