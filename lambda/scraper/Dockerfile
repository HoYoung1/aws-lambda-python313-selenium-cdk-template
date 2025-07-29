FROM --platform=linux/amd64 public.ecr.aws/lambda/python@sha256:489d4abc8644060e2e16db2ffaaafa157359761feaf9438bf26ed88e37e43d9c as build
RUN yum install -y unzip && \
    curl -Lo "/tmp/chromedriver.zip" "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip" && \
    curl -Lo "/tmp/chrome-linux.zip" "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F1135561%2Fchrome-linux.zip?alt=media" && \
    unzip /tmp/chromedriver.zip -d /opt/ && \
    unzip /tmp/chrome-linux.zip -d /opt/

FROM --platform=linux/amd64 public.ecr.aws/lambda/python@sha256:489d4abc8644060e2e16db2ffaaafa157359761feaf9438bf26ed88e37e43d9c
RUN yum install libc6-compat atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel -y
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt
COPY --from=build /opt/chrome-linux /opt/chrome
COPY --from=build /opt/chromedriver /opt/
COPY lambda_function.py ${LAMBDA_TASK_ROOT}
CMD [ "lambda_function.handler" ]