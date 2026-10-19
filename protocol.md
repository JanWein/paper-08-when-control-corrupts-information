# Empirical protocol, intervention scripts, and data dictionary

**Paper 08. Proposed study only, programme revision R1, 17 October 2026.** No organization recruited; no approval, data transfer, treatment assignment, registration, or experiment completed. All proposed tables remain unpopulated. This protocol must be finalized and registered after blinded feasibility work and before treatment outcomes are observed.

## R1 interpretation restriction

The primary theoretical design excludes awareness penalties (F=0). The empirical study cannot causally separate discovery from deliberate suppression without independently observed prior awareness or an additional credible design. Missing reports and audit-positive items alone are not such evidence. Timestamped traces identify a selected subset, not all awareness. The policy-specific sensitivity contrast remains the primary informational estimand. Organizational diagnostic audit capability and the measurement accuracy of research auditors are separate objects.

This prospective study is not part of the completed theoretical results. No experimental data or treatment effect has been produced. The paper's finite policy menu and synthetic values are not study estimates.

## 1. Setting and target population

Low-risk, repeated reconciliation items in administrative operations, such as matching duplicate internal entries in a sandbox or approved noncritical workflow. Do not alter financial controls, safety processes, client rights, legal reporting obligations, or mandatory incident channels. Do not insert actual financial errors into production. Use ordinary naturally arising discrepancies with an independently archived source record.

Eligibility: teams with comparable item flows, stable assignment, common taxonomy, an immutable item universe, and independent source artifacts that allow blinded audits even if employees create no report. Include every eligible completed item, not just exceptions. Exclude legally privileged or restricted material unless organizational counsel approves its use. The study needs sufficient independent team clusters; there is no assumed partner or sample size.

Collection technology means the same interface, event taxonomy, input fields, timestamping, case definitions, and retention in all arms. Treatment changes who may use identified records and for what purpose. Training length, contact frequency, audit sampling, and operational learning feedback are held equal. Access-control changes are necessarily part of the intervention, not evidence that technology is literally unchanged in every respect.

## 2. Assignment and arms

Use a parallel, blocked cluster design. Cluster at the highest shared supervisor or regular knowledge-sharing group needed to limit interference. Randomize eligible clusters in equal proportions, blocked on baseline workload and independent audited defect prevalence, after fixing baseline measures and the roster. A statistician stores the random seed and assignment file before release. No crossover: beliefs about protection and learning persist.

A: protected learning. Identifiers are retained by an authorized research custodian for linkage; managers receive aggregate diagnostic summaries. Diagnostic reports are excluded from individual ranking, pay, and promotion decisions within the explicitly approved boundary. Ordinary occurrence-based audit accountability remains unchanged.

B: identified developmental feedback. A named supervisor can discuss individual records for coaching. They cannot use counts for ranking, compensation, or promotion under the protocol. This arm distinguishes identification from formal evaluation, while allowing perceived reputation exposure to be measured.

C: bounded evaluation. Existing approved individual quality evaluation may use identified reports only within a documented cap and review procedure. No new financial penalty, disciplinary threshold, or harmful sanction is introduced. Independently audited quality is also available under the same policy in all arms. If an organization cannot implement this contrast ethically and credibly, do not run the field trial; use an incentivized harmless sandbox study instead and narrow external-validity claims.

Primary contrast: A versus C. B contrasts are secondary. The intervention estimates the policy bundle's intention-to-treat effect, not a structural derivative with respect to a perfectly measured s. If comprehension or protection credibility differs, report it; do not condition the main estimate on post-treatment comprehension.

## 3. Timing

Provisional schedule: 8 weeks of baseline, 2 weeks implementation and comprehension checks, 16 weeks treatment, and 8 weeks follow-up. Freeze the primary reporting horizon at 30 calendar days after work-item completion. Analysis includes all treatment items with a full 30-day horizon. Later recurrence and severe rework are secondary follow-up outcomes. Before final registration, revise timing from blinded counts and workflow cadence; do not choose a window to maximize significance.

