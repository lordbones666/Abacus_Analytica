# Replay Procedure

1. Load `forecast_ledger.jsonl` and locate record by `question_id` and `as_of`.
2. Pull `evidence_ids` from forecast row.
3. Load evidence rows matching those IDs.
4. Verify config versions from forecast row.
5. Recompute update and compare probability equality.
