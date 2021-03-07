.PHONY: all
.DEFAULT_GOAL := help

# ----------------------------------------------------------------------------
# Local Variables
#
# ============================================================================

PROJECT=marina
DOCKER_REGISTRY=965067289393.dkr.ecr.us-west-2.amazonaws.com

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "⚡ \033[34m%-30s\033[0m %s\n", $$1, $$2}'

# ----------------------------------------------------------------------------
# OPTIONAL Commands (helper calls, unrelated to terraform)
#
# ============================================================================

randpass: ## Generate random password
	openssl rand -base64 16

django_security_key: ## Generate django security key
	python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

whoami: ## IAM Who Am I?
	aws sts get-caller-identity

# ----------------------------------------------------------------------------
# ECR/Docker Helper Commands
	# VERSION=v1.0.0 make build_app_image
#
# ============================================================================

ecr_login: ## Login to ECR Docker Registry
	aws ecr get-login-password | docker login -u AWS --password-stdin https://${DOCKER_REGISTRY}

build_app_image: ecr_login ## Build app image and store it in ECR
	docker build --network=host -t ${PROJECT}:latest --build-arg ENVIRONMENT=development -f .devops/docker/webapp/Dockerfile .
	docker tag ${PROJECT}:latest ${DOCKER_REGISTRY}/saritasa/devops/tools/${PROJECT}:${VERSION}
	docker tag ${PROJECT}:${VERSION} ${DOCKER_REGISTRY}/saritasa/devops/tools/${PROJECT}:${VERSION}
	docker push ${DOCKER_REGISTRY}/saritasa/devops/tools/${PROJECT}

build_ecr: ecr_login build_app_image  ## Build both base and app images and store them in ECR