Audits should not immediately inform employees about sampled items before the 30-day reporting horizon closes, except where ordinary controls require prompt action. Mandatory escalation always overrides research timing; mark those items and estimate a separate stratum. Audit-related feedback must follow the same timing across arms. No severe finding is withheld to preserve an experiment.

## 4. Outcomes and estimands

The unit is a completed eligible item. Treatment is assigned to clusters. The finite eligible-work-item population is the target for probability-weighted arm summaries; an equal-team-weight sensitivity analysis assesses domination by large teams.

Two co-primary outcomes, A minus C:

1. Actual defect prevalence p, based on the validated independent audit process.
2. Reporting sensitivity q, a ratio of reported true defects to all true defects under each assigned policy, by day 30.

These are different policy-specific populations of defects. A difference in q does not identify the behavioral effect among items defective under both assignments. Report the joint probability P(R=1,Z=1) and prevalence alongside q so selection is visible. If an arm has no validated defects, q is undefined and a confidence set or upper/lower information limit replaces a point estimate.

Secondary outcomes: false alarm probability f; raw report rate; reporting by days 1, 7, 30; severity distribution of actual defects and of reports separately; count and direction of retrospective edits; intake-to-headquarters attrition; downstream independently adjudicated recurrence; severe rework cost; workload, throughput, departures, reassignment; perceived protection and evaluation use. Report employee-level and managerial filtering separately. Do not define evidence use by reduced defects. Log actual meetings, remedial decisions, and their supporting report identifiers as process measures.

Primary economic targets for planning: 2 percentage points in p around .10, and 10 percentage points in q around .60. These are planning choices requiring partner validation, not established economically meaningful thresholds. Welfare requires separate valuations of defect harm, remedial gains, labor time, channel costs, and learning benefits; report a threshold range rather than a monetary welfare estimate if those inputs are unavailable.

## 5. Sampling and independent validation

Audit from the immutable universe, including report-negative items. Sample with the same known probability by arm within pre-specified workload and baseline risk strata. Sampling may oversample severe baseline categories if inclusion probabilities remain known. Never select only reported or escalated cases. Record the original random selection even when an audit fails.

Auditors see source artifacts and apply a frozen rubric. They are blinded to arm, original report status, worker identity, and supervisor assessment where feasible. A separate linkage custodian matches audits to reports only after audit classification is locked. Random double review and adjudication measure disagreement; disagreement alone is not known sensitivity or specificity. For a validation subset, use a stronger independent source or full re-performance of the item. Estimate audit sensitivity and specificity with uncertainty. If no credible stronger benchmark exists, present results as effects on independently detected defects plus sensitivity bounds, not known actual defects.

Stratify validation by arm and report status to test shared-error concerns, recognizing limited precision. An audit based on the same incomplete documentation is not an independent denominator. Conduct a blinded feasibility test of source completeness before randomization.

## 6. Estimation and uncertainty

Estimate weighted joint cells of audit classification and recording using known inclusion probabilities. At the simplest level, q is a Horvitz-Thompson numerator divided by the corresponding weighted count of true defects. Correct audit error by the manuscript's validated matrix or a constrained multinomial likelihood; propagate validation uncertainty by resampling clusters and the validation sample. Negative unconstrained corrected cells are a specification warning, not values to be silently clipped.

Use blocked randomization inference at cluster level for intention-to-treat contrasts. Report cluster-robust confidence intervals with small-sample correction as a complementary summary; if clusters are few, emphasize randomization-based intervals and attainable precision. Freeze the test statistic, weighting, and covariate adjustment before assignment. Baseline p, workload, and blocks can improve precision. Do not adjust primary estimates for post-treatment workload or severity; report standardized descriptive contrasts separately.

