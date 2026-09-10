# Week 03 Lab

Build an ingestion pipeline from a public API/dataset; handle errors and retries.

Starter files for this week's lab will be added here before the lab session
(pulled into your repo via `git fetch upstream && git merge upstream/main`,
as introduced in the Week 1 lab).

1. Whcih failure type was easiest/hardest to trigger and why?
Easiest: Timeout and HTTP 400 errors. Setting timeout=0.001 or LATITUDE=999 instantly forces predictable failure handling locally.  
Hardest: Connection Error. Simulating network failure requires changing DNS/hostnames or turning off network adapters, which is harder to mock cleanly without code changes.

2. How did exponential backoff change the timing between attempts? 
Delays doubled sequentially with each attempt (1s -> 2s -> 4s). This geometric increase gives network congestion or API rate limits time to recover without hammering the server repeatedly.

3. Why skip retries on HTTP 400 Bad Request?
An HTTP 400 error indicates a client-side syntax or validation error (e.g., invalid parameters like LATITUDE=999). It is non-transient, meaning identical subsequent requests will continuously fail. Retrying non-transient errors wastes client resources and contributes to thundering herd problems on API servers.

4. Data contract specifications for data/raw/ consumers
Schema: Define required top-level JSON keys (current, current_units, latitude, longitude).
Semantics: Specify precise units (°C, km/h, %) and timezone handling. 
SLA: Guarantee batch ingestion frequency and raw storage path structure
Change Management: Commit to semantic versioning for payload schema changes and deprecation notices before breaking key removals.

