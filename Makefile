.PHONY: build-push-amd64

REPO ?= custom-health-app
VERSION ?= latest
HEALTH_CHECK_ENDPOINT ?= /health

run:
	docker run --rm -it -p 8080:8080 -e HEALTH_CHECK_ENDPOINT=$(HEALTH_CHECK_ENDPOINT) $(REPO):$(VERSION)

build:
	docker build -t $(REPO):$(VERSION) .

build-push-amd64:
	docker buildx build --platform linux/amd64 -t $(REPO):$(VERSION) . --push

build-push-arm64:
	docker buildx build --platform linux/arm64 -t $(REPO):$(VERSION) . --push