Apply Holm's step-down procedure to the two A-versus-C primary two-sided tests, family-wise alpha .05. Report unadjusted estimates, 95% intervals, and adjusted p-values. Secondary outcomes are explicitly exploratory, with false-discovery-rate summaries within pre-specified reporting and learning families. A positive mechanism claim cannot rest on whichever of many categories happens to be significant.

For missing selected audits, publish rates and reasons by arm. Use inverse response weighting only under a justified conditional missing-at-random model; otherwise bound event status and match status for missing cases. For delayed reporting, report cumulative sensitivity at each horizon so never-reporters remain in the denominator. For unavailable follow-up artifacts, report attrition bounds. The primary roster is fixed before assignment; analyze turnover and transfers as outcomes, while a stable-roster analysis is secondary and selected.

## 7. Power and precision requirements

Under independent sampling, a two-arm normal approximation for a .10 difference near q=.60 gives n_positive per arm approximately 2(1.96+.84)^2(.6)(.4)/(.1)^2 = 376.32. This ignores clustering, multiplicity, audit error, unequal cluster size, and variation in prevalence. It is a lower-complexity illustration, not the final sample size. About 3,770 audited items per arm would yield that many positives at prevalence .10 in expectation.

Before launch, use blinded baseline cluster data to simulate the registered estimator and assignment procedure over cluster counts, size imbalance, defect prevalence, intra-cluster dependence, validation rates, and missing audits. Require 80% power for both planning targets with Holm correction or report feasible precision and redesign. If the partner offers too few clusters or too few audited positives, declare the causal study infeasible at those targets. Do not substitute many observations within two or three teams for independent clusters.

## 8. Mechanisms, alternative explanations, and falsification

Genuine improvement: p falls, q does not deteriorate beyond a pre-specified noninferiority margin, audited severity falls or remains stable, and workload transfer does not explain the change. A nonsignificant deterioration is not noninferiority; a margin and powered test are needed.

Information loss: q falls while p is stable or falls much less than r. This identifies lower policy-specific reporting sensitivity, not proven concealment. Attention measures include time spent on independently assigned diagnostic review and evidence-search actions, interpreted cautiously because logging can itself affect behavior.

Deliberate suppression: a finding is demonstrably known before the reporting deadline yet fails to reach the channel. Timestamped drafts or explicit sandbox exposure provide evidence, but do not enumerate all known findings. No worker is accused using an inferred residual.

Rational reclassification: report-positive rates fall in ambiguous categories while adjudicated underlying severity and source findings remain similar; false alarms may also fall. Freeze the taxonomy and retain all versions. Category heterogeneity is descriptive unless multiplicity and composition are addressed.

Managerial filtering: match immutable employee intake to subsequent summaries and headquarters records. Compare attrition conditional on recorded intake, preserving version history. This does not identify unrecorded employee awareness.

Falsification and diagnostics: audit completion and blinded classification quality by arm; benchmark mechanically verifiable events; pre-treatment placebo trends; cross-arm workload transfers; severity and task-mix shifts; supervisor access logs; contamination surveys. Hard-to-hide categories may respond to real prevention, so stability is not assumed.

## 9. Participant-facing intervention scripts

Common text, subject to actual organizational approval:

“Please use the existing exception screen, categories, and deadlines. Report genuine discrepancies and uncertainty as you normally would. The study does not change mandatory reporting or ordinary controls. Independent reviews will sample both items with reports and items without reports. An absent report will not automatically be treated as deliberate concealment. Questions and concerns can be directed to the approved study contact named in your information sheet.”

A, protected learning addition:

“Your diagnostic entries will support team learning. The authorized custodian retains identifiers only for approved linkage and review. Your manager receives aggregate learning summaries. Within the approved study boundary, these diagnostic entries will not be used for individual ranking, pay, or promotion. The information sheet explains required exceptions and the access limits. Ordinary independently audited quality controls continue.”

B, developmental addition:

“Your supervisor may see your identified entries and discuss them with you for developmental feedback. Under this protocol, diagnostic counts will not determine individual ranking, pay, or promotion. Ordinary independently audited quality controls continue.”

