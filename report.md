# JIRA Issue Data Quality Report

**Generated:** 2025-09-30 16:09:12  
**Project:** AP (TM Forum JIRA)

---

- [DEBUG] Creating rule engine...
- [DEBUG] Getting rule summary...
### DEBUG] Summary keys: ['total_rules', 'enabled_rules', 'rules_by_category', 'rules_by_severity', 'loaded_rules'

## Rule Engine Configuration

**Status:** ✅ Initialized  
**Rules:** 18/18 enabled

### Rules by Category
- **assignment:** 2 rules
- **metadata:** 6 rules
- **content:** 2 rules
- **workflow:** 4 rules
- **business:** 4 rules


- [AUTH] Step 1: Authenticating with JIRA...
Cookies loaded from jira_cookies.json
- [AUTH] Authenticated as: Stephen Harrop (stephen.harrop@vodafone.com)
Logged in as: Stephen Harrop
Email: stephen.harrop@vodafone.com
- [SETUP] Step 2: Loading project components...
Found 198 Components in AP project
- [SELECT] Step 3: Selecting issue types to check...
Available issue types:
1. Story
2. Task
3. Bug
4. Epic
5. Sub-task
Checking 5 issue types: Story, Task, Bug, Epic, Sub-task

## Checking Story Issues

**JQL Query:** `project = AP AND type = "Story" AND status not in ("Closed", "Resolved", "Done") AND (updated >= "-6M" OR status = "In Progress")`

- [WARNING] JQL Warnings: Field 'type' may not be accessible
- [PERFORMANCE] Performance Warnings: Date queries without ORDER BY may be slow
- [OK] No Story issues found matching the criteria

## Checking Task Issues

**JQL Query:** `project = AP AND type = "Task" AND status not in ("Closed", "Resolved", "Done") AND (updated >= "-6M" OR status = "In Progress")`

- [WARNING] JQL Warnings: Field 'type' may not be accessible
- [PERFORMANCE] Performance Warnings: Date queries without ORDER BY may be slow
**Found:** 43 Task issues to check (Total matching: 43)

### 1. Task: AP-7080

**Title:** Update - Conformance - TMF645 Service Qualification V5.0.0
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-7080](https://projects.tmforum.org/jira/browse/AP-7080)

**TMF APIs Referenced:**
- **TMF645: Service Qualification Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5](https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5)

- [WARNING] TASK [AP-7080] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-7080] has no description
- [SUGGESTION] Add a clear description explaining the task's purpose and acceptance criteria
- [WARNING] TASK [AP-7080] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, FY24-25-Q3, Migration
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 645 Service Qualification
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 1 days (reasonable timeframe)
- [PASS] Updated 1 day ago (27.2 hours)
- [PASS] In progress for 1 days (within 30 day threshold)
- [PASS] Priority: Medium
- [PASS] References TMF645: Service Qualification Management API (Latest: v5)
### 2. Task: AP-7079

**Title:** Update - User Guide - TMF645 Service Qualification V5.0.0
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-7079](https://projects.tmforum.org/jira/browse/AP-7079)

**TMF APIs Referenced:**
- **TMF645: Service Qualification Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5](https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5)

- [WARNING] TASK [AP-7079] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-7079] has no description
- [SUGGESTION] Add a clear description explaining the task's purpose and acceptance criteria
- [WARNING] TASK [AP-7079] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, FY24-25-Q3, Migration
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 645 Service Qualification
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 1 days (reasonable timeframe)
- [PASS] Updated 1 day ago (27.2 hours)
- [PASS] In progress for 1 days (within 30 day threshold)
- [PASS] Priority: Medium
- [PASS] References TMF645: Service Qualification Management API (Latest: v5)
### 3. Task: AP-7078

**Title:** Update - OAS - TMF645 Service Qualification V5.0.0
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-7078](https://projects.tmforum.org/jira/browse/AP-7078)

**TMF APIs Referenced:**
- **TMF645: Service Qualification Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5](https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5)

- [WARNING] TASK [AP-7078] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-7078] has no description
- [SUGGESTION] Add a clear description explaining the task's purpose and acceptance criteria
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, FY24-25-Q3, Migration
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 645 Service Qualification
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 1 days (reasonable timeframe)
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (27.2 hours)
- [PASS] In progress for 1 days (within 30 day threshold)
- [PASS] Priority: Medium
- [PASS] References TMF645: Service Qualification Management API (Latest: v5)
### 4. Task: AP-6970

**Title:** TMF658 - relax dependency to TopicEvent and ProductUsage
**Status:** In Progress
**Assignee:** Dan d'Albuquerque (dan.a@entronica.co.th)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6970](https://projects.tmforum.org/jira/browse/AP-6970)

**TMF APIs Referenced:**
- **TMF635: Usage Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/usage-management-api-TMF635/v4](https://www.tmforum.org/oda/open-apis/directory/usage-management-api-TMF635/v4)
- **TMF701: Process Flow Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5](https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5)
- **TMF658: Loyalty Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/loyalty-management-api-TMF658/v5](https://www.tmforum.org/oda/open-apis/directory/loyalty-management-api-TMF658/v5)

- [WARNING] TASK [AP-6970] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-6970] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6970] in progress for 43 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Dan d'Albuquerque is active
- [PASS] Assigned to: Dan d'Albuquerque
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 658 Loyalty Management
- [PASS] Has description (736 characters)
- [PASS] In progress for 43 days (reasonable timeframe)
- [PASS] Updated 29 days ago
- [PASS] Priority: Medium
- [PASS] References TMF658: Loyalty Management API (Latest: v5)
### 5. Task: AP-6632

**Title:** #33 Alignment with Open API tooling for the PDF generation
**Status:** In Progress
**Assignee:** Knut Johannessen (knut@paneon.no)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6632](https://projects.tmforum.org/jira/browse/AP-6632)

- [WARNING] Task [AP-6632] in progress for 233 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] References TMF763: API not found in database
- [WARNING] Referenced TMF API 'TMF763' not found in API database
- [PASS] Assignee Knut Johannessen is active
- [PASS] Assigned to: Knut Johannessen
- [PASS] No comments
- [PASS] Labels: git-issue
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 763 API Design guidelines
- [PASS] Has description (128 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 233 days (reasonable timeframe)
- [PASS] Has 2 linked issues
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 6. Task: AP-6630

**Title:** PR #921 TMF732_Data_Sharing_Agreement
**Status:** In Progress
**Assignee:** Nikhita Dhanoa (ndhanoa@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6630](https://projects.tmforum.org/jira/browse/AP-6630)

- [WARNING] Task [AP-6630] in progress for 233 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] References TMF732: API not found in database
- [WARNING] Referenced TMF API 'TMF732' not found in API database
- [PASS] Assignee Nikhita Dhanoa is active
- [PASS] Assigned to: Nikhita Dhanoa
- [PASS] No comments
- [PASS] Labels: 2024-03-Montreal, FY24-25-Q1, data_governance, pull-request
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 732 Data Sharing Agreement Management
- [PASS] Has description (68 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 233 days (reasonable timeframe)
- [PASS] Has 3 linked issues
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 7. Task: AP-6628

**Title:** PR #918 TMF725_Metadata_Catalog
**Status:** In Progress
**Assignee:** Nikhita Dhanoa (ndhanoa@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6628](https://projects.tmforum.org/jira/browse/AP-6628)

**TMF APIs Referenced:**
- **TMF725: Metadata Catalog Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4](https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4)

- [WARNING] Task [AP-6628] in progress for 233 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Nikhita Dhanoa is active
- [PASS] Assigned to: Nikhita Dhanoa
- [PASS] No comments
- [PASS] Labels: 2024-03-Montreal, FY24-25-Q1, data_governance, pull-request
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 725 Metadata Catalog management
- [PASS] Has description (102 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 233 days (reasonable timeframe)
- [PASS] Has 3 linked issues
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
- [PASS] References TMF725: Metadata Catalog Management API (Latest: v4)
### 8. Task: AP-6590

**Title:** PR  #1399 add /definitions/ ref of PartyRevSharingModel.schema.json
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6590](https://projects.tmforum.org/jira/browse/AP-6590)

**TMF APIs Referenced:**
- **TMF738: Revenue Sharing Model Management (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/revenue-sharing-model-management-TMF738/v5](https://www.tmforum.org/oda/open-apis/directory/revenue-sharing-model-management-TMF738/v5)

- [WARNING] TASK [AP-6590] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6590] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6590] in progress for 240 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 738 Revenue Sharing Models Management
- [PASS] Has description (425 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 240 days (reasonable timeframe)
- [PASS] Updated 134 days ago
- [PASS] Priority: Medium
- [PASS] References TMF738: Revenue Sharing Model Management (Latest: v5)
### 9. Task: AP-6572

**Title:** PR #1321 Help resolve conflicts on OAS - TMF717 Customer360 V5.0.1
**Status:** In Progress
**Assignee:** Abhilash Prasad (abhilash.prasad@ril.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6572](https://projects.tmforum.org/jira/browse/AP-6572)

**TMF APIs Referenced:**
- **TMF649: Performance Thresholding Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/performance-thresholding-management-api-TMF649/v4](https://www.tmforum.org/oda/open-apis/directory/performance-thresholding-management-api-TMF649/v4)
- **TMF717: Customer360 Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/customer360-management-api-TMF717/v5](https://www.tmforum.org/oda/open-apis/directory/customer360-management-api-TMF717/v5)

- [WARNING] Task [AP-6572] in progress for 245 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Abhilash Prasad is active
- [PASS] Assigned to: Abhilash Prasad
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, FY24-25-Q3, api-team-forge
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 717 Customer360
- [PASS] Has description (1245 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 245 days (reasonable timeframe)
- [PASS] Has 4 linked issues
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
- [PASS] References TMF717: Customer360 Management API (Latest: v5)
### 10. Task: AP-6537

**Title:** TMF763 API Design Guidelines V5 - Part 7
**Status:** In Progress
**Assignee:** Lutz Bettge (lutz.bettge@telekom.de)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6537](https://projects.tmforum.org/jira/browse/AP-6537)

- [WARNING] TASK [AP-6537] has not been updated in 190 days (since 2025-03-12)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-6537] in progress for 249 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] References TMF763: API not found in database
- [WARNING] Referenced TMF API 'TMF763' not found in API database
- [PASS] Assignee Lutz Bettge is active
- [PASS] Assigned to: Lutz Bettge
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 763 API Design guidelines
- [PASS] Has description (844 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 249 days (reasonable timeframe)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
### 11. Task: AP-6536

**Title:** #554 Allow long keys (128 chars) in conformance yaml file
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6536](https://projects.tmforum.org/jira/browse/AP-6536)

- [WARNING] TASK [AP-6536] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6536] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] Task [AP-6536] in progress for 250 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] TASK [AP-6536] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this task to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] No comments
- [PASS] Labels: FY24-25-Q3
- [PASS] Has 2 components: OAS, Tooling
- [PASS] Has description (116 characters)
- [PASS] In progress for 250 days (reasonable timeframe)
- [PASS] Has 1 linked issues
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 12. Task: AP-6523

**Title:** #1360 References in Schema files to non-existing Schemas�
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6523](https://projects.tmforum.org/jira/browse/AP-6523)

- [WARNING] TASK [AP-6523] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6523] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this task
- [WARNING] TASK [AP-6523] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6523] in progress for 251 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (135 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 13. Task: AP-6519

**Title:** #1362 Duplicate schema files
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6519](https://projects.tmforum.org/jira/browse/AP-6519)

- [WARNING] TASK [AP-6519] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6519] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this task
- [WARNING] TASK [AP-6519] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6519] in progress for 251 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (71 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 14. Task: AP-6518

**Title:** �#1359 Schema titles do not match schema file names�
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6518](https://projects.tmforum.org/jira/browse/AP-6518)

- [WARNING] TASK [AP-6518] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6518] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this task
- [WARNING] TASK [AP-6518] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6518] in progress for 251 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (129 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 15. Task: AP-6516

**Title:** #1357 API names do not match API rules file names
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6516](https://projects.tmforum.org/jira/browse/AP-6516)

- [WARNING] TASK [AP-6516] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6516] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this task
- [WARNING] TASK [AP-6516] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6516] in progress for 251 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (71 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 16. Task: AP-6515

**Title:** #1356  API rules files and schema files contain references with "PLACEHOLDER"
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6515](https://projects.tmforum.org/jira/browse/AP-6515)

- [WARNING] TASK [AP-6515] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6515] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this task
- [WARNING] TASK [AP-6515] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6515] in progress for 251 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (71 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 17. Task: AP-6506

**Title:** #1353 schema 'schemas/Tmf/Common/ManagedArtifact.schema.json' does not contain title
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6506](https://projects.tmforum.org/jira/browse/AP-6506)

- [WARNING] TASK [AP-6506] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6506] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this task
- [WARNING] TASK [AP-6506] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6506] in progress for 251 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (159 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 18. Task: AP-6502

**Title:** #1352 APIs and Schemas contain invalid characters
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6502](https://projects.tmforum.org/jira/browse/AP-6502)

- [WARNING] TASK [AP-6502] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6502] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this task
- [WARNING] TASK [AP-6502] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6502] in progress for 251 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (76 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Updated 135 days ago
- [PASS] Priority: Medium
### 19. Task: AP-6432

**Title:** #530  Bulk update coversheet and Release history/ Version history tables on User Guides and Conformance Profiles: runs every 6-8 weeks for TM Forum Approved assets
**Status:** In Progress
**Assignee:** Revathi Sivaji (rsivaji@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6432](https://projects.tmforum.org/jira/browse/AP-6432)

**TMF APIs Referenced:**
- **TMF678: Customer Bill Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/customer-bill-management-api-TMF678/v5](https://www.tmforum.org/oda/open-apis/directory/customer-bill-management-api-TMF678/v5)
- **TMF735: CDR Transaction Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/cdr-transaction-management-api-TMF735/v5](https://www.tmforum.org/oda/open-apis/directory/cdr-transaction-management-api-TMF735/v5)
- **TMF634: Resource Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-catalog-management-api-TMF634/v5](https://www.tmforum.org/oda/open-apis/directory/resource-catalog-management-api-TMF634/v5)
- **TMF638: Service Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5](https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5)
- **TMF738: Revenue Sharing Model Management (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/revenue-sharing-model-management-TMF738/v5](https://www.tmforum.org/oda/open-apis/directory/revenue-sharing-model-management-TMF738/v5)
- **TMF656: Service Problem Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-problem-management-api-TMF656/v5](https://www.tmforum.org/oda/open-apis/directory/service-problem-management-api-TMF656/v5)
- **TMF621: Trouble Ticket Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/trouble-ticket-management-api-TMF621/v5](https://www.tmforum.org/oda/open-apis/directory/trouble-ticket-management-api-TMF621/v5)
- **TMF663: Shopping Cart Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/shopping-cart-management-api-TMF663/v5](https://www.tmforum.org/oda/open-apis/directory/shopping-cart-management-api-TMF663/v5)
- **TMF737: Revenue Sharing Report Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/revenue-sharing-report-management-api-TMF737/v5](https://www.tmforum.org/oda/open-apis/directory/revenue-sharing-report-management-api-TMF737/v5)
- **TMF632: Party Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/party-management-api-TMF632/v5](https://www.tmforum.org/oda/open-apis/directory/party-management-api-TMF632/v5)
- **TMF736: Revenue Sharing Algorithm Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/revenue-sharing-algorithm-management-api-TMF736/v5](https://www.tmforum.org/oda/open-apis/directory/revenue-sharing-algorithm-management-api-TMF736/v5)
- **TMF622: Product Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-ordering-management-api-TMF622/v5](https://www.tmforum.org/oda/open-apis/directory/product-ordering-management-api-TMF622/v5)
- **TMF629: Customer Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/customer-management-api-TMF629/v5](https://www.tmforum.org/oda/open-apis/directory/customer-management-api-TMF629/v5)
- **TMF760: Product Configuration Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-configuration-management-api-TMF760/v5](https://www.tmforum.org/oda/open-apis/directory/product-configuration-management-api-TMF760/v5)
- **TMF637: Product Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-inventory-management-api-TMF637/v5](https://www.tmforum.org/oda/open-apis/directory/product-inventory-management-api-TMF637/v5)
- **TMF669: Party Role Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/party-role-management-api-TMF669/v5](https://www.tmforum.org/oda/open-apis/directory/party-role-management-api-TMF669/v5)
- **TMF620: Product Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-catalog-management-api-TMF620/v5](https://www.tmforum.org/oda/open-apis/directory/product-catalog-management-api-TMF620/v5)
- **TMF644: Privacy Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/privacy-management-api-TMF644/v5](https://www.tmforum.org/oda/open-apis/directory/privacy-management-api-TMF644/v5)
- **TMF683: Party Interaction Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/party-interaction-management-api-TMF683/v5](https://www.tmforum.org/oda/open-apis/directory/party-interaction-management-api-TMF683/v5)

- [WARNING] TASK [AP-6432] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] TASK [AP-6432] has not been updated in 238 days (since 2025-01-22)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-6432] in progress for 287 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] TASK [AP-6432] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this task to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [WARNING] References TMF365: API not found in database
- [WARNING] Referenced TMF API 'TMF365' not found in API database
- [PASS] Assignee Revathi Sivaji is active
- [PASS] Assigned to: Revathi Sivaji
- [PASS] No comments
- [PASS] Labels: DevOps, FY24-25-Q3
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 2 components: OAS, Tooling
- [PASS] Has description (4081 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 287 days (reasonable timeframe)
- [PASS] Priority: Medium
- [PASS] References TMF678: Customer Bill Management API (Latest: v5)
- [PASS] References TMF735: CDR Transaction Management API (Latest: v5)
- [PASS] References TMF634: Resource Catalog Management API (Latest: v5)
- [PASS] References TMF638: Service Inventory Management API (Latest: v5)
- [PASS] References TMF738: Revenue Sharing Model Management (Latest: v5)
- [PASS] References TMF656: Service Problem Management API (Latest: v5)
- [PASS] References TMF621: Trouble Ticket Management API (Latest: v5)
- [PASS] References TMF663: Shopping Cart Management API (Latest: v5)
- [PASS] References TMF737: Revenue Sharing Report Management API (Latest: v5)
- [PASS] References TMF632: Party Management API (Latest: v5)
- [PASS] References TMF736: Revenue Sharing Algorithm Management API (Latest: v5)
- [PASS] References TMF622: Product Ordering Management API (Latest: v5)
- [PASS] References TMF629: Customer Management API (Latest: v5)
- [PASS] References TMF760: Product Configuration Management API (Latest: v5)
- [PASS] References TMF637: Product Inventory Management API (Latest: v5)
- [PASS] References TMF669: Party Role Management API (Latest: v5)
- [PASS] References TMF620: Product Catalog Management API (Latest: v5)
- [PASS] References TMF644: Privacy Management API (Latest: v5)
- [PASS] References TMF683: Party Interaction Management API (Latest: v5)
### 20. Task: AP-6179

**Title:** #313 OAS - Discriminator - JSON Schema - Validation - comment/feedback request
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6179](https://projects.tmforum.org/jira/browse/AP-6179)

- [WARNING] TASK [AP-6179] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-6179] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-6179] has been 'In Progress' for 619 days (created 2024-01-08)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-6179] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-6179] in progress for 619 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] TASK [AP-6179] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this task to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] No comments
- [PASS] Labels: FY24-25-Q3, OASC, accelerate-25
- [PASS] Has 3 components: DevOps, Technology, Tooling
- [PASS] Has description (334 characters)
- [PASS] Updated 2 days ago
- [PASS] Priority: Medium
### 21. Task: AP-6093

**Title:** TMF653 - Defining Lifecycle State Machine
**Status:** In Progress
**Assignee:** Pushan Mukerjee (pushan.mukerjee@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6093](https://projects.tmforum.org/jira/browse/AP-6093)

**TMF APIs Referenced:**
- **TMF653: Service Test Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-test-management-api-TMF653/v5](https://www.tmforum.org/oda/open-apis/directory/service-test-management-api-TMF653/v5)

- [WARNING] TASK [AP-6093] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] TASK [AP-6093] has not been updated in 192 days (since 2025-03-10)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-6093] in progress for 344 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Pushan Mukerjee is active
- [PASS] Assigned to: Pushan Mukerjee
- [PASS] No comments
- [PASS] Labels: improvement
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 653 Service Test Management
- [PASS] Has description (999 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 344 days (reasonable timeframe)
- [PASS] Priority: Medium
- [PASS] References TMF653: Service Test Management API (Latest: v5)
### 22. Task: AP-6054

**Title:** Testing new Innovation Hub tooling against  Virtual Service (VS) and CTK
**Status:** In Progress
**Assignee:** Denis Miano (dmiano@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6054](https://projects.tmforum.org/jira/browse/AP-6054)

**TMF APIs Referenced:**
- **TMF639: Resource Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5](https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5)

- [WARNING] TASK [AP-6054] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-6054] has not been updated in 239 days (since 2025-01-21)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-6054] in progress for 357 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] TASK [AP-6054] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this task to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [WARNING] Issue references TMF639 (Resource Inventory Management API) with version(s) v2 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Denis Miano is active
- [PASS] Assigned to: Denis Miano
- [PASS] No comments
- [PASS] Labels: FY24-25-Q3, api-team-forge, innovation-hub
- [PASS] Has 1 components: Tooling
- [PASS] Has description (1978 characters)
- [PASS] In progress for 357 days (reasonable timeframe)
- [PASS] Has 2 linked issues
- [PASS] Priority: Medium
- [PASS] References TMF639: Resource Inventory Management API (Latest: v5)
### 23. Task: AP-5596

**Title:** Add WebFormContactMedium
**Status:** In Progress
**Assignee:** olivier arnaud (olivier.arnaud@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5596](https://projects.tmforum.org/jira/browse/AP-5596)

**TMF APIs Referenced:**
- **TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5](https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5)

- [WARNING] TASK [AP-5596] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-5596] has been 'In Progress' for 437 days (created 2024-07-08)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-5596] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] TASK [AP-5596] has not been updated in 324 days (since 2024-10-29)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-5596] in progress for 437 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee olivier arnaud is active
- [PASS] Assigned to: olivier arnaud
- [PASS] No comments
- [PASS] Labels: improvement
- [PASS] Has 1 components: API Data Model
- [PASS] Has description (969 characters)
- [PASS] Priority: Medium
- [PASS] References TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)
### 24. Task: AP-5578

**Title:** issue #391 Task resource POST - Allow specifying distinct examples for 201 and 200
**Status:** In Progress
**Assignee:** Revathi Sivaji (rsivaji@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5578](https://projects.tmforum.org/jira/browse/AP-5578)

**TMF APIs Referenced:**
- **TMF679: Product Offering Qualification Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-offering-qualification-management-api-TMF679/v5](https://www.tmforum.org/oda/open-apis/directory/product-offering-qualification-management-api-TMF679/v5)

- [ERROR] High priority issue [AP-5578] not updated in 233 days
- [SUGGESTION] High priority issues should be updated weekly - review and update status
- [WARNING] TASK [AP-5578] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-5578] has been 'In Progress' for 441 days (created 2024-07-04)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-5578] has not been updated in 233 days (since 2025-01-28)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-5578] in progress for 441 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] TASK [AP-5578] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this task to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] Assignee Revathi Sivaji is active
- [PASS] Assigned to: Revathi Sivaji
- [PASS] No comments
- [PASS] Labels: DevOps, FY24-25-Q3, api-team-forge, innovation-hub, kanban
- [PASS] Has 2 components: OAS, Tooling
- [PASS] Has description (701 characters)
- [PASS] Has 6 linked issues
- [PASS] Priority: Highest
- [PASS] References TMF679: Product Offering Qualification Management API (Latest: v5)
### 25. Task: AP-5409

**Title:** TMF931 - Add Authorization Data in Notification Subscriptions [Fix version 5.2]
**Status:** In Progress
**Assignee:** olivier arnaud (olivier.arnaud@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5409](https://projects.tmforum.org/jira/browse/AP-5409)

**TMF APIs Referenced:**
- **TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5](https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5)

- [WARNING] TASK [AP-5409] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-5409] has been 'In Progress' for 476 days (created 2024-05-30)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Task [AP-5409] in progress for 476 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee olivier arnaud is active
- [PASS] Assigned to: olivier arnaud
- [PASS] No comments
- [PASS] Labels: improvement
- [PASS] Has 1 components: 931 Operate API
- [PASS] Has description (3574 characters)
- [PASS] Has 1 linked issues
- [PASS] Updated 155 days ago
- [PASS] Priority: Medium
- [PASS] References TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)
### 26. Task: AP-5207

