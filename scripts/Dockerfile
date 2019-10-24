FROM python:3.6.6 as builder

# Install Pipenv
# --------------
# https://pip.pypa.io/en/stable/user_guide/#configuration
ARG PIP_NO_CACHE_DIR=0
ARG PIPENV_VERSION="2018.10.13"
RUN pip install pipenv==$PIPENV_VERSION

# Install python libs
# -------------------
WORKDIR /tmp/lib
COPY . .
RUN pipenv install --system  --deploy
RUN pip install .

# Multi-stage-build
# -----------------
# The docs for `ARG` warn against using them to pass build-time secrets, as
# their contents are visible in the final image using the `docker history` cmd.
# For now, we're mitigating the problems with `ARG`s by using a multi-stage build.
FROM python:3.6.6-slim

# Copy python dependencies
# ------------------------
COPY --from=builder /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=builder /usr/local/bin/scripts /usr/local/bin/scripts

# Set default cmd (unbuffered logs)
# ---------------------------------
# https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED=1
CMD ["/bin/bash"]