C, bounded evaluation addition:

“Your identified entries may be considered within the existing approved quality-review process, with the limits and review rights set out in your information sheet. The study adds no new financial or disciplinary sanction. A lower count will not on its own be treated as better quality. Independently audited outcomes and the completeness of reporting will also be considered under the approved policy.”

Manager commitment:

“Use records only for the authorized purpose of your team's assigned policy. Do not create parallel scorecards, discourage reports, or remove findings from learning summaries. Preserve changes and escalation trails. Mandatory obligations and ordinary safeguards take precedence. Access and use will be checked against the approved policy.”

These texts are templates, not promises already made to participants. If the organization cannot honor a statement, revise the design and consent material before launch, not the statement alone.

## 10. Proposed data dictionary

| Field | Unit/type | Source and purpose |
|:--|:--|:--|
| cluster_id | Pseudonymous team code | Assignment and cluster inference |
| worker_id | Restricted pseudonymous code | Roster/turnover; not released publicly |
| item_id | Immutable unique code | Complete denominator and linkage |
| completion_time | UTC timestamp | Exposure and reporting horizon |
| arm | A/B/C | Assignment file, locked before release |
| baseline_stratum | Categorical | Pre-treatment audit-sampling block |
| inclusion_probability | (0,1] | Random audit selection log |
| audit_selected | Boolean | Retain selected but missing audits |
| audit_completed | Boolean | Missingness and feasibility |
| audit_missing_reason | Categorical | Missing-source and access diagnostics |
| audit_label_Y | 0/1/uncertain | Blinded independent occurrence review |
| validation_label | 0/1/uncertain/missing | Stronger re-performance subset |
| validation_probability | (0,1] or missing | Validation sampling weights |
| auditor_id | Pseudonymous code | Reliability and reviewer balance |
| source_artifact_hash | Restricted string | Source integrity, not public content |
| report_R30 | Boolean | Recorded by 30 days |
| first_report_time | Timestamp/missing | Cumulative sensitivity and delay |
| initial_category | Frozen taxonomy | Discretion and ambiguity |
| severity_audited | Frozen ordinal rubric | Actual severity independently assessed |
| severity_reported | Frozen ordinal rubric | Severity distortion diagnostic |
| known_before_deadline | 1/0/unknown | Evidence trace, not inferred from Z |
| edit_count | Nonnegative integer | Retrospective edits |
| edit_direction | Categorical | Downgrade/upgrade/other |
| HQ_received | Boolean/NA | Managerial filtering |
| corrective_action_id | Pseudonymous code/NA | Evidence-use process measure |
| recurrence_60d | 0/1/missing | Independently assessed follow-up |
| item_workload | Pre-defined units | Exposure and reassignment diagnostics |
| roster_exit | Date/NA | Selection and turnover |

Use separate access-controlled linkage tables; release only synthetic examples and non-disclosive aggregate analysis subject to approval. Retention periods and controller/processor responsibilities must be agreed before data transfer.

## 11. Planned results tables, deliberately unpopulated

| Table | Required content | Status |
|:--|:--|:--|
| 1 | Cluster roster, workload, audited baseline prevalence | Not collected |
| 2 | Audit selection, completion, validation error by arm | Not collected |
| 3 | p, q, f and joint report-positive prevalence by arm | Not estimated |
| 4 | A-C primary effects with corrected uncertainty | Not estimated |
| 5 | Delays, edits, severity, and managerial filtering | Not estimated |
| 6 | Recurrence and welfare-input ranges | Not estimated |

## 12. Feasibility decision

Current status: theoretical and pre-results only. Public ASRS and MAUDE data lack the necessary jointly observed denominator, policy assignment, and employee linkage. A participating organization must supply an immutable item universe, original source artifacts, a validated audit process, many independent clusters, lawful permission, and enforceable use restrictions. Failure on independent source completeness is a stop condition for claims about actual defect prevalence. No public-data substitute identified here completes the intended causal test.