**Title:** 699 Sales: Many API have xxxRef that are not related to any managed REST resource on an API TMF
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-5207](https://projects.tmforum.org/jira/browse/AP-5207)

**TMF APIs Referenced:**
- **TMF699: Sales Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/sales-management-api-TMF699/v5](https://www.tmforum.org/oda/open-apis/directory/sales-management-api-TMF699/v5)
- **TMF620: Product Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-catalog-management-api-TMF620/v5](https://www.tmforum.org/oda/open-apis/directory/product-catalog-management-api-TMF620/v5)

- [WARNING] TASK [AP-5207] is in progress but not assigned to anyone
- [SUGGESTION] Assign the task to a team member responsible for its delivery
- [WARNING] TASK [AP-5207] has been 'In Progress' for 507 days (created 2024-04-29)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Task [AP-5207] in progress for 507 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 2 components: 620 Product Catalog Management, 699 Sales
- [PASS] Has description (363 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 57 days ago
- [PASS] Priority: Medium
- [PASS] References TMF699: Sales Management API (Latest: v5)
- [PASS] References TMF620: Product Catalog Management API (Latest: v5)
### 27. Task: AP-4950

**Title:** TMF 931 - Add call flows UML code into OAS Open API model
**Status:** In Progress
**Assignee:** Stephen Harrop (stephen.harrop@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4950](https://projects.tmforum.org/jira/browse/AP-4950)

**TMF APIs Referenced:**
- **TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5](https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5)

- [WARNING] TASK [AP-4950] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-4950] has been 'In Progress' for 556 days (created 2024-03-11)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Task [AP-4950] in progress for 556 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF931 (Open Gateway Onboarding and Ordering Component Suite) with version(s) v2 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Stephen Harrop is active
- [PASS] Assigned to: Stephen Harrop
- [PASS] No comments
- [PASS] Labels: FY24-25-Q3, Open_Gateway, api-team-forge, unplanned_FY24-25Q1
- [PASS] Has 1 components: 931 Operate API
- [PASS] Has description (960 characters)
- [PASS] Has 1 linked issues
- [PASS] Updated 44 days ago
- [PASS] Priority: Medium
- [PASS] References TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)
### 28. Task: AP-4892

**Title:** UAT  Draft 1 / Test 1 for How to Guide for API developers Test with Micha? ??czy?ski, MEF API Lead�
**Status:** In Progress
**Assignee:** Stephen Harrop (stephen.harrop@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4892](https://projects.tmforum.org/jira/browse/AP-4892)

- [WARNING] TASK [AP-4892] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-4892] has been 'In Progress' for 570 days (created 2024-02-26)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4892] has not been updated in 401 days (since 2024-08-13)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-4892] in progress for 570 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Stephen Harrop is active
- [PASS] Assigned to: Stephen Harrop
- [PASS] No comments
- [PASS] Labels: Definition_of_Fit_Deliverable, FY24-25-Q1, FY24-25-Q2
- [PASS] Has 2 components: Deliverables, Non-API Specification Related Artefact
- [PASS] Has description (970 characters)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
### 29. Task: AP-4838

**Title:** TMF640 v5 - Conformance behaviour query
**Status:** In Progress
**Assignee:** Anu Aulakh (anu.aulakh@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4838](https://projects.tmforum.org/jira/browse/AP-4838)

**TMF APIs Referenced:**
- **TMF640: Service Activation Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5](https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5)

- [ERROR] High priority issue [AP-4838] not updated in 232 days
- [SUGGESTION] High priority issues should be updated weekly - review and update status
- [WARNING] TASK [AP-4838] has been 'In Progress' for 604 days (created 2024-01-23)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4838] has not been updated in 232 days (since 2025-01-29)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-4838] in progress for 604 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Anu Aulakh is active
- [PASS] Assigned to: Anu Aulakh
- [PASS] No comments
- [PASS] Labels: api-team-forge
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 640 Service Activation
- [PASS] Has description (474 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 6 linked issues
- [PASS] Priority: High
- [PASS] References TMF640: Service Activation Management API (Latest: v5)
### 30. Task: AP-4823

**Title:** TMF639 - supportingResource association to be added.
**Status:** In Progress
**Assignee:** Lutz Bettge (lutz.bettge@telekom.de)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4823](https://projects.tmforum.org/jira/browse/AP-4823)

**TMF APIs Referenced:**
- **TMF639: Resource Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5](https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5)
- **TMF638: Service Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5](https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5)

- [WARNING] TASK [AP-4823] has been 'In Progress' for 583 days (created 2024-02-13)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4823] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-4823] in progress for 583 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Lutz Bettge is active
- [PASS] Assigned to: Lutz Bettge
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris, FY24-25-Q2, improvement, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 2 components: 639 Resource Inventory, triage
- [PASS] Has description (785 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 72 days ago
- [PASS] Priority: Medium
- [PASS] References TMF639: Resource Inventory Management API (Latest: v5)
### 31. Task: AP-4761

**Title:** Deprecate instantSync in all API
**Status:** In Progress
**Assignee:** olivier arnaud (olivier.arnaud@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4761](https://projects.tmforum.org/jira/browse/AP-4761)

- [WARNING] TASK [AP-4761] has been 'In Progress' for 636 days (created 2023-12-22)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4761] has not been updated in 230 days (since 2025-01-30)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-4761] in progress for 636 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] TASK [AP-4761] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this task to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] Assignee olivier arnaud is active
- [PASS] Assigned to: olivier arnaud
- [PASS] No comments
- [PASS] Labels: 2024-04-Dallas, improvement, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 9 components: 645 Service Qualification, 648 Quote Management, 679 Product Offering Qualification, 680 Recommendation , 687 Stock Management, 760 Product Configuration, 909 NaaS CS, 914 IoT Service Component Suite, Tooling
- [PASS] Has description (437 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 3 linked issues
- [PASS] Priority: Medium
### 32. Task: AP-4649

**Title:** TMF670: PaymentMethod: Relaxing PaymentMethod.relatedParty 0..1 to 0..*
**Status:** In Progress
**Assignee:** Dominic Oyeniran (dominic.oyeniran@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4649](https://projects.tmforum.org/jira/browse/AP-4649)

**TMF APIs Referenced:**
- **TMF670: Payment Method Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/payment-method-management-api-TMF670/v5](https://www.tmforum.org/oda/open-apis/directory/payment-method-management-api-TMF670/v5)

- [WARNING] TASK [AP-4649] has been 'In Progress' for 701 days (created 2023-10-18)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4649] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] TASK [AP-4649] has not been updated in 324 days (since 2024-10-29)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-4649] in progress for 701 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Dominic Oyeniran is active
- [PASS] Assigned to: Dominic Oyeniran
- [PASS] No comments
- [PASS] Labels: improvement
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 670 Payment Methods
- [PASS] Has description (424 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Priority: Medium
- [PASS] References TMF670: Payment Method Management API (Latest: v5)
### 33. Task: AP-4572

**Title:** Add LogicalResource and PhysicalResource in the model
**Status:** In Progress
**Assignee:** Lutz Bettge (lutz.bettge@telekom.de)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4572](https://projects.tmforum.org/jira/browse/AP-4572)

**TMF APIs Referenced:**
- **TMF639: Resource Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5](https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5)

- [WARNING] TASK [AP-4572] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-4572] has been 'In Progress' for 756 days (created 2023-08-24)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4572] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] TASK [AP-4572] has not been updated in 324 days (since 2024-10-29)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-4572] in progress for 756 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Lutz Bettge is active
- [PASS] Assigned to: Lutz Bettge
- [PASS] No comments
- [PASS] Labels: improvement
- [PASS] Has 1 components: 702 Resource Activation & Configuration
- [PASS] Has description (119 characters)
- [PASS] Priority: Medium
- [PASS] References TMF639: Resource Inventory Management API (Latest: v5)
- [INFO] Issue references TMF639 (Resource Inventory Management API) but doesn't specify version. Latest available is v5
- [SUGGESTION] Consider specifying version v5 for clarity
### 34. Task: AP-4558

**Title:** TMF 664 - Resource Function API - Fix misalignment of API spec and ref implementation
**Status:** In Progress
**Assignee:** Jonathan Goldberg (jonathan.goldberg@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4558](https://projects.tmforum.org/jira/browse/AP-4558)

**TMF APIs Referenced:**
- **TMF664: Resource Function Activation Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-function-activation-management-api-TMF664/v4](https://www.tmforum.org/oda/open-apis/directory/resource-function-activation-management-api-TMF664/v4)

- [WARNING] TASK [AP-4558] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] TASK [AP-4558] has been 'In Progress' for 797 days (created 2023-07-14)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4558] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] TASK [AP-4558] has not been updated in 324 days (since 2024-10-29)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-4558] in progress for 797 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Jonathan Goldberg is active
- [PASS] Assigned to: Jonathan Goldberg
- [PASS] No comments
- [PASS] Labels: FY24-25-Q3, Migration, improvement
- [PASS] Has 1 components: 664 Resource Function Activation and Configuration
- [PASS] Has description (455 characters)
- [PASS] FixVersion(s): v4.0.0
- [PASS] Priority: Medium
- [PASS] References TMF664: Resource Function Activation Management API (Latest: v4)
### 35. Task: AP-4462

**Title:** change StatusChange schema name into TroubleTicketStatusChange
**Status:** In Progress
**Assignee:** Jacob Avraham (jacoba@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4462](https://projects.tmforum.org/jira/browse/AP-4462)

- [WARNING] TASK [AP-4462] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-4462] has been 'In Progress' for 857 days (created 2023-05-15)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4462] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] TASK [AP-4462] has not been updated in 283 days (since 2024-12-09)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-4462] in progress for 857 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Jacob Avraham is active
- [PASS] Assigned to: Jacob Avraham
- [PASS] No comments
- [PASS] Labels: improvement
- [PASS] Has 1 components: 621 Trouble Ticket
- [PASS] Has description (270 characters)
- [PASS] Priority: Medium
### 36. Task: AP-4388

**Title:** TMF630 - Events Clarification - AttributeValueChange
**Status:** In Progress
**Assignee:** Florin Tene (florin.tene@cityfibre.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4388](https://projects.tmforum.org/jira/browse/AP-4388)

- [WARNING] TASK [AP-4388] has been 'In Progress' for 906 days (created 2023-03-27)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4388] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] TASK [AP-4388] has not been updated in 324 days (since 2024-10-29)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-4388] in progress for 906 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] References TMF630: API not found in database
- [WARNING] Referenced TMF API 'TMF630' not found in API database
- [PASS] Assignee Florin Tene is active
- [PASS] Assigned to: Florin Tene
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, improvement
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 763 API Design guidelines
- [PASS] Has description (175 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Priority: Medium
### 37. Task: AP-4385

**Title:** TMF630 - guidance needed for notification hub when no notification type specified
**Status:** In Progress
**Assignee:** Jonathan Goldberg (jonathan.goldberg@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4385](https://projects.tmforum.org/jira/browse/AP-4385)

**TMF APIs Referenced:**
- **TMF622: Product Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-ordering-management-api-TMF622/v5](https://www.tmforum.org/oda/open-apis/directory/product-ordering-management-api-TMF622/v5)

- [WARNING] TASK [AP-4385] has been 'In Progress' for 912 days (created 2023-03-21)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4385] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-4385] in progress for 912 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] References TMF630: API not found in database
- [WARNING] Referenced TMF API 'TMF630' not found in API database
- [PASS] Assignee Jonathan Goldberg is active
- [PASS] Assigned to: Jonathan Goldberg
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, improvement
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 763 API Design guidelines
- [PASS] Has description (404 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 76 days ago
- [PASS] Priority: Medium
### 38. Task: AP-4236

**Title:** Harmonize sub-resources between entities and specifications
**Status:** In Progress
**Assignee:** olivier arnaud (olivier.arnaud@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4236](https://projects.tmforum.org/jira/browse/AP-4236)

**TMF APIs Referenced:**
- **TMF701: Process Flow Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5](https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5)

- [WARNING] TASK [AP-4236] has been 'In Progress' for 976 days (created 2023-01-16)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4236] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] TASK [AP-4236] has not been updated in 230 days (since 2025-01-30)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-4236] in progress for 976 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF701 (Process Flow Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee olivier arnaud is active
- [PASS] Assigned to: olivier arnaud
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris, FY24-25-Q2, FY24-25-Q3, ODA, improvement
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 701 Work Flow
- [PASS] Has description (989 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Priority: Medium
- [PASS] References TMF701: Process Flow Management API (Latest: v5)
### 39. Task: AP-4235

**Title:** add Delete operation to TaskFlow
**Status:** In Progress
**Assignee:** Stephen Harrop (stephen.harrop@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4235](https://projects.tmforum.org/jira/browse/AP-4235)

- [WARNING] TASK [AP-4235] has been 'In Progress' for 976 days (created 2023-01-16)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4235] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-4235] in progress for 976 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Stephen Harrop is active
- [PASS] Assigned to: Stephen Harrop
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris, FY24-25-Q2, FY24-25-Q3, ODA, improvement
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 701 Work Flow
- [PASS] Has description (280 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 15 days ago
- [PASS] Priority: Medium
### 40. Task: AP-4234

**Title:** Add name in TaskFlow and ProcessFlow
**Status:** In Progress
**Assignee:** Amani Dkhil (amani.dkhil@sofrecom.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4234](https://projects.tmforum.org/jira/browse/AP-4234)

**TMF APIs Referenced:**
- **TMF701: Process Flow Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5](https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5)

- [WARNING] TASK [AP-4234] has been 'In Progress' for 976 days (created 2023-01-16)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-4234] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this task
- [WARNING] Task [AP-4234] in progress for 976 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Amani Dkhil is active
- [PASS] Assigned to: Amani Dkhil
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris, FY24-25-Q2, FY24-25-Q3, ODA, improvement
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 701 Work Flow
- [PASS] Has description (511 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 15 days ago
- [PASS] Priority: Medium
- [PASS] References TMF701: Process Flow Management API (Latest: v5)
### 41. Task: AP-3898

**Title:** Miscellany of changes requested for the catalog - all changes preserve compatibility
**Status:** In Progress
**Assignee:** Christophe MICHEL (cmichel@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3898](https://projects.tmforum.org/jira/browse/AP-3898)

- [WARNING] TASK [AP-3898] has legacy FixVersion 4.2.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] TASK [AP-3898] has been 'In Progress' for 1214 days (created 2022-05-23)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] TASK [AP-3898] has not been updated in 232 days (since 2025-01-29)
- [SUGGESTION] Review and update task status - no activity for over 180 days
- [WARNING] Task [AP-3898] in progress for 1214 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Christophe MICHEL is active
- [PASS] Assigned to: Christophe MICHEL
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 620 Product Catalog Management
- [PASS] Has description (84 characters)
- [PASS] FixVersion(s): v4.2.0
- [PASS] Has 13 linked issues
- [PASS] Priority: Medium
### 42. Task: AP-3003

**Title:** Schema Location of Referred Type
**Status:** In Progress
**Assignee:** Vance Shipley (vances@sigscale.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3003](https://projects.tmforum.org/jira/browse/AP-3003)

- [WARNING] TASK [AP-3003] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-3003] has been 'In Progress' for 1417 days (created 2021-10-31)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Task [AP-3003] in progress for 1417 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Vance Shipley is active
- [PASS] Assigned to: Vance Shipley
- [PASS] No comments
- [PASS] Labels: New_Feature_Technical_Requirement, v5
- [PASS] Has 1 components: API Data Model
- [PASS] Has description (609 characters)
- [PASS] Has 2 linked issues
- [PASS] Updated 9.1 hours ago (today)
- [PASS] Priority: Medium
### 43. Task: AP-2277

**Title:** Cross SDO Domain References
**Status:** In Progress
**Assignee:** Vance Shipley (vances@sigscale.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-2277](https://projects.tmforum.org/jira/browse/AP-2277)

**TMF APIs Referenced:**
- **TMF639: Resource Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5](https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5)
- **TMF633: Service Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-catalog-management-api-TMF633/v5](https://www.tmforum.org/oda/open-apis/directory/service-catalog-management-api-TMF633/v5)

- [WARNING] TASK [AP-2277] has no FixVersion set
- [SUGGESTION] Set a target release version for this task
- [WARNING] TASK [AP-2277] has been 'In Progress' for 1900 days (created 2020-07-05)
- [SUGGESTION] Review task scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Task [AP-2277] in progress for 1900 days (>30 day threshold)
- [SUGGESTION] Review task scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF639 (Resource Inventory Management API) with version(s) v2 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [WARNING] Issue references TMF633 (Service Catalog Management API) with version(s) v2 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Vance Shipley is active
- [PASS] Assigned to: Vance Shipley
- [PASS] No comments
- [PASS] Labels: New_Feature_Technical_Requirement
- [PASS] Has 2 components: 633 Service Catalog Management, 639 Resource Inventory
- [PASS] Has description (2896 characters)
- [PASS] Has 3 linked issues
- [PASS] Updated 63 days ago
- [PASS] Priority: Medium
- [PASS] References TMF639: Resource Inventory Management API (Latest: v5)
- [PASS] References TMF633: Service Catalog Management API (Latest: v5)
- [SUMMARY] Task Summary:
Issues checked: 43
Total violations: 168
Violations by severity:
WARNING: 165
ERROR: 2
INFO: 1
Average violations per issue: 3.9
- [WARNING] Data Quality: NEEDS ATTENTION - Multiple issues found

## Checking Bug Issues

**JQL Query:** `project = AP AND type = "Bug" AND status not in ("Closed", "Resolved", "Done") AND (updated >= "-6M" OR status = "In Progress")`

- [WARNING] JQL Warnings: Field 'type' may not be accessible
- [PERFORMANCE] Performance Warnings: Date queries without ORDER BY may be slow
**Found:** 21 Bug issues to check (Total matching: 21)

### 1. Bug: AP-6870

**Title:** StandardIdentifier schema should not include allOf Entity
**Status:** In Progress
**Assignee:** Stephen Harrop (stephen.harrop@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6870](https://projects.tmforum.org/jira/browse/AP-6870)

- [WARNING] BUG [AP-6870] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-6870] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] Bug [AP-6870] in progress for 86 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [PASS] Assignee Stephen Harrop is active
- [PASS] Assigned to: Stephen Harrop
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 673 Geographic Address Management
- [PASS] Has description (320 characters)
- [PASS] In progress for 86 days (reasonable timeframe)
- [PASS] Updated 17 days ago
- [PASS] Priority: Medium
### 2. Bug: AP-6643

**Title:** Redundant (Orphaned) schemas POPCharge POPAlteration ProductPriceValue - suggest to remove
**Status:** In Progress
**Assignee:** Christophe MICHEL (cmichel@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6643](https://projects.tmforum.org/jira/browse/AP-6643)

- [WARNING] BUG [AP-6643] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-6643] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-6643] has not been updated in 219 days (since 2025-02-11)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-6643] in progress for 227 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [PASS] Assignee Christophe MICHEL is active
- [PASS] Assigned to: Christophe MICHEL
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: Non-API Specification Related Artefact
- [PASS] Has description (266 characters)
- [PASS] In progress for 227 days (reasonable timeframe)
- [PASS] Priority: Medium
### 3. Bug: AP-6424

**Title:** #502 Examples check - not all examples are checked
**Status:** In Progress
**Assignee:** Joel Rosario (joel.rosario@ril.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6424](https://projects.tmforum.org/jira/browse/AP-6424)

- [WARNING] BUG [AP-6424] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-6424] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-6424] has not been updated in 225 days (since 2025-02-05)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-6424] in progress for 290 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] BUG [AP-6424] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this bug to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] Assignee Joel Rosario is active
- [PASS] Assigned to: Joel Rosario
- [PASS] No comments
- [PASS] Labels: DevOps, api-team-forge, git-issue, innovation-hub
- [PASS] Has 1 components: Tooling
- [PASS] Has description (251 characters)
- [PASS] In progress for 290 days (reasonable timeframe)
- [PASS] Priority: Medium
### 4. Bug: AP-6114

**Title:** #474 API tooling Checklist and Examples (OAS3) output validations produce different results
**Status:** In Progress
**Assignee:** Bruno Fernandes (bruno.sfernandes@nos.pt)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6114](https://projects.tmforum.org/jira/browse/AP-6114)

- [WARNING] BUG [AP-6114] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-6114] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-6114] has not been updated in 239 days (since 2025-01-21)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-6114] in progress for 338 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] BUG [AP-6114] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this bug to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] Assignee Bruno Fernandes is active
- [PASS] Assigned to: Bruno Fernandes
- [PASS] No comments
- [PASS] Labels: api-team-forge, innovation-hub
- [PASS] Has 1 components: Tooling
- [PASS] Has description (147 characters)
- [PASS] In progress for 338 days (reasonable timeframe)
- [PASS] Priority: Medium
### 5. Bug: AP-5773

**Title:** Feedback for: TMF630 REST API Design Guidelines 4.2.0
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-5773](https://projects.tmforum.org/jira/browse/AP-5773)

- [WARNING] BUG [AP-5773] is in progress but not assigned to anyone
- [SUGGESTION] Assign the bug to a team member responsible for its delivery
- [WARNING] BUG [AP-5773] has legacy FixVersion 4.2.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] BUG [AP-5773] has been 'In Progress' for 407 days (created 2024-08-07)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Bug [AP-5773] in progress for 407 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] References TMF630: API not found in database
- [WARNING] Referenced TMF API 'TMF630' not found in API database
- [PASS] No comments
- [PASS] Labels: feedback
- [PASS] Has 1 components: 630 API Design Guidelines
- [PASS] Has description (318 characters)
- [PASS] FixVersion(s): v4.2.0
- [PASS] Has 1 linked issues
- [PASS] Updated 20 days ago
- [PASS] Priority: Medium
### 6. Bug: AP-5516

**Title:** TMF931 - remove clientId from POST and PATCH /Application [Fix version 5.2 or 6.0]
**Status:** In Progress
**Assignee:** olivier arnaud (olivier.arnaud@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5516](https://projects.tmforum.org/jira/browse/AP-5516)

**TMF APIs Referenced:**
- **TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5](https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5)

- [WARNING] BUG [AP-5516] has been 'In Progress' for 455 days (created 2024-06-20)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-5516] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] Bug [AP-5516] in progress for 455 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF931 (Open Gateway Onboarding and Ordering Component Suite) with version(s) v1, v2 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee olivier arnaud is active
- [PASS] Assigned to: olivier arnaud
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q1
- [PASS] FixVersion 5.1.0 is current
- [PASS] Has 1 components: 931 Operate API
- [PASS] Has description (1469 characters)
- [PASS] FixVersion(s): v5.1.0
- [PASS] Updated 155 days ago
- [PASS] Priority: Medium
- [PASS] References TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)
### 7. Bug: AP-5230

**Title:** TMF649 Change 'changeEvent' into 'AttributeValueChangeEvent'
**Status:** In Progress
**Assignee:** subhanshu shukla (shubhanshu.shukla@airtel.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5230](https://projects.tmforum.org/jira/browse/AP-5230)

**TMF APIs Referenced:**
- **TMF709: Test Scenario Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/test-scenario-management-api-TMF709/v4](https://www.tmforum.org/oda/open-apis/directory/test-scenario-management-api-TMF709/v4)
- **TMF711: Shipment Management Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/shipment-management-management-api-TMF711/v4](https://www.tmforum.org/oda/open-apis/directory/shipment-management-management-api-TMF711/v4)
- **TMF645: Service Qualification Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5](https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5)
- **TMF679: Product Offering Qualification Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-offering-qualification-management-api-TMF679/v5](https://www.tmforum.org/oda/open-apis/directory/product-offering-qualification-management-api-TMF679/v5)
- **TMF634: Resource Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-catalog-management-api-TMF634/v5](https://www.tmforum.org/oda/open-apis/directory/resource-catalog-management-api-TMF634/v5)
- **TMF667: Document Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/document-management-api-TMF667/v5](https://www.tmforum.org/oda/open-apis/directory/document-management-api-TMF667/v5)
- **TMF638: Service Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5](https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5)
- **TMF702: Resource Activation Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-activation-management-api-TMF702/v4](https://www.tmforum.org/oda/open-apis/directory/resource-activation-management-api-TMF702/v4)
- **TMF623: SLA Management API (Latest: v2)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/sla-management-api-TMF623/v2](https://www.tmforum.org/oda/open-apis/directory/sla-management-api-TMF623/v2)
- **TMF628: Performance Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/performance-management-api-TMF628/v5](https://www.tmforum.org/oda/open-apis/directory/performance-management-api-TMF628/v5)
- **TMF641: Service Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5](https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5)
- **TMF656: Service Problem Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-problem-management-api-TMF656/v5](https://www.tmforum.org/oda/open-apis/directory/service-problem-management-api-TMF656/v5)
- **TMF646: Appointment Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/appointment-management-api-TMF646/v4](https://www.tmforum.org/oda/open-apis/directory/appointment-management-api-TMF646/v4)
- **TMF621: Trouble Ticket Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/trouble-ticket-management-api-TMF621/v5](https://www.tmforum.org/oda/open-apis/directory/trouble-ticket-management-api-TMF621/v5)
- **TMF657: Service Quality Management Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-quality-management-management-api-TMF657/v4](https://www.tmforum.org/oda/open-apis/directory/service-quality-management-management-api-TMF657/v4)
- **TMF707: Test Result Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/test-result-management-api-TMF707/v4](https://www.tmforum.org/oda/open-apis/directory/test-result-management-api-TMF707/v4)
- **TMF675: Geographic Location Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/geographic-location-management-api-TMF675/v4](https://www.tmforum.org/oda/open-apis/directory/geographic-location-management-api-TMF675/v4)
- **TMF635: Usage Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/usage-management-api-TMF635/v4](https://www.tmforum.org/oda/open-apis/directory/usage-management-api-TMF635/v4)
- **TMF663: Shopping Cart Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/shopping-cart-management-api-TMF663/v5](https://www.tmforum.org/oda/open-apis/directory/shopping-cart-management-api-TMF663/v5)
- **TMF632: Party Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/party-management-api-TMF632/v5](https://www.tmforum.org/oda/open-apis/directory/party-management-api-TMF632/v5)
- **TMF725: Metadata Catalog Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4](https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4)
- **TMF651: Agreement Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/agreement-management-api-TMF651/v5](https://www.tmforum.org/oda/open-apis/directory/agreement-management-api-TMF651/v5)
- **TMF681: Communication Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/communication-management-api-TMF681/v4](https://www.tmforum.org/oda/open-apis/directory/communication-management-api-TMF681/v4)
- **TMF664: Resource Function Activation Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-function-activation-management-api-TMF664/v4](https://www.tmforum.org/oda/open-apis/directory/resource-function-activation-management-api-TMF664/v4)
- **TMF700: Shipping Order Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/shipping-order-management-api-TMF700/v5](https://www.tmforum.org/oda/open-apis/directory/shipping-order-management-api-TMF700/v5)
- **TMF673: Geographic Address Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/geographic-address-management-api-TMF673/v5](https://www.tmforum.org/oda/open-apis/directory/geographic-address-management-api-TMF673/v5)
- **TMF642: Alarm Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/alarm-management-api-TMF642/v5](https://www.tmforum.org/oda/open-apis/directory/alarm-management-api-TMF642/v5)
- **TMF622: Product Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-ordering-management-api-TMF622/v5](https://www.tmforum.org/oda/open-apis/directory/product-ordering-management-api-TMF622/v5)
- **TMF704: Test Case Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/test-case-management-api-TMF704/v4](https://www.tmforum.org/oda/open-apis/directory/test-case-management-api-TMF704/v4)
- **TMF710: General Test Artifact Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/general-test-artifact-management-api-TMF710/v4](https://www.tmforum.org/oda/open-apis/directory/general-test-artifact-management-api-TMF710/v4)
- **TMF687: Stock Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/stock-management-api-TMF687/v4](https://www.tmforum.org/oda/open-apis/directory/stock-management-api-TMF687/v4)
- **TMF720: Digital Identity Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/digital-identity-management-api-TMF720/v5](https://www.tmforum.org/oda/open-apis/directory/digital-identity-management-api-TMF720/v5)
- **TMF672: User Role Permission Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/user-role-permission-management-api-TMF672/v5](https://www.tmforum.org/oda/open-apis/directory/user-role-permission-management-api-TMF672/v5)
- **TMF716: Resource Reservation (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-reservation-TMF716/v4](https://www.tmforum.org/oda/open-apis/directory/resource-reservation-TMF716/v4)
- **TMF633: Service Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-catalog-management-api-TMF633/v5](https://www.tmforum.org/oda/open-apis/directory/service-catalog-management-api-TMF633/v5)
- **TMF629: Customer Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/customer-management-api-TMF629/v5](https://www.tmforum.org/oda/open-apis/directory/customer-management-api-TMF629/v5)
- **TMF688: Event Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/event-management-api-TMF688/v4](https://www.tmforum.org/oda/open-apis/directory/event-management-api-TMF688/v4)
- **TMF649: Performance Thresholding Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/performance-thresholding-management-api-TMF649/v4](https://www.tmforum.org/oda/open-apis/directory/performance-thresholding-management-api-TMF649/v4)
- **TMF915: AI Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/ai-management-api-TMF915/v4](https://www.tmforum.org/oda/open-apis/directory/ai-management-api-TMF915/v4)
- **TMF701: Process Flow Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5](https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5)
- **TMF655: Change Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/change-management-api-TMF655/v4](https://www.tmforum.org/oda/open-apis/directory/change-management-api-TMF655/v4)
- **TMF670: Payment Method Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/payment-method-management-api-TMF670/v5](https://www.tmforum.org/oda/open-apis/directory/payment-method-management-api-TMF670/v5)
- **TMF713: Work Management (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/work-management-TMF713/v4](https://www.tmforum.org/oda/open-apis/directory/work-management-TMF713/v4)
- **TMF648: Quote Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/quote-management-api-TMF648/v5](https://www.tmforum.org/oda/open-apis/directory/quote-management-api-TMF648/v5)
- **TMF686: Topology Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/topology-management-api-TMF686/v4](https://www.tmforum.org/oda/open-apis/directory/topology-management-api-TMF686/v4)
- **TMF674: Geographic Site Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/geographic-site-management-api-TMF674/v5](https://www.tmforum.org/oda/open-apis/directory/geographic-site-management-api-TMF674/v5)
- **TMF699: Sales Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/sales-management-api-TMF699/v5](https://www.tmforum.org/oda/open-apis/directory/sales-management-api-TMF699/v5)
- **TMF666: Account Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/account-management-api-TMF666/v5](https://www.tmforum.org/oda/open-apis/directory/account-management-api-TMF666/v5)
- **TMF724: Incident Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/incident-management-api-TMF724/v4](https://www.tmforum.org/oda/open-apis/directory/incident-management-api-TMF724/v4)
- **TMF640: Service Activation Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5](https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5)
- **TMF714: Work Qualification Management (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/work-qualification-management-TMF714/v4](https://www.tmforum.org/oda/open-apis/directory/work-qualification-management-TMF714/v4)
- **TMF706: Test Data Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/test-data-management-api-TMF706/v4](https://www.tmforum.org/oda/open-apis/directory/test-data-management-api-TMF706/v4)
- **TMF676: Payment Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/payment-management-api-TMF676/v4](https://www.tmforum.org/oda/open-apis/directory/payment-management-api-TMF676/v4)
- **TMF703: Entity Inventory Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/entity-inventory-management-api-TMF703/v4](https://www.tmforum.org/oda/open-apis/directory/entity-inventory-management-api-TMF703/v4)
- **TMF921: Intent Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/intent-management-api-TMF921/v5](https://www.tmforum.org/oda/open-apis/directory/intent-management-api-TMF921/v5)
- **TMF715: Warranty Management (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/warranty-management-TMF715/v4](https://www.tmforum.org/oda/open-apis/directory/warranty-management-TMF715/v4)
- **TMF669: Party Role Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/party-role-management-api-TMF669/v5](https://www.tmforum.org/oda/open-apis/directory/party-role-management-api-TMF669/v5)
- **TMF620: Product Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-catalog-management-api-TMF620/v5](https://www.tmforum.org/oda/open-apis/directory/product-catalog-management-api-TMF620/v5)
- **TMF637: Product Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-inventory-management-api-TMF637/v5](https://www.tmforum.org/oda/open-apis/directory/product-inventory-management-api-TMF637/v5)
- **TMF644: Privacy Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/privacy-management-api-TMF644/v5](https://www.tmforum.org/oda/open-apis/directory/privacy-management-api-TMF644/v5)
- **TMF705: Test Environment Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/test-environment-management-api-TMF705/v4](https://www.tmforum.org/oda/open-apis/directory/test-environment-management-api-TMF705/v4)
- **TMF668: Partnership Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/partnership-management-api-TMF668/v4](https://www.tmforum.org/oda/open-apis/directory/partnership-management-api-TMF668/v4)
- **TMF697: Work Order Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/work-order-management-api-TMF697/v5](https://www.tmforum.org/oda/open-apis/directory/work-order-management-api-TMF697/v5)
- **TMF662: Entity Catalog Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/entity-catalog-management-api-TMF662/v4](https://www.tmforum.org/oda/open-apis/directory/entity-catalog-management-api-TMF662/v4)
- **TMF654: Prepay Balance Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/prepay-balance-management-api-TMF654/v5](https://www.tmforum.org/oda/open-apis/directory/prepay-balance-management-api-TMF654/v5)
- **TMF653: Service Test Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-test-management-api-TMF653/v5](https://www.tmforum.org/oda/open-apis/directory/service-test-management-api-TMF653/v5)
- **TMF639: Resource Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5](https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5)
- **TMF683: Party Interaction Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/party-interaction-management-api-TMF683/v5](https://www.tmforum.org/oda/open-apis/directory/party-interaction-management-api-TMF683/v5)
- **TMF652: Resource Order Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-order-management-api-TMF652/v4](https://www.tmforum.org/oda/open-apis/directory/resource-order-management-api-TMF652/v4)

- [WARNING] BUG [AP-5230] has been 'In Progress' for 506 days (created 2024-04-29)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-5230] has not been updated in 198 days (since 2025-03-04)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-5230] in progress for 506 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] Referenced TMF API 'TMF712' not found in API database
- [WARNING] Referenced TMF API 'TMF726' not found in API database
- [WARNING] Referenced TMF API 'TMF913' not found in API database
- [PASS] Assignee subhanshu shukla is active
- [PASS] Assigned to: subhanshu shukla
- [PASS] No comments
- [PASS] Labels: FY24-25-Q3, Migration, api-team-forge
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 649 Performance Management Thresholding
- [PASS] Has description (1087 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
- [PASS] References TMF649: Performance Thresholding Management API (Latest: v4)
### 8. Bug: AP-4555

**Title:** Example validation - product.id is not required in Order and Shopping cart
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-4555](https://projects.tmforum.org/jira/browse/AP-4555)

- [WARNING] BUG [AP-4555] is in progress but not assigned to anyone
- [SUGGESTION] Assign the bug to a team member responsible for its delivery
- [WARNING] BUG [AP-4555] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-4555] has been 'In Progress' for 802 days (created 2023-07-09)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-4555] has not been updated in 508 days (since 2024-04-28)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-4555] in progress for 802 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] BUG [AP-4555] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this bug to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: Tooling
- [PASS] Has description (361 characters)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
### 9. Bug: AP-4554

**Title:** Diagram - Some arrows are strange
**Status:** In Progress
**Assignee:** Knut Johannessen (knut@paneon.no)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4554](https://projects.tmforum.org/jira/browse/AP-4554)

- [WARNING] BUG [AP-4554] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-4554] has been 'In Progress' for 805 days (created 2023-07-06)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-4554] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-4554] has not been updated in 508 days (since 2024-04-28)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-4554] in progress for 805 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] BUG [AP-4554] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this bug to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] Assignee Knut Johannessen is active
- [PASS] Assigned to: Knut Johannessen
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: Tooling
- [PASS] Has description (96 characters)
- [PASS] Priority: Medium
### 10. Bug: AP-4553

**Title:** User Guide - Duplicated Notification
**Status:** In Progress
**Assignee:** Knut Johannessen (knut@paneon.no)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4553](https://projects.tmforum.org/jira/browse/AP-4553)

- [WARNING] BUG [AP-4553] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-4553] has been 'In Progress' for 805 days (created 2023-07-06)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-4553] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-4553] has not been updated in 508 days (since 2024-04-28)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-4553] in progress for 805 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] BUG [AP-4553] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this bug to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] Assignee Knut Johannessen is active
- [PASS] Assigned to: Knut Johannessen
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: Tooling
- [PASS] Has description (154 characters)
- [PASS] Priority: Medium
### 11. Bug: AP-4241

**Title:** TM641 Service Order state attribute in embedded Service is incorrect
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4241](https://projects.tmforum.org/jira/browse/AP-4241)

**TMF APIs Referenced:**
- **TMF641: Service Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5](https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5)

- [WARNING] BUG [AP-4241] has been 'In Progress' for 962 days (created 2023-01-30)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-4241] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] Bug [AP-4241] in progress for 962 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 641 Service Ordering Management
- [PASS] Has description (237 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 21 days ago
- [PASS] Priority: Low
- [PASS] References TMF641: Service Ordering Management API (Latest: v5)
### 12. Bug: AP-4142

**Title:** Mandatory fields in PaymentMethod_Update
**Status:** In Progress
**Assignee:** Dominic Oyeniran (dominic.oyeniran@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4142](https://projects.tmforum.org/jira/browse/AP-4142)

- [WARNING] BUG [AP-4142] has been 'In Progress' for 1062 days (created 2022-10-22)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-4142] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-4142] has not been updated in 335 days (since 2024-10-18)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-4142] in progress for 1062 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [PASS] Assignee Dominic Oyeniran is active
- [PASS] Assigned to: Dominic Oyeniran
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 670 Payment Methods
- [PASS] Has description (333 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Priority: Medium
### 13. Bug: AP-2927

**Title:** Defining serviceRelationshipCharacteristic via Service Catalog
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-2927](https://projects.tmforum.org/jira/browse/AP-2927)

**TMF APIs Referenced:**
- **TMF640: Service Activation Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5](https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5)
- **TMF633: Service Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-catalog-management-api-TMF633/v5](https://www.tmforum.org/oda/open-apis/directory/service-catalog-management-api-TMF633/v5)

- [WARNING] BUG [AP-2927] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-2927] has been 'In Progress' for 1452 days (created 2021-09-27)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-2927] has not been updated in 508 days (since 2024-04-28)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-2927] in progress for 1452 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF640 (Service Activation Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [WARNING] Issue references TMF633 (Service Catalog Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 633 Service Catalog Management
- [PASS] Has description (268 characters)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
- [PASS] References TMF640: Service Activation Management API (Latest: v5)
- [PASS] References TMF633: Service Catalog Management API (Latest: v5)
### 14. Bug: AP-2604

**Title:** TMF640 ServiceActivationConfiguration Basepath deviates from other TMF APIs
**Status:** In Progress
**Assignee:** Johanne Mayer (jmayer@mayerconsult.ca)
**URL:** [https://projects.tmforum.org/jira/browse/AP-2604](https://projects.tmforum.org/jira/browse/AP-2604)

**TMF APIs Referenced:**
- **TMF640: Service Activation Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5](https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5)
- **TMF638: Service Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5](https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5)

- [ERROR] High priority issue [AP-2604] not updated in 508 days
- [SUGGESTION] High priority issues should be updated weekly - review and update status
- [WARNING] BUG [AP-2604] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-2604] has been 'In Progress' for 1739 days (created 2020-12-14)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-2604] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-2604] has not been updated in 508 days (since 2024-04-28)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-2604] in progress for 1739 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF640 (Service Activation Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [WARNING] Issue references TMF638 (Service Inventory Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Johanne Mayer is active
- [PASS] Assigned to: Johanne Mayer
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 640 Service Activation
- [PASS] Has description (590 characters)
- [PASS] Priority: High
- [PASS] References TMF640: Service Activation Management API (Latest: v5)
### 15. Bug: AP-2424

**Title:** TMF633 - Unable to define Characteristics at Order Level (Not part of Service)
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-2424](https://projects.tmforum.org/jira/browse/AP-2424)

**TMF APIs Referenced:**
- **TMF633: Service Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-catalog-management-api-TMF633/v5](https://www.tmforum.org/oda/open-apis/directory/service-catalog-management-api-TMF633/v5)

- [WARNING] BUG [AP-2424] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-2424] has been 'In Progress' for 1746 days (created 2020-12-07)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-2424] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-2424] has not been updated in 416 days (since 2024-07-29)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-2424] in progress for 1746 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 2 components: 633 Service Catalog Management, 641 Service Ordering Management
- [PASS] Has description (2773 characters)
- [PASS] Priority: Medium
- [PASS] References TMF633: Service Catalog Management API (Latest: v5)
- [INFO] Issue references TMF633 (Service Catalog Management API) but doesn't specify version. Latest available is v5
- [SUGGESTION] Consider specifying version v5 for clarity
### 16. Bug: AP-2376

**Title:** externalReference has id/href
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-2376](https://projects.tmforum.org/jira/browse/AP-2376)

**TMF APIs Referenced:**
- **TMF641: Service Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5](https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5)

- [WARNING] BUG [AP-2376] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-2376] has been 'In Progress' for 1799 days (created 2020-10-14)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-2376] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-2376] has not been updated in 508 days (since 2024-04-28)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-2376] in progress for 1799 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF641 (Service Ordering Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 641 Service Ordering Management
- [PASS] Has description (572 characters)
- [PASS] Priority: Medium
- [PASS] References TMF641: Service Ordering Management API (Latest: v5)
### 17. Bug: AP-2343

**Title:** TMF641: CancelServiceOrder Error Details
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-2343](https://projects.tmforum.org/jira/browse/AP-2343)

**TMF APIs Referenced:**
- **TMF641: Service Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5](https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5)

- [WARNING] BUG [AP-2343] has no FixVersion set
- [SUGGESTION] Set a target release version for this bug
- [WARNING] BUG [AP-2343] has been 'In Progress' for 1840 days (created 2020-09-04)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-2343] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-2343] has not been updated in 508 days (since 2024-04-28)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-2343] in progress for 1840 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF641 (Service Ordering Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 641 Service Ordering Management
- [PASS] Has description (1070 characters)
- [PASS] Priority: Medium
- [PASS] References TMF641: Service Ordering Management API (Latest: v5)
### 18. Bug: AP-2336

**Title:** TMF641: Corrections to CancelServiceOrder schema
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-2336](https://projects.tmforum.org/jira/browse/AP-2336)

**TMF APIs Referenced:**
- **TMF641: Service Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5](https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5)

- [WARNING] BUG [AP-2336] has legacy FixVersion 4.2.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] BUG [AP-2336] has been 'In Progress' for 1848 days (created 2020-08-27)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-2336] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] Bug [AP-2336] in progress for 1848 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF641 (Service Ordering Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q2
- [PASS] Has 1 components: 641 Service Ordering Management
- [PASS] Has description (2421 characters)
- [PASS] FixVersion(s): v4.2.0
- [PASS] Updated 20 days ago
- [PASS] Priority: Medium
- [PASS] References TMF641: Service Ordering Management API (Latest: v5)
### 19. Bug: AP-2120

**Title:** Notification Object Definition Inconsistencies in the Rules files
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-2120](https://projects.tmforum.org/jira/browse/AP-2120)

- [WARNING] BUG [AP-2120] is in progress but not assigned to anyone
- [SUGGESTION] Assign the bug to a team member responsible for its delivery
- [WARNING] BUG [AP-2120] has been 'In Progress' for 2019 days (created 2020-03-09)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-2120] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-2120] has not been updated in 377 days (since 2024-09-06)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-2120] in progress for 2019 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] Labels: propose-review
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: Other
- [PASS] Has description (801 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Priority: Medium
### 20. Bug: AP-2053

**Title:** TMF680_Recommendation API : Swagger modification for issue correction
**Status:** In Progress
**Assignee:** Gregoire Laurent (gregoire.laurent@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-2053](https://projects.tmforum.org/jira/browse/AP-2053)

**TMF APIs Referenced:**
- **TMF680: Recommendation Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/recommendation-management-api-TMF680/v4](https://www.tmforum.org/oda/open-apis/directory/recommendation-management-api-TMF680/v4)

- [WARNING] BUG [AP-2053] has been 'In Progress' for 2079 days (created 2020-01-09)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-2053] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-2053] has not been updated in 230 days (since 2025-01-30)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-2053] in progress for 2079 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [PASS] Assignee Gregoire Laurent is active
- [PASS] Assigned to: Gregoire Laurent
- [PASS] No comments
- [PASS] Labels: 2024-04-Dallas, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 680 Recommendation
- [PASS] Has description (351 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Priority: Medium
- [PASS] References TMF680: Recommendation Management API (Latest: v4)
### 21. Bug: AP-2047

**Title:** Service Activation and Configuration spec examples are invalid JSON (extra } )
**Status:** In Progress
**Assignee:** Johanne Mayer (jmayer@mayerconsult.ca)
**URL:** [https://projects.tmforum.org/jira/browse/AP-2047](https://projects.tmforum.org/jira/browse/AP-2047)

- [WARNING] BUG [AP-2047] has legacy FixVersion 4.1.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] BUG [AP-2047] has been 'In Progress' for 2090 days (created 2019-12-29)
- [SUGGESTION] Review bug scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] BUG [AP-2047] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this bug
- [WARNING] BUG [AP-2047] has not been updated in 464 days (since 2024-06-11)
- [SUGGESTION] Review and update bug status - no activity for over 180 days
- [WARNING] Bug [AP-2047] in progress for 2090 days (>14 day threshold)
- [SUGGESTION] Review bug scope and progress - consider breaking down or reassigning
- [PASS] Assignee Johanne Mayer is active
- [PASS] Assigned to: Johanne Mayer
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 640 Service Activation
- [PASS] Has description (326 characters)
- [PASS] FixVersion(s): v4.1.0
- [PASS] Priority: Medium
- [SUMMARY] Bug Summary:
Issues checked: 21
Total violations: 109
Violations by severity:
WARNING: 107
ERROR: 1
INFO: 1
Average violations per issue: 5.2
- [POOR] Data Quality: POOR - Many issues require immediate attention

## Checking Epic Issues

**JQL Query:** `project = AP AND type = "Epic" AND status not in ("Closed", "Resolved", "Done") AND (updated >= "-6M" OR status = "In Progress")`

- [WARNING] JQL Warnings: Field 'type' may not be accessible
- [PERFORMANCE] Performance Warnings: Date queries without ORDER BY may be slow
**Found:** 100 Epic issues to check (Total matching: 141)

### 1. Epic: AP-7003

