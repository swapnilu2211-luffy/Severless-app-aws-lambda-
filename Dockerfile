# Use the official AWS base image for Python
FROM public.ecr.aws/lambda/python:3.9

# Copy your application code into the container
COPY app.py ${LAMBDA_TASK_ROOT}

# Tell the container which function to run
CMD [ "app.handler" ]
