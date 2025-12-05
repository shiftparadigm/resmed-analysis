# Multi-Agent Analysis Setup

## Overview
This project is set up for parallel analysis using 4 agents working on separate chunks of the 32 ResMed sites.

## Directory Structure
```
data/chunks/
├── chunk_1_sites.csv      # Agent 1: Sites 1-8
├── chunk_1_urls.json
├── chunk_2_sites.csv      # Agent 2: Sites 9-16
├── chunk_2_urls.json
├── chunk_3_sites.csv      # Agent 3: Sites 17-24
├── chunk_3_urls.json
├── chunk_4_sites.csv      # Agent 4: Sites 25-32
└── chunk_4_urls.json
```

## Agent Assignments

### Agent 1 - Chunk 1 (Sites 1-8)
**Input**: `data/chunks/chunk_1_sites.csv` or `chunk_1_urls.json`
**Output**: `data/analysis/analysis_chunk_1.md`

### Agent 2 - Chunk 2 (Sites 9-16)
**Input**: `data/chunks/chunk_2_sites.csv` or `chunk_2_urls.json`
**Output**: `data/analysis/analysis_chunk_2.md`

### Agent 3 - Chunk 3 (Sites 17-24)
**Input**: `data/chunks/chunk_3_sites.csv` or `chunk_3_urls.json`
**Output**: `data/analysis/analysis_chunk_3.md`

### Agent 4 - Chunk 4 (Sites 25-32)
**Input**: `data/chunks/chunk_4_sites.csv` or `chunk_4_urls.json`
**Output**: `data/analysis/analysis_chunk_4.md`

## Task Instructions

Each agent should:
1. Read their assigned chunk file (`chunk_N_sites.csv` or `chunk_N_urls.json`)
2. Follow the instructions in [`AGENT_TASK_INSTRUCTIONS.md`](./AGENT_TASK_INSTRUCTIONS.md)
3. Analyze all sites in their chunk
4. Output results to `data/analysis/analysis_chunk_N.md`

## Agent Task Summary

Each agent will:
- **Analyze 8 sites** for HTML consistency, content patterns, and migration difficulty
- **Score each site** from 1-10 (10=easy, 1=very difficult)
- **Estimate effort** (total pages, hours per page, total hours)
- **Identify platforms** (WordPress, HubSpot, Shopify, etc.)
- **Assess automation potential** (what % can be automated vs manual)
- **Provide summary** of their chunk with key insights

## Expected Output Format

Each agent produces a markdown report with:
1. Detailed analysis for each site (8 sites per agent)
2. Summary report at the end with aggregated data

See [`AGENT_TASK_INSTRUCTIONS.md`](./AGENT_TASK_INSTRUCTIONS.md) for detailed output format.

## Running the Analysis

### Option 1: Manual Agent Assignment
Assign each chunk to a different agent/container:
```bash
# Agent 1
./your-agent-tool --chunk=1 --input=data/chunks/chunk_1_urls.json

# Agent 2
./your-agent-tool --chunk=2 --input=data/chunks/chunk_2_urls.json

# ... etc
```

### Option 2: Parallel Execution
Run all 4 agents in parallel:
```bash
./your-agent-tool --parallel --chunks=4
```

## After Analysis Complete

Once all 4 agents complete their analysis:

1. **Collect Reports**: Gather all 4 markdown files from `data/analysis/`
2. **Merge Results**: Create a consolidated report
3. **Generate Summary**: Aggregate scores, effort estimates, platform distribution
4. **Prioritize Sites**: Rank by migration difficulty

## Consolidation Script

After agents complete, run:
```bash
python scripts/consolidate_analysis.py
```

This will:
- Read all 4 chunk analysis files
- Merge into single report
- Calculate totals (hours, costs, etc.)
- Generate priority ranking
- Output to `data/analysis/CONSOLIDATED_REPORT.md`

## Key Metrics to Track

Across all 4 chunks, we need:
- **Total sites analyzed**: 32
- **Score distribution**: How many easy (7-10), medium (4-6), difficult (1-3)
- **Total effort estimate**: Sum of all hours
- **Platform breakdown**: WordPress vs HubSpot vs Shopify vs Custom
- **Average automation potential**: Across all sites
- **Highest priority sites**: Easy wins (high score, low hours)
- **Most challenging sites**: Low scores, high complexity

## Timeline

- **Parallel execution**: All 4 agents run simultaneously (~1-2 hours)
- **Sequential execution**: ~4-8 hours total (1-2 hours per chunk)

## Notes

- Each agent works independently (no coordination needed)
- Agents should NOT prompt for input - run autonomously
- All analysis done via web scraping (view source, check HTML)
- No need for WordPress/HubSpot admin access at this stage
- Focus on HTML quality assessment, not content auditing

## Success Criteria

After analysis, we should be able to answer:
- Which sites are easiest to migrate? (quick wins)
- Which sites are most difficult? (need special attention)
- What's the total effort estimate? (hours across all sites)
- Should we proceed with migration? (feasibility assessment)
- What CMS should we choose? (informed by platform analysis)
