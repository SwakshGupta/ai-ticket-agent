The Problem: Engineering and customer success teams waste countless hours triaging vague bug reports and support tickets. 
When a ticket arrives, a human engineer must manually read it, check the user's account status or environment via an API, 
search internal documentation for known issues, and search the web for external error codes. 
This manual context-gathering creates a massive bottleneck and delays time-to-resolution.

The Solution: An AI Agent built with a ReAct (Reasoning and Acting) workflow that automatically handles Level 1 triage. 
The agent will ingest a new ticket, autonomously use external tools (mock APIs) to gather user context, 
query an internal RAG pipeline (Vector DB) for known runbooks, and fall back to web search if needed. 
Finally, it will synthesize this data into a structured root-cause assessment and draft a response for human approval.
