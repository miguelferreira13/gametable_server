IMAGE=game_table
PROJECT=game-table-379523

deploy:
	 gcloud builds submit --tag gcr.io/${PROJECT}/${IMAGE}
	 gcloud run deploy gametable --image gcr.io/${PROJECT}/${IMAGE} --regio europe-west4 --platform managed