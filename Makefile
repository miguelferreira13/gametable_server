IMAGE=game_table
PROJECT=game-table-379523

build:
	docker build -t game_table .

run-dev: build
	docker run -p 8080:8080 \
		-it --rm game_table

run-dev-nc:
	python setup.py

deploy:
	 gcloud builds submit --tag gcr.io/${PROJECT}/${IMAGE}
	 gcloud run deploy gametable --image gcr.io/${PROJECT}/${IMAGE} --region europe-west4 --platform managed