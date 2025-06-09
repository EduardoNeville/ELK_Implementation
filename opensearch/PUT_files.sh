curl -k -u admin:Respvblica.118 -X PUT "https://localhost:9200/_ingest/pipeline/pdf_pipeline" -H 'Content-Type: application/json' -d'
{
  "description": "Extract text from PDFs using the attachment processor",
  "processors": [
    {
      "attachment": {
        "field": "data",
        "target_field": "attachment"
      }
    },
    {
      "remove": {
        "field": "data"
      }
    }
  ]
}'