**Title:** TMF013 Signalling Data Transformation and Analytics API v5.0.0
**Status:** In Progress
**Assignee:** HAI WEI (knightwei@hk.chinamobile.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-7003](https://projects.tmforum.org/jira/browse/AP-7003)

- [WARNING] EPIC [AP-7003] has no components set
- [SUGGESTION] No matching components found for TMF number 013
- [WARNING] EPIC [AP-7003] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF013: API not found in database
- [WARNING] Referenced TMF API 'TMF013' not found in API database
- [PASS] Assignee HAI WEI is active
- [PASS] Assigned to: HAI WEI
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (946 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 2. Epic: AP-7002

**Title:** TMF012 Speech Analysis API v5.0.0
**Status:** In Progress
**Assignee:** XIN QU (quxin1@hn.chinamobile.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-7002](https://projects.tmforum.org/jira/browse/AP-7002)

- [WARNING] EPIC [AP-7002] has no components set
- [SUGGESTION] No matching components found for TMF number 012
- [WARNING] EPIC [AP-7002] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF012: API not found in database
- [WARNING] Referenced TMF API 'TMF012' not found in API database
- [PASS] Assignee XIN QU is active
- [PASS] Assigned to: XIN QU
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (917 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 3. Epic: AP-7001

**Title:** TMF011 Image Content Recognition v5.0.0
**Status:** In Progress
**Assignee:** pingsh lii (lipingsh@sd.chinamobile.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-7001](https://projects.tmforum.org/jira/browse/AP-7001)

- [WARNING] EPIC [AP-7001] has no components set
- [SUGGESTION] No matching components found for TMF number 011
- [WARNING] EPIC [AP-7001] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF011: API not found in database
- [WARNING] Referenced TMF API 'TMF011' not found in API database
- [PASS] Assignee pingsh lii is active
- [PASS] Assigned to: pingsh lii
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (923 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 4. Epic: AP-7000

**Title:** TMF010 Agentic AI as a Service v5.0.0
**Status:** In Progress
**Assignee:** Haojie LI (lihaojie@chinamobile.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-7000](https://projects.tmforum.org/jira/browse/AP-7000)

- [WARNING] EPIC [AP-7000] has no components set
- [SUGGESTION] No matching components found for TMF number 010
- [WARNING] EPIC [AP-7000] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF010: API not found in database
- [WARNING] Referenced TMF API 'TMF010' not found in API database
- [PASS] Assignee Haojie LI is active
- [PASS] Assigned to: Haojie LI
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (921 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 5. Epic: AP-6999

**Title:** TMF009 Internet TV Complaint Prediction API v5.0.0
**Status:** In Progress
**Assignee:** Jianye Dong (dongjianye@fj.chinamobile.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6999](https://projects.tmforum.org/jira/browse/AP-6999)

- [WARNING] EPIC [AP-6999] has no components set
- [SUGGESTION] No matching components found for TMF number 009
- [WARNING] EPIC [AP-6999] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF009: API not found in database
- [WARNING] Referenced TMF API 'TMF009' not found in API database
- [PASS] Assignee Jianye Dong is active
- [PASS] Assigned to: Jianye Dong
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (934 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 6. Epic: AP-6998

**Title:** TMF008 End-to-End path Computation API v5.0.0
**Status:** In Progress
**Assignee:** weijie Xu (xuweijie@fj.chinamobile.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6998](https://projects.tmforum.org/jira/browse/AP-6998)

- [WARNING] EPIC [AP-6998] has no components set
- [SUGGESTION] No matching components found for TMF number 008
- [WARNING] EPIC [AP-6998] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF008: API not found in database
- [WARNING] Referenced TMF API 'TMF008' not found in API database
- [PASS] Assignee weijie Xu is active
- [PASS] Assigned to: weijie Xu
- [PASS] No comments
- [PASS] Labels: Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (929 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 7. Epic: AP-6997

**Title:** TMF007 Capability invocation frequency management API - Template v5.0.0
**Status:** In Progress
**Assignee:** Margaret Pan (panby@chinatelecom.cn)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6997](https://projects.tmforum.org/jira/browse/AP-6997)

- [WARNING] EPIC [AP-6997] has no components set
- [SUGGESTION] No matching components found for TMF number 007
- [WARNING] EPIC [AP-6997] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF007: API not found in database
- [WARNING] Referenced TMF API 'TMF007' not found in API database
- [PASS] Assignee Margaret Pan is active
- [PASS] Assigned to: Margaret Pan
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (955 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 8. Epic: AP-6996

**Title:** TMF006 Capability invocation allow/block list management API v5.0.0
**Status:** In Progress
**Assignee:** Margaret Pan (panby@chinatelecom.cn)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6996](https://projects.tmforum.org/jira/browse/AP-6996)

- [WARNING] EPIC [AP-6996] has no components set
- [SUGGESTION] No matching components found for TMF number 006
- [WARNING] EPIC [AP-6996] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF006: API not found in database
- [WARNING] Referenced TMF API 'TMF006' not found in API database
- [PASS] Assignee Margaret Pan is active
- [PASS] Assigned to: Margaret Pan
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (952 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 9. Epic: AP-6995

**Title:** TMF005 Intent-Based Service Specification Design API v5.0.0
**Status:** In Progress
**Assignee:** Margaret Pan (panby@chinatelecom.cn)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6995](https://projects.tmforum.org/jira/browse/AP-6995)

- [WARNING] EPIC [AP-6995] has no components set
- [SUGGESTION] No matching components found for TMF number 005
- [WARNING] EPIC [AP-6995] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF005: API not found in database
- [WARNING] Referenced TMF API 'TMF005' not found in API database
- [PASS] Assignee Margaret Pan is active
- [PASS] Assigned to: Margaret Pan
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (943 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 10. Epic: AP-6994

**Title:** TMF004 Power and Environmental Equipment Room System API v5.0.0
**Status:** In Progress
**Assignee:** Huang Changchun (huangcc@js.chinamobile.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6994](https://projects.tmforum.org/jira/browse/AP-6994)

- [WARNING] EPIC [AP-6994] has no components set
- [SUGGESTION] No matching components found for TMF number 004
- [WARNING] EPIC [AP-6994] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF004: API not found in database
- [WARNING] Referenced TMF API 'TMF004' not found in API database
- [PASS] Assignee Huang Changchun is active
- [PASS] Assigned to: Huang Changchun
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (947 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 11. Epic: AP-6992

**Title:** TMF002 Collaboration API v5.0.0
**Status:** In Progress
**Assignee:** Yun LI (liyun9@asiainfo.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6992](https://projects.tmforum.org/jira/browse/AP-6992)

- [WARNING] EPIC [AP-6992] has no components set
- [SUGGESTION] No matching components found for TMF number 002
- [WARNING] EPIC [AP-6992] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF002: API not found in database
- [WARNING] Referenced TMF API 'TMF002' not found in API database
- [PASS] Assignee Yun LI is active
- [PASS] Assigned to: Yun LI
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (915 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 12. Epic: AP-6991

**Title:** TMF001 Engagement AI Agent API v5.0.0
**Status:** In Progress
**Assignee:** liu weitao (liu.weitao@iwhalecloud.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6991](https://projects.tmforum.org/jira/browse/AP-6991)

- [WARNING] EPIC [AP-6991] has no components set
- [SUGGESTION] No matching components found for TMF number 001
- [WARNING] EPIC [AP-6991] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF001: API not found in database
- [WARNING] Referenced TMF API 'TMF001' not found in API database
- [PASS] Assignee liu weitao is active
- [PASS] Assigned to: liu weitao
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, Inception
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (920 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 32 days (reasonable timeframe)
- [PASS] Updated 2 days ago
- [PASS] In progress for 32 days (within 365 day threshold)
- [PASS] Priority: Medium
### 13. Epic: AP-6799

**Title:** TMF730 Software and Compute Entity Management API Suite v5.0.0
**Status:** In Progress
**Assignee:** Vance Shipley (vances@sigscale.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6799](https://projects.tmforum.org/jira/browse/AP-6799)

**TMF APIs Referenced:**
- **TMF730: Software And Compute Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/software-and-compute-management-api-TMF730/v4](https://www.tmforum.org/oda/open-apis/directory/software-and-compute-management-api-TMF730/v4)

- [ERROR] High priority issue [AP-6799] not updated in 88 days
- [SUGGESTION] High priority issues should be updated weekly - review and update status
- [WARNING] EPIC [AP-6799] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [PASS] Assignee Vance Shipley is active
- [PASS] Assigned to: Vance Shipley
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q2
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 730 Software and Compute Entity Management API
- [PASS] Has description (458 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 120 days (reasonable timeframe)
- [PASS] Updated 88 days ago
- [PASS] In progress for 120 days (within 365 day threshold)
- [PASS] Priority: High
- [PASS] References TMF730: Software And Compute Management API (Latest: v4)
### 14. Epic: AP-6782

**Title:** TMF683 Party Interaction v5.1.0
**Status:** In Progress
**Assignee:** Jacob Avraham (jacoba@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6782](https://projects.tmforum.org/jira/browse/AP-6782)

**TMF APIs Referenced:**
- **TMF683: Party Interaction Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/party-interaction-management-api-TMF683/v5](https://www.tmforum.org/oda/open-apis/directory/party-interaction-management-api-TMF683/v5)

- [WARNING] EPIC [AP-6782] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [PASS] Assignee Jacob Avraham is active
- [PASS] Assigned to: Jacob Avraham
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q2
- [PASS] FixVersion 5.1.0 is current
- [PASS] Has 1 components: 683 User Interactions
- [PASS] Has description (920 characters)
- [PASS] FixVersion(s): v5.1.0
- [PASS] In progress for 128 days (reasonable timeframe)
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] In progress for 128 days (within 365 day threshold)
- [PASS] Priority: Medium
- [PASS] References TMF683: Party Interaction Management API (Latest: v5)
### 15. Epic: AP-6760

**Title:** TMF621 Trouble Ticket V5.0.1
**Status:** In Progress
**Assignee:** Jacob Avraham (jacoba@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6760](https://projects.tmforum.org/jira/browse/AP-6760)

**TMF APIs Referenced:**
- **TMF621: Trouble Ticket Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/trouble-ticket-management-api-TMF621/v5](https://www.tmforum.org/oda/open-apis/directory/trouble-ticket-management-api-TMF621/v5)

- [WARNING] EPIC [AP-6760] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [PASS] Assignee Jacob Avraham is active
- [PASS] Assigned to: Jacob Avraham
- [PASS] No comments
- [PASS] Labels: BAU, Open_Gateway
- [PASS] FixVersion 5.0.1 is current
- [PASS] Has 1 components: 621 Trouble Ticket
- [PASS] Has description (917 characters)
- [PASS] FixVersion(s): v5.0.1
- [PASS] In progress for 148 days (reasonable timeframe)
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] In progress for 148 days (within 365 day threshold)
- [PASS] Priority: Medium
- [PASS] References TMF621: Trouble Ticket Management API (Latest: v5)
### 16. Epic: AP-6713

**Title:** TMF783 Configuration Profile Management API V5.0.0
**Status:** In Progress
**Assignee:** Vance Shipley (vances@sigscale.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6713](https://projects.tmforum.org/jira/browse/AP-6713)

- [WARNING] References TMF783: API not found in database
- [WARNING] Referenced TMF API 'TMF783' not found in API database
- [PASS] Assignee Vance Shipley is active
- [PASS] Assigned to: Vance Shipley
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 2 components: 722 Entity Configuration, 783 Configuration Profile Management
- [PASS] Has description (945 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 189 days (reasonable timeframe)
- [PASS] Has 3 linked issues
- [PASS] Updated 9.1 hours ago (today)
- [PASS] In progress for 189 days (within 365 day threshold)
- [PASS] Priority: Medium
### 17. Epic: AP-6588

**Title:** Pull requests needing review or with issues that need solving for API developers
**Status:** In Progress
**Assignee:** Nikhita Dhanoa (ndhanoa@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6588](https://projects.tmforum.org/jira/browse/AP-6588)

- [WARNING] EPIC [AP-6588] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this epic
- [WARNING] EPIC [AP-6588] has no FixVersion set
- [SUGGESTION] Set a target release version for this epic
- [WARNING] EPIC [AP-6588] has not been updated in 224 days (since 2025-02-06)
- [SUGGESTION] Review and update epic status - no activity for over 180 days
- [PASS] Assignee Nikhita Dhanoa is active
- [PASS] Assigned to: Nikhita Dhanoa
- [PASS] No comments
- [PASS] Labels: DevOps
- [PASS] Has description (84 characters)
- [PASS] In progress for 240 days (reasonable timeframe)
- [PASS] Has 13 linked issues
- [PASS] In progress for 240 days (within 365 day threshold)
- [PASS] Priority: Medium
### 18. Epic: AP-6501

**Title:** v5.0 API Clean Up Work
**Status:** In Progress
**Assignee:** Lutz Bettge (lutz.bettge@telekom.de)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6501](https://projects.tmforum.org/jira/browse/AP-6501)

- [WARNING] EPIC [AP-6501] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this epic
- [WARNING] EPIC [AP-6501] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [PASS] Assignee Lutz Bettge is active
- [PASS] Assigned to: Lutz Bettge
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (359 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Updated 14 days ago
- [PASS] In progress for 251 days (within 365 day threshold)
- [PASS] Priority: Medium
### 19. Epic: AP-6402

**Title:** TMF781 Resource Discovery V5.0.0
**Status:** In Progress
**Assignee:** Margaret Pan (panby@chinatelecom.cn)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6402](https://projects.tmforum.org/jira/browse/AP-6402)

- [WARNING] EPIC [AP-6402] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF781: API not found in database
- [WARNING] Referenced TMF API 'TMF781' not found in API database
- [PASS] Assignee Margaret Pan is active
- [PASS] Assigned to: Margaret Pan
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, china_specjam_2024
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 781 Resource Discovery
- [PASS] Has description (916 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 293 days (reasonable timeframe)
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] In progress for 293 days (within 365 day threshold)
- [PASS] Priority: Medium
### 20. Epic: AP-6359

**Title:** TMF780 MaaS API  V5.0.0
**Status:** In Progress
**Assignee:** Cece Li (celi@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6359](https://projects.tmforum.org/jira/browse/AP-6359)

- [WARNING] EPIC [AP-6359] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF780: API not found in database
- [WARNING] Referenced TMF API 'TMF780' not found in API database
- [PASS] Assignee Cece Li is active
- [PASS] Assigned to: Cece Li
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, china_specjam_2024
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 780MaaS
- [PASS] Has description (905 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 294 days (reasonable timeframe)
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] In progress for 294 days (within 365 day threshold)
- [PASS] Priority: Medium
### 21. Epic: AP-6349

**Title:** TMF778 Digital Twin - Network Optimisation API V5.0.0
**Status:** In Progress
**Assignee:** Cece Li (celi@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6349](https://projects.tmforum.org/jira/browse/AP-6349)

- [WARNING] EPIC [AP-6349] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] References TMF778: API not found in database
- [WARNING] Referenced TMF API 'TMF778' not found in API database
- [PASS] Assignee Cece Li is active
- [PASS] Assigned to: Cece Li
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, china_specjam_2024
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 778 Digital twin - Network Optimisation
- [PASS] Has description (936 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 294 days (reasonable timeframe)
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] In progress for 294 days (within 365 day threshold)
- [PASS] Priority: Medium
### 22. Epic: AP-6206

**Title:** TMF938 API Suite (Broadband Team)
**Status:** In Progress
**Assignee:** Bartosz Michalik (bartosz.michalik@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6206](https://projects.tmforum.org/jira/browse/AP-6206)

- [WARNING] EPIC [AP-6206] has no components set
- [SUGGESTION] Consider adding component(s): TMF938
- [WARNING] References TMF938: API not found in database
- [WARNING] Referenced TMF API 'TMF938' not found in API database
- [PASS] Assignee Bartosz Michalik is active
- [PASS] Assigned to: Bartosz Michalik
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (1641 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Has 6 linked issues
- [PASS] Updated 6 days ago
- [PASS] In progress for 318 days (within 365 day threshold)
- [PASS] Priority: Medium
### 23. Epic: AP-5968

**Title:** Open API Tooling & Branch prep- Vienna Spec Jam 2024
**Status:** In Progress
**Assignee:** Joel Burgess (joel.burgess@oracle.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5968](https://projects.tmforum.org/jira/browse/AP-5968)

- [WARNING] EPIC [AP-5968] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this epic
- [WARNING] EPIC [AP-5968] has no FixVersion set
- [SUGGESTION] Set a target release version for this epic
- [WARNING] EPIC [AP-5968] has been 'In Progress' for 372 days (created 2024-09-11)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5968] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] EPIC [AP-5968] has not been updated in 371 days (since 2024-09-12)
- [SUGGESTION] Review and update epic status - no activity for over 180 days
- [WARNING] Epic [AP-5968] in progress for 372 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Joel Burgess is active
- [PASS] Assigned to: Joel Burgess
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna
- [PASS] Has description (47 characters)
- [PASS] Priority: Medium
### 24. Epic: AP-5866

**Title:** TMF773 Authorization and Token Issuance V5.0.0
**Status:** In Progress
**Assignee:** Bruno Fernandes (bruno.sfernandes@nos.pt)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5866](https://projects.tmforum.org/jira/browse/AP-5866)

- [WARNING] EPIC [AP-5866] has been 'In Progress' for 387 days (created 2024-08-27)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5866] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-5866] in progress for 387 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF773: API not found in database
- [WARNING] Referenced TMF API 'TMF773' not found in API database
- [PASS] Assignee Bruno Fernandes is active
- [PASS] Assigned to: Bruno Fernandes
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 773 Authorization and Token Issuance
- [PASS] Has description (1025 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 25. Epic: AP-5776

**Title:** TMF656 Service Problem v5.1.0
**Status:** In Progress
**Assignee:** Sheilja Bajaj (sheilja.bajaj@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5776](https://projects.tmforum.org/jira/browse/AP-5776)

**TMF APIs Referenced:**
- **TMF656: Service Problem Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-problem-management-api-TMF656/v5](https://www.tmforum.org/oda/open-apis/directory/service-problem-management-api-TMF656/v5)

- [WARNING] EPIC [AP-5776] has been 'In Progress' for 401 days (created 2024-08-12)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-5776] in progress for 401 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Sheilja Bajaj is active
- [PASS] Assigned to: Sheilja Bajaj
- [PASS] No comments
- [PASS] Labels: BAU, FY24-25-Q2, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.1 is current
- [PASS] Has 1 components: 656 Service Problem Management
- [PASS] Has description (918 characters)
- [PASS] FixVersion(s): v5.0.1
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF656: Service Problem Management API (Latest: v5)
### 26. Epic: AP-5710

**Title:** TMF774 Engagement Access  API v5.0.0
**Status:** In Progress
**Assignee:** Cece Li (celi@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5710](https://projects.tmforum.org/jira/browse/AP-5710)

- [WARNING] EPIC [AP-5710] has been 'In Progress' for 414 days (created 2024-07-31)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5710] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-5710] in progress for 414 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF774: API not found in database
- [WARNING] Referenced TMF API 'TMF774' not found in API database
- [PASS] Assignee Cece Li is active
- [PASS] Assigned to: Cece Li
- [PASS] No comments
- [PASS] Labels: Accelerate_Asia25, china_specjam_2024
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 774 Engagement Access API
- [PASS] Has description (919 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 27. Epic: AP-5673

**Title:** Versions naming and Branching strategy to support v5.0.1 and v5.1.0 and future versions
**Status:** In Progress
**Assignee:** Revathi Sivaji (rsivaji@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5673](https://projects.tmforum.org/jira/browse/AP-5673)

- [WARNING] EPIC [AP-5673] has no FixVersion set
- [SUGGESTION] Set a target release version for this epic
- [WARNING] EPIC [AP-5673] has been 'In Progress' for 422 days (created 2024-07-23)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5673] has not been updated in 335 days (since 2024-10-18)
- [SUGGESTION] Review and update epic status - no activity for over 180 days
- [WARNING] Epic [AP-5673] in progress for 422 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] EPIC [AP-5673] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this epic to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [PASS] Assignee Revathi Sivaji is active
- [PASS] Assigned to: Revathi Sivaji
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 2 components: DevOps, Tooling
- [PASS] Has description (115 characters)
- [PASS] Has 6 linked issues
- [PASS] Priority: Medium
### 28. Epic: AP-5651

**Title:** TMF672 User Role Permission V5.1.0
**Status:** In Progress
**Assignee:** Bruno Fernandes (bruno.sfernandes@nos.pt)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5651](https://projects.tmforum.org/jira/browse/AP-5651)

**TMF APIs Referenced:**
- **TMF672: User Role Permission Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/user-role-permission-management-api-TMF672/v5](https://www.tmforum.org/oda/open-apis/directory/user-role-permission-management-api-TMF672/v5)

- [WARNING] EPIC [AP-5651] has been 'In Progress' for 427 days (created 2024-07-17)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-5651] in progress for 427 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Bruno Fernandes is active
- [PASS] Assigned to: Bruno Fernandes
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.1.0 is current
- [PASS] Has 1 components: 672 User Roles & Permissions
- [PASS] Has description (1423 characters)
- [PASS] FixVersion(s): v5.1.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF672: User Role Permission Management API (Latest: v5)
### 29. Epic: AP-5585

**Title:** TMF638 Service Inventory V5.1.0
**Status:** In Progress
**Assignee:** Amita Giriya (amita.giriya@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5585](https://projects.tmforum.org/jira/browse/AP-5585)

**TMF APIs Referenced:**
- **TMF640: Service Activation Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5](https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5)
- **TMF638: Service Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5](https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5)

- [WARNING] EPIC [AP-5585] has been 'In Progress' for 437 days (created 2024-07-08)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-5585] in progress for 437 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Amita Giriya is active
- [PASS] Assigned to: Amita Giriya
- [PASS] No comments
- [PASS] Labels: api-team-forge
- [PASS] FixVersion 5.1.0 is current
- [PASS] Has 1 components: 638 Service Inventory Management
- [PASS] Has description (1285 characters)
- [PASS] FixVersion(s): v5.1.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF638: Service Inventory Management API (Latest: v5)
### 30. Epic: AP-5582

**Title:** TMF777 Outage API v5.0.0
**Status:** In Progress
**Assignee:** Anu Aulakh (anu.aulakh@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5582](https://projects.tmforum.org/jira/browse/AP-5582)

**TMF APIs Referenced:**
- **TMF777: Outage Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/outage-management-api-TMF777](https://www.tmforum.org/oda/open-apis/directory/outage-management-api-TMF777)

- [WARNING] EPIC [AP-5582] has been 'In Progress' for 438 days (created 2024-07-07)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5582] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-5582] in progress for 438 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Anu Aulakh is active
- [PASS] Assigned to: Anu Aulakh
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q3
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 2 components: 777 Outage, New API Proposal
- [PASS] Has description (941 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF777: Outage Management API (Latest: v5)
### 31. Epic: AP-5539

**Title:** TMF637 Product Inventory V5.0.1
**Status:** In Progress
**Assignee:** Anh Tuan NGUYEN (anhtuan.nguyen@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5539](https://projects.tmforum.org/jira/browse/AP-5539)

**TMF APIs Referenced:**
- **TMF637: Product Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-inventory-management-api-TMF637/v5](https://www.tmforum.org/oda/open-apis/directory/product-inventory-management-api-TMF637/v5)

- [WARNING] EPIC [AP-5539] has been 'In Progress' for 447 days (created 2024-06-28)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-5539] in progress for 447 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Anh Tuan NGUYEN is active
- [PASS] Assigned to: Anh Tuan NGUYEN
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, FY24-25-Q3, api-team-forge
- [PASS] FixVersion 5.0.1 is current
- [PASS] Has 1 components: 637 Product Inventory Management
- [PASS] Has description (920 characters)
- [PASS] FixVersion(s): v5.0.1
- [PASS] Has 4 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF637: Product Inventory Management API (Latest: v5)
### 32. Epic: AP-5454

**Title:** TMF673E Async  Geographic Address V5.0.0
**Status:** In Progress
**Assignee:** Naresh Jain (naresh1.jain@ril.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5454](https://projects.tmforum.org/jira/browse/AP-5454)

**TMF APIs Referenced:**
- **TMF673: Geographic Address Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/geographic-address-management-api-TMF673/v5](https://www.tmforum.org/oda/open-apis/directory/geographic-address-management-api-TMF673/v5)

- [WARNING] EPIC [AP-5454] has been 'In Progress' for 465 days (created 2024-06-10)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5454] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-5454] in progress for 465 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Naresh Jain is active
- [PASS] Assigned to: Naresh Jain
- [PASS] No comments
- [PASS] Labels: Async, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0E is current
- [PASS] Has 2 components: 673 Geographic Address Management, Async
- [PASS] Has description (921 characters)
- [PASS] FixVersion(s): v5.0.0E
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] High priority issue updated 1 days ago (acceptable)
- [PASS] Priority: High
- [PASS] References TMF673: Geographic Address Management API (Latest: v5)
### 33. Epic: AP-5348

**Title:** TMF678E Async Customer Bill V5.0.0
**Status:** In Progress
**Assignee:** Naresh Jain (naresh1.jain@ril.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5348](https://projects.tmforum.org/jira/browse/AP-5348)

**TMF APIs Referenced:**
- **TMF678: Customer Bill Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/customer-bill-management-api-TMF678/v5](https://www.tmforum.org/oda/open-apis/directory/customer-bill-management-api-TMF678/v5)

- [WARNING] EPIC [AP-5348] has been 'In Progress' for 477 days (created 2024-05-28)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-5348] in progress for 477 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Naresh Jain is active
- [PASS] Assigned to: Naresh Jain
- [PASS] No comments
- [PASS] Labels: Async, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0E is current
- [PASS] Has 2 components: 678 Customer Bill Management, Async
- [PASS] Has description (916 characters)
- [PASS] FixVersion(s): v5.0.0E
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF678: Customer Bill Management API (Latest: v5)
### 34. Epic: AP-5312

**Title:** TMF675E Async Geographic Location v5.0.0
**Status:** In Progress
**Assignee:** Naresh Jain (naresh1.jain@ril.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5312](https://projects.tmforum.org/jira/browse/AP-5312)

**TMF APIs Referenced:**
- **TMF675: Geographic Location Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/geographic-location-management-api-TMF675/v4](https://www.tmforum.org/oda/open-apis/directory/geographic-location-management-api-TMF675/v4)

- [WARNING] EPIC [AP-5312] has no description
- [SUGGESTION] Add a clear description explaining the epic's purpose and acceptance criteria
- [WARNING] EPIC [AP-5312] has been 'In Progress' for 483 days (created 2024-05-22)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5312] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-5312] in progress for 483 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Naresh Jain is active
- [PASS] Assigned to: Naresh Jain
- [PASS] No comments
- [PASS] Labels: Async, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0E is current
- [PASS] Has 2 components: 675 Geographic Location, Async
- [PASS] FixVersion(s): v5.0.0E
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF675: Geographic Location Management API (Latest: v4)
### 35. Epic: AP-5256

**Title:** TMF931 Open Gateway Onboarding and Ordering Component Suite v5.1.x
**Status:** In Progress
**Assignee:** Jesus Iglesias (jesus.iglesiasmaqueda@telefonica.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5256](https://projects.tmforum.org/jira/browse/AP-5256)

**TMF APIs Referenced:**
- **TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5](https://www.tmforum.org/oda/open-apis/directory/open-gateway-onboarding-and-ordering-component-suite-TMF931/v5)

- [WARNING] EPIC [AP-5256] has been 'In Progress' for 503 days (created 2024-05-02)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-5256] in progress for 503 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Jesus Iglesias is active
- [PASS] Assigned to: Jesus Iglesias
- [PASS] No comments
- [PASS] Labels: FY24-25-Q3, Open_Gateway, api-team-forge, unplanned_FY24-25Q1
- [PASS] FixVersion 5.1.0 is current
- [PASS] Has 1 components: 931 Operate API
- [PASS] Has description (1246 characters)
- [PASS] FixVersion(s): v5.1.0
- [PASS] Has 5 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] High priority issue updated 1 days ago (acceptable)
- [PASS] Priority: Highest
- [PASS] References TMF931: Open Gateway Onboarding and Ordering Component Suite (Latest: v5)
### 36. Epic: AP-5168

**Title:** Improve GitHub structure and information
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-5168](https://projects.tmforum.org/jira/browse/AP-5168)

- [WARNING] EPIC [AP-5168] is in progress but not assigned to anyone
- [SUGGESTION] Assign the epic to a team member responsible for its delivery
- [WARNING] EPIC [AP-5168] has no FixVersion set
- [SUGGESTION] Set a target release version for this epic
- [WARNING] EPIC [AP-5168] has been 'In Progress' for 1172 days (created 2022-07-04)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5168] has not been updated in 470 days (since 2024-06-05)
- [SUGGESTION] Review and update epic status - no activity for over 180 days
- [WARNING] Epic [AP-5168] in progress for 1172 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: Technology
- [PASS] Has description (220 characters)
- [PASS] Has 8 linked issues
- [PASS] Priority: Medium
### 37. Epic: AP-5048

**Title:** Async  Tooling work new features/functionality needed
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-5048](https://projects.tmforum.org/jira/browse/AP-5048)

**TMF APIs Referenced:**
- **TMF640: Service Activation Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5](https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5)
- **TMF727: Service Usage Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-usage-management-api-TMF727/v5](https://www.tmforum.org/oda/open-apis/directory/service-usage-management-api-TMF727/v5)
- **TMF730: Software And Compute Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/software-and-compute-management-api-TMF730/v4](https://www.tmforum.org/oda/open-apis/directory/software-and-compute-management-api-TMF730/v4)
- **TMF645: Service Qualification Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5](https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5)
- **TMF638: Service Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5](https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5)
- **TMF656: Service Problem Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-problem-management-api-TMF656/v5](https://www.tmforum.org/oda/open-apis/directory/service-problem-management-api-TMF656/v5)
- **TMF641: Service Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5](https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5)

- [WARNING] EPIC [AP-5048] is in progress but not assigned to anyone
- [SUGGESTION] Assign the epic to a team member responsible for its delivery
- [WARNING] EPIC [AP-5048] has no FixVersion set
- [SUGGESTION] Set a target release version for this epic
- [WARNING] EPIC [AP-5048] has been 'In Progress' for 694 days (created 2023-10-25)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5048] has not been updated in 273 days (since 2024-12-19)
- [SUGGESTION] Review and update epic status - no activity for over 180 days
- [WARNING] Epic [AP-5048] in progress for 694 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] EPIC [AP-5048] has 'Tooling' component and should be transferred to Git
- [SUGGESTION] Consider transferring this epic to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
- [WARNING] Issue references TMF640 (Service Activation Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [WARNING] Issue references TMF727 (Service Usage Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [WARNING] Issue references TMF645 (Service Qualification Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [WARNING] Issue references TMF638 (Service Inventory Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [WARNING] Issue references TMF656 (Service Problem Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [WARNING] Issue references TMF641 (Service Ordering Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q1
- [PASS] Has 2 components: Technology, Tooling
- [PASS] Has description (679 characters)
- [PASS] Has 5 linked issues
- [PASS] Priority: Medium
- [PASS] References TMF640: Service Activation Management API (Latest: v5)
- [PASS] References TMF727: Service Usage Management API (Latest: v5)
- [PASS] References TMF730: Software And Compute Management API (Latest: v4)
- [PASS] References TMF645: Service Qualification Management API (Latest: v5)
- [PASS] References TMF638: Service Inventory Management API (Latest: v5)
- [PASS] References TMF656: Service Problem Management API (Latest: v5)
- [PASS] References TMF641: Service Ordering Management API (Latest: v5)
### 38. Epic: AP-5024

**Title:** TMF770 Fraud Management API v5.0.0
**Status:** In Progress
**Assignee:** Anand Raval (anand.raval@verizon.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5024](https://projects.tmforum.org/jira/browse/AP-5024)

- [WARNING] EPIC [AP-5024] has been 'In Progress' for 545 days (created 2024-03-22)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-5024] in progress for 545 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF770: API not found in database
- [WARNING] Referenced TMF API 'TMF770' not found in API database
- [PASS] Assignee Anand Raval is active
- [PASS] Assigned to: Anand Raval
- [PASS] No comments
- [PASS] Labels: 2024-04-Dallas, FY24-25-Q2, api-team-forge, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 770 Fraud Management
- [PASS] Has description (921 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 39. Epic: AP-5009

**Title:** TMF769 Product Test API V5.0.0
**Status:** In Progress
**Assignee:** Florin Tene (florin.tene@cityfibre.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-5009](https://projects.tmforum.org/jira/browse/AP-5009)

**TMF APIs Referenced:**
- **TMF769: Product Test API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-test-api-TMF769/v5](https://www.tmforum.org/oda/open-apis/directory/product-test-api-TMF769/v5)

- [WARNING] EPIC [AP-5009] has been 'In Progress' for 545 days (created 2024-03-22)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-5009] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-5009] in progress for 545 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Florin Tene is active
- [PASS] Assigned to: Florin Tene
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 769 Product Test
- [PASS] Has description (914 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF769: Product Test API (Latest: v5)
### 40. Epic: AP-4923

**Title:** TMF732 Data Sharing Agreement Management API V5.0.0
**Status:** In Progress
**Assignee:** Sarah Ness (sarah.ness@telus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4923](https://projects.tmforum.org/jira/browse/AP-4923)

**TMF APIs Referenced:**
- **TMF725: Metadata Catalog Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4](https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4)

- [WARNING] EPIC [AP-4923] has been 'In Progress' for 560 days (created 2024-03-07)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-4923] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-4923] in progress for 560 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF732: API not found in database
- [WARNING] Referenced TMF API 'TMF726' not found in API database
- [WARNING] Referenced TMF API 'TMF732' not found in API database
- [WARNING] Referenced TMF API 'TMF733' not found in API database
- [WARNING] Referenced TMF API 'TMF731' not found in API database
- [PASS] Assignee Sarah Ness is active
- [PASS] Assigned to: Sarah Ness
- [PASS] No comments
- [PASS] Labels: 2024-03-Montreal, FY24-25-Q1, data_governance
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 732 Data Sharing Agreement Management
- [PASS] Has description (1784 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 41. Epic: AP-4913

**Title:** TMF731 Data Quality Management API V5.0.0
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-4913](https://projects.tmforum.org/jira/browse/AP-4913)

- [WARNING] EPIC [AP-4913] is in progress but not assigned to anyone
- [SUGGESTION] Assign the epic to a team member responsible for its delivery
- [WARNING] EPIC [AP-4913] has been 'In Progress' for 561 days (created 2024-03-06)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4913] in progress for 561 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF731: API not found in database
- [WARNING] Referenced TMF API 'TMF731' not found in API database
- [PASS] No comments
- [PASS] Labels: 2024-03-Montreal, FY24-25-Q1, data_governance
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 731 Data Quality Management
- [PASS] Has description (925 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 42. Epic: AP-4899

**Title:** TMF764 Cost Management API v5.0.0
**Status:** In Progress
**Assignee:** Anu Aulakh (anu.aulakh@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4899](https://projects.tmforum.org/jira/browse/AP-4899)

**TMF APIs Referenced:**
- **TMF764: Cost Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/cost-management-api-TMF764](https://www.tmforum.org/oda/open-apis/directory/cost-management-api-TMF764)

- [WARNING] EPIC [AP-4899] has been 'In Progress' for 562 days (created 2024-03-05)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-4899] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-4899] in progress for 562 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Anu Aulakh is active
- [PASS] Assigned to: Anu Aulakh
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 764 Cost Management
- [PASS] Has description (920 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] High priority issue updated 1 days ago (acceptable)
- [PASS] Priority: Highest
- [PASS] References TMF764: Cost Management API (Latest: v5)
### 43. Epic: AP-4856

**Title:** TMF768 Resource Role API V5.0.0
**Status:** In Progress
**Assignee:** Bruno Fernandes (bruno.sfernandes@nos.pt)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4856](https://projects.tmforum.org/jira/browse/AP-4856)

**TMF APIs Referenced:**
- **TMF768: Resource Role API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-role-api--TMF768](https://www.tmforum.org/oda/open-apis/directory/resource-role-api--TMF768)

- [WARNING] EPIC [AP-4856] has been 'In Progress' for 570 days (created 2024-02-26)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-4856] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-4856] in progress for 570 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Bruno Fernandes is active
- [PASS] Assigned to: Bruno Fernandes
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, api-team-forge, unplanned_FY24-25Q1, unplanned_FY24-25Q3
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 768 Resource Role
- [PASS] Has description (909 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF768: Resource Role API (Latest: v5)
### 44. Epic: AP-4842

**Title:** TMF728 Dunning Case management API v5.0.0
**Status:** In Progress
**Assignee:** Nitin Patil (nitinpat@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4842](https://projects.tmforum.org/jira/browse/AP-4842)

**TMF APIs Referenced:**
- **TMF728: Dunning Case Management (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/dunning-case-management-TMF728/v4](https://www.tmforum.org/oda/open-apis/directory/dunning-case-management-TMF728/v4)

- [WARNING] EPIC [AP-4842] has been 'In Progress' for 574 days (created 2024-02-22)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4842] in progress for 574 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Nitin Patil is active
- [PASS] Assigned to: Nitin Patil
- [PASS] No comments
- [PASS] Labels: FY24-25-Q1, FY24-25-Q2, api-team-forge
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 728 Dunning Case management
- [PASS] Has description (925 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF728: Dunning Case Management (Latest: v4)
### 45. Epic: AP-4826

**Title:** IG1353 How to Guide for API developers: onboarding (Create & Publish)
**Status:** In Progress
**Assignee:** Stephen Harrop (stephen.harrop@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4826](https://projects.tmforum.org/jira/browse/AP-4826)

- [WARNING] EPIC [AP-4826] has legacy FixVersion 1.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-4826] has been 'In Progress' for 580 days (created 2024-02-16)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-4826] has not been updated in 239 days (since 2025-01-22)
- [SUGGESTION] Review and update epic status - no activity for over 180 days
- [WARNING] Epic [AP-4826] in progress for 580 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Stephen Harrop is active
- [PASS] Assigned to: Stephen Harrop
- [PASS] No comments
- [PASS] Labels: Definition_of_Fit_Deliverable, FY24-25-Q1, FY24-25-Q2
- [PASS] Has 2 components: Deliverables, Non-API Specification Related Artefact
- [PASS] Has description (2458 characters)
- [PASS] FixVersion(s): v1.0.0
- [PASS] Has 6 linked issues
- [PASS] Priority: Medium
### 46. Epic: AP-4798

**Title:** TMF767 Product Usage Catalog API v5.0.0
**Status:** In Progress
**Assignee:** olivier arnaud (olivier.arnaud@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4798](https://projects.tmforum.org/jira/browse/AP-4798)

**TMF APIs Referenced:**
- **TMF767: Product Usage Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-usage-management-api-TMF767/v5](https://www.tmforum.org/oda/open-apis/directory/product-usage-management-api-TMF767/v5)
- **TMF635: Usage Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/usage-management-api-TMF635/v4](https://www.tmforum.org/oda/open-apis/directory/usage-management-api-TMF635/v4)
- **TMF620: Product Catalog Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-catalog-management-api-TMF620/v5](https://www.tmforum.org/oda/open-apis/directory/product-catalog-management-api-TMF620/v5)

- [WARNING] EPIC [AP-4798] has been 'In Progress' for 598 days (created 2024-01-29)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4798] in progress for 598 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee olivier arnaud is active
- [PASS] Assigned to: olivier arnaud
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna, FY24-25-Q2, FY24-25-Q3, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 767 Product Usage
- [PASS] Has description (1742 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF767: Product Usage Management API (Latest: v5)
### 47. Epic: AP-4685

**Title:** TMF751 Anomaly Management API v5.0.0
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4685](https://projects.tmforum.org/jira/browse/AP-4685)

- [WARNING] EPIC [AP-4685] has been 'In Progress' for 678 days (created 2023-11-10)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4685] in progress for 678 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF751: API not found in database
- [WARNING] Referenced TMF API 'TMF751' not found in API database
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] Labels: 2024-04-Dallas, AI, AN, FY24-25-Q1, FY24-25-Q2, api-team-forge
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 751 Anomaly Management
- [PASS] Has description (36 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 4 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 48. Epic: AP-4630

**Title:** TMF641 Service Ordering V4.2.0
**Status:** In Progress
**Assignee:** Amita Giriya (amita.giriya@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4630](https://projects.tmforum.org/jira/browse/AP-4630)

**TMF APIs Referenced:**
- **TMF641: Service Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5](https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5)

- [WARNING] EPIC [AP-4630] has legacy FixVersion 4.2.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-4630] has been 'In Progress' for 706 days (created 2023-10-13)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4630] in progress for 706 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF641 (Service Ordering Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Amita Giriya is active
- [PASS] Assigned to: Amita Giriya
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q2
- [PASS] Has 1 components: 641 Service Ordering Management
- [PASS] Has description (926 characters)
- [PASS] FixVersion(s): v4.2.0
- [PASS] Has 4 linked issues
- [PASS] Updated 1.1 hours ago (today)
- [PASS] Priority: Medium
- [PASS] References TMF641: Service Ordering Management API (Latest: v5)
### 49. Epic: AP-4622

**Title:** TMF935 DCS Wholesale Carrier Ethernet Product Ordering API V5.0.0
**Status:** In Progress
**Assignee:** Frank Wong (frank.wong@csgi.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4622](https://projects.tmforum.org/jira/browse/AP-4622)

- [WARNING] EPIC [AP-4622] has been 'In Progress' for 708 days (created 2023-10-11)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4622] in progress for 708 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF935: API not found in database
- [WARNING] Referenced TMF API 'TMF935' not found in API database
- [PASS] Assignee Frank Wong is active
- [PASS] Assigned to: Frank Wong
- [PASS] No comments
- [PASS] Labels: DCS
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 935 DCS Wholesale Carrier Ethernet Product Ordering
- [PASS] Has description (943 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 50. Epic: AP-4601

**Title:** TMF924 DCS 5GSlice Service Activation API V5.0.0
**Status:** In Progress
**Assignee:** Frank Wong (frank.wong@csgi.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4601](https://projects.tmforum.org/jira/browse/AP-4601)

**TMF APIs Referenced:**
- **TMF924: DCS 5GSlice Service Activation API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/dcs-5gslice-service-activation-api-TMF924/v4](https://www.tmforum.org/oda/open-apis/directory/dcs-5gslice-service-activation-api-TMF924/v4)

- [WARNING] EPIC [AP-4601] has been 'In Progress' for 708 days (created 2023-10-11)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4601] in progress for 708 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Frank Wong is active
- [PASS] Assigned to: Frank Wong
- [PASS] No comments
- [PASS] Labels: DCS
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 924 DCS 5Gslice
- [PASS] Has description (927 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF924: DCS 5GSlice Service Activation API (Latest: v4)
### 51. Epic: AP-4473

**Title:** TMF760 Product Configuration API v5.0.0
**Status:** In Progress
**Assignee:** olivier arnaud (olivier.arnaud@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4473](https://projects.tmforum.org/jira/browse/AP-4473)

**TMF APIs Referenced:**
- **TMF760: Product Configuration Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/product-configuration-management-api-TMF760/v5](https://www.tmforum.org/oda/open-apis/directory/product-configuration-management-api-TMF760/v5)

- [WARNING] EPIC [AP-4473] has been 'In Progress' for 855 days (created 2023-05-17)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-4473] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-4473] in progress for 855 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee olivier arnaud is active
- [PASS] Assigned to: olivier arnaud
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 760 Product Configuration
- [PASS] Has description (923 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF760: Product Configuration Management API (Latest: v5)
### 52. Epic: AP-4463

**Title:** TMF727 Service Usage API v5.0.0
**Status:** In Progress
**Assignee:** Sergei Lukin (sergei.lukin@telekom.de)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4463](https://projects.tmforum.org/jira/browse/AP-4463)

**TMF APIs Referenced:**
- **TMF727: Service Usage Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-usage-management-api-TMF727/v5](https://www.tmforum.org/oda/open-apis/directory/service-usage-management-api-TMF727/v5)

- [WARNING] EPIC [AP-4463] has been 'In Progress' for 857 days (created 2023-05-15)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4463] in progress for 857 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Sergei Lukin is active
- [PASS] Assigned to: Sergei Lukin
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna, FY24-25-Q1, unplanned_FY24-25Q2
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 727 Service Usage
- [PASS] Has description (897 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 5 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF727: Service Usage Management API (Latest: v5)
### 53. Epic: AP-4394

**Title:** TMF759 Private Optimized Binding API V5.0.0
**Status:** In Progress
**Assignee:** Gervais-Martial Ngueko (gervais-martial.ngueko@intl.att.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4394](https://projects.tmforum.org/jira/browse/AP-4394)

**TMF APIs Referenced:**
- **TMF759: Private Optimized Binding (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/private-optimized-binding-TMF759/v5](https://www.tmforum.org/oda/open-apis/directory/private-optimized-binding-TMF759/v5)
- **TMF702: Resource Activation Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-activation-management-api-TMF702/v4](https://www.tmforum.org/oda/open-apis/directory/resource-activation-management-api-TMF702/v4)

- [WARNING] EPIC [AP-4394] has been 'In Progress' for 897 days (created 2023-04-05)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-4394] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-4394] in progress for 897 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Gervais-Martial Ngueko is active
- [PASS] Assigned to: Gervais-Martial Ngueko
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 3 components: 759 Private Optimized Binding, 909 NaaS CS, 930 NaaS Fulfilment
- [PASS] Has description (1303 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] High priority issue updated 1 days ago (acceptable)
- [PASS] Priority: High
- [PASS] References TMF759: Private Optimized Binding (Latest: v5)
### 54. Epic: AP-4337

**Title:** TMF724 Incident Management V5.0.0
**Status:** In Progress
**Assignee:** Kevin McDonnell (kevin.mcdonnell@huawei.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4337](https://projects.tmforum.org/jira/browse/AP-4337)

**TMF APIs Referenced:**
- **TMF724: Incident Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/incident-management-api-TMF724/v4](https://www.tmforum.org/oda/open-apis/directory/incident-management-api-TMF724/v4)

- [WARNING] EPIC [AP-4337] has been 'In Progress' for 926 days (created 2023-03-07)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4337] in progress for 926 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Kevin McDonnell is active
- [PASS] Assigned to: Kevin McDonnell
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 724 Incident Management
- [PASS] Has description (922 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF724: Incident Management API (Latest: v4)
### 55. Epic: AP-4314

**Title:** TMF753 Closed Loop API v5.0.0
**Status:** In Progress
**Assignee:** Emmanuel A. Otchere (emmanuel.otchere@huawei.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4314](https://projects.tmforum.org/jira/browse/AP-4314)

**TMF APIs Referenced:**
- **TMF753: Closed Loop Management (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/closed-loop-management-TMF753/v5](https://www.tmforum.org/oda/open-apis/directory/closed-loop-management-TMF753/v5)

- [WARNING] EPIC [AP-4314] has been 'In Progress' for 927 days (created 2023-03-06)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4314] in progress for 927 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Emmanuel A. Otchere is active
- [PASS] Assigned to: Emmanuel A. Otchere
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna, AI, AN
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 753 Closed Loop Automation Management
- [PASS] Has description (929 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 7 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] High priority issue updated 1 days ago (acceptable)
- [PASS] Priority: High
- [PASS] References TMF753: Closed Loop Management (Latest: v5)
### 56. Epic: AP-4291

**Title:** TMF741 Partner Bill as a specialization of CustomerBill API V5.0.0
**Status:** In Progress
**Assignee:** Rajesh Sinha (rajesh.ra.sinha@ril.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4291](https://projects.tmforum.org/jira/browse/AP-4291)

- [WARNING] EPIC [AP-4291] has been 'In Progress' for 930 days (created 2023-03-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-4291] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-4291] in progress for 930 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF741: API not found in database
- [WARNING] Referenced TMF API 'TMF741' not found in API database
- [PASS] Assignee Rajesh Sinha is active
- [PASS] Assigned to: Rajesh Sinha
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 2 components: 741 Partner Bill as a specialization of CustomerBill API, ZTP
- [PASS] Has description (944 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 57. Epic: AP-4229

**Title:** TMF639 Resource Inventory v5.0.0
**Status:** In Progress
**Assignee:** Lutz Bettge (lutz.bettge@telekom.de)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4229](https://projects.tmforum.org/jira/browse/AP-4229)

**TMF APIs Referenced:**
- **TMF639: Resource Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5](https://www.tmforum.org/oda/open-apis/directory/resource-inventory-management-api-TMF639/v5)

- [WARNING] EPIC [AP-4229] has been 'In Progress' for 983 days (created 2023-01-09)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4229] in progress for 983 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Lutz Bettge is active
- [PASS] Assigned to: Lutz Bettge
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris, FY24-25-Q2, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 639 Resource Inventory
- [PASS] Has description (915 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF639: Resource Inventory Management API (Latest: v5)
### 58. Epic: AP-4192

**Title:** TMF924 DCS 5GSlice Service Activation API V4.0.0
**Status:** In Progress
**Assignee:** Stephen Harrop (stephen.harrop@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4192](https://projects.tmforum.org/jira/browse/AP-4192)

**TMF APIs Referenced:**
- **TMF924: DCS 5GSlice Service Activation API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/dcs-5gslice-service-activation-api-TMF924/v4](https://www.tmforum.org/oda/open-apis/directory/dcs-5gslice-service-activation-api-TMF924/v4)

- [WARNING] EPIC [AP-4192] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-4192] has been 'In Progress' for 1030 days (created 2022-11-23)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4192] in progress for 1030 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Stephen Harrop is active
- [PASS] Assigned to: Stephen Harrop
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q1
- [PASS] Has 1 components: 924 DCS 5Gslice
- [PASS] Has description (933 characters)
- [PASS] FixVersion(s): v4.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF924: DCS 5GSlice Service Activation API (Latest: v4)
### 59. Epic: AP-4168

**Title:** TMF645 Service Qualification API v4.2.0
**Status:** In Progress
**Assignee:** Anu Aulakh (anu.aulakh@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4168](https://projects.tmforum.org/jira/browse/AP-4168)

**TMF APIs Referenced:**
- **TMF645: Service Qualification Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5](https://www.tmforum.org/oda/open-apis/directory/service-qualification-management-api-TMF645/v5)

- [WARNING] EPIC [AP-4168] has legacy FixVersion 4.2.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-4168] has been 'In Progress' for 1037 days (created 2022-11-16)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4168] in progress for 1037 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF645 (Service Qualification Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Anu Aulakh is active
- [PASS] Assigned to: Anu Aulakh
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q1
- [PASS] Has 1 components: 645 Service Qualification
- [PASS] Has description (918 characters)
- [PASS] FixVersion(s): v4.2.0
- [PASS] Has 4 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF645: Service Qualification Management API (Latest: v5)
### 60. Epic: AP-4156

**Title:** TMF751 Anomaly Management API v4.0.0
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4156](https://projects.tmforum.org/jira/browse/AP-4156)

- [WARNING] EPIC [AP-4156] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-4156] has been 'In Progress' for 1044 days (created 2022-11-09)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4156] in progress for 1044 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF751: API not found in database
- [WARNING] Referenced TMF API 'TMF751' not found in API database
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 751 Anomaly Management
- [PASS] Has description (36 characters)
- [PASS] FixVersion(s): v4.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 61. Epic: AP-4128

**Title:** TMF640 Service Activation v4.2.0
**Status:** In Progress
**Assignee:** Anu Aulakh (anu.aulakh@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4128](https://projects.tmforum.org/jira/browse/AP-4128)

**TMF APIs Referenced:**
- **TMF640: Service Activation Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5](https://www.tmforum.org/oda/open-apis/directory/service-activation-management-api-TMF640/v5)

- [WARNING] EPIC [AP-4128] has legacy FixVersion 4.2.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-4128] has been 'In Progress' for 1077 days (created 2022-10-07)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4128] in progress for 1077 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF640 (Service Activation Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Anu Aulakh is active
- [PASS] Assigned to: Anu Aulakh
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2
- [PASS] Has 1 components: 640 Service Activation
- [PASS] Has description (915 characters)
- [PASS] FixVersion(s): v4.2.0
- [PASS] Has 8 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF640: Service Activation Management API (Latest: v5)
### 62. Epic: AP-4121

**Title:** TMF638 Service Inventory V4.2.0
**Status:** In Progress
**Assignee:** Amita Giriya (amita.giriya@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4121](https://projects.tmforum.org/jira/browse/AP-4121)

**TMF APIs Referenced:**
- **TMF638: Service Inventory Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5](https://www.tmforum.org/oda/open-apis/directory/service-inventory-management-api-TMF638/v5)

- [WARNING] EPIC [AP-4121] has legacy FixVersion 4.2.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-4121] has been 'In Progress' for 1077 days (created 2022-10-07)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4121] in progress for 1077 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF638 (Service Inventory Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Amita Giriya is active
- [PASS] Assigned to: Amita Giriya
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, ready-for-ctk-development
- [PASS] Has 1 components: 638 Service Inventory Management
- [PASS] Has description (914 characters)
- [PASS] FixVersion(s): v4.2.0
- [PASS] Has 10 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF638: Service Inventory Management API (Latest: v5)
### 63. Epic: AP-4104

**Title:** TMF653 Service Test API v5.0.0
**Status:** In Progress
**Assignee:** Pushan Mukerjee (pushan.mukerjee@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4104](https://projects.tmforum.org/jira/browse/AP-4104)

**TMF APIs Referenced:**
- **TMF653: Service Test Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-test-management-api-TMF653/v5](https://www.tmforum.org/oda/open-apis/directory/service-test-management-api-TMF653/v5)

- [WARNING] EPIC [AP-4104] has been 'In Progress' for 1100 days (created 2022-09-14)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4104] in progress for 1100 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Pushan Mukerjee is active
- [PASS] Assigned to: Pushan Mukerjee
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 653 Service Test Management
- [PASS] Has description (910 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF653: Service Test Management API (Latest: v5)
### 64. Epic: AP-4097

**Title:** TMF641 Service Ordering v5.0.0
**Status:** In Progress
**Assignee:** Amita Giriya (amita.giriya@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4097](https://projects.tmforum.org/jira/browse/AP-4097)

**TMF APIs Referenced:**
- **TMF641: Service Ordering Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5](https://www.tmforum.org/oda/open-apis/directory/service-ordering-management-api-TMF641/v5)

- [WARNING] EPIC [AP-4097] has been 'In Progress' for 1100 days (created 2022-09-14)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4097] in progress for 1100 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Amita Giriya is active
- [PASS] Assigned to: Amita Giriya
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 641 Service Ordering Management
- [PASS] Has description (1052 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF641: Service Ordering Management API (Latest: v5)
### 65. Epic: AP-4069

**Title:** TMF654 PrepayBalance v4.1.0
**Status:** In Progress
**Assignee:** Elisabeth Andersson (elisabeth.andersson@matrixx.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-4069](https://projects.tmforum.org/jira/browse/AP-4069)

**TMF APIs Referenced:**
- **TMF654: Prepay Balance Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/prepay-balance-management-api-TMF654/v5](https://www.tmforum.org/oda/open-apis/directory/prepay-balance-management-api-TMF654/v5)

- [WARNING] EPIC [AP-4069] has legacy FixVersion 4.1.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-4069] has been 'In Progress' for 1134 days (created 2022-08-10)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-4069] in progress for 1134 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF654 (Prepay Balance Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Elisabeth Andersson is active
- [PASS] Assigned to: Elisabeth Andersson
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q1
- [PASS] Has 1 components: 654 Prepay Balance Management
- [PASS] Has description (916 characters)
- [PASS] FixVersion(s): v4.1.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF654: Prepay Balance Management API (Latest: v5)
### 66. Epic: AP-3992

**Title:** TMF728 Dunning Case management API V4.0.0
**Status:** In Progress
**Assignee:** Nitin Patil (nitinpat@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3992](https://projects.tmforum.org/jira/browse/AP-3992)

**TMF APIs Referenced:**
- **TMF728: Dunning Case Management (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/dunning-case-management-TMF728/v4](https://www.tmforum.org/oda/open-apis/directory/dunning-case-management-TMF728/v4)

- [WARNING] EPIC [AP-3992] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3992] has been 'In Progress' for 1155 days (created 2022-07-21)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3992] in progress for 1155 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Nitin Patil is active
- [PASS] Assigned to: Nitin Patil
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 2 components: 623 SLA Management, 728 Dunning Case management
- [PASS] Has description (919 characters)
- [PASS] FixVersion(s): v4.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF728: Dunning Case Management (Latest: v4)
### 67. Epic: AP-3978

**Title:** TMF697 Work Order V4.0.0
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-3978](https://projects.tmforum.org/jira/browse/AP-3978)

**TMF APIs Referenced:**
- **TMF697: Work Order Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/work-order-management-api-TMF697/v5](https://www.tmforum.org/oda/open-apis/directory/work-order-management-api-TMF697/v5)

- [WARNING] EPIC [AP-3978] is in progress but not assigned to anyone
- [SUGGESTION] Assign the epic to a team member responsible for its delivery
- [WARNING] EPIC [AP-3978] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3978] has been 'In Progress' for 1155 days (created 2022-07-21)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3978] in progress for 1155 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF697 (Work Order Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] No comments
- [PASS] Labels: pre_production_table
- [PASS] Has 1 components: 697 Work Order
- [PASS] Has description (907 characters)
- [PASS] FixVersion(s): v4.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF697: Work Order Management API (Latest: v5)
### 68. Epic: AP-3960

**Title:** TMF670 Payment Method API v4.1.0
**Status:** In Progress
**Assignee:** Dominic Oyeniran (dominic.oyeniran@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3960](https://projects.tmforum.org/jira/browse/AP-3960)

**TMF APIs Referenced:**
- **TMF670: Payment Method Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/payment-method-management-api-TMF670/v5](https://www.tmforum.org/oda/open-apis/directory/payment-method-management-api-TMF670/v5)

- [WARNING] EPIC [AP-3960] has legacy FixVersion 4.1.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3960] has no description
- [SUGGESTION] Add a clear description explaining the epic's purpose and acceptance criteria
- [WARNING] EPIC [AP-3960] has been 'In Progress' for 1170 days (created 2022-07-06)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3960] in progress for 1170 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF670 (Payment Method Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Dominic Oyeniran is active
- [PASS] Assigned to: Dominic Oyeniran
- [PASS] No comments
- [PASS] Labels: FY24-25-Q3
- [PASS] Has 1 components: 670 Payment Methods
- [PASS] FixVersion(s): v4.1.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF670: Payment Method Management API (Latest: v5)
### 69. Epic: AP-3926

**Title:** TMF909 Network as a Service v4.2.0
**Status:** In Progress
**Assignee:** Johanne Mayer (jmayer@ciena.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3926](https://projects.tmforum.org/jira/browse/AP-3926)

**TMF APIs Referenced:**
- **TMF909: Network as a Service Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/network-as-a-service-management-api-TMF909/v4](https://www.tmforum.org/oda/open-apis/directory/network-as-a-service-management-api-TMF909/v4)

- [WARNING] EPIC [AP-3926] has legacy FixVersion 4.2.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3926] has been 'In Progress' for 1177 days (created 2022-06-29)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-3926] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-3926] in progress for 1177 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Johanne Mayer is active
- [PASS] Assigned to: Johanne Mayer
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 909 NaaS CS
- [PASS] Has description (873 characters)
- [PASS] FixVersion(s): v4.2.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF909: Network as a Service Management API (Latest: v4)
### 70. Epic: AP-3915

**Title:** TMF676 Payment V4.1.0
**Status:** In Progress
**Assignee:** Anh Tuan NGUYEN (anhtuan.nguyen@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3915](https://projects.tmforum.org/jira/browse/AP-3915)

**TMF APIs Referenced:**
- **TMF676: Payment Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/payment-management-api-TMF676/v4](https://www.tmforum.org/oda/open-apis/directory/payment-management-api-TMF676/v4)

- [WARNING] EPIC [AP-3915] has legacy FixVersion 4.1.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3915] has been 'In Progress' for 1190 days (created 2022-06-16)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3915] in progress for 1190 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Anh Tuan NGUYEN is active
- [PASS] Assigned to: Anh Tuan NGUYEN
- [PASS] No comments
- [PASS] Labels: production_table, v4.1.0
- [PASS] Has 1 components: 676 Payment Management
- [PASS] Has description (904 characters)
- [PASS] FixVersion(s): v4.1.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF676: Payment Management API (Latest: v4)
### 71. Epic: AP-3905

**Title:** TMF916 Zero-Touch Partnering API Suite v1.0.0
**Status:** In Progress
**Assignee:** Joann O'Brien (jobrien@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3905](https://projects.tmforum.org/jira/browse/AP-3905)

- [WARNING] EPIC [AP-3905] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3905] has no description
- [SUGGESTION] Add a clear description explaining the epic's purpose and acceptance criteria
- [WARNING] EPIC [AP-3905] has been 'In Progress' for 1193 days (created 2022-06-13)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-3905] has not been updated in 345 days (since 2024-10-08)
- [SUGGESTION] Review and update epic status - no activity for over 180 days
- [WARNING] Epic [AP-3905] in progress for 1193 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF916: API not found in database
- [WARNING] Referenced TMF API 'TMF916' not found in API database
- [PASS] Assignee Joann O'Brien is active
- [PASS] Assigned to: Joann O'Brien
- [PASS] No comments
- [PASS] Labels: unplanned_FY24-25Q1, v4.1.0
- [PASS] Has 1 components: 916 Zero-Touch Partnering
- [PASS] FixVersion(s): v4.0.0
- [PASS] Has 16 linked issues
- [PASS] Priority: Medium
### 72. Epic: AP-3868

**Title:** TMF918A RAN Management API Component Suite Profile v1.0.0
**Status:** In Progress
**Assignee:** Bruno Vasquez (bvazquez@deloitte.pt)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3868](https://projects.tmforum.org/jira/browse/AP-3868)

- [WARNING] EPIC [AP-3868] has no components set
- [SUGGESTION] No matching components found for TMF number 918A
- [WARNING] EPIC [AP-3868] has no description
- [SUGGESTION] Add a clear description explaining the epic's purpose and acceptance criteria
- [WARNING] EPIC [AP-3868] has no FixVersion set
- [SUGGESTION] Set a target release version for this epic
- [WARNING] EPIC [AP-3868] has been 'In Progress' for 1232 days (created 2022-05-05)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-3868] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-3868] in progress for 1232 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF918: API not found in database
- [WARNING] Referenced TMF API 'TMF918' not found in API database
- [PASS] Assignee Bruno Vasquez is active
- [PASS] Assigned to: Bruno Vasquez
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Updated 1 day ago (48.0 hours)
- [PASS] High priority issue updated 1 days ago (acceptable)
- [PASS] Priority: High
### 73. Epic: AP-3816

**Title:** TMF727 Service Usage API v4.0.0
**Status:** In Progress
**Assignee:** Varun Nair (varun.nair@team.telstra.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3816](https://projects.tmforum.org/jira/browse/AP-3816)

**TMF APIs Referenced:**
- **TMF727: Service Usage Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/service-usage-management-api-TMF727/v5](https://www.tmforum.org/oda/open-apis/directory/service-usage-management-api-TMF727/v5)

- [WARNING] EPIC [AP-3816] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3816] has been 'In Progress' for 1291 days (created 2022-03-07)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3816] in progress for 1291 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF727 (Service Usage Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Varun Nair is active
- [PASS] Assigned to: Varun Nair
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 727 Service Usage
- [PASS] Has description (897 characters)
- [PASS] FixVersion(s): v4.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF727: Service Usage Management API (Latest: v5)
### 74. Epic: AP-3793

**Title:** TMF621 Trouble Ticket v4.1.0
**Status:** In Progress
**Assignee:** Jacob Avraham (jacoba@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3793](https://projects.tmforum.org/jira/browse/AP-3793)

**TMF APIs Referenced:**
- **TMF621: Trouble Ticket Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/trouble-ticket-management-api-TMF621/v5](https://www.tmforum.org/oda/open-apis/directory/trouble-ticket-management-api-TMF621/v5)

- [WARNING] EPIC [AP-3793] has legacy FixVersion 4.1.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3793] has been 'In Progress' for 1323 days (created 2022-02-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-3793] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-3793] in progress for 1323 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF621 (Trouble Ticket Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Jacob Avraham is active
- [PASS] Assigned to: Jacob Avraham
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 2 components: 621 Trouble Ticket, ZTP
- [PASS] Has description (911 characters)
- [PASS] FixVersion(s): v4.1.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF621: Trouble Ticket Management API (Latest: v5)
### 75. Epic: AP-3776

**Title:** TMF669 Party Role Management v4.1.0
**Status:** In Progress
**Assignee:** olivier arnaud (olivier.arnaud@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3776](https://projects.tmforum.org/jira/browse/AP-3776)

**TMF APIs Referenced:**
- **TMF669: Party Role Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/party-role-management-api-TMF669/v5](https://www.tmforum.org/oda/open-apis/directory/party-role-management-api-TMF669/v5)

- [WARNING] EPIC [AP-3776] has legacy FixVersion 4.1.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3776] has been 'In Progress' for 1333 days (created 2022-01-24)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3776] in progress for 1333 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF669 (Party Role Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee olivier arnaud is active
- [PASS] Assigned to: olivier arnaud
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 2 components: 669 Party Role Management, 916 Zero-Touch Partnering
- [PASS] Has description (907 characters)
- [PASS] FixVersion(s): v4.1.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF669: Party Role Management API (Latest: v5)
### 76. Epic: AP-3759

**Title:** TMF726 Metadata Inventory Management V5.0.0
**Status:** In Progress
**Assignee:** Sarah Ness (sarah.ness@telus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3759](https://projects.tmforum.org/jira/browse/AP-3759)

**TMF APIs Referenced:**
- **TMF725: Metadata Catalog Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4](https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4)

- [WARNING] EPIC [AP-3759] has been 'In Progress' for 1355 days (created 2022-01-02)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3759] in progress for 1355 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF726: API not found in database
- [WARNING] Referenced TMF API 'TMF726' not found in API database
- [WARNING] Referenced TMF API 'TMF732' not found in API database
- [WARNING] Referenced TMF API 'TMF733' not found in API database
- [WARNING] Referenced TMF API 'TMF731' not found in API database
- [PASS] Assignee Sarah Ness is active
- [PASS] Assigned to: Sarah Ness
- [PASS] No comments
- [PASS] Labels: 2024-03-Montreal, FY24-25-Q1, api-team-forge, data_governance
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 726 Metadata Inventory Management
- [PASS] Has description (1774 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 77. Epic: AP-3752

**Title:** TMF725 Metadata Catalog Management V5.0.0
**Status:** In Progress
**Assignee:** Sarah Ness (sarah.ness@telus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3752](https://projects.tmforum.org/jira/browse/AP-3752)

**TMF APIs Referenced:**
- **TMF725: Metadata Catalog Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4](https://www.tmforum.org/oda/open-apis/directory/metadata-catalog-management-api-TMF725/v4)

- [WARNING] EPIC [AP-3752] has been 'In Progress' for 1355 days (created 2022-01-02)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3752] in progress for 1355 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Referenced TMF API 'TMF726' not found in API database
- [WARNING] Referenced TMF API 'TMF732' not found in API database
- [WARNING] Referenced TMF API 'TMF733' not found in API database
- [WARNING] Referenced TMF API 'TMF731' not found in API database
- [PASS] Assignee Sarah Ness is active
- [PASS] Assigned to: Sarah Ness
- [PASS] No comments
- [PASS] Labels: 2024-03-Montreal, FY24-25-Q1, data_governance
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 725 Metadata Catalog management
- [PASS] Has description (1772 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF725: Metadata Catalog Management API (Latest: v4)
### 78. Epic: AP-3738

**Title:** TMF723 Policy V5.0.0
**Status:** In Progress
**Assignee:** Jonathan Goldberg (jgoldberg@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3738](https://projects.tmforum.org/jira/browse/AP-3738)

**TMF APIs Referenced:**
- **TMF723: Policy Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/policy-management-api-TMF723/v5](https://www.tmforum.org/oda/open-apis/directory/policy-management-api-TMF723/v5)

- [WARNING] EPIC [AP-3738] has been 'In Progress' for 1355 days (created 2022-01-02)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3738] in progress for 1355 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Jonathan Goldberg is active
- [PASS] Assigned to: Jonathan Goldberg
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna, FY24-25-Q2, FY24-25-Q3
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 723 Policy
- [PASS] Has description (903 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF723: Policy Management API (Latest: v5)
### 79. Epic: AP-3708

**Title:** TMF717 Customer360 V4.0.0
**Status:** In Progress
**Assignee:** Shantanu Raje (shantanu.raje@rci.rogers.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3708](https://projects.tmforum.org/jira/browse/AP-3708)

**TMF APIs Referenced:**
- **TMF717: Customer360 Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/customer360-management-api-TMF717/v5](https://www.tmforum.org/oda/open-apis/directory/customer360-management-api-TMF717/v5)

- [WARNING] EPIC [AP-3708] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3708] has been 'In Progress' for 1371 days (created 2021-12-17)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3708] in progress for 1371 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF717 (Customer360 Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Shantanu Raje is active
- [PASS] Assigned to: Shantanu Raje
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 717 Customer360
- [PASS] Has description (908 characters)
- [PASS] FixVersion(s): v4.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF717: Customer360 Management API (Latest: v5)
### 80. Epic: AP-3687

**Title:** TMF713 Work Management V4.0.0
**Status:** In Progress
**Assignee:** Pierre Robitaille (pierre.robitaille@videotron.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3687](https://projects.tmforum.org/jira/browse/AP-3687)

**TMF APIs Referenced:**
- **TMF713: Work Management (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/work-management-TMF713/v4](https://www.tmforum.org/oda/open-apis/directory/work-management-TMF713/v4)

- [WARNING] EPIC [AP-3687] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3687] has been 'In Progress' for 1371 days (created 2021-12-17)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3687] in progress for 1371 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Pierre Robitaille is active
- [PASS] Assigned to: Pierre Robitaille
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 713 Work Management
- [PASS] Has description (912 characters)
- [PASS] FixVersion(s): v4.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF713: Work Management (Latest: v4)
### 81. Epic: AP-3673

**Title:** TMF711 Shipment Management V4.0.0
**Status:** In Progress
**Assignee:** Florin Tene (florin.tene@cityfibre.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3673](https://projects.tmforum.org/jira/browse/AP-3673)

**TMF APIs Referenced:**
- **TMF711: Shipment Management Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/shipment-management-management-api-TMF711/v4](https://www.tmforum.org/oda/open-apis/directory/shipment-management-management-api-TMF711/v4)

- [WARNING] EPIC [AP-3673] has legacy FixVersion 4.0.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3673] has been 'In Progress' for 1371 days (created 2021-12-17)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3673] in progress for 1371 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Florin Tene is active
- [PASS] Assigned to: Florin Tene
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna
- [PASS] Has 1 components: 711 Shipment Management
- [PASS] Has description (916 characters)
- [PASS] FixVersion(s): v4.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF711: Shipment Management Management API (Latest: v4)
### 82. Epic: AP-3665

**Title:** TMF699 Sales v4.1.0
**Status:** In Progress
**Assignee:** Gregoire Laurent (gregoire.laurent@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3665](https://projects.tmforum.org/jira/browse/AP-3665)

**TMF APIs Referenced:**
- **TMF699: Sales Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/sales-management-api-TMF699/v5](https://www.tmforum.org/oda/open-apis/directory/sales-management-api-TMF699/v5)

- [WARNING] EPIC [AP-3665] has legacy FixVersion 4.1.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3665] has been 'In Progress' for 1372 days (created 2021-12-16)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3665] in progress for 1372 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF699 (Sales Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Gregoire Laurent is active
- [PASS] Assigned to: Gregoire Laurent
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has 1 components: 699 Sales
- [PASS] Has description (902 characters)
- [PASS] FixVersion(s): v4.1.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF699: Sales Management API (Latest: v5)
### 83. Epic: AP-3657

**Title:** TMF666 - Account Management API V4.1.0
**Status:** In Progress
**Assignee:** Jonathan Goldberg (jonathan.goldberg@amdocs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3657](https://projects.tmforum.org/jira/browse/AP-3657)

**TMF APIs Referenced:**
- **TMF666: Account Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/account-management-api-TMF666/v5](https://www.tmforum.org/oda/open-apis/directory/account-management-api-TMF666/v5)

- [WARNING] EPIC [AP-3657] has legacy FixVersion 4.1.0 (< 5.0)
- [SUGGESTION] Consider updating to a current release version
- [WARNING] EPIC [AP-3657] has been 'In Progress' for 1382 days (created 2021-12-06)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3657] in progress for 1382 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] Issue references TMF666 (Account Management API) with version(s) v4 but latest available is v5
- [SUGGESTION] Consider updating to use current version v5
- [PASS] Assignee Jonathan Goldberg is active
- [PASS] Assigned to: Jonathan Goldberg
- [PASS] No comments
- [PASS] Labels: v4.1.0
- [PASS] Has 1 components: 666 Account Management
- [PASS] Has description (23 characters)
- [PASS] FixVersion(s): v4.1.0
- [PASS] Has 5 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF666: Account Management API (Latest: v5)
### 84. Epic: AP-3615

**Title:** TMF720 Digital Identity V5.0.0
**Status:** In Progress
**Assignee:** Bruno Fernandes (bruno.sfernandes@nos.pt)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3615](https://projects.tmforum.org/jira/browse/AP-3615)

**TMF APIs Referenced:**
- **TMF720: Digital Identity Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/digital-identity-management-api-TMF720/v5](https://www.tmforum.org/oda/open-apis/directory/digital-identity-management-api-TMF720/v5)

- [WARNING] EPIC [AP-3615] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3615] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Bruno Fernandes is active
- [PASS] Assigned to: Bruno Fernandes
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 720 Digital Identity
- [PASS] Has description (913 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF720: Digital Identity Management API (Latest: v5)
### 85. Epic: AP-3608

**Title:** TMF717 Customer360 V5.0.0
**Status:** In Progress
**Assignee:** Abhilash Prasad (abhilash.prasad@ril.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3608](https://projects.tmforum.org/jira/browse/AP-3608)

**TMF APIs Referenced:**
- **TMF717: Customer360 Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/customer360-management-api-TMF717/v5](https://www.tmforum.org/oda/open-apis/directory/customer360-management-api-TMF717/v5)

- [WARNING] EPIC [AP-3608] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3608] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Abhilash Prasad is active
- [PASS] Assigned to: Abhilash Prasad
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, FY24-25-Q3, api-team-forge
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 717 Customer360
- [PASS] Has description (908 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF717: Customer360 Management API (Latest: v5)
### 86. Epic: AP-3601

**Title:** TMF716 Resource Reservation V5.0.0
**Status:** In Progress
**Assignee:** Dan d'Albuquerque (dan.a@entronica.co.th)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3601](https://projects.tmforum.org/jira/browse/AP-3601)

**TMF APIs Referenced:**
- **TMF716: Resource Reservation (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-reservation-TMF716/v4](https://www.tmforum.org/oda/open-apis/directory/resource-reservation-TMF716/v4)

- [WARNING] EPIC [AP-3601] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3601] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Dan d'Albuquerque is active
- [PASS] Assigned to: Dan d'Albuquerque
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna, FY24-25-Q3, Migration
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 716 Resource Reservation
- [PASS] Has description (923 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF716: Resource Reservation (Latest: v4)
### 87. Epic: AP-3594

**Title:** TMF714 Work Qualification V5.0.0
**Status:** In Progress
**Assignee:** Florin Tene (florin.tene@cityfibre.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3594](https://projects.tmforum.org/jira/browse/AP-3594)

**TMF APIs Referenced:**
- **TMF714: Work Qualification Management (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/work-qualification-management-TMF714/v4](https://www.tmforum.org/oda/open-apis/directory/work-qualification-management-TMF714/v4)

- [WARNING] EPIC [AP-3594] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3594] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Florin Tene is active
- [PASS] Assigned to: Florin Tene
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris, FY24-25-Q2, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 714 Work Qualification
- [PASS] Has description (921 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF714: Work Qualification Management (Latest: v4)
### 88. Epic: AP-3587

**Title:** TMF713 Work Management V5.0.0
**Status:** In Progress
**Assignee:** Florin Tene (florin.tene@cityfibre.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3587](https://projects.tmforum.org/jira/browse/AP-3587)

**TMF APIs Referenced:**
- **TMF713: Work Management (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/work-management-TMF713/v4](https://www.tmforum.org/oda/open-apis/directory/work-management-TMF713/v4)

- [WARNING] EPIC [AP-3587] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3587] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Florin Tene is active
- [PASS] Assigned to: Florin Tene
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 713 Work Management
- [PASS] Has description (918 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF713: Work Management (Latest: v4)
### 89. Epic: AP-3573

**Title:** TMF711 Shipment Management V5.0.0
**Status:** In Progress
**Assignee:** Sergei Lukin (sergei.lukin@telekom.de)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3573](https://projects.tmforum.org/jira/browse/AP-3573)

**TMF APIs Referenced:**
- **TMF711: Shipment Management Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/shipment-management-management-api-TMF711/v4](https://www.tmforum.org/oda/open-apis/directory/shipment-management-management-api-TMF711/v4)

- [WARNING] EPIC [AP-3573] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3573] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Sergei Lukin is active
- [PASS] Assigned to: Sergei Lukin
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 711 Shipment Management
- [PASS] Has description (922 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF711: Shipment Management Management API (Latest: v4)
### 90. Epic: AP-3510

**Title:** TMF702 Resource Activation V5.0.0
**Status:** In Progress
**Assignee:** Goutham Babu (gbabu@tmforum.org)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3510](https://projects.tmforum.org/jira/browse/AP-3510)

**TMF APIs Referenced:**
- **TMF702: Resource Activation Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-activation-management-api-TMF702/v4](https://www.tmforum.org/oda/open-apis/directory/resource-activation-management-api-TMF702/v4)

- [WARNING] EPIC [AP-3510] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] EPIC [AP-3510] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this epic
- [WARNING] Epic [AP-3510] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Goutham Babu is active
- [PASS] Assigned to: Goutham Babu
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna, FY24-25-Q3, Migration
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 702 Resource Activation & Configuration
- [PASS] Has description (922 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF702: Resource Activation Management API (Latest: v4)
### 91. Epic: AP-3503

**Title:** TMF701 Process v5.0.0
**Status:** In Progress
**Assignee:** Amani Dkhil (amani.dkhil@sofrecom.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3503](https://projects.tmforum.org/jira/browse/AP-3503)

**TMF APIs Referenced:**
- **TMF701: Process Flow Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5](https://www.tmforum.org/oda/open-apis/directory/process-flow-management-api-TMF701/v5)

- [WARNING] EPIC [AP-3503] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3503] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Amani Dkhil is active
- [PASS] Assigned to: Amani Dkhil
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris, FY24-25-Q2, FY24-25-Q3, ODA
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 701 Work Flow
- [PASS] Has description (909 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 50 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] High priority issue updated 1 days ago (acceptable)
- [PASS] Priority: High
- [PASS] References TMF701: Process Flow Management API (Latest: v5)
### 92. Epic: AP-3496

**Title:** TMF700 Shipping Order V5.0.0
**Status:** In Progress
**Assignee:** Akram Mohammed (akram.mohammed4@tcs.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3496](https://projects.tmforum.org/jira/browse/AP-3496)

**TMF APIs Referenced:**
- **TMF700: Shipping Order Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/shipping-order-management-api-TMF700/v5](https://www.tmforum.org/oda/open-apis/directory/shipping-order-management-api-TMF700/v5)

- [WARNING] EPIC [AP-3496] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3496] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Akram Mohammed is active
- [PASS] Assigned to: Akram Mohammed
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris, FY24-25-Q2
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 700 Shipping Order Management
- [PASS] Has description (917 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF700: Shipping Order Management API (Latest: v5)
### 93. Epic: AP-3482

**Title:** TMF697 Work Order V5.0.0
**Status:** In Progress
**Assignee:** Florin Tene (florin.tene@cityfibre.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3482](https://projects.tmforum.org/jira/browse/AP-3482)

**TMF APIs Referenced:**
- **TMF697: Work Order Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/work-order-management-api-TMF697/v5](https://www.tmforum.org/oda/open-apis/directory/work-order-management-api-TMF697/v5)

- [WARNING] EPIC [AP-3482] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3482] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Florin Tene is active
- [PASS] Assigned to: Florin Tene
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 697 Work Order
- [PASS] Has description (907 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF697: Work Order Management API (Latest: v5)
### 94. Epic: AP-3475

**Title:** TMF696 Risk Management V5.0.0
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-3475](https://projects.tmforum.org/jira/browse/AP-3475)

**TMF APIs Referenced:**
- **TMF696: Risk Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/risk-management-api-TMF696/v5](https://www.tmforum.org/oda/open-apis/directory/risk-management-api-TMF696/v5)

- [WARNING] EPIC [AP-3475] is in progress but not assigned to anyone
- [SUGGESTION] Assign the epic to a team member responsible for its delivery
- [WARNING] EPIC [AP-3475] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3475] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] Labels: 2024-06-Paris, FY24-25-Q2, FY24-25-Q3
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 696 Risk Management
- [PASS] Has description (912 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF696: Risk Management API (Latest: v5)
### 95. Epic: AP-3468

**Title:** TMF695 Distributed Ledger V5.0.0
**Status:** In Progress
**Assignee:** Carl Thobane (carl.thobane@globetom.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3468](https://projects.tmforum.org/jira/browse/AP-3468)

- [WARNING] EPIC [AP-3468] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3468] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF695: API not found in database
- [WARNING] Referenced TMF API 'TMF695' not found in API database
- [PASS] Assignee Carl Thobane is active
- [PASS] Assigned to: Carl Thobane
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 695 Distributed Ledger
- [PASS] Has description (921 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 96. Epic: AP-3461

**Title:** TMF691 Federated ID V5.0.0
**Status:** In Progress
**Assignee:** Dominic Oyeniran (dominic.oyeniran@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3461](https://projects.tmforum.org/jira/browse/AP-3461)

**TMF APIs Referenced:**
- **TMF691: Federated ID Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/federated-id-management-api-TMF691/v5](https://www.tmforum.org/oda/open-apis/directory/federated-id-management-api-TMF691/v5)

- [WARNING] EPIC [AP-3461] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3461] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Dominic Oyeniran is active
- [PASS] Assigned to: Dominic Oyeniran
- [PASS] No comments
- [PASS] Labels: FY24-25-Q2, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 691 Federated Identity
- [PASS] Has description (909 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 2 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF691: Federated ID Management API (Latest: v5)
### 97. Epic: AP-3454

**Title:** TMF689 Resource Portability V5.0.0
**Status:** In Progress
**Assignee:** Abhilash Prasad (abhilash.prasad@ril.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3454](https://projects.tmforum.org/jira/browse/AP-3454)

- [WARNING] EPIC [AP-3454] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3454] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [WARNING] References TMF689: API not found in database
- [WARNING] Referenced TMF API 'TMF689' not found in API database
- [PASS] Assignee Abhilash Prasad is active
- [PASS] Assigned to: Abhilash Prasad
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna, FY24-25-Q3, Migration, api-team-forge
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 689 Resource Portability
- [PASS] Has description (923 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
### 98. Epic: AP-3440

**Title:** TMF687 Stock V5.0.0
**Status:** In Progress
**Assignee:** Anh Tuan NGUYEN (anhtuan.nguyen@orange.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3440](https://projects.tmforum.org/jira/browse/AP-3440)

**TMF APIs Referenced:**
- **TMF687: Stock Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/stock-management-api-TMF687/v4](https://www.tmforum.org/oda/open-apis/directory/stock-management-api-TMF687/v4)

- [WARNING] EPIC [AP-3440] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3440] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Anh Tuan NGUYEN is active
- [PASS] Assigned to: Anh Tuan NGUYEN
- [PASS] No comments
- [PASS] Labels: 2024-04-Dallas, 2024-06-Paris, 2024-09-Vienna, FY24-25-Q2, unplanned_FY24-25Q1
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 687 Stock Management
- [PASS] Has description (908 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 3 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF687: Stock Management API (Latest: v4)
### 99. Epic: AP-3433

**Title:** TMF686 Topology V5.0.0
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3433](https://projects.tmforum.org/jira/browse/AP-3433)

**TMF APIs Referenced:**
- **TMF686: Topology Management API (Latest: v4)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/topology-management-api-TMF686/v4](https://www.tmforum.org/oda/open-apis/directory/topology-management-api-TMF686/v4)

- [WARNING] EPIC [AP-3433] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3433] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] Labels: 2024-04-Dallas, FY24-25-Q2, api-team-forge
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 686 Topology
- [PASS] Has description (911 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF686: Topology Management API (Latest: v4)
### 100. Epic: AP-3426

**Title:** TMF685 Resource Pool V5.0.0
**Status:** In Progress
**Assignee:** Dan d'Albuquerque (dan.a@entronica.co.th)
**URL:** [https://projects.tmforum.org/jira/browse/AP-3426](https://projects.tmforum.org/jira/browse/AP-3426)

**TMF APIs Referenced:**
- **TMF685: Resource Pool Management API (Latest: v5)**
  - Documentation: [https://www.tmforum.org/oda/open-apis/directory/resource-pool-management-api-TMF685](https://www.tmforum.org/oda/open-apis/directory/resource-pool-management-api-TMF685)

- [WARNING] EPIC [AP-3426] has been 'In Progress' for 1385 days (created 2021-12-03)
- [SUGGESTION] Review epic scope - in progress for over 365 days. Consider breaking into smaller items.
- [WARNING] Epic [AP-3426] in progress for 1385 days (>365 day threshold)
- [SUGGESTION] Review epic scope and progress - consider breaking down or reassigning
- [PASS] Assignee Dan d'Albuquerque is active
- [PASS] Assigned to: Dan d'Albuquerque
- [PASS] No comments
- [PASS] Labels: 2024-09-Vienna, FY24-25-Q3
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 685 Resource Pool Management
- [PASS] Has description (916 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] Has 1 linked issues
- [PASS] Updated 1 day ago (31.3 hours)
- [PASS] Priority: Medium
- [PASS] References TMF685: Resource Pool Management API (Latest: v5)
- [SUMMARY] Epic Summary:
Issues checked: 100
Total violations: 347
Violations by severity:
WARNING: 346
ERROR: 1
Average violations per issue: 3.5
- [WARNING] Data Quality: NEEDS ATTENTION - Multiple issues found

## Checking Sub-Task Issues

**JQL Query:** `project = AP AND type = "Sub-task" AND status not in ("Closed", "Resolved", "Done") AND (updated >= "-6M" OR status = "In Progress")`

- [WARNING] JQL Warnings: Field 'type' may not be accessible
- [PERFORMANCE] Performance Warnings: Date queries without ORDER BY may be slow
1. Sub-task: AP-6544
**Title:** Explanation of "State" vs. "Status"
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6544](https://projects.tmforum.org/jira/browse/AP-6544)

- [ERROR] SUB-TASK [AP-6544] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6544] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6544] has not been updated in 237 days (since 2025-01-23)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6544] in progress for 248 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 763 API Design guidelines
- [PASS] Has description (131 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 248 days (reasonable timeframe)
- [PASS] Priority: Medium
2. Sub-task: AP-6540
**Title:** Define folder structure and naming convention for DCS
**Status:** In Progress
**Assignee:** Lutz Bettge (lutz.bettge@telekom.de)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6540](https://projects.tmforum.org/jira/browse/AP-6540)

- [ERROR] SUB-TASK [AP-6540] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6540] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6540] has not been updated in 245 days (since 2025-01-16)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6540] in progress for 248 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Lutz Bettge is active
- [PASS] Assigned to: Lutz Bettge
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 763 API Design guidelines
- [PASS] Has description (587 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 248 days (reasonable timeframe)
- [PASS] Priority: Medium
3. Sub-task: AP-6539
**Title:** Domains in schemas folder structure
**Status:** In Progress
**Assignee:** Kamal Maghsoudlou (kamal.maghsoudlou@ericsson.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6539](https://projects.tmforum.org/jira/browse/AP-6539)

- [ERROR] SUB-TASK [AP-6539] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6539] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6539] has not been updated in 245 days (since 2025-01-16)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6539] in progress for 248 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Kamal Maghsoudlou is active
- [PASS] Assigned to: Kamal Maghsoudlou
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 763 API Design guidelines
- [PASS] Has description (902 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 248 days (reasonable timeframe)
- [PASS] Priority: Medium
4. Sub-task: AP-6538
**Title:** Folder structure
**Status:** In Progress
**Assignee:** Lutz Bettge (lutz.bettge@telekom.de)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6538](https://projects.tmforum.org/jira/browse/AP-6538)

- [ERROR] SUB-TASK [AP-6538] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6538] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6538] has not been updated in 245 days (since 2025-01-16)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6538] in progress for 248 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Lutz Bettge is active
- [PASS] Assigned to: Lutz Bettge
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has 1 components: 763 API Design guidelines
- [PASS] Has description (156 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 248 days (reasonable timeframe)
- [PASS] Priority: Medium
5. Sub-task: AP-6532
**Title:** Appointment OAS Response & Request Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6532](https://projects.tmforum.org/jira/browse/AP-6532)

- [ERROR] SUB-TASK [AP-6532] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6532] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6532] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6532] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6532] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6532] in progress for 251 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
6. Sub-task: AP-6531
**Title:** Product Test OAS Response & Request Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6531](https://projects.tmforum.org/jira/browse/AP-6531)

- [ERROR] SUB-TASK [AP-6531] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6531] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6531] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6531] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6531] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6531] in progress for 251 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Has 2 linked issues
- [PASS] Priority: Medium
7. Sub-task: AP-6530
**Title:** Appointment OAS Resource Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6530](https://projects.tmforum.org/jira/browse/AP-6530)

- [ERROR] SUB-TASK [AP-6530] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6530] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6530] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6530] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6530] in progress for 251 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has description (113 characters)
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
8. Sub-task: AP-6529
**Title:** Product Test OAS Resource Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6529](https://projects.tmforum.org/jira/browse/AP-6529)

- [ERROR] SUB-TASK [AP-6529] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6529] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6529] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6529] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6529] in progress for 251 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has description (113 characters)
- [PASS] In progress for 251 days (reasonable timeframe)
- [PASS] Has 2 linked issues
- [PASS] Priority: Medium
9. Sub-task: AP-6496
**Title:** Appointment OAS
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6496](https://projects.tmforum.org/jira/browse/AP-6496)

- [ERROR] SUB-TASK [AP-6496] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6496] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6496] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6496] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6496] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] Sub-task [AP-6496] in progress for 252 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] In progress for 252 days (reasonable timeframe)
- [PASS] Updated 122 days ago
- [PASS] Priority: Medium
10. Sub-task: AP-6495
**Title:** Product Test OAS
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6495](https://projects.tmforum.org/jira/browse/AP-6495)

- [ERROR] SUB-TASK [AP-6495] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6495] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6495] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6495] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6495] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6495] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6495] in progress for 252 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] In progress for 252 days (reasonable timeframe)
- [PASS] Priority: Medium
11. Sub-task: AP-6494
**Title:** TMF938: Creation of JSON Schema - Product Inventory
**Status:** In Progress
**Assignee:** Bartosz Michalik (bartosz.michalik@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6494](https://projects.tmforum.org/jira/browse/AP-6494)

- [ERROR] SUB-TASK [AP-6494] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6494] has no components set
- [SUGGESTION] No matching components found for TMF number 938:
- [WARNING] SUB-TASK [AP-6494] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6494] has not been updated in 252 days (since 2025-01-09)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6494] in progress for 252 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [WARNING] References TMF938: API not found in database
- [WARNING] Referenced TMF API 'TMF938' not found in API database
- [PASS] Assignee Bartosz Michalik is active
- [PASS] Assigned to: Bartosz Michalik
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has description (230 characters)
- [PASS] In progress for 252 days (reasonable timeframe)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
12. Sub-task: AP-6447
**Title:** Product Offering Qualification OAS Resource Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6447](https://projects.tmforum.org/jira/browse/AP-6447)

- [ERROR] SUB-TASK [AP-6447] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6447] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6447] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6447] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6447] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6447] in progress for 281 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has description (141 characters)
- [PASS] In progress for 281 days (reasonable timeframe)
- [PASS] Priority: Medium
13. Sub-task: AP-6446
**Title:** Product Offering OAS Resource Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6446](https://projects.tmforum.org/jira/browse/AP-6446)

- [ERROR] SUB-TASK [AP-6446] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6446] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6446] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6446] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6446] in progress for 281 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has description (113 characters)
- [PASS] In progress for 281 days (reasonable timeframe)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
14. Sub-task: AP-6445
**Title:** Geo-graphical address and site OAS Resource Example
**Status:** In Progress
**Assignee:** Stephen Harrop (stephen.harrop@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6445](https://projects.tmforum.org/jira/browse/AP-6445)

- [ERROR] SUB-TASK [AP-6445] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6445] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6445] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6445] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6445] has not been updated in 195 days (since 2025-03-07)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6445] in progress for 281 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Stephen Harrop is active
- [PASS] Assigned to: Stephen Harrop
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has description (141 characters)
- [PASS] In progress for 281 days (reasonable timeframe)
- [PASS] Priority: Medium
15. Sub-task: AP-6444
**Title:** Product Specification OAS Resource Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6444](https://projects.tmforum.org/jira/browse/AP-6444)

- [ERROR] SUB-TASK [AP-6444] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6444] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6444] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6444] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6444] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6444] in progress for 281 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has description (123 characters)
- [PASS] In progress for 281 days (reasonable timeframe)
- [PASS] Priority: Medium
16. Sub-task: AP-6443
**Title:** Product Inventory OAS Resource Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6443](https://projects.tmforum.org/jira/browse/AP-6443)

- [ERROR] SUB-TASK [AP-6443] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6443] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6443] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6443] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6443] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6443] in progress for 281 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has description (115 characters)
- [PASS] In progress for 281 days (reasonable timeframe)
- [PASS] Priority: Medium
17. Sub-task: AP-6442
**Title:** Product Ordering OAS Resource Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6442](https://projects.tmforum.org/jira/browse/AP-6442)

- [ERROR] SUB-TASK [AP-6442] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6442] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6442] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6442] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6442] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6442] in progress for 281 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] Has description (107 characters)
- [PASS] In progress for 281 days (reasonable timeframe)
- [PASS] Priority: Medium
18. Sub-task: AP-6417
**Title:** TMF938: Creation of JSON Schema - Product Ordering
**Status:** In Progress
**Assignee:** Bartosz Michalik (bartosz.michalik@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6417](https://projects.tmforum.org/jira/browse/AP-6417)

- [ERROR] SUB-TASK [AP-6417] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6417] has no components set
- [SUGGESTION] No matching components found for TMF number 938:
- [WARNING] SUB-TASK [AP-6417] has not been updated in 252 days (since 2025-01-09)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6417] in progress for 293 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [WARNING] References TMF938: API not found in database
- [WARNING] Referenced TMF API 'TMF938' not found in API database
- [PASS] Assignee Bartosz Michalik is active
- [PASS] Assigned to: Bartosz Michalik
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (254 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 293 days (reasonable timeframe)
- [PASS] Has 3 linked issues
- [PASS] Priority: Medium
19. Sub-task: AP-6416
**Title:** TMF938: Creation of JSON Schema - Address
**Status:** In Progress
**Assignee:** Bartosz Michalik (bartosz.michalik@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6416](https://projects.tmforum.org/jira/browse/AP-6416)

- [ERROR] SUB-TASK [AP-6416] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6416] has no components set
- [SUGGESTION] No matching components found for TMF number 938:
- [WARNING] SUB-TASK [AP-6416] has not been updated in 252 days (since 2025-01-09)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6416] in progress for 293 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [WARNING] References TMF938: API not found in database
- [WARNING] Referenced TMF API 'TMF938' not found in API database
- [PASS] Assignee Bartosz Michalik is active
- [PASS] Assigned to: Bartosz Michalik
- [PASS] No comments
- [PASS] No labels assigned
- [PASS] FixVersion 5.0.0 is current
- [PASS] Has description (53 characters)
- [PASS] FixVersion(s): v5.0.0
- [PASS] In progress for 293 days (reasonable timeframe)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
20. Sub-task: AP-6229
**Title:** Geo-graphical address and site  OAS
**Status:** In Progress
**Assignee:** Stephen Harrop (stephen.harrop@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6229](https://projects.tmforum.org/jira/browse/AP-6229)

- [ERROR] SUB-TASK [AP-6229] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6229] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6229] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6229] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] Sub-task [AP-6229] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Stephen Harrop is active
- [PASS] Assigned to: Stephen Harrop
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Has 3 linked issues
- [PASS] Updated 122 days ago
- [PASS] Priority: Medium
21. Sub-task: AP-6228
**Title:** Product Specification OAS
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6228](https://projects.tmforum.org/jira/browse/AP-6228)

- [ERROR] SUB-TASK [AP-6228] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6228] is in progress but not assigned to anyone
- [SUGGESTION] Assign the sub-task to a team member responsible for its delivery
- [WARNING] SUB-TASK [AP-6228] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6228] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6228] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6228] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6228] has not been updated in 195 days (since 2025-03-07)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6228] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Priority: Medium
22. Sub-task: AP-6227
**Title:** Product Inventory OAS
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6227](https://projects.tmforum.org/jira/browse/AP-6227)

- [ERROR] SUB-TASK [AP-6227] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6227] is in progress but not assigned to anyone
- [SUGGESTION] Assign the sub-task to a team member responsible for its delivery
- [WARNING] SUB-TASK [AP-6227] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6227] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6227] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6227] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6227] has not been updated in 195 days (since 2025-03-07)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6227] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Priority: Medium
23. Sub-task: AP-6226
**Title:** Product Offering Qualification OAS
**Status:** In Progress
**Assignee:** Bartosz Michalik (bartosz.michalik@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6226](https://projects.tmforum.org/jira/browse/AP-6226)

- [ERROR] SUB-TASK [AP-6226] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6226] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6226] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6226] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6226] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] Sub-task [AP-6226] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Bartosz Michalik is active
- [PASS] Assigned to: Bartosz Michalik
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Updated 69 days ago
- [PASS] Priority: Medium
24. Sub-task: AP-6225
**Title:** Product Offering OAS
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6225](https://projects.tmforum.org/jira/browse/AP-6225)

- [ERROR] SUB-TASK [AP-6225] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6225] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6225] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6225] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6225] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6225] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6225] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Priority: Medium
25. Sub-task: AP-6224
**Title:** Product Ordering OAS
**Status:** In Progress
**Assignee:** Unassigned
**URL:** [https://projects.tmforum.org/jira/browse/AP-6224](https://projects.tmforum.org/jira/browse/AP-6224)

- [ERROR] SUB-TASK [AP-6224] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6224] is in progress but not assigned to anyone
- [SUGGESTION] Assign the sub-task to a team member responsible for its delivery
- [WARNING] SUB-TASK [AP-6224] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6224] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6224] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6224] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6224] has not been updated in 195 days (since 2025-03-07)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6224] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Priority: Medium
26. Sub-task: AP-6223
**Title:** Geo-graphical address and site OAS Response & Request Example
**Status:** In Progress
**Assignee:** Stephen Harrop (stephen.harrop@vodafone.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6223](https://projects.tmforum.org/jira/browse/AP-6223)

- [ERROR] SUB-TASK [AP-6223] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6223] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6223] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6223] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6223] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6223] has not been updated in 195 days (since 2025-03-07)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6223] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Stephen Harrop is active
- [PASS] Assigned to: Stephen Harrop
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Priority: Medium
27. Sub-task: AP-6222
**Title:** Product Specification OAS Response & Request Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6222](https://projects.tmforum.org/jira/browse/AP-6222)

- [ERROR] SUB-TASK [AP-6222] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6222] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6222] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6222] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6222] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6222] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6222] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Priority: Medium
28. Sub-task: AP-6221
**Title:** Product Inventory OAS Response & Request Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6221](https://projects.tmforum.org/jira/browse/AP-6221)

- [ERROR] SUB-TASK [AP-6221] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6221] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6221] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6221] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6221] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6221] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6221] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Priority: Medium
29. Sub-task: AP-6220
**Title:** Product Offering Qualification OAS Response & Request Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6220](https://projects.tmforum.org/jira/browse/AP-6220)

- [ERROR] SUB-TASK [AP-6220] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6220] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6220] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6220] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6220] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6220] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Has 1 linked issues
- [PASS] Priority: Medium
30. Sub-task: AP-6219
**Title:** Product Offering OAS Response & Request Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6219](https://projects.tmforum.org/jira/browse/AP-6219)

- [ERROR] SUB-TASK [AP-6219] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6219] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6219] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6219] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6219] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6219] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6219] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Priority: Medium
31. Sub-task: AP-6218
**Title:** Product Ordering OAS Response & Request Example
**Status:** In Progress
**Assignee:** Boris Trinajstic (boris.trinajstic@amartus.com)
**URL:** [https://projects.tmforum.org/jira/browse/AP-6218](https://projects.tmforum.org/jira/browse/AP-6218)

- [ERROR] SUB-TASK [AP-6218] has no parent issue
- [SUGGESTION] Link this sub-task to its parent Story or Epic
- [WARNING] SUB-TASK [AP-6218] has no components set
- [SUGGESTION] Add relevant component(s) to categorize this sub-task
- [WARNING] SUB-TASK [AP-6218] has no description
- [SUGGESTION] Add a clear description explaining the sub-task's purpose and acceptance criteria
- [WARNING] SUB-TASK [AP-6218] has no FixVersion set
- [SUGGESTION] Set a target release version for this sub-task
- [WARNING] SUB-TASK [AP-6218] has no linked JIRAs
- [SUGGESTION] Link related stories, tasks, or bugs to this sub-task
- [WARNING] SUB-TASK [AP-6218] has not been updated in 231 days (since 2025-01-30)
- [SUGGESTION] Review and update sub-task status - no activity for over 180 days
- [WARNING] Sub-task [AP-6218] in progress for 318 days (>7 day threshold)
- [SUGGESTION] Review sub-task scope and progress - consider breaking down or reassigning
- [PASS] Assignee Boris Trinajstic is active
- [PASS] Assigned to: Boris Trinajstic
- [PASS] No comments
- [PASS] Labels: template
- [PASS] In progress for 318 days (reasonable timeframe)
- [PASS] Priority: Medium
- [SUMMARY] Sub-task Summary:
Issues checked: 31
Total violations: 188
Violations by severity:
WARNING: 157
ERROR: 31
Average violations per issue: 6.1
- [POOR] Data Quality: POOR - Many issues require immediate attention
## Label Usage Report

- [SUMMARY]:
Total unique labels found: 41
- **Total label usages:** 271
- **Average labels per issue:** 2.2

- [LABELS] Label Details (sorted by usage count):
### 1. Label: 'FY24-25-Q2' (used 32 times)

Epics (21):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5776](https://projects.tmforum.org/jira/browse/AP-5776)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5539](https://projects.tmforum.org/jira/browse/AP-5539)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5024](https://projects.tmforum.org/jira/browse/AP-5024)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4856](https://projects.tmforum.org/jira/browse/AP-4856)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4842](https://projects.tmforum.org/jira/browse/AP-4842)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4826](https://projects.tmforum.org/jira/browse/AP-4826)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4798](https://projects.tmforum.org/jira/browse/AP-4798)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4685](https://projects.tmforum.org/jira/browse/AP-4685)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4229](https://projects.tmforum.org/jira/browse/AP-4229)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4128](https://projects.tmforum.org/jira/browse/AP-4128)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4121](https://projects.tmforum.org/jira/browse/AP-4121)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3738](https://projects.tmforum.org/jira/browse/AP-3738)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3615](https://projects.tmforum.org/jira/browse/AP-3615)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3608](https://projects.tmforum.org/jira/browse/AP-3608)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3594](https://projects.tmforum.org/jira/browse/AP-3594)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3503](https://projects.tmforum.org/jira/browse/AP-3503)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3496](https://projects.tmforum.org/jira/browse/AP-3496)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3475](https://projects.tmforum.org/jira/browse/AP-3475)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3461](https://projects.tmforum.org/jira/browse/AP-3461)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3440](https://projects.tmforum.org/jira/browse/AP-3440)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3433](https://projects.tmforum.org/jira/browse/AP-3433)

Tasks (11):
**URL:** [https://projects.tmforum.org/jira/browse/AP-7080](https://projects.tmforum.org/jira/browse/AP-7080)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7079](https://projects.tmforum.org/jira/browse/AP-7079)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7078](https://projects.tmforum.org/jira/browse/AP-7078)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6572](https://projects.tmforum.org/jira/browse/AP-6572)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4892](https://projects.tmforum.org/jira/browse/AP-4892)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4823](https://projects.tmforum.org/jira/browse/AP-4823)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4388](https://projects.tmforum.org/jira/browse/AP-4388)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4385](https://projects.tmforum.org/jira/browse/AP-4385)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4236](https://projects.tmforum.org/jira/browse/AP-4236)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4235](https://projects.tmforum.org/jira/browse/AP-4235)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4234](https://projects.tmforum.org/jira/browse/AP-4234)

### 2. Label: 'FY24-25-Q3' (used 27 times)

Bugs (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5230](https://projects.tmforum.org/jira/browse/AP-5230)

Epics (12):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5539](https://projects.tmforum.org/jira/browse/AP-5539)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5256](https://projects.tmforum.org/jira/browse/AP-5256)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4798](https://projects.tmforum.org/jira/browse/AP-4798)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3960](https://projects.tmforum.org/jira/browse/AP-3960)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3738](https://projects.tmforum.org/jira/browse/AP-3738)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3608](https://projects.tmforum.org/jira/browse/AP-3608)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3601](https://projects.tmforum.org/jira/browse/AP-3601)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3510](https://projects.tmforum.org/jira/browse/AP-3510)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3503](https://projects.tmforum.org/jira/browse/AP-3503)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3475](https://projects.tmforum.org/jira/browse/AP-3475)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3454](https://projects.tmforum.org/jira/browse/AP-3454)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3426](https://projects.tmforum.org/jira/browse/AP-3426)

Tasks (14):
**URL:** [https://projects.tmforum.org/jira/browse/AP-7080](https://projects.tmforum.org/jira/browse/AP-7080)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7079](https://projects.tmforum.org/jira/browse/AP-7079)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7078](https://projects.tmforum.org/jira/browse/AP-7078)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6572](https://projects.tmforum.org/jira/browse/AP-6572)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6536](https://projects.tmforum.org/jira/browse/AP-6536)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6432](https://projects.tmforum.org/jira/browse/AP-6432)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6179](https://projects.tmforum.org/jira/browse/AP-6179)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6054](https://projects.tmforum.org/jira/browse/AP-6054)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5578](https://projects.tmforum.org/jira/browse/AP-5578)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4950](https://projects.tmforum.org/jira/browse/AP-4950)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4558](https://projects.tmforum.org/jira/browse/AP-4558)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4236](https://projects.tmforum.org/jira/browse/AP-4236)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4235](https://projects.tmforum.org/jira/browse/AP-4235)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4234](https://projects.tmforum.org/jira/browse/AP-4234)

### 3. Label: 'unplanned_FY24-25Q1' (used 24 times)

Bugs (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5516](https://projects.tmforum.org/jira/browse/AP-5516)

**URL:** [https://projects.tmforum.org/jira/browse/AP-2053](https://projects.tmforum.org/jira/browse/AP-2053)

Epics (19):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5776](https://projects.tmforum.org/jira/browse/AP-5776)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5454](https://projects.tmforum.org/jira/browse/AP-5454)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5348](https://projects.tmforum.org/jira/browse/AP-5348)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5312](https://projects.tmforum.org/jira/browse/AP-5312)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5256](https://projects.tmforum.org/jira/browse/AP-5256)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5048](https://projects.tmforum.org/jira/browse/AP-5048)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5024](https://projects.tmforum.org/jira/browse/AP-5024)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4856](https://projects.tmforum.org/jira/browse/AP-4856)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4798](https://projects.tmforum.org/jira/browse/AP-4798)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4337](https://projects.tmforum.org/jira/browse/AP-4337)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4229](https://projects.tmforum.org/jira/browse/AP-4229)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4192](https://projects.tmforum.org/jira/browse/AP-4192)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4168](https://projects.tmforum.org/jira/browse/AP-4168)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4069](https://projects.tmforum.org/jira/browse/AP-4069)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3905](https://projects.tmforum.org/jira/browse/AP-3905)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3615](https://projects.tmforum.org/jira/browse/AP-3615)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3594](https://projects.tmforum.org/jira/browse/AP-3594)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3461](https://projects.tmforum.org/jira/browse/AP-3461)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3440](https://projects.tmforum.org/jira/browse/AP-3440)

Tasks (3):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4950](https://projects.tmforum.org/jira/browse/AP-4950)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4823](https://projects.tmforum.org/jira/browse/AP-4823)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4761](https://projects.tmforum.org/jira/browse/AP-4761)

### 4. Label: 'api-team-forge' (used 19 times)

Bugs (3):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6424](https://projects.tmforum.org/jira/browse/AP-6424)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6114](https://projects.tmforum.org/jira/browse/AP-6114)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5230](https://projects.tmforum.org/jira/browse/AP-5230)

Epics (11):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5585](https://projects.tmforum.org/jira/browse/AP-5585)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5539](https://projects.tmforum.org/jira/browse/AP-5539)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5256](https://projects.tmforum.org/jira/browse/AP-5256)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5024](https://projects.tmforum.org/jira/browse/AP-5024)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4856](https://projects.tmforum.org/jira/browse/AP-4856)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4842](https://projects.tmforum.org/jira/browse/AP-4842)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4685](https://projects.tmforum.org/jira/browse/AP-4685)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3759](https://projects.tmforum.org/jira/browse/AP-3759)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3608](https://projects.tmforum.org/jira/browse/AP-3608)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3454](https://projects.tmforum.org/jira/browse/AP-3454)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3433](https://projects.tmforum.org/jira/browse/AP-3433)

Tasks (5):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6572](https://projects.tmforum.org/jira/browse/AP-6572)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6054](https://projects.tmforum.org/jira/browse/AP-6054)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5578](https://projects.tmforum.org/jira/browse/AP-5578)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4950](https://projects.tmforum.org/jira/browse/AP-4950)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4838](https://projects.tmforum.org/jira/browse/AP-4838)

### 5. Label: 'Accelerate_Asia25' (used 15 times)

Epics (15):
**URL:** [https://projects.tmforum.org/jira/browse/AP-7003](https://projects.tmforum.org/jira/browse/AP-7003)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7002](https://projects.tmforum.org/jira/browse/AP-7002)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7001](https://projects.tmforum.org/jira/browse/AP-7001)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7000](https://projects.tmforum.org/jira/browse/AP-7000)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6999](https://projects.tmforum.org/jira/browse/AP-6999)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6997](https://projects.tmforum.org/jira/browse/AP-6997)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6996](https://projects.tmforum.org/jira/browse/AP-6996)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6995](https://projects.tmforum.org/jira/browse/AP-6995)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6994](https://projects.tmforum.org/jira/browse/AP-6994)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6992](https://projects.tmforum.org/jira/browse/AP-6992)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6991](https://projects.tmforum.org/jira/browse/AP-6991)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6402](https://projects.tmforum.org/jira/browse/AP-6402)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6359](https://projects.tmforum.org/jira/browse/AP-6359)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6349](https://projects.tmforum.org/jira/browse/AP-6349)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5710](https://projects.tmforum.org/jira/browse/AP-5710)

### 6. Label: 'improvement' (used 14 times)

Tasks (14):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6093](https://projects.tmforum.org/jira/browse/AP-6093)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5596](https://projects.tmforum.org/jira/browse/AP-5596)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5409](https://projects.tmforum.org/jira/browse/AP-5409)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4823](https://projects.tmforum.org/jira/browse/AP-4823)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4761](https://projects.tmforum.org/jira/browse/AP-4761)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4649](https://projects.tmforum.org/jira/browse/AP-4649)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4572](https://projects.tmforum.org/jira/browse/AP-4572)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4558](https://projects.tmforum.org/jira/browse/AP-4558)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4462](https://projects.tmforum.org/jira/browse/AP-4462)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4388](https://projects.tmforum.org/jira/browse/AP-4388)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4385](https://projects.tmforum.org/jira/browse/AP-4385)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4236](https://projects.tmforum.org/jira/browse/AP-4236)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4235](https://projects.tmforum.org/jira/browse/AP-4235)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4234](https://projects.tmforum.org/jira/browse/AP-4234)

### 7. Label: 'Inception' (used 12 times)

Epics (12):
**URL:** [https://projects.tmforum.org/jira/browse/AP-7003](https://projects.tmforum.org/jira/browse/AP-7003)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7002](https://projects.tmforum.org/jira/browse/AP-7002)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7001](https://projects.tmforum.org/jira/browse/AP-7001)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7000](https://projects.tmforum.org/jira/browse/AP-7000)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6999](https://projects.tmforum.org/jira/browse/AP-6999)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6998](https://projects.tmforum.org/jira/browse/AP-6998)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6997](https://projects.tmforum.org/jira/browse/AP-6997)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6996](https://projects.tmforum.org/jira/browse/AP-6996)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6995](https://projects.tmforum.org/jira/browse/AP-6995)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6994](https://projects.tmforum.org/jira/browse/AP-6994)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6992](https://projects.tmforum.org/jira/browse/AP-6992)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6991](https://projects.tmforum.org/jira/browse/AP-6991)

### 8. Label: 'template' (used 12 times)

Sub-tasks (12):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6229](https://projects.tmforum.org/jira/browse/AP-6229)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6228](https://projects.tmforum.org/jira/browse/AP-6228)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6227](https://projects.tmforum.org/jira/browse/AP-6227)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6226](https://projects.tmforum.org/jira/browse/AP-6226)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6225](https://projects.tmforum.org/jira/browse/AP-6225)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6224](https://projects.tmforum.org/jira/browse/AP-6224)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6223](https://projects.tmforum.org/jira/browse/AP-6223)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6222](https://projects.tmforum.org/jira/browse/AP-6222)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6221](https://projects.tmforum.org/jira/browse/AP-6221)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6220](https://projects.tmforum.org/jira/browse/AP-6220)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6219](https://projects.tmforum.org/jira/browse/AP-6219)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6218](https://projects.tmforum.org/jira/browse/AP-6218)

### 9. Label: 'FY24-25-Q1' (used 11 times)

Epics (8):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4923](https://projects.tmforum.org/jira/browse/AP-4923)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4913](https://projects.tmforum.org/jira/browse/AP-4913)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4842](https://projects.tmforum.org/jira/browse/AP-4842)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4826](https://projects.tmforum.org/jira/browse/AP-4826)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4685](https://projects.tmforum.org/jira/browse/AP-4685)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4463](https://projects.tmforum.org/jira/browse/AP-4463)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3759](https://projects.tmforum.org/jira/browse/AP-3759)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3752](https://projects.tmforum.org/jira/browse/AP-3752)

Tasks (3):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6630](https://projects.tmforum.org/jira/browse/AP-6630)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6628](https://projects.tmforum.org/jira/browse/AP-6628)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4892](https://projects.tmforum.org/jira/browse/AP-4892)

### 10. Label: '2024-06-Paris' (used 11 times)

Epics (7):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4229](https://projects.tmforum.org/jira/browse/AP-4229)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3594](https://projects.tmforum.org/jira/browse/AP-3594)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3587](https://projects.tmforum.org/jira/browse/AP-3587)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3503](https://projects.tmforum.org/jira/browse/AP-3503)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3496](https://projects.tmforum.org/jira/browse/AP-3496)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3475](https://projects.tmforum.org/jira/browse/AP-3475)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3440](https://projects.tmforum.org/jira/browse/AP-3440)

Tasks (4):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4823](https://projects.tmforum.org/jira/browse/AP-4823)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4236](https://projects.tmforum.org/jira/browse/AP-4236)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4235](https://projects.tmforum.org/jira/browse/AP-4235)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4234](https://projects.tmforum.org/jira/browse/AP-4234)

### 11. Label: '2024-09-Vienna' (used 11 times)

Epics (11):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5968](https://projects.tmforum.org/jira/browse/AP-5968)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4798](https://projects.tmforum.org/jira/browse/AP-4798)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4463](https://projects.tmforum.org/jira/browse/AP-4463)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4314](https://projects.tmforum.org/jira/browse/AP-4314)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3738](https://projects.tmforum.org/jira/browse/AP-3738)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3673](https://projects.tmforum.org/jira/browse/AP-3673)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3601](https://projects.tmforum.org/jira/browse/AP-3601)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3510](https://projects.tmforum.org/jira/browse/AP-3510)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3454](https://projects.tmforum.org/jira/browse/AP-3454)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3440](https://projects.tmforum.org/jira/browse/AP-3440)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3426](https://projects.tmforum.org/jira/browse/AP-3426)

### 12. Label: 'Migration' (used 8 times)

Bugs (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5230](https://projects.tmforum.org/jira/browse/AP-5230)

Epics (3):
**URL:** [https://projects.tmforum.org/jira/browse/AP-3601](https://projects.tmforum.org/jira/browse/AP-3601)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3510](https://projects.tmforum.org/jira/browse/AP-3510)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3454](https://projects.tmforum.org/jira/browse/AP-3454)

Tasks (4):
**URL:** [https://projects.tmforum.org/jira/browse/AP-7080](https://projects.tmforum.org/jira/browse/AP-7080)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7079](https://projects.tmforum.org/jira/browse/AP-7079)

**URL:** [https://projects.tmforum.org/jira/browse/AP-7078](https://projects.tmforum.org/jira/browse/AP-7078)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4558](https://projects.tmforum.org/jira/browse/AP-4558)

### 13. Label: '2024-03-Montreal' (used 6 times)

Epics (4):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4923](https://projects.tmforum.org/jira/browse/AP-4923)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4913](https://projects.tmforum.org/jira/browse/AP-4913)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3759](https://projects.tmforum.org/jira/browse/AP-3759)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3752](https://projects.tmforum.org/jira/browse/AP-3752)

Tasks (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6630](https://projects.tmforum.org/jira/browse/AP-6630)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6628](https://projects.tmforum.org/jira/browse/AP-6628)

### 14. Label: 'data_governance' (used 6 times)

Epics (4):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4923](https://projects.tmforum.org/jira/browse/AP-4923)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4913](https://projects.tmforum.org/jira/browse/AP-4913)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3759](https://projects.tmforum.org/jira/browse/AP-3759)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3752](https://projects.tmforum.org/jira/browse/AP-3752)

Tasks (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6630](https://projects.tmforum.org/jira/browse/AP-6630)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6628](https://projects.tmforum.org/jira/browse/AP-6628)

### 15. Label: '2024-04-Dallas' (used 6 times)

Bugs (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-2053](https://projects.tmforum.org/jira/browse/AP-2053)

Epics (4):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5024](https://projects.tmforum.org/jira/browse/AP-5024)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4685](https://projects.tmforum.org/jira/browse/AP-4685)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3440](https://projects.tmforum.org/jira/browse/AP-3440)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3433](https://projects.tmforum.org/jira/browse/AP-3433)

Tasks (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4761](https://projects.tmforum.org/jira/browse/AP-4761)

### 16. Label: 'unplanned_FY24-25Q2' (used 5 times)

Bugs (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-2336](https://projects.tmforum.org/jira/browse/AP-2336)

Epics (4):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6799](https://projects.tmforum.org/jira/browse/AP-6799)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6782](https://projects.tmforum.org/jira/browse/AP-6782)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4630](https://projects.tmforum.org/jira/browse/AP-4630)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4463](https://projects.tmforum.org/jira/browse/AP-4463)

### 17. Label: 'DevOps' (used 4 times)

Bugs (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6424](https://projects.tmforum.org/jira/browse/AP-6424)

Epics (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6588](https://projects.tmforum.org/jira/browse/AP-6588)

Tasks (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6432](https://projects.tmforum.org/jira/browse/AP-6432)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5578](https://projects.tmforum.org/jira/browse/AP-5578)

### 18. Label: 'innovation-hub' (used 4 times)

Bugs (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6424](https://projects.tmforum.org/jira/browse/AP-6424)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6114](https://projects.tmforum.org/jira/browse/AP-6114)

Tasks (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6054](https://projects.tmforum.org/jira/browse/AP-6054)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5578](https://projects.tmforum.org/jira/browse/AP-5578)

### 19. Label: 'ODA' (used 4 times)

Epics (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-3503](https://projects.tmforum.org/jira/browse/AP-3503)

Tasks (3):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4236](https://projects.tmforum.org/jira/browse/AP-4236)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4235](https://projects.tmforum.org/jira/browse/AP-4235)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4234](https://projects.tmforum.org/jira/browse/AP-4234)

### 20. Label: 'china_specjam_2024' (used 4 times)

Epics (4):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6402](https://projects.tmforum.org/jira/browse/AP-6402)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6359](https://projects.tmforum.org/jira/browse/AP-6359)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6349](https://projects.tmforum.org/jira/browse/AP-6349)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5710](https://projects.tmforum.org/jira/browse/AP-5710)

### 21. Label: 'Open_Gateway' (used 3 times)

Epics (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6760](https://projects.tmforum.org/jira/browse/AP-6760)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5256](https://projects.tmforum.org/jira/browse/AP-5256)

Tasks (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4950](https://projects.tmforum.org/jira/browse/AP-4950)

### 22. Label: 'Async' (used 3 times)

Epics (3):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5454](https://projects.tmforum.org/jira/browse/AP-5454)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5348](https://projects.tmforum.org/jira/browse/AP-5348)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5312](https://projects.tmforum.org/jira/browse/AP-5312)

### 23. Label: 'v4.1.0' (used 3 times)

Epics (3):
**URL:** [https://projects.tmforum.org/jira/browse/AP-3915](https://projects.tmforum.org/jira/browse/AP-3915)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3905](https://projects.tmforum.org/jira/browse/AP-3905)

**URL:** [https://projects.tmforum.org/jira/browse/AP-3657](https://projects.tmforum.org/jira/browse/AP-3657)

### 24. Label: 'git-issue' (used 2 times)

Bugs (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6424](https://projects.tmforum.org/jira/browse/AP-6424)

Tasks (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6632](https://projects.tmforum.org/jira/browse/AP-6632)

### 25. Label: 'pull-request' (used 2 times)

Tasks (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6630](https://projects.tmforum.org/jira/browse/AP-6630)

**URL:** [https://projects.tmforum.org/jira/browse/AP-6628](https://projects.tmforum.org/jira/browse/AP-6628)

### 26. Label: 'Definition_of_Fit_Deliverable' (used 2 times)

Epics (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4826](https://projects.tmforum.org/jira/browse/AP-4826)

Tasks (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4892](https://projects.tmforum.org/jira/browse/AP-4892)

### 27. Label: 'New_Feature_Technical_Requirement' (used 2 times)

Tasks (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-3003](https://projects.tmforum.org/jira/browse/AP-3003)

**URL:** [https://projects.tmforum.org/jira/browse/AP-2277](https://projects.tmforum.org/jira/browse/AP-2277)

### 28. Label: 'BAU' (used 2 times)

Epics (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6760](https://projects.tmforum.org/jira/browse/AP-6760)

**URL:** [https://projects.tmforum.org/jira/browse/AP-5776](https://projects.tmforum.org/jira/browse/AP-5776)

### 29. Label: 'unplanned_FY24-25Q3' (used 2 times)

Epics (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5582](https://projects.tmforum.org/jira/browse/AP-5582)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4856](https://projects.tmforum.org/jira/browse/AP-4856)

### 30. Label: 'AI' (used 2 times)

Epics (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4685](https://projects.tmforum.org/jira/browse/AP-4685)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4314](https://projects.tmforum.org/jira/browse/AP-4314)

### 31. Label: 'AN' (used 2 times)

Epics (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4685](https://projects.tmforum.org/jira/browse/AP-4685)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4314](https://projects.tmforum.org/jira/browse/AP-4314)

### 32. Label: 'DCS' (used 2 times)

Epics (2):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4622](https://projects.tmforum.org/jira/browse/AP-4622)

**URL:** [https://projects.tmforum.org/jira/browse/AP-4601](https://projects.tmforum.org/jira/browse/AP-4601)

### 33. Label: 'OASC' (used 1 times)

Tasks (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6179](https://projects.tmforum.org/jira/browse/AP-6179)

### 34. Label: 'accelerate-25' (used 1 times)

Tasks (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-6179](https://projects.tmforum.org/jira/browse/AP-6179)

### 35. Label: 'kanban' (used 1 times)

Tasks (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5578](https://projects.tmforum.org/jira/browse/AP-5578)

### 36. Label: 'v5' (used 1 times)

Tasks (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-3003](https://projects.tmforum.org/jira/browse/AP-3003)

### 37. Label: 'feedback' (used 1 times)

Bugs (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-5773](https://projects.tmforum.org/jira/browse/AP-5773)

### 38. Label: 'propose-review' (used 1 times)

Bugs (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-2120](https://projects.tmforum.org/jira/browse/AP-2120)

### 39. Label: 'ready-for-ctk-development' (used 1 times)

Epics (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-4121](https://projects.tmforum.org/jira/browse/AP-4121)

### 40. Label: 'pre_production_table' (used 1 times)

Epics (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-3978](https://projects.tmforum.org/jira/browse/AP-3978)

### 41. Label: 'production_table' (used 1 times)

Epics (1):
**URL:** [https://projects.tmforum.org/jira/browse/AP-3915](https://projects.tmforum.org/jira/browse/AP-3915)

### Label Insights

Top 5 most used labels:
1. 'FY24-25-Q2' - 32 issues
2. 'FY24-25-Q3' - 27 issues
3. 'unplanned_FY24-25Q1' - 24 issues
4. 'api-team-forge' - 19 issues
5. 'Accelerate_Asia25' - 15 issues
Labels used only once (9):
Label usage by issue type:
Bug: 11 unique labels
Epic: 29 unique labels
Sub-task: 1 unique labels
Task: 23 unique labels
- [SUCCESS] Multi-issue type data quality check completed successfully!
- [TIPS] Tips for improving data quality:
---

*Report generated by JIRA Issue Data Quality Checker*  
*For more information, see the project documentation.*
