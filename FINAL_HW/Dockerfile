FROM python:3.11-slim-bookworm@sha256:f06d01d4ba3f8ad5af45a3ec87df19c1d317d8e8961edc0fabda61811af6f7cf AS build
ARG SOURCE_DATE_EPOCH=1700000000
ENV SOURCE_DATE_EPOCH=$SOURCE_DATE_EPOCH PYTHONDONTWRITEBYTECODE=1 PIP_DISABLE_PIP_VERSION_CHECK=1
RUN pip install --no-cache-dir poetry==2.5.1 poetry-plugin-export==1.9.0
WORKDIR /build
COPY pyproject.toml poetry.lock README.md ./
RUN poetry export --only main --without-hashes -f requirements.txt -o requirements.txt     && pip wheel --no-cache-dir -r requirements.txt -w /wheels
COPY src/ src/
RUN poetry build -f wheel && cp dist/*.whl /wheels/

FROM python:3.11-slim-bookworm@sha256:f06d01d4ba3f8ad5af45a3ec87df19c1d317d8e8961edc0fabda61811af6f7cf
ARG SOURCE_DATE_EPOCH=1700000000
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 HOST=0.0.0.0 PORT=8080
COPY --from=build /wheels /wheels
RUN pip install --no-cache-dir --no-compile --no-index --no-deps /wheels/*.whl     && rm -rf /wheels     && groupadd -g 10001 audit     && useradd -u 10001 -g 10001 -M -s /usr/sbin/nologin audit
USER 10001:10001
EXPOSE 8080
CMD ["server"]
