#!/usr/bin/env python3
import anthropic
import json
from datetime import datetime

client = anthropic.Anthropic()

# Read batch requests from JSONL (as JSON objects, not binary file)
print("📤 Uploading comparison batch...")
requests = []
with open('batch-jobs/batch-job-comparison-20260210-222752.jsonl', 'r') as f:
    for line in f:
        requests.append(json.loads(line))

print(f"   Requests: {len(requests)}")

# Upload batch
batch = client.messages.batches.create(requests=requests)

print(f"✅ Batch uploaded!")
print(f"📋 Batch ID: {batch.id}")
print(f"📊 Status: {batch.processing_status}")

# Update tracking
with open('batch-jobs/batch-job-comparison-20260210-222752-tracking.json', 'r') as f:
    tracking = json.load(f)

tracking['batch_id'] = batch.id
tracking['uploaded_at'] = datetime.now().isoformat()
tracking['status'] = batch.processing_status

with open('batch-jobs/batch-job-comparison-20260210-222752-tracking.json', 'w') as f:
    json.dump(tracking, f, indent=2)

print(f"⏱️  Check status in 12-24 hours with: python scripts/check-batch-status.py")
print(f"\n✅ Done! Comparison test running.")
