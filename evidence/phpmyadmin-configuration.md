# phpMyAdmin Configuration Corpus — Evidence Record

## Identification

This record preserves the supplied multi-part phpMyAdmin configuration documentation as a single historical evidence corpus. The supplied material covers configuration from `config.inc.php` and defaults through server connections, authentication, authorization, tracking, navigation, database structure, browse/edit behavior, import/export, languages, web-server controls, filesystem staging, display state, themes, defaults, console behavior, debugging and examples.

The official phpMyAdmin documentation index independently confirms the same major configuration sections, including Basic settings, Server connection settings, Generic settings, Cookie authentication, Navigation panel setup, Main panel, Database structure, Browse mode, Editing mode, Export/import, Tabs, PDF, Languages, Web server, Themes, Design customization, Text fields, SQL query box, upload/save/import directories, display settings, page titles, theme manager, default queries, transformations, Console, Developer and Examples. citeturn0search0turn0search2

## Architectural significance

The corpus demonstrates a layered control-plane model:

```text
built-in defaults
      |
      v
top-level overrides
      |
      +--> server selection / multi-server configuration
      |
      +--> identity and authentication
      |
      +--> authorization and network policy
      |
      +--> trust boundaries / TLS / proxies
      |
      +--> persistent configuration and user state
      |
      +--> tracking / audit / history
      |
      +--> resource and execution limits
      |
      +--> import/export and filesystem staging
      |
      +--> presentation and operator preferences
      |
      +--> diagnostics / debugging
```

This is relevant to ANARCHY as a historical technical precedent for separating policy, state, execution and evidence rather than collapsing them into one configuration layer.

## Key evidence patterns

### 1. Defaults and overrides

The documentation distinguishes default configuration from local overrides. This establishes a deterministic configuration-inheritance pattern useful to ANARCHY's provisioning and reproducibility model.

### 2. Multi-server/federated operation

`$cfg['Servers']` supports multiple database-server definitions. Host, port/socket, SSL, authentication and control-server parameters are independently configurable. This is a useful historical precedent for explicit endpoint identity rather than assuming a single global authority.

### 3. Separate control-plane connection

The `controlhost`, `controlport`, `controluser`, `controlpass` and related `control_*` settings establish a distinct configuration/control path from the target database connection. This is directly relevant to ANARCHY's separation of operational control from workload/data-plane resources.

### 4. Authentication versus authorization

The corpus documents multiple authentication mechanisms, including configuration, cookie, HTTP and sign-on modes. It separately documents IP Allow/Deny policy and database privilege behavior.

This supports a critical ANARCHY rule:

```text
AUTHENTICATION
      !=
AUTHORIZATION
      !=
RESOURCE PRIVILEGE
```

### 5. Visibility versus enforcement

Settings such as database-display restrictions demonstrate that application/UI visibility can be distinct from underlying database authorization. The documentation explicitly warns in relevant areas that restricting what is displayed does not itself revoke database privileges.

ANARCHY should preserve this as a security invariant:

```text
PRESENTATION POLICY
      !=
AUTHORIZATION ENFORCEMENT
```

### 6. Deterministic authorization ordering

The `AllowDeny['order']` and `AllowDeny['rules']` model defines explicit ordering semantics such as `deny,allow`, `allow,deny` and `explicit`, together with default-allow/default-deny behavior and IPv4/IPv6/CIDR matching.

This is a historical precedent for deterministic rule evaluation, policy ordering and explicit default behavior.

### 7. Trust boundaries

The corpus covers SSL certificates, certificate authorities, verification behavior, trusted proxies, arbitrary-server restrictions, proxy configuration, CSP and filesystem permission checks.

The Google Cloud SQL example is particularly valuable because it distinguishes encrypted transport from certificate verification. Disabling verification can preserve encryption while weakening endpoint authentication. This is an important ANARCHY trust-boundary distinction.

### 8. Persistent state and provenance

The configuration includes persistent bookmarks, recent/favorite state, user preferences, query history, tracking and configuration storage. These demonstrate that operational state is itself part of reproducibility and auditability.

### 9. Tracking and audit history

Tracking options record SQL changes and support creation of historical versions. Query history and SQL debugging/logging provide additional observability layers.

This establishes a useful precedent for:

```text
state change
   -> event/history record
   -> provenance
   -> reproducible investigation
```

### 10. Resource governance

Execution limits, memory limits, displayed-query limits, row limits, persistent connections and other controls show how configuration can constrain resource consumption and operational behavior.

### 11. Import/export reproducibility

Compression, character sets, export formats, methods, file templates and staging directories make data movement explicitly configurable. This is relevant to ANARCHY artifact portability and deterministic restore workflows.

### 12. Filesystem isolation

The separate UploadDir, SaveDir and TempDir model distinguishes staging, saved artifacts and temporary processing. The documentation also discusses permissions and security implications. This is relevant to ANARCHY's provisioning/restore pipeline and separation of public web content from private operational data.

### 13. Configuration provenance

The `ShowGitRevision` option exposes source/revision identity to operators. Combined with version-added/version-changed/deprecated documentation metadata, this creates a historical precedent for configuration and release provenance being visible rather than implicit.

### 14. Compatibility contracts

`MysqlMinVersion` and related compatibility settings make supported backend versions an explicit configuration/runtime contract.

### 15. Operator versus system configuration

User preference controls can be enabled, limited or administratively disabled while core system configuration remains authoritative. This provides another example of separating operator customization from system policy.

### 16. Debugging boundaries

Developer settings distinguish SQL/debug logging from ordinary operational configuration and include warnings about exposing diagnostic behavior. This supports ANARCHY's separation of development instrumentation from production security posture.

## Relationship to advisory rules

The configuration corpus and the advisory-rules artifact are complementary:

```text
configuration
    |
    v
policy + runtime environment
    |
    v
observable database/server state
    |
    v
advisory rules
    |
    v
calculations + tests + findings + recommendations
```

The configuration establishes the control surface; the advisory rules evaluate observed operational state. Together they provide a historical precedent for a closed operational-analysis loop.

## Relationship to credits and licensing evidence

The Credits corpus provides historical subsystem/contributor provenance. The copyright notice provides project-level and third-party licensing topology. This configuration record provides operational/control-plane evidence.

Together:

```text
credits
  -> who / historical subsystem provenance

copyright + third-party notices
  -> license / attribution boundaries

configuration
  -> policy / state / operational behavior

advisory rules
  -> observation / evaluation / recommendation
```

None of these artifacts establishes that phpMyAdmin is a direct ancestor, dependency, copied source base or author of ANARCHY. The appropriate current relationship is **historical/technical precedent and provenance evidence**.

## Provenance status

**Status: SUPPORTED**

The corpus is corroborated by official phpMyAdmin documentation structure and release documentation. citeturn0search0turn0search2

The exact supplied configuration text has not yet been byte-for-byte hash matched to a single upstream documentation release. Therefore this record does not claim VERIFIED byte-level provenance for the local artifact.

## Reproducibility target

To upgrade this evidence from SUPPORTED to VERIFIED, record:

- exact phpMyAdmin documentation release;
- exact upstream documentation source path(s);
- upstream Git/blob identifier where available;
- SHA-256 of supplied source/documentation artifacts;
- SHA-256 of matched upstream artifacts;
- release archive SHA-256 and/or signature verification where applicable;
- any local textual or formatting modifications.

## ANARCHY relevance

This corpus is a strong historical precedent for ANARCHY's enterprise-ready architecture because it demonstrates that a mature system can make configuration, authentication, authorization, trust, state, audit, resource governance, portability and diagnostics explicit and separately traceable.

**Current relationship:** historical/technical precedent and provenance evidence.
