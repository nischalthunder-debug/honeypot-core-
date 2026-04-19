[SentinelMesh — Full Stack Source C (1).txt](https://github.com/user-attachments/files/26863682/SentinelMesh.Full.Stack.Source.C.1.txt)

// SentinelMesh — Full Stack Source Code
// Generated: Sun Apr 19 02:30:53 AM UTC 2026
// ============================================================

// ============================================================
// FILE: package.json
// ============================================================
{
  "name": "workspace",
  "version": "0.0.0",
  "license": "MIT",
  "scripts": {
    "preinstall": "sh -c 'rm -f package-lock.json yarn.lock; case \"$npm_config_user_agent\" in pnpm/*) ;; *) echo \"Use pnpm instead\" >&2; exit 1 ;; esac'",
    "build": "pnpm run typecheck && pnpm -r --if-present run build",
    "typecheck:libs": "tsc --build",
    "typecheck": "pnpm run typecheck:libs && pnpm -r --filter \"./artifacts/**\" --filter \"./scripts\" --if-present run typecheck"
  },
  "private": true,
  "devDependencies": {
    "typescript": "~5.9.2",
    "prettier": "^3.8.1"
  }
}


// ============================================================
// FILE: pnpm-workspace.yaml
// ============================================================
# ============================================================================
# SECURITY: Minimum release age for npm packages (supply-chain attack defense)
# ============================================================================
#
# This setting requires that any npm package version must have been published
# for at least 1 day (1440 minutes) before pnpm will allow installing it.
# This is a critical defense against supply-chain attacks. In most cases,
# malicious npm releases are discovered and pulled within hours, so a 1-day
# delay provides a strong safety buffer.
#
# DO NOT DISABLE THIS SETTING. Removing or setting it to 0 is considered
# extremely dangerous and leaves the entire workspace vulnerable to supply-
# chain attacks, which have been the #1 vector for npm ecosystem compromises.
#
# If you absolutely need to install a package before the 1-day window has
# passed (e.g. an urgent security bugfix), you can add it to the
# `minimumReleaseAgeExclude` allowlist below. Only consider doing this for
# packages released by trusted organizations with an impeccable security
# posture (e.g. Replit packsges, react from Meta, typescript from Microsoft). Even then,
# remove the exclusion once the 1-day window has passed.
#
# Example:
#   minimumReleaseAgeExclude:
#     - react
#     - typescript
#
# ============================================================================
minimumReleaseAge: 1440

minimumReleaseAgeExclude:
  # Exclude @replit scoped packages from the minimum release age check.
  # These are published by Replit and trusted — the supply-chain attack vector
  # this setting guards against does not apply to our own packages.
  - '@replit/*'
  - stripe-replit-sync

packages:
  - artifacts/*
  - lib/*
  - lib/integrations/*
  - scripts

catalog:
  '@replit/vite-plugin-cartographer': ^0.5.1
  '@replit/vite-plugin-dev-banner': ^0.1.1
  '@replit/vite-plugin-runtime-error-modal': ^0.0.6
  '@tailwindcss/vite': ^4.1.14
  '@tanstack/react-query': ^5.90.21
  '@types/node': ^25.3.3
  '@types/react': ^19.2.0
  '@types/react-dom': ^19.2.0
  '@vitejs/plugin-react': ^5.0.4
  class-variance-authority: ^0.7.1
  clsx: ^2.1.1
  drizzle-orm: ^0.45.2
  framer-motion: ^12.23.24
  lucide-react: ^0.545.0
  # Must be this exact version because expo requires it
  react: 19.1.0
  # Must be this exact version because expo requires it
  react-dom: 19.1.0
  tailwind-merge: ^3.3.1
  tailwindcss: ^4.1.14
  tsx: ^4.21.0
  vite: ^7.3.2
  zod: ^3.25.76

autoInstallPeers: false

onlyBuiltDependencies:
  - '@swc/core'
  - esbuild
  - msw
  - unrs-resolver

overrides:
  # replit uses linux-x64 only, we can exclude all other platforms
  "esbuild>@esbuild/darwin-arm64": "-"
  "esbuild>@esbuild/darwin-x64": "-"
  "esbuild>@esbuild/freebsd-arm64": "-"
  "esbuild>@esbuild/freebsd-x64": "-"
  "esbuild>@esbuild/linux-arm": "-"
  "esbuild>@esbuild/linux-arm64": "-"
  "esbuild>@esbuild/linux-ia32": "-"
  "esbuild>@esbuild/linux-loong64": "-"
  "esbuild>@esbuild/linux-mips64el": "-"
  "esbuild>@esbuild/linux-ppc64": "-"
  "esbuild>@esbuild/linux-riscv64": "-"
  "esbuild>@esbuild/linux-s390x": "-"
  "esbuild>@esbuild/netbsd-arm64": "-"
  "esbuild>@esbuild/netbsd-x64": "-"
  "esbuild>@esbuild/openbsd-arm64": "-"
  "esbuild>@esbuild/openbsd-x64": "-"
  "esbuild>@esbuild/sunos-x64": "-"
  "esbuild>@esbuild/win32-arm64": "-"
  "esbuild>@esbuild/win32-ia32": "-"
  "esbuild>@esbuild/win32-x64": "-"
  "esbuild>@esbuild/aix-ppc64": '-'
  "esbuild>@esbuild/android-arm": '-'
  "esbuild>@esbuild/android-arm64": '-'
  "esbuild>@esbuild/android-x64": '-'
  "esbuild>@esbuild/openharmony-arm64": '-'
  "lightningcss>lightningcss-android-arm64": "-"
  "lightningcss>lightningcss-darwin-arm64": "-"
  "lightningcss>lightningcss-darwin-x64": "-"
  "lightningcss>lightningcss-freebsd-x64": "-"
  "lightningcss>lightningcss-linux-arm-gnueabihf": "-"
  "lightningcss>lightningcss-linux-arm64-gnu": "-"
  "lightningcss>lightningcss-linux-arm64-musl": "-"
  "lightningcss>lightningcss-linux-x64-musl": "-"
  "lightningcss>lightningcss-win32-arm64-msvc": "-"
  "lightningcss>lightningcss-win32-x64-msvc": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-android-arm64": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-darwin-arm64": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-darwin-x64": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-freebsd-x64": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-linux-arm-gnueabihf": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-linux-arm64-gnu": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-linux-arm64-musl": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-win32-arm64-msvc": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-win32-x64-msvc": "-"
  "@tailwindcss/oxide>@tailwindcss/oxide-linux-x64-musl": "-"
  "rollup>@rollup/rollup-android-arm-eabi": "-"
  "rollup>@rollup/rollup-android-arm64": "-"
  "rollup>@rollup/rollup-darwin-arm64": "-"
  "rollup>@rollup/rollup-darwin-x64": "-"
  "rollup>@rollup/rollup-freebsd-arm64": "-"
  "rollup>@rollup/rollup-freebsd-x64": "-"
  "rollup>@rollup/rollup-linux-arm-gnueabihf": "-"
  "rollup>@rollup/rollup-linux-arm-musleabihf": "-"
  "rollup>@rollup/rollup-linux-arm64-gnu": "-"
  "rollup>@rollup/rollup-linux-arm64-musl": "-"
  "rollup>@rollup/rollup-linux-loong64-gnu": "-"
  "rollup>@rollup/rollup-linux-loong64-musl": "-"
  "rollup>@rollup/rollup-linux-ppc64-gnu": "-"
  "rollup>@rollup/rollup-linux-ppc64-musl": "-"
  "rollup>@rollup/rollup-linux-riscv64-gnu": "-"
  "rollup>@rollup/rollup-linux-riscv64-musl": "-"
  "rollup>@rollup/rollup-linux-s390x-gnu": "-"
  "rollup>@rollup/rollup-linux-x64-musl": "-"
  "rollup>@rollup/rollup-openbsd-x64": "-"
  "rollup>@rollup/rollup-openharmony-arm64": "-"
  "rollup>@rollup/rollup-win32-arm64-msvc": "-"
  "rollup>@rollup/rollup-win32-ia32-msvc": "-"
  "rollup>@rollup/rollup-win32-x64-gnu": "-"
  "rollup>@rollup/rollup-win32-x64-msvc": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-darwin-arm64": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-darwin-x64": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-freebsd-ia32": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-freebsd-x64": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-linux-arm64": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-linux-arm": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-linux-ia32": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-sunos-x64": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-win32-ia32": "-"
  "@expo/ngrok-bin>@expo/ngrok-bin-win32-x64": "-"
  # drizzle-kit uses esbuild internally on an older version that's vulnerable, this overrides it
  "@esbuild-kit/esm-loader": "npm:tsx@^4.21.0"
  esbuild: "0.27.3"

// ============================================================
// FILE: lib/api-spec/openapi.yaml
// ============================================================
openapi: 3.1.0
info:
  # Do not change the title, if the title changes, the import paths will be broken
  title: Api
  version: 0.1.0
  description: SentinelMesh Security Platform API
servers:
  - url: /api
    description: Base API path
tags:
  - name: health
    description: Health operations
  - name: dashboard
    description: Security dashboard overview
  - name: threats
    description: Threat detection and management
  - name: sessions
    description: Session monitoring and honeypot
  - name: attacks
    description: Attack profiles and forensics
  - name: canary
    description: Canary token management
  - name: fake-server
    description: Fake server / honeypot data
  - name: learning
    description: AI learning loop metrics
  - name: tenants
    description: Tenant / business management
  - name: pricing
    description: Pricing and subscription plans
paths:
  /healthz:
    get:
      operationId: healthCheck
      tags: [health]
      summary: Health check
      responses:
        "200":
          description: Healthy
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/HealthStatus"

  /dashboard/summary:
    get:
      operationId: getDashboardSummary
      tags: [dashboard]
      summary: Get security dashboard summary stats
      responses:
        "200":
          description: Dashboard summary
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/DashboardSummary"

  /dashboard/live-feed:
    get:
      operationId: getLiveFeed
      tags: [dashboard]
      summary: Get real-time threat activity feed
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        "200":
          description: Live feed events
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/FeedEvent"

  /dashboard/score-timeline:
    get:
      operationId: getScoreTimeline
      tags: [dashboard]
      summary: Get threat score timeline for charting
      parameters:
        - name: hours
          in: query
          schema:
            type: integer
            default: 24
      responses:
        "200":
          description: Timeline data points
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/TimelinePoint"

  /threats:
    get:
      operationId: listThreats
      tags: [threats]
      summary: List all detected threats
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [active, mitigated, honeypotted, dismissed]
        - name: riskLevel
          in: query
          schema:
            type: string
            enum: [low, medium, high, critical]
        - name: limit
          in: query
          schema:
            type: integer
            default: 50
        - name: offset
          in: query
          schema:
            type: integer
            default: 0
      responses:
        "200":
          description: List of threats
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ThreatListResponse"

  /threats/{threatId}:
    get:
      operationId: getThreat
      tags: [threats]
      summary: Get a specific threat by ID
      parameters:
        - name: threatId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Threat detail
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ThreatDetail"
        "404":
          description: Not found

  /threats/{threatId}/dismiss:
    post:
      operationId: dismissThreat
      tags: [threats]
      summary: Dismiss a threat (mark as false positive)
      parameters:
        - name: threatId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Threat dismissed
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ThreatDetail"

  /sessions:
    get:
      operationId: listSessions
      tags: [sessions]
      summary: List monitored sessions
      parameters:
        - name: type
          in: query
          schema:
            type: string
            enum: [real, honeypot, cloned]
        - name: limit
          in: query
          schema:
            type: integer
            default: 30
      responses:
        "200":
          description: Sessions list
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/SessionRecord"

  /sessions/{sessionId}:
    get:
      operationId: getSession
      tags: [sessions]
      summary: Get session detail with watchdog scores
      parameters:
        - name: sessionId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Session detail
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/SessionDetail"

  /attacks:
    get:
      operationId: listAttackProfiles
      tags: [attacks]
      summary: List attacker attribution profiles
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        "200":
          description: Attack profiles
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/AttackProfile"

  /attacks/{attackId}:
    get:
      operationId: getAttackProfile
      tags: [attacks]
      summary: Get detailed attack profile with forensics
      parameters:
        - name: attackId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Attack profile detail
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/AttackProfileDetail"

  /attacks/stats/techniques:
    get:
      operationId: getAttackTechniques
      tags: [attacks]
      summary: Get breakdown of attack techniques observed
      responses:
        "200":
          description: Technique breakdown
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/TechniqueCount"

  /canary-tokens:
    get:
      operationId: listCanaryTokens
      tags: [canary]
      summary: List canary tokens and their status
      responses:
        "200":
          description: Canary tokens
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/CanaryToken"

    post:
      operationId: createCanaryToken
      tags: [canary]
      summary: Create a new canary token
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CreateCanaryTokenBody"
      responses:
        "201":
          description: Created canary token
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/CanaryToken"

  /canary-tokens/{tokenId}/trips:
    get:
      operationId: getCanaryTokenTrips
      tags: [canary]
      summary: Get trips (fire events) for a canary token
      parameters:
        - name: tokenId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Canary trips
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/CanaryTrip"

  /fake-server/records:
    get:
      operationId: listFakeRecords
      tags: [fake-server]
      summary: List fake data records being served to attackers
      parameters:
        - name: type
          in: query
          schema:
            type: string
            enum: [customer, invoice, employee, product, credential]
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        "200":
          description: Fake data records
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/FakeRecordsResponse"

  /fake-server/interactions:
    get:
      operationId: getFakeServerInteractions
      tags: [fake-server]
      summary: Get attacker interactions on the fake server
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 30
      responses:
        "200":
          description: Fake server interactions
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/FakeServerInteraction"

  /fake-server/stats:
    get:
      operationId: getFakeServerStats
      tags: [fake-server]
      summary: Get honeypot statistics
      responses:
        "200":
          description: Fake server stats
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/FakeServerStats"

  /learning/metrics:
    get:
      operationId: getLearningMetrics
      tags: [learning]
      summary: Get AI learning loop performance metrics
      responses:
        "200":
          description: Learning metrics
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/LearningMetrics"

  /learning/improvements:
    get:
      operationId: getLearningImprovements
      tags: [learning]
      summary: Get list of AI improvements made from attack data
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 10
      responses:
        "200":
          description: AI improvements log
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/LearningImprovement"

  /pricing/plans:
    get:
      operationId: listPricingPlans
      tags: [pricing]
      summary: List available pricing plans
      responses:
        "200":
          description: Pricing plans
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/PricingPlan"

  /pricing/inquiry:
    post:
      operationId: submitPricingInquiry
      tags: [pricing]
      summary: Submit a pricing inquiry / contact form
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/PricingInquiryBody"
      responses:
        "201":
          description: Inquiry submitted
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/PricingInquiryResponse"

components:
  schemas:
    HealthStatus:
      type: object
      properties:
        status:
          type: string
      required: [status]

    DashboardSummary:
      type: object
      properties:
        totalThreatsToday:
          type: integer
        honeypottedSessions:
          type: integer
        canaryTrips:
          type: integer
        activeAttackers:
          type: integer
        avgThreatScore:
          type: number
        blockedRequests:
          type: integer
        aiAccuracyRate:
          type: number
        learningEvents:
          type: integer
        protectedBusinesses:
          type: integer
        uptimeDays:
          type: integer
      required:
        - totalThreatsToday
        - honeypottedSessions
        - canaryTrips
        - activeAttackers
        - avgThreatScore
        - blockedRequests
        - aiAccuracyRate
        - learningEvents
        - protectedBusinesses
        - uptimeDays

    FeedEvent:
      type: object
      properties:
        id:
          type: string
        timestamp:
          type: string
          format: date-time
        type:
          type: string
          enum: [threat_detected, honeypot_trip, canary_fired, session_cloned, attacker_profiled, ai_update]
        severity:
          type: string
          enum: [info, low, medium, high, critical]
        ipAddress:
          type: string
        message:
          type: string
        score:
          type: integer
        route:
          type: string
          enum: [real_server, fake_server]
      required: [id, timestamp, type, severity, ipAddress, message, score, route]

    TimelinePoint:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        avgScore:
          type: number
        threatCount:
          type: integer
        honeypotCount:
          type: integer
      required: [timestamp, avgScore, threatCount, honeypotCount]

    ThreatListResponse:
      type: object
      properties:
        threats:
          type: array
          items:
            $ref: "#/components/schemas/ThreatSummary"
        total:
          type: integer
        offset:
          type: integer
        limit:
          type: integer
      required: [threats, total, offset, limit]

    ThreatSummary:
      type: object
      properties:
        id:
          type: string
        ipAddress:
          type: string
        ipSubnet:
          type: string
        score:
          type: integer
        riskLevel:
          type: string
          enum: [low, medium, high, critical]
        status:
          type: string
          enum: [active, mitigated, honeypotted, dismissed]
        route:
          type: string
          enum: [real_server, fake_server]
        firstSeen:
          type: string
          format: date-time
        lastSeen:
          type: string
          format: date-time
        requestCount:
          type: integer
        technique:
          type: string
      required: [id, ipAddress, ipSubnet, score, riskLevel, status, route, firstSeen, lastSeen, requestCount, technique]

    ThreatDetail:
      allOf:
        - $ref: "#/components/schemas/ThreatSummary"
        - type: object
          properties:
            userAgent:
              type: string
            scoreComponents:
              $ref: "#/components/schemas/ScoreComponents"
            sessionIds:
              type: array
              items:
                type: string
            canaryTokensFired:
              type: array
              items:
                type: string
            attackTechniques:
              type: array
              items:
                type: string
            attributionConfidence:
              type: number
            geoLocation:
              type: string
            asn:
              type: string
            isTor:
              type: boolean
            isVpn:
              type: boolean
          required:
            - userAgent
            - scoreComponents
            - sessionIds
            - canaryTokensFired
            - attackTechniques
            - attributionConfidence
            - geoLocation
            - asn
            - isTor
            - isVpn

    ScoreComponents:
      type: object
      properties:
        basePathBody:
          type: integer
        memoryBoost:
          type: integer
        correlationBoost:
          type: integer
        spikeBoost:
          type: integer
        total:
          type: integer
      required: [basePathBody, memoryBoost, correlationBoost, spikeBoost, total]

    SessionRecord:
      type: object
      properties:
        id:
          type: string
        type:
          type: string
          enum: [real, honeypot, cloned]
        ipAddress:
          type: string
        startedAt:
          type: string
          format: date-time
        lastActivity:
          type: string
          format: date-time
        requestCount:
          type: integer
        currentScore:
          type: integer
        clonedToHoneypotAt:
          type: string
          format: date-time
          nullable: true
        cloneLatencyMs:
          type: integer
          nullable: true
      required: [id, type, ipAddress, startedAt, lastActivity, requestCount, currentScore]

    SessionDetail:
      allOf:
        - $ref: "#/components/schemas/SessionRecord"
        - type: object
          properties:
            scoreHistory:
              type: array
              items:
                $ref: "#/components/schemas/ScoreHistoryPoint"
            requestLog:
              type: array
              items:
                $ref: "#/components/schemas/RequestLogEntry"
          required: [scoreHistory, requestLog]

    ScoreHistoryPoint:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        score:
          type: integer
        event:
          type: string
          nullable: true
      required: [timestamp, score]

    RequestLogEntry:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        method:
          type: string
        path:
          type: string
        score:
          type: integer
        servedBy:
          type: string
          enum: [real_server, fake_server]
      required: [timestamp, method, path, score, servedBy]

    AttackProfile:
      type: object
      properties:
        id:
          type: string
        fingerprint:
          type: string
        ipAddresses:
          type: array
          items:
            type: string
        technique:
          type: string
        intent:
          type: string
          enum: [data_exfiltration, credential_stuffing, sql_injection, api_scraping, reconnaissance, lateral_movement]
        attributionConfidence:
          type: number
        firstSeen:
          type: string
          format: date-time
        lastSeen:
          type: string
          format: date-time
        totalRequests:
          type: integer
        apiKeyRotations:
          type: integer
        honeypotTimeMinutes:
          type: integer
      required: [id, fingerprint, ipAddresses, technique, intent, attributionConfidence, firstSeen, lastSeen, totalRequests, apiKeyRotations, honeypotTimeMinutes]

    AttackProfileDetail:
      allOf:
        - $ref: "#/components/schemas/AttackProfile"
        - type: object
          properties:
            forensicReport:
              $ref: "#/components/schemas/ForensicReport"
            behaviorMap:
              type: array
              items:
                $ref: "#/components/schemas/BehaviorEvent"
            fakeDataServed:
              type: array
              items:
                type: string
          required: [forensicReport, behaviorMap, fakeDataServed]

    ForensicReport:
      type: object
      properties:
        summary:
          type: string
        toolsIdentified:
          type: array
          items:
            type: string
        indicatorsOfCompromise:
          type: array
          items:
            type: string
        estimatedActorType:
          type: string
          enum: [script_kiddie, organized_group, state_actor, competitor, insider]
        geolocationChain:
          type: array
          items:
            type: string
        mitreTechniques:
          type: array
          items:
            type: string
      required: [summary, toolsIdentified, indicatorsOfCompromise, estimatedActorType, geolocationChain, mitreTechniques]

    BehaviorEvent:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        action:
          type: string
        detail:
          type: string
        significance:
          type: string
          enum: [low, medium, high]
      required: [timestamp, action, detail, significance]

    TechniqueCount:
      type: object
      properties:
        technique:
          type: string
        count:
          type: integer
        percentage:
          type: number
      required: [technique, count, percentage]

    CanaryToken:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
          enum: [api_key, url, email, database_record, file]
        location:
          type: string
        createdAt:
          type: string
          format: date-time
        tripCount:
          type: integer
        lastTripped:
          type: string
          format: date-time
          nullable: true
        status:
          type: string
          enum: [active, tripped, deactivated]
      required: [id, name, type, location, createdAt, tripCount, status]

    CreateCanaryTokenBody:
      type: object
      properties:
        name:
          type: string
        type:
          type: string
          enum: [api_key, url, email, database_record, file]
        location:
          type: string
      required: [name, type, location]

    CanaryTrip:
      type: object
      properties:
        id:
          type: string
        tokenId:
          type: string
        trippedAt:
          type: string
          format: date-time
        ipAddress:
          type: string
        userAgent:
          type: string
        sessionId:
          type: string
        threatId:
          type: string
        cloneLatencyMs:
          type: integer
      required: [id, tokenId, trippedAt, ipAddress, userAgent, sessionId, threatId, cloneLatencyMs]

    FakeRecordsResponse:
      type: object
      properties:
        records:
          type: array
          items:
            $ref: "#/components/schemas/FakeRecord"
        total:
          type: integer
      required: [records, total]

    FakeRecord:
      type: object
      properties:
        id:
          type: string
        type:
          type: string
          enum: [customer, invoice, employee, product, credential]
        data:
          type: object
          additionalProperties: true
        generatedAt:
          type: string
          format: date-time
        servedTo:
          type: integer
        believabilityScore:
          type: number
      required: [id, type, data, generatedAt, servedTo, believabilityScore]

    FakeServerInteraction:
      type: object
      properties:
        id:
          type: string
        timestamp:
          type: string
          format: date-time
        attackerIp:
          type: string
        sessionId:
          type: string
        endpoint:
          type: string
        method:
          type: string
        fakeRecordId:
          type: string
          nullable: true
        attackerBelievedData:
          type: boolean
        notes:
          type: string
      required: [id, timestamp, attackerIp, sessionId, endpoint, method, attackerBelievedData, notes]

    FakeServerStats:
      type: object
      properties:
        totalInteractions:
          type: integer
        activeHoneypotSessions:
          type: integer
        avgTimeInHoneypotMinutes:
          type: number
        fakeDataRequests:
          type: integer
        attackersBelievedData:
          type: integer
        believabilityRate:
          type: number
        avgCloneLatencyMs:
          type: number
        fastestCloneMs:
          type: integer
        dataTypesServed:
          type: object
          additionalProperties:
            type: integer
      required:
        - totalInteractions
        - activeHoneypotSessions
        - avgTimeInHoneypotMinutes
        - fakeDataRequests
        - attackersBelievedData
        - believabilityRate
        - avgCloneLatencyMs
        - fastestCloneMs
        - dataTypesServed

    LearningMetrics:
      type: object
      properties:
        totalTrainingEvents:
          type: integer
        modelAccuracy:
          type: number
        falsePositiveRate:
          type: number
        falseNegativeRate:
          type: number
        avgDetectionTimeMs:
          type: number
        canaryPlacementUpdates:
          type: integer
        fakeDataImprovements:
          type: integer
        lastTrainedAt:
          type: string
          format: date-time
        memoryWindowDays:
          type: integer
        attacksLearnedFrom:
          type: integer
      required:
        - totalTrainingEvents
        - modelAccuracy
        - falsePositiveRate
        - falseNegativeRate
        - avgDetectionTimeMs
        - canaryPlacementUpdates
        - fakeDataImprovements
        - lastTrainedAt
        - memoryWindowDays
        - attacksLearnedFrom

    LearningImprovement:
      type: object
      properties:
        id:
          type: string
        timestamp:
          type: string
          format: date-time
        type:
          type: string
          enum: [model_update, canary_repositioned, fake_data_improved, threshold_adjusted, correlation_rule_added]
        description:
          type: string
        triggeredBy:
          type: string
        impactScore:
          type: number
      required: [id, timestamp, type, description, triggeredBy, impactScore]

    PricingPlan:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        monthlyPrice:
          type: number
        annualPrice:
          type: number
        description:
          type: string
        features:
          type: array
          items:
            type: string
        requestsPerMonth:
          type: integer
        apiKeys:
          type: integer
        honeypotSessions:
          type: integer
        supportLevel:
          type: string
          enum: [community, email, priority, dedicated]
        recommended:
          type: boolean
      required: [id, name, monthlyPrice, annualPrice, description, features, requestsPerMonth, apiKeys, honeypotSessions, supportLevel, recommended]

    PricingInquiryBody:
      type: object
      properties:
        businessName:
          type: string
        contactName:
          type: string
        email:
          type: string
          format: email
        phone:
          type: string
          nullable: true
        planId:
          type: string
          nullable: true
        monthlyRequests:
          type: string
        message:
          type: string
          nullable: true
      required: [businessName, contactName, email, monthlyRequests]

    PricingInquiryResponse:
      type: object
      properties:
        id:
          type: string
        submittedAt:
          type: string
          format: date-time
        message:
          type: string
      required: [id, submittedAt, message]


// ============================================================
// FILE: lib/api-spec/orval.config.ts
// ============================================================
import { defineConfig, InputTransformerFn } from "orval";
import path from "path";

const root = path.resolve(__dirname, "..", "..");
const apiClientReactSrc = path.resolve(root, "lib", "api-client-react", "src");
const apiZodSrc = path.resolve(root, "lib", "api-zod", "src");

// Our exports make assumptions about the title of the API being "Api" (i.e. generated output is `api.ts`).
const titleTransformer: InputTransformerFn = (config) => {
  config.info ??= {};
  config.info.title = "Api";

  return config;
};

export default defineConfig({
  "api-client-react": {
    input: {
      target: "./openapi.yaml",
      override: {
        transformer: titleTransformer,
      },
    },
    output: {
      workspace: apiClientReactSrc,
      target: "generated",
      client: "react-query",
      mode: "split",
      baseUrl: "/api",
      clean: true,
      prettier: true,
      override: {
        fetch: {
          includeHttpResponseReturnType: false,
        },
        mutator: {
          path: path.resolve(apiClientReactSrc, "custom-fetch.ts"),
          name: "customFetch",
        },
      },
    },
  },
  zod: {
    input: {
      target: "./openapi.yaml",
      override: {
        transformer: titleTransformer,
      },
    },
    output: {
      workspace: apiZodSrc,
      client: "zod",
      target: "generated",

      mode: "split",
      clean: true,
      prettier: true,
      override: {
        zod: {
          coerce: {
            query: ['boolean', 'number', 'string'],
            param: ['boolean', 'number', 'string'],
            body: ['bigint', 'date'],
            response: ['bigint', 'date'],
          },
        },
        useDates: true,
        useBigInt: true,
      },
    },
  },
});


// ============================================================
// FILE: lib/api-spec/package.json
// ============================================================
{
  "name": "@workspace/api-spec",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "codegen": "orval --config ./orval.config.ts && pnpm -w run typecheck:libs"
  },
  "devDependencies": {
    "orval": "^8.5.2"
  }
}


// ============================================================
// FILE: lib/db/src/schema/threats.ts
// ============================================================
import { pgTable, text, serial, integer, boolean, timestamp, real, jsonb } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod/v4";

export const threatsTable = pgTable("threats", {
  id: text("id").primaryKey(),
  ipAddress: text("ip_address").notNull(),
  ipSubnet: text("ip_subnet").notNull(),
  score: integer("score").notNull(),
  riskLevel: text("risk_level").notNull(),
  status: text("status").notNull().default("active"),
  route: text("route").notNull(),
  userAgent: text("user_agent"),
  technique: text("technique").notNull(),
  requestCount: integer("request_count").notNull().default(1),
  attributionConfidence: real("attribution_confidence"),
  geoLocation: text("geo_location"),
  asn: text("asn"),
  isTor: boolean("is_tor").notNull().default(false),
  isVpn: boolean("is_vpn").notNull().default(false),
  scoreComponents: jsonb("score_components"),
  attackTechniques: text("attack_techniques").array(),
  firstSeen: timestamp("first_seen", { withTimezone: true }).notNull().defaultNow(),
  lastSeen: timestamp("last_seen", { withTimezone: true }).notNull().defaultNow(),
});

export const insertThreatSchema = createInsertSchema(threatsTable).omit({ firstSeen: true, lastSeen: true });
export type InsertThreat = z.infer<typeof insertThreatSchema>;
export type Threat = typeof threatsTable.$inferSelect;


// ============================================================
// FILE: lib/db/src/schema/sessions.ts
// ============================================================
import { pgTable, text, integer, timestamp, jsonb } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod/v4";

export const sessionsTable = pgTable("sessions", {
  id: text("id").primaryKey(),
  type: text("type").notNull(),
  ipAddress: text("ip_address").notNull(),
  requestCount: integer("request_count").notNull().default(1),
  currentScore: integer("current_score").notNull().default(0),
  clonedToHoneypotAt: timestamp("cloned_to_honeypot_at", { withTimezone: true }),
  cloneLatencyMs: integer("clone_latency_ms"),
  scoreHistory: jsonb("score_history"),
  requestLog: jsonb("request_log"),
  startedAt: timestamp("started_at", { withTimezone: true }).notNull().defaultNow(),
  lastActivity: timestamp("last_activity", { withTimezone: true }).notNull().defaultNow(),
});

export const insertSessionSchema = createInsertSchema(sessionsTable).omit({ startedAt: true, lastActivity: true });
export type InsertSession = z.infer<typeof insertSessionSchema>;
export type Session = typeof sessionsTable.$inferSelect;


// ============================================================
// FILE: lib/db/src/schema/attack_profiles.ts
// ============================================================
import { pgTable, text, integer, real, timestamp, jsonb } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod/v4";

export const attackProfilesTable = pgTable("attack_profiles", {
  id: text("id").primaryKey(),
  fingerprint: text("fingerprint").notNull(),
  ipAddresses: text("ip_addresses").array().notNull(),
  technique: text("technique").notNull(),
  intent: text("intent").notNull(),
  attributionConfidence: real("attribution_confidence").notNull(),
  totalRequests: integer("total_requests").notNull().default(0),
  apiKeyRotations: integer("api_key_rotations").notNull().default(0),
  honeypotTimeMinutes: integer("honeypot_time_minutes").notNull().default(0),
  forensicReport: jsonb("forensic_report"),
  behaviorMap: jsonb("behavior_map"),
  fakeDataServed: text("fake_data_served").array(),
  firstSeen: timestamp("first_seen", { withTimezone: true }).notNull().defaultNow(),
  lastSeen: timestamp("last_seen", { withTimezone: true }).notNull().defaultNow(),
});

export const insertAttackProfileSchema = createInsertSchema(attackProfilesTable).omit({ firstSeen: true, lastSeen: true });
export type InsertAttackProfile = z.infer<typeof insertAttackProfileSchema>;
export type AttackProfile = typeof attackProfilesTable.$inferSelect;


// ============================================================
// FILE: lib/db/src/schema/canary_tokens.ts
// ============================================================
import { pgTable, text, integer, timestamp } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod/v4";

export const canaryTokensTable = pgTable("canary_tokens", {
  id: text("id").primaryKey(),
  name: text("name").notNull(),
  type: text("type").notNull(),
  location: text("location").notNull(),
  tripCount: integer("trip_count").notNull().default(0),
  lastTripped: timestamp("last_tripped", { withTimezone: true }),
  status: text("status").notNull().default("active"),
  createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
});

export const insertCanaryTokenSchema = createInsertSchema(canaryTokensTable).omit({ createdAt: true });
export type InsertCanaryToken = z.infer<typeof insertCanaryTokenSchema>;
export type CanaryToken = typeof canaryTokensTable.$inferSelect;

export const canaryTripsTable = pgTable("canary_trips", {
  id: text("id").primaryKey(),
  tokenId: text("token_id").notNull().references(() => canaryTokensTable.id),
  ipAddress: text("ip_address").notNull(),
  userAgent: text("user_agent").notNull(),
  sessionId: text("session_id").notNull(),
  threatId: text("threat_id").notNull(),
  cloneLatencyMs: integer("clone_latency_ms").notNull(),
  trippedAt: timestamp("tripped_at", { withTimezone: true }).notNull().defaultNow(),
});

export const insertCanaryTripSchema = createInsertSchema(canaryTripsTable).omit({ trippedAt: true });
export type InsertCanaryTrip = z.infer<typeof insertCanaryTripSchema>;
export type CanaryTrip = typeof canaryTripsTable.$inferSelect;


// ============================================================
// FILE: lib/db/src/schema/fake_server.ts
// ============================================================
import { pgTable, text, integer, real, boolean, timestamp, jsonb } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod/v4";

export const fakeRecordsTable = pgTable("fake_records", {
  id: text("id").primaryKey(),
  type: text("type").notNull(),
  data: jsonb("data").notNull(),
  believabilityScore: real("believability_score").notNull(),
  servedTo: integer("served_to").notNull().default(0),
  generatedAt: timestamp("generated_at", { withTimezone: true }).notNull().defaultNow(),
});

export const insertFakeRecordSchema = createInsertSchema(fakeRecordsTable).omit({ generatedAt: true });
export type InsertFakeRecord = z.infer<typeof insertFakeRecordSchema>;
export type FakeRecord = typeof fakeRecordsTable.$inferSelect;

export const fakeServerInteractionsTable = pgTable("fake_server_interactions", {
  id: text("id").primaryKey(),
  attackerIp: text("attacker_ip").notNull(),
  sessionId: text("session_id").notNull(),
  endpoint: text("endpoint").notNull(),
  method: text("method").notNull(),
  fakeRecordId: text("fake_record_id"),
  attackerBelievedData: boolean("attacker_believed_data").notNull().default(false),
  notes: text("notes").notNull().default(""),
  timestamp: timestamp("timestamp", { withTimezone: true }).notNull().defaultNow(),
});

export const insertFakeServerInteractionSchema = createInsertSchema(fakeServerInteractionsTable).omit({ timestamp: true });
export type InsertFakeServerInteraction = z.infer<typeof insertFakeServerInteractionSchema>;
export type FakeServerInteraction = typeof fakeServerInteractionsTable.$inferSelect;


// ============================================================
// FILE: lib/db/src/schema/learning.ts
// ============================================================
import { pgTable, text, real, timestamp } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod/v4";

export const learningImprovementsTable = pgTable("learning_improvements", {
  id: text("id").primaryKey(),
  type: text("type").notNull(),
  description: text("description").notNull(),
  triggeredBy: text("triggered_by").notNull(),
  impactScore: real("impact_score").notNull(),
  timestamp: timestamp("timestamp", { withTimezone: true }).notNull().defaultNow(),
});

export const insertLearningImprovementSchema = createInsertSchema(learningImprovementsTable).omit({ timestamp: true });
export type InsertLearningImprovement = z.infer<typeof insertLearningImprovementSchema>;
export type LearningImprovement = typeof learningImprovementsTable.$inferSelect;


// ============================================================
// FILE: lib/db/src/schema/pricing.ts
// ============================================================
import { pgTable, text, integer, real, boolean, timestamp, jsonb } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod/v4";

export const pricingPlansTable = pgTable("pricing_plans", {
  id: text("id").primaryKey(),
  name: text("name").notNull(),
  monthlyPrice: real("monthly_price").notNull(),
  annualPrice: real("annual_price").notNull(),
  description: text("description").notNull(),
  features: text("features").array().notNull(),
  requestsPerMonth: integer("requests_per_month").notNull(),
  apiKeys: integer("api_keys").notNull(),
  honeypotSessions: integer("honeypot_sessions").notNull(),
  supportLevel: text("support_level").notNull(),
  recommended: boolean("recommended").notNull().default(false),
  createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
});

export const pricingInquiriesTable = pgTable("pricing_inquiries", {
  id: text("id").primaryKey(),
  businessName: text("business_name").notNull(),
  contactName: text("contact_name").notNull(),
  email: text("email").notNull(),
  phone: text("phone"),
  planId: text("plan_id"),
  monthlyRequests: text("monthly_requests").notNull(),
  message: text("message"),
  submittedAt: timestamp("submitted_at", { withTimezone: true }).notNull().defaultNow(),
});

export const insertPricingInquirySchema = createInsertSchema(pricingInquiriesTable).omit({ submittedAt: true });
export type InsertPricingInquiry = z.infer<typeof insertPricingInquirySchema>;
export type PricingInquiry = typeof pricingInquiriesTable.$inferSelect;


// ============================================================
// FILE: lib/db/src/schema/index.ts
// ============================================================
export * from "./threats";
export * from "./sessions";
export * from "./attack_profiles";
export * from "./canary_tokens";
export * from "./fake_server";
export * from "./learning";
export * from "./pricing";


// ============================================================
// FILE: lib/db/src/index.ts
// ============================================================
import { drizzle } from "drizzle-orm/node-postgres";
import pg from "pg";
import * as schema from "./schema";

const { Pool } = pg;

if (!process.env.DATABASE_URL) {
  throw new Error(
    "DATABASE_URL must be set. Did you forget to provision a database?",
  );
}

export const pool = new Pool({ connectionString: process.env.DATABASE_URL });
export const db = drizzle(pool, { schema });

export * from "./schema";


// ============================================================
// FILE: lib/db/package.json
// ============================================================
{
  "name": "@workspace/db",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "exports": {
    ".": "./src/index.ts",
    "./schema": "./src/schema/index.ts"
  },
  "scripts": {
    "push": "drizzle-kit push --config ./drizzle.config.ts",
    "push-force": "drizzle-kit push --force --config ./drizzle.config.ts"
  },
  "dependencies": {
    "drizzle-orm": "catalog:",
    "drizzle-zod": "^0.8.3",
    "pg": "^8.20.0",
    "zod": "catalog:"
  },
  "devDependencies": {
    "@types/node": "catalog:",
    "@types/pg": "^8.18.0",
    "drizzle-kit": "^0.31.9"
  }
}


// ============================================================
// FILE: artifacts/api-server/src/index.ts
// ============================================================
import app from "./app";
import { logger } from "./lib/logger";
import { seedIfEmpty } from "./lib/seed";

const rawPort = process.env["PORT"];

if (!rawPort) {
  throw new Error(
    "PORT environment variable is required but was not provided.",
  );
}

const port = Number(rawPort);

if (Number.isNaN(port) || port <= 0) {
  throw new Error(`Invalid PORT value: "${rawPort}"`);
}

app.listen(port, async (err) => {
  if (err) {
    logger.error({ err }, "Error listening on port");
    process.exit(1);
  }

  logger.info({ port }, "Server listening");
  await seedIfEmpty().catch((e) => logger.error({ err: e }, "Seeding failed"));
});


// ============================================================
// FILE: artifacts/api-server/src/app.ts
// ============================================================
import express, { type Express } from "express";
import cors from "cors";
import pinoHttp from "pino-http";
import router from "./routes";
import { logger } from "./lib/logger";

const app: Express = express();

app.use(
  pinoHttp({
    logger,
    serializers: {
      req(req) {
        return {
          id: req.id,
          method: req.method,
          url: req.url?.split("?")[0],
        };
      },
      res(res) {
        return {
          statusCode: res.statusCode,
        };
      },
    },
  }),
);
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/api", router);

export default app;


// ============================================================
// FILE: artifacts/api-server/src/lib/logger.ts
// ============================================================
import pino from "pino";

const isProduction = process.env.NODE_ENV === "production";

export const logger = pino({
  level: process.env.LOG_LEVEL ?? "info",
  redact: [
    "req.headers.authorization",
    "req.headers.cookie",
    "res.headers['set-cookie']",
  ],
  ...(isProduction
    ? {}
    : {
        transport: {
          target: "pino-pretty",
          options: { colorize: true },
        },
      }),
});


// ============================================================
// FILE: artifacts/api-server/src/lib/seed.ts
// ============================================================
import crypto from "crypto";
import { db } from "@workspace/db";
import {
  threatsTable,
  sessionsTable,
  attackProfilesTable,
  canaryTokensTable,
  canaryTripsTable,
  fakeRecordsTable,
  fakeServerInteractionsTable,
  learningImprovementsTable,
  pricingPlansTable,
} from "@workspace/db";
import { logger } from "./logger";

function uid() {
  return crypto.randomUUID();
}

function randomInt(min: number, max: number) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function hoursAgo(h: number) {
  const d = new Date();
  d.setHours(d.getHours() - h);
  return d;
}

function minutesAgo(m: number) {
  const d = new Date();
  d.setMinutes(d.getMinutes() - m);
  return d;
}

export async function seedIfEmpty() {
  const existing = await db.select().from(threatsTable).limit(1);
  if (existing.length > 0) {
    logger.info("Database already seeded, skipping");
    return;
  }

  logger.info("Seeding database with sample data");

  // Pricing Plans
  await db.insert(pricingPlansTable).values([
    {
      id: "starter",
      name: "Starter",
      monthlyPrice: 49,
      annualPrice: 470,
      description: "Perfect for small businesses getting started with API security.",
      features: [
        "Up to 100K API requests/month",
        "AI threat scoring",
        "Honeypot redirection",
        "3 canary tokens",
        "Email threat alerts",
        "7-day memory window",
        "Basic forensic reports",
        "Community support",
      ],
      requestsPerMonth: 100000,
      apiKeys: 3,
      honeypotSessions: 50,
      supportLevel: "community",
      recommended: false,
    },
    {
      id: "professional",
      name: "Professional",
      monthlyPrice: 149,
      annualPrice: 1430,
      description: "Full threat intelligence with extended memory and priority support.",
      features: [
        "Up to 1M API requests/month",
        "30-day behavioural memory",
        "Cross-key correlation engine",
        "20 canary tokens",
        "Real-time fake data AI",
        "Full attacker attribution",
        "Session cloning (<100ms)",
        "Webhook notifications",
        "Priority email support",
      ],
      requestsPerMonth: 1000000,
      apiKeys: 10,
      honeypotSessions: 500,
      supportLevel: "priority",
      recommended: true,
    },
    {
      id: "enterprise",
      name: "Enterprise",
      monthlyPrice: 499,
      annualPrice: 4790,
      description: "Unlimited protection with dedicated security experts and custom integrations.",
      features: [
        "Unlimited API requests",
        "Custom threat thresholds",
        "Unlimited canary tokens",
        "Dedicated fake server AI",
        "Full MITRE ATT&CK mapping",
        "Custom forensic templates",
        "SIEM integration",
        "SLA guarantees",
        "Dedicated security team",
        "Custom learning models",
      ],
      requestsPerMonth: -1,
      apiKeys: -1,
      honeypotSessions: -1,
      supportLevel: "dedicated",
      recommended: false,
    },
  ]);

  // Threats
  const threatId1 = uid();
  const threatId2 = uid();
  const threatId3 = uid();

  await db.insert(threatsTable).values([
    {
      id: threatId1,
      ipAddress: "185.220.101.47",
      ipSubnet: "185.220.101.0/24",
      score: 87,
      riskLevel: "critical",
      status: "honeypotted",
      route: "fake_server",
      userAgent: "python-requests/2.28.0",
      technique: "SQL Injection via REST",
      requestCount: 342,
      attributionConfidence: 0.91,
      geoLocation: "Chisinau, Moldova",
      asn: "AS60068 (Datacamp Ltd)",
      isTor: false,
      isVpn: true,
      scoreComponents: { basePathBody: 54, memoryBoost: 18, correlationBoost: 12, spikeBoost: 3, total: 87 },
      attackTechniques: ["SQL injection", "Parameter enumeration", "Error-based extraction"],
      firstSeen: hoursAgo(48),
      lastSeen: minutesAgo(12),
    },
    {
      id: threatId2,
      ipAddress: "45.142.212.100",
      ipSubnet: "45.142.212.0/24",
      score: 72,
      riskLevel: "high",
      status: "honeypotted",
      route: "fake_server",
      userAgent: "curl/7.68.0",
      technique: "Credential Stuffing",
      requestCount: 1847,
      attributionConfidence: 0.78,
      geoLocation: "Amsterdam, Netherlands",
      asn: "AS202425 (IP Volume Inc)",
      isTor: false,
      isVpn: true,
      scoreComponents: { basePathBody: 38, memoryBoost: 20, correlationBoost: 12, spikeBoost: 2, total: 72 },
      attackTechniques: ["Credential stuffing", "API key rotation", "Distributed requests"],
      firstSeen: hoursAgo(6),
      lastSeen: minutesAgo(3),
    },
    {
      id: threatId3,
      ipAddress: "104.21.67.89",
      ipSubnet: "104.21.67.0/24",
      score: 61,
      riskLevel: "high",
      status: "active",
      route: "fake_server",
      userAgent: "axios/1.4.0",
      technique: "API Scraping",
      requestCount: 523,
      attributionConfidence: 0.62,
      geoLocation: "San Jose, USA",
      asn: "AS13335 (Cloudflare Inc)",
      isTor: false,
      isVpn: false,
      scoreComponents: { basePathBody: 29, memoryBoost: 15, correlationBoost: 12, spikeBoost: 5, total: 61 },
      attackTechniques: ["Systematic endpoint enumeration", "Rate limit probing"],
      firstSeen: hoursAgo(2),
      lastSeen: minutesAgo(1),
    },
  ]);

  // Sessions
  const sess1 = uid();
  const sess2 = uid();
  const sess3 = uid();

  await db.insert(sessionsTable).values([
    {
      id: sess1,
      type: "honeypot",
      ipAddress: "185.220.101.47",
      requestCount: 342,
      currentScore: 87,
      clonedToHoneypotAt: hoursAgo(47),
      cloneLatencyMs: 74,
      scoreHistory: [
        { timestamp: hoursAgo(48).toISOString(), score: 32 },
        { timestamp: hoursAgo(47).toISOString(), score: 61, event: "canary_tripped" },
        { timestamp: hoursAgo(47).toISOString(), score: 87, event: "cloned_to_honeypot" },
      ],
      requestLog: [
        { timestamp: hoursAgo(48).toISOString(), method: "GET", path: "/api/users", score: 22, servedBy: "real_server" },
        { timestamp: hoursAgo(47).toISOString(), method: "GET", path: "/api/admin/config", score: 61, servedBy: "real_server" },
        { timestamp: minutesAgo(30).toISOString(), method: "POST", path: "/api/users/search", score: 87, servedBy: "fake_server" },
      ],
    },
    {
      id: sess2,
      type: "honeypot",
      ipAddress: "45.142.212.100",
      requestCount: 1847,
      currentScore: 72,
      clonedToHoneypotAt: hoursAgo(5),
      cloneLatencyMs: 88,
      scoreHistory: [
        { timestamp: hoursAgo(6).toISOString(), score: 28 },
        { timestamp: hoursAgo(5).toISOString(), score: 58, event: "key_rotation_detected" },
        { timestamp: hoursAgo(5).toISOString(), score: 72, event: "cloned_to_honeypot" },
      ],
      requestLog: [
        { timestamp: hoursAgo(6).toISOString(), method: "POST", path: "/api/auth/login", score: 28, servedBy: "real_server" },
        { timestamp: hoursAgo(5).toISOString(), method: "POST", path: "/api/auth/login", score: 72, servedBy: "fake_server" },
      ],
    },
    {
      id: sess3,
      type: "real",
      ipAddress: "192.168.1.50",
      requestCount: 12,
      currentScore: 8,
      clonedToHoneypotAt: null,
      cloneLatencyMs: null,
      scoreHistory: [
        { timestamp: hoursAgo(1).toISOString(), score: 5 },
        { timestamp: minutesAgo(20).toISOString(), score: 8 },
      ],
      requestLog: [
        { timestamp: hoursAgo(1).toISOString(), method: "GET", path: "/api/products", score: 5, servedBy: "real_server" },
        { timestamp: minutesAgo(20).toISOString(), method: "GET", path: "/api/orders/123", score: 8, servedBy: "real_server" },
      ],
    },
  ]);

  // Attack Profiles
  const attackId1 = uid();
  const attackId2 = uid();

  await db.insert(attackProfilesTable).values([
    {
      id: attackId1,
      fingerprint: "fp_a7c3d9e2b1f845",
      ipAddresses: ["185.220.101.47", "185.220.101.52", "185.220.101.61"],
      technique: "SQL Injection via REST",
      intent: "data_exfiltration",
      attributionConfidence: 0.91,
      totalRequests: 342,
      apiKeyRotations: 3,
      honeypotTimeMinutes: 2847,
      forensicReport: {
        summary: "Organized actor conducting systematic SQL injection against customer data endpoints. Multiple API keys used with coordinated timing suggests automated tooling with human oversight.",
        toolsIdentified: ["sqlmap 1.7.8", "python-requests", "Custom injection framework"],
        indicatorsOfCompromise: ["User-agent: python-requests/2.28.0", "185.220.101.0/24 subnet", "Consistent 2.3s request cadence"],
        estimatedActorType: "organized_group",
        geolocationChain: ["Chisinau, Moldova", "Frankfurt, Germany (VPN exit)"],
        mitreTechniques: ["T1190", "T1078", "T1560", "T1041"],
      },
      behaviorMap: [
        { timestamp: hoursAgo(48).toISOString(), action: "Initial reconnaissance", detail: "Probed /api/users endpoint structure", significance: "low" },
        { timestamp: hoursAgo(47).toISOString(), action: "SQL injection attempt", detail: "UNION-based injection on /api/users/search", significance: "high" },
        { timestamp: hoursAgo(47).toISOString(), action: "Canary token tripped", detail: "Accessed synthetic customer record ID cny_8f2a1", significance: "high" },
        { timestamp: hoursAgo(46).toISOString(), action: "Cloned to fake server", detail: "Session transparently redirected, attacker unaware", significance: "high" },
        { timestamp: hoursAgo(40).toISOString(), action: "Exfiltration attempt", detail: "Attempted bulk download of 'customer' records", significance: "high" },
      ],
      fakeDataServed: ["fr_cust_001", "fr_cust_002", "fr_inv_001"],
      firstSeen: hoursAgo(48),
      lastSeen: minutesAgo(12),
    },
    {
      id: attackId2,
      fingerprint: "fp_b2e8f1a4c79d36",
      ipAddresses: ["45.142.212.100", "45.142.212.105"],
      technique: "Credential Stuffing",
      intent: "credential_stuffing",
      attributionConfidence: 0.78,
      totalRequests: 1847,
      apiKeyRotations: 7,
      honeypotTimeMinutes: 302,
      forensicReport: {
        summary: "Automated credential stuffing attack using a list of known breached credentials. High API key rotation rate suggests awareness of detection systems.",
        toolsIdentified: ["Sentry MBA", "OpenBullet 2", "Custom proxy rotator"],
        indicatorsOfCompromise: ["curl/7.68.0 user-agent pattern", "7 API key rotations in 6 hours", "Sequential credential patterns"],
        estimatedActorType: "script_kiddie",
        geolocationChain: ["Amsterdam, Netherlands", "Rotterdam, Netherlands (proxy)"],
        mitreTechniques: ["T1110.004", "T1078.004", "T1557"],
      },
      behaviorMap: [
        { timestamp: hoursAgo(6).toISOString(), action: "Credential list upload", detail: "Started testing credential pairs at /api/auth/login", significance: "medium" },
        { timestamp: hoursAgo(5).toISOString(), action: "API key rotation", detail: "Switched to new API key after 250 requests", significance: "high" },
        { timestamp: hoursAgo(5).toISOString(), action: "Correlation detected", detail: "Cross-key fingerprint matched — same device across 7 keys", significance: "high" },
        { timestamp: hoursAgo(5).toISOString(), action: "Honeypot redirect", detail: "All requests now routed to fake authentication server", significance: "high" },
      ],
      fakeDataServed: ["fr_cred_001", "fr_cred_002"],
      firstSeen: hoursAgo(6),
      lastSeen: minutesAgo(3),
    },
  ]);

  // Canary Tokens
  const tokenId1 = uid();
  const tokenId2 = uid();
  const tokenId3 = uid();

  await db.insert(canaryTokensTable).values([
    {
      id: tokenId1,
      name: "Admin API Key Canary",
      type: "api_key",
      location: "/api/admin responses",
      tripCount: 2,
      lastTripped: hoursAgo(47),
      status: "tripped",
    },
    {
      id: tokenId2,
      name: "Customer Data URL Canary",
      type: "url",
      location: "/api/customers/export",
      tripCount: 0,
      lastTripped: null,
      status: "active",
    },
    {
      id: tokenId3,
      name: "Salary Database Canary",
      type: "database_record",
      location: "employee table, row_id: emp_canary_001",
      tripCount: 1,
      lastTripped: hoursAgo(5),
      status: "tripped",
    },
  ]);

  // Canary Trips
  await db.insert(canaryTripsTable).values([
    {
      id: uid(),
      tokenId: tokenId1,
      ipAddress: "185.220.101.47",
      userAgent: "python-requests/2.28.0",
      sessionId: sess1,
      threatId: threatId1,
      cloneLatencyMs: 74,
      trippedAt: hoursAgo(47),
    },
    {
      id: uid(),
      tokenId: tokenId3,
      ipAddress: "45.142.212.100",
      userAgent: "curl/7.68.0",
      sessionId: sess2,
      threatId: threatId2,
      cloneLatencyMs: 88,
      trippedAt: hoursAgo(5),
    },
  ]);

  // Fake Records
  const fr1 = uid();
  const fr2 = uid();
  const fr3 = uid();
  const fr4 = uid();

  await db.insert(fakeRecordsTable).values([
    {
      id: fr1,
      type: "customer",
      data: {
        id: "cust_8f2a1c9d",
        name: "Northgate Industrial Ltd",
        email: "accounts@northgate-ind.co.uk",
        phone: "+44 20 7946 0234",
        revenue: "$4.2M",
        creditLimit: "$500,000",
        accountManager: "Sarah Pemberton",
        status: "premium",
      },
      believabilityScore: 0.97,
      servedTo: 1,
    },
    {
      id: fr2,
      type: "invoice",
      data: {
        id: "INV-2024-10847",
        client: "Northgate Industrial Ltd",
        amount: "$128,450.00",
        currency: "USD",
        dueDate: "2024-11-15",
        items: [
          { description: "Q4 Supply Agreement - Phase 1", qty: 1, unit: "$89,000" },
          { description: "Logistics & Handling", qty: 1, unit: "$39,450" },
        ],
        bankDetails: { account: "****4721", routing: "****8834", bank: "First Commerce Bank" },
      },
      believabilityScore: 0.95,
      servedTo: 1,
    },
    {
      id: fr3,
      type: "employee",
      data: {
        id: "emp_canary_001",
        name: "Marcus Thompson",
        role: "VP of Sales",
        salary: "$187,500",
        bonus: "$45,000",
        ssn: "***-**-4821",
        email: "m.thompson@company.internal",
        department: "Commercial",
        startDate: "2019-03-01",
      },
      believabilityScore: 0.93,
      servedTo: 1,
    },
    {
      id: fr4,
      type: "credential",
      data: {
        username: "admin@company.internal",
        apiKey: "gw_live_FAKE7xKp9mQr2vBnLsYzEd",
        permissions: ["read:all", "write:users", "admin:billing"],
        lastUsed: "2024-04-18T14:23:11Z",
        note: "Production API key — rotate quarterly",
      },
      believabilityScore: 0.94,
      servedTo: 2,
    },
  ]);

  // Fake Server Interactions
  await db.insert(fakeServerInteractionsTable).values([
    {
      id: uid(),
      attackerIp: "185.220.101.47",
      sessionId: sess1,
      endpoint: "/api/customers",
      method: "GET",
      fakeRecordId: fr1,
      attackerBelievedData: true,
      notes: "Attacker retrieved customer list and continued querying — did not detect fake data",
      timestamp: hoursAgo(46),
    },
    {
      id: uid(),
      attackerIp: "185.220.101.47",
      sessionId: sess1,
      endpoint: "/api/invoices/bulk",
      method: "GET",
      fakeRecordId: fr2,
      attackerBelievedData: true,
      notes: "Bulk invoice export attempted — served 2,340 fake invoice records",
      timestamp: hoursAgo(40),
    },
    {
      id: uid(),
      attackerIp: "45.142.212.100",
      sessionId: sess2,
      endpoint: "/api/auth/login",
      method: "POST",
      fakeRecordId: fr4,
      attackerBelievedData: true,
      notes: "Fake successful auth response served — attacker continued with fake session token",
      timestamp: hoursAgo(5),
    },
  ]);

  // Learning Improvements
  await db.insert(learningImprovementsTable).values([
    {
      id: uid(),
      type: "model_update",
      description: "Improved SQL injection pattern detection — added 12 new UNION-based payloads from this session",
      triggeredBy: `Threat ${threatId1}`,
      impactScore: 0.87,
      timestamp: hoursAgo(24),
    },
    {
      id: uid(),
      type: "canary_repositioned",
      description: "Moved API key canary to /api/admin/config response body — higher attacker discovery rate expected",
      triggeredBy: "Attack session analysis",
      impactScore: 0.72,
      timestamp: hoursAgo(20),
    },
    {
      id: uid(),
      type: "fake_data_improved",
      description: "Enhanced fake invoice believability — added realistic line items, bank routing numbers, and PDF metadata",
      triggeredBy: `Session ${sess1}`,
      impactScore: 0.91,
      timestamp: hoursAgo(12),
    },
    {
      id: uid(),
      type: "correlation_rule_added",
      description: "New rule: Flag fingerprints rotating API keys at >1/hour — cross-key correlation threshold tightened",
      triggeredBy: `Attack ${attackId2}`,
      impactScore: 0.79,
      timestamp: hoursAgo(4),
    },
    {
      id: uid(),
      type: "threshold_adjusted",
      description: "Lowered honeypot redirect threshold for /api/admin paths from 55 to 42 — faster detection on sensitive endpoints",
      triggeredBy: "False negative analysis",
      impactScore: 0.68,
      timestamp: minutesAgo(90),
    },
  ]);

  logger.info("Database seeding complete");
}


// ============================================================
// FILE: artifacts/api-server/src/routes/index.ts
// ============================================================
import { Router, type IRouter } from "express";
import healthRouter from "./health";
import dashboardRouter from "./dashboard";
import threatsRouter from "./threats";
import sessionsRouter from "./sessions";
import attacksRouter from "./attacks";
import canaryRouter from "./canary";
import fakeServerRouter from "./fake_server";
import learningRouter from "./learning";
import pricingRouter from "./pricing";

const router: IRouter = Router();

router.use(healthRouter);
router.use(dashboardRouter);
router.use(threatsRouter);
router.use(sessionsRouter);
router.use(attacksRouter);
router.use(canaryRouter);
router.use(fakeServerRouter);
router.use(learningRouter);
router.use(pricingRouter);

export default router;


// ============================================================
// FILE: artifacts/api-server/src/routes/dashboard.ts
// ============================================================
import { Router, type IRouter } from "express";
import { db } from "@workspace/db";
import {
  threatsTable,
  sessionsTable,
  canaryTripsTable,
  learningImprovementsTable,
} from "@workspace/db";
import { sql, gte, desc } from "drizzle-orm";

const router: IRouter = Router();

router.get("/dashboard/summary", async (_req, res): Promise<void> => {
  const oneDayAgo = new Date(Date.now() - 86400000);

  const [threatsToday] = await db
    .select({ count: sql<number>`count(*)` })
    .from(threatsTable)
    .where(gte(threatsTable.firstSeen, oneDayAgo));

  const [honeypotted] = await db
    .select({ count: sql<number>`count(*)` })
    .from(sessionsTable)
    .where(sql`type = 'honeypot'`);

  const [canaryTrips] = await db
    .select({ count: sql<number>`count(*)` })
    .from(canaryTripsTable)
    .where(gte(canaryTripsTable.trippedAt, oneDayAgo));

  const [activeAttackers] = await db
    .select({ count: sql<number>`count(*)` })
    .from(threatsTable)
    .where(sql`status = 'active' or status = 'honeypotted'`);

  const [avgScore] = await db
    .select({ avg: sql<number>`avg(score)` })
    .from(threatsTable);

  const [blockedReqs] = await db
    .select({ total: sql<number>`sum(request_count)` })
    .from(threatsTable)
    .where(sql`status = 'honeypotted'`);

  const [learningEvents] = await db
    .select({ count: sql<number>`count(*)` })
    .from(learningImprovementsTable);

  res.json({
    totalThreatsToday: Number(threatsToday.count),
    honeypottedSessions: Number(honeypotted.count),
    canaryTrips: Number(canaryTrips.count),
    activeAttackers: Number(activeAttackers.count),
    avgThreatScore: Math.round(Number(avgScore.avg) || 0),
    blockedRequests: Number(blockedReqs.total || 0),
    aiAccuracyRate: 0.968,
    learningEvents: Number(learningEvents.count),
    protectedBusinesses: 147,
    uptimeDays: 312,
  });
});

router.get("/dashboard/live-feed", async (req, res): Promise<void> => {
  const limit = Number(req.query["limit"] ?? 20);

  const threats = await db
    .select()
    .from(threatsTable)
    .orderBy(desc(threatsTable.lastSeen))
    .limit(limit);

  const feed = threats.map((t) => ({
    id: t.id,
    timestamp: t.lastSeen,
    type: t.status === "honeypotted" ? "honeypot_trip" : "threat_detected",
    severity: t.riskLevel as "low" | "medium" | "high" | "critical",
    ipAddress: t.ipAddress,
    message: `${t.technique} detected from ${t.ipAddress} — score ${t.score}`,
    score: t.score,
    route: t.route as "real_server" | "fake_server",
  }));

  res.json(feed);
});

router.get("/dashboard/score-timeline", async (req, res): Promise<void> => {
  const hours = Number(req.query["hours"] ?? 24);
  const cutoff = new Date(Date.now() - hours * 3600000);

  const threats = await db
    .select()
    .from(threatsTable)
    .where(gte(threatsTable.firstSeen, cutoff));

  const buckets: Record<string, { scores: number[]; honeypot: number }> = {};

  for (const t of threats) {
    const key = new Date(t.firstSeen).toISOString().slice(0, 13) + ":00:00Z";
    if (!buckets[key]) buckets[key] = { scores: [], honeypot: 0 };
    buckets[key].scores.push(t.score);
    if (t.status === "honeypotted") buckets[key].honeypot++;
  }

  const timeline = Object.entries(buckets)
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([ts, data]) => ({
      timestamp: ts,
      avgScore: data.scores.length
        ? Math.round(data.scores.reduce((a, b) => a + b, 0) / data.scores.length)
        : 0,
      threatCount: data.scores.length,
      honeypotCount: data.honeypot,
    }));

  if (timeline.length === 0) {
    const now = new Date();
    for (let i = hours - 1; i >= 0; i--) {
      const d = new Date(now.getTime() - i * 3600000);
      d.setMinutes(0, 0, 0);
      timeline.push({
        timestamp: d.toISOString(),
        avgScore: 0,
        threatCount: 0,
        honeypotCount: 0,
      });
    }
  }

  res.json(timeline);
});

export default router;


// ============================================================
// FILE: artifacts/api-server/src/routes/threats.ts
// ============================================================
import { Router, type IRouter } from "express";
import { db } from "@workspace/db";
import { threatsTable } from "@workspace/db";
import { eq, desc, and, sql } from "drizzle-orm";

const router: IRouter = Router();

router.get("/threats", async (req, res): Promise<void> => {
  const { status, riskLevel } = req.query;
  const limit = Number(req.query["limit"] ?? 50);
  const offset = Number(req.query["offset"] ?? 0);

  const conditions = [];
  if (status && typeof status === "string") {
    conditions.push(eq(threatsTable.status, status));
  }
  if (riskLevel && typeof riskLevel === "string") {
    conditions.push(eq(threatsTable.riskLevel, riskLevel));
  }

  const where = conditions.length > 0 ? and(...conditions) : undefined;

  const [{ count }] = await db
    .select({ count: sql<number>`count(*)` })
    .from(threatsTable)
    .where(where);

  const threats = await db
    .select()
    .from(threatsTable)
    .where(where)
    .orderBy(desc(threatsTable.lastSeen))
    .limit(limit)
    .offset(offset);

  res.json({
    threats: threats.map((t) => ({
      id: t.id,
      ipAddress: t.ipAddress,
      ipSubnet: t.ipSubnet,
      score: t.score,
      riskLevel: t.riskLevel,
      status: t.status,
      route: t.route,
      firstSeen: t.firstSeen,
      lastSeen: t.lastSeen,
      requestCount: t.requestCount,
      technique: t.technique,
    })),
    total: Number(count),
    offset,
    limit,
  });
});

router.get("/threats/:threatId", async (req, res): Promise<void> => {
  const id = Array.isArray(req.params["threatId"]) ? req.params["threatId"][0] : req.params["threatId"];
  const threat = await db.select().from(threatsTable).where(eq(threatsTable.id, id)).limit(1);

  if (!threat[0]) {
    res.status(404).json({ error: "Threat not found" });
    return;
  }

  const t = threat[0];
  res.json({
    id: t.id,
    ipAddress: t.ipAddress,
    ipSubnet: t.ipSubnet,
    score: t.score,
    riskLevel: t.riskLevel,
    status: t.status,
    route: t.route,
    firstSeen: t.firstSeen,
    lastSeen: t.lastSeen,
    requestCount: t.requestCount,
    technique: t.technique,
    userAgent: t.userAgent ?? "",
    scoreComponents: (t.scoreComponents as Record<string, number>) ?? { basePathBody: 0, memoryBoost: 0, correlationBoost: 0, spikeBoost: 0, total: 0 },
    sessionIds: [],
    canaryTokensFired: [],
    attackTechniques: t.attackTechniques ?? [],
    attributionConfidence: t.attributionConfidence ?? 0,
    geoLocation: t.geoLocation ?? "Unknown",
    asn: t.asn ?? "Unknown",
    isTor: t.isTor,
    isVpn: t.isVpn,
  });
});

router.post("/threats/:threatId/dismiss", async (req, res): Promise<void> => {
  const id = Array.isArray(req.params["threatId"]) ? req.params["threatId"][0] : req.params["threatId"];

  const [updated] = await db
    .update(threatsTable)
    .set({ status: "dismissed" })
    .where(eq(threatsTable.id, id))
    .returning();

  if (!updated) {
    res.status(404).json({ error: "Threat not found" });
    return;
  }

  res.json({
    id: updated.id,
    ipAddress: updated.ipAddress,
    ipSubnet: updated.ipSubnet,
    score: updated.score,
    riskLevel: updated.riskLevel,
    status: updated.status,
    route: updated.route,
    firstSeen: updated.firstSeen,
    lastSeen: updated.lastSeen,
    requestCount: updated.requestCount,
    technique: updated.technique,
    userAgent: updated.userAgent ?? "",
    scoreComponents: (updated.scoreComponents as Record<string, number>) ?? { basePathBody: 0, memoryBoost: 0, correlationBoost: 0, spikeBoost: 0, total: 0 },
    sessionIds: [],
    canaryTokensFired: [],
    attackTechniques: updated.attackTechniques ?? [],
    attributionConfidence: updated.attributionConfidence ?? 0,
    geoLocation: updated.geoLocation ?? "Unknown",
    asn: updated.asn ?? "Unknown",
    isTor: updated.isTor,
    isVpn: updated.isVpn,
  });
});

export default router;


// ============================================================
// FILE: artifacts/api-server/src/routes/sessions.ts
// ============================================================
import { Router, type IRouter } from "express";
import { db } from "@workspace/db";
import { sessionsTable } from "@workspace/db";
import { eq, desc } from "drizzle-orm";

const router: IRouter = Router();

router.get("/sessions", async (req, res): Promise<void> => {
  const { type } = req.query;
  const limit = Number(req.query["limit"] ?? 30);

  let query = db.select().from(sessionsTable).orderBy(desc(sessionsTable.lastActivity)).limit(limit);
  if (type && typeof type === "string") {
    const sessions = await db
      .select()
      .from(sessionsTable)
      .where(eq(sessionsTable.type, type))
      .orderBy(desc(sessionsTable.lastActivity))
      .limit(limit);
    res.json(sessions.map(mapSession));
    return;
  }

  const sessions = await query;
  res.json(sessions.map(mapSession));
});

router.get("/sessions/:sessionId", async (req, res): Promise<void> => {
  const id = Array.isArray(req.params["sessionId"]) ? req.params["sessionId"][0] : req.params["sessionId"];
  const rows = await db.select().from(sessionsTable).where(eq(sessionsTable.id, id)).limit(1);

  if (!rows[0]) {
    res.status(404).json({ error: "Session not found" });
    return;
  }

  const s = rows[0];
  res.json({
    ...mapSession(s),
    scoreHistory: (s.scoreHistory as object[]) ?? [],
    requestLog: (s.requestLog as object[]) ?? [],
  });
});

function mapSession(s: typeof sessionsTable.$inferSelect) {
  return {
    id: s.id,
    type: s.type,
    ipAddress: s.ipAddress,
    startedAt: s.startedAt,
    lastActivity: s.lastActivity,
    requestCount: s.requestCount,
    currentScore: s.currentScore,
    clonedToHoneypotAt: s.clonedToHoneypotAt ?? null,
    cloneLatencyMs: s.cloneLatencyMs ?? null,
  };
}

export default router;


// ============================================================
// FILE: artifacts/api-server/src/routes/attacks.ts
// ============================================================
import { Router, type IRouter } from "express";
import { db } from "@workspace/db";
import { attackProfilesTable } from "@workspace/db";
import { eq, desc } from "drizzle-orm";

const router: IRouter = Router();

router.get("/attacks", async (req, res): Promise<void> => {
  const limit = Number(req.query["limit"] ?? 20);

  const profiles = await db
    .select()
    .from(attackProfilesTable)
    .orderBy(desc(attackProfilesTable.lastSeen))
    .limit(limit);

  res.json(profiles.map(mapProfile));
});

router.get("/attacks/stats/techniques", async (_req, res): Promise<void> => {
  const profiles = await db.select().from(attackProfilesTable);

  const counts: Record<string, number> = {};
  for (const p of profiles) {
    counts[p.intent] = (counts[p.intent] ?? 0) + 1;
  }

  const total = Object.values(counts).reduce((a, b) => a + b, 0) || 1;

  const result = Object.entries(counts).map(([technique, count]) => ({
    technique,
    count,
    percentage: Math.round((count / total) * 1000) / 10,
  }));

  res.json(result);
});

router.get("/attacks/:attackId", async (req, res): Promise<void> => {
  const id = Array.isArray(req.params["attackId"]) ? req.params["attackId"][0] : req.params["attackId"];

  const rows = await db
    .select()
    .from(attackProfilesTable)
    .where(eq(attackProfilesTable.id, id))
    .limit(1);

  if (!rows[0]) {
    res.status(404).json({ error: "Attack profile not found" });
    return;
  }

  const p = rows[0];
  res.json({
    ...mapProfile(p),
    forensicReport: p.forensicReport ?? {},
    behaviorMap: (p.behaviorMap as object[]) ?? [],
    fakeDataServed: p.fakeDataServed ?? [],
  });
});

function mapProfile(p: typeof attackProfilesTable.$inferSelect) {
  return {
    id: p.id,
    fingerprint: p.fingerprint,
    ipAddresses: p.ipAddresses,
    technique: p.technique,
    intent: p.intent,
    attributionConfidence: p.attributionConfidence,
    firstSeen: p.firstSeen,
    lastSeen: p.lastSeen,
    totalRequests: p.totalRequests,
    apiKeyRotations: p.apiKeyRotations,
    honeypotTimeMinutes: p.honeypotTimeMinutes,
  };
}

export default router;


// ============================================================
// FILE: artifacts/api-server/src/routes/canary.ts
// ============================================================
import { Router, type IRouter } from "express";
import crypto from "crypto";
import { db } from "@workspace/db";
import { canaryTokensTable, canaryTripsTable } from "@workspace/db";
import { eq, desc } from "drizzle-orm";
import { CreateCanaryTokenBody } from "@workspace/api-zod";

const router: IRouter = Router();

router.get("/canary-tokens", async (_req, res): Promise<void> => {
  const tokens = await db
    .select()
    .from(canaryTokensTable)
    .orderBy(desc(canaryTokensTable.createdAt));

  res.json(tokens);
});

router.post("/canary-tokens", async (req, res): Promise<void> => {
  const parsed = CreateCanaryTokenBody.safeParse(req.body);
  if (!parsed.success) {
    res.status(400).json({ error: parsed.error.message });
    return;
  }

  const [token] = await db
    .insert(canaryTokensTable)
    .values({
      id: `cny_${crypto.randomBytes(8).toString("hex")}`,
      name: parsed.data.name,
      type: parsed.data.type,
      location: parsed.data.location,
      tripCount: 0,
      status: "active",
    })
    .returning();

  res.status(201).json(token);
});

router.get("/canary-tokens/:tokenId/trips", async (req, res): Promise<void> => {
  const id = Array.isArray(req.params["tokenId"]) ? req.params["tokenId"][0] : req.params["tokenId"];

  const trips = await db
    .select()
    .from(canaryTripsTable)
    .where(eq(canaryTripsTable.tokenId, id))
    .orderBy(desc(canaryTripsTable.trippedAt));

  res.json(trips);
});

export default router;


// ============================================================
// FILE: artifacts/api-server/src/routes/fake_server.ts
// ============================================================
import { Router, type IRouter } from "express";
import { db } from "@workspace/db";
import { fakeRecordsTable, fakeServerInteractionsTable, sessionsTable } from "@workspace/db";
import { eq, desc, sql } from "drizzle-orm";

const router: IRouter = Router();

router.get("/fake-server/records", async (req, res): Promise<void> => {
  const { type } = req.query;
  const limit = Number(req.query["limit"] ?? 20);

  const [{ count }] = await db
    .select({ count: sql<number>`count(*)` })
    .from(fakeRecordsTable)
    .where(type && typeof type === "string" ? eq(fakeRecordsTable.type, type) : undefined);

  const records = await db
    .select()
    .from(fakeRecordsTable)
    .where(type && typeof type === "string" ? eq(fakeRecordsTable.type, type) : undefined)
    .orderBy(desc(fakeRecordsTable.generatedAt))
    .limit(limit);

  res.json({
    records,
    total: Number(count),
  });
});

router.get("/fake-server/interactions", async (req, res): Promise<void> => {
  const limit = Number(req.query["limit"] ?? 30);

  const interactions = await db
    .select()
    .from(fakeServerInteractionsTable)
    .orderBy(desc(fakeServerInteractionsTable.timestamp))
    .limit(limit);

  res.json(
    interactions.map((i) => ({
      id: i.id,
      timestamp: i.timestamp,
      attackerIp: i.attackerIp,
      sessionId: i.sessionId,
      endpoint: i.endpoint,
      method: i.method,
      fakeRecordId: i.fakeRecordId ?? null,
      attackerBelievedData: i.attackerBelievedData,
      notes: i.notes,
    }))
  );
});

router.get("/fake-server/stats", async (_req, res): Promise<void> => {
  const [{ total }] = await db
    .select({ total: sql<number>`count(*)` })
    .from(fakeServerInteractionsTable);

  const [{ active }] = await db
    .select({ active: sql<number>`count(*)` })
    .from(sessionsTable)
    .where(sql`type = 'honeypot'`);

  const [{ believed }] = await db
    .select({ believed: sql<number>`count(*)` })
    .from(fakeServerInteractionsTable)
    .where(sql`attacker_believed_data = true`);

  const [{ fakeReqs }] = await db
    .select({ fakeReqs: sql<number>`count(*)` })
    .from(fakeServerInteractionsTable)
    .where(sql`fake_record_id is not null`);

  const totalNum = Number(total);
  const believedNum = Number(believed);

  res.json({
    totalInteractions: totalNum,
    activeHoneypotSessions: Number(active),
    avgTimeInHoneypotMinutes: 214.3,
    fakeDataRequests: Number(fakeReqs),
    attackersBelievedData: believedNum,
    believabilityRate: totalNum > 0 ? Math.round((believedNum / totalNum) * 1000) / 10 : 0,
    avgCloneLatencyMs: 81.2,
    fastestCloneMs: 61,
    dataTypesServed: {
      customer: 1,
      invoice: 1,
      employee: 1,
      credential: 2,
    },
  });
});

export default router;


// ============================================================
// FILE: artifacts/api-server/src/routes/learning.ts
// ============================================================
import { Router, type IRouter } from "express";
import { db } from "@workspace/db";
import { learningImprovementsTable } from "@workspace/db";
import { desc } from "drizzle-orm";

const router: IRouter = Router();

router.get("/learning/metrics", async (_req, res): Promise<void> => {
  const improvements = await db.select().from(learningImprovementsTable);
  const lastImprovement = improvements.sort(
    (a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime()
  )[0];

  res.json({
    totalTrainingEvents: 18742,
    modelAccuracy: 0.968,
    falsePositiveRate: 0.021,
    falseNegativeRate: 0.011,
    avgDetectionTimeMs: 47.3,
    canaryPlacementUpdates: improvements.filter((i) => i.type === "canary_repositioned").length,
    fakeDataImprovements: improvements.filter((i) => i.type === "fake_data_improved").length,
    lastTrainedAt: lastImprovement?.timestamp ?? new Date().toISOString(),
    memoryWindowDays: 30,
    attacksLearnedFrom: improvements.length,
  });
});

router.get("/learning/improvements", async (req, res): Promise<void> => {
  const limit = Number(req.query["limit"] ?? 10);

  const improvements = await db
    .select()
    .from(learningImprovementsTable)
    .orderBy(desc(learningImprovementsTable.timestamp))
    .limit(limit);

  res.json(improvements);
});

export default router;


// ============================================================
// FILE: artifacts/api-server/src/routes/pricing.ts
// ============================================================
import { Router, type IRouter } from "express";
import crypto from "crypto";
import { db } from "@workspace/db";
import { pricingPlansTable, pricingInquiriesTable } from "@workspace/db";
import { SubmitPricingInquiryBody } from "@workspace/api-zod";

const router: IRouter = Router();

router.get("/pricing/plans", async (_req, res): Promise<void> => {
  const plans = await db.select().from(pricingPlansTable);
  res.json(plans);
});

router.post("/pricing/inquiry", async (req, res): Promise<void> => {
  const parsed = SubmitPricingInquiryBody.safeParse(req.body);
  if (!parsed.success) {
    res.status(400).json({ error: parsed.error.message });
    return;
  }

  const id = `inq_${crypto.randomBytes(8).toString("hex")}`;

  await db.insert(pricingInquiriesTable).values({
    id,
    businessName: parsed.data.businessName,
    contactName: parsed.data.contactName,
    email: parsed.data.email,
    phone: parsed.data.phone ?? null,
    planId: parsed.data.planId ?? null,
    monthlyRequests: parsed.data.monthlyRequests,
    message: parsed.data.message ?? null,
  });

  res.status(201).json({
    id,
    submittedAt: new Date().toISOString(),
    message: "Thank you! Our security team will contact you within 24 hours to discuss your protection needs.",
  });
});

export default router;


// ============================================================
// FILE: artifacts/api-server/src/routes/health.ts
// ============================================================
import { Router, type IRouter } from "express";
import { HealthCheckResponse } from "@workspace/api-zod";

const router: IRouter = Router();

router.get("/healthz", (_req, res) => {
  const data = HealthCheckResponse.parse({ status: "ok" });
  res.json(data);
});

export default router;


// ============================================================
// FILE: artifacts/api-server/package.json
// ============================================================
{
  "name": "@workspace/api-server",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "export NODE_ENV=development && pnpm run build && pnpm run start",
    "build": "node ./build.mjs",
    "start": "node --enable-source-maps ./dist/index.mjs",
    "typecheck": "tsc -p tsconfig.json --noEmit"
  },
  "dependencies": {
    "@workspace/api-zod": "workspace:*",
    "@workspace/db": "workspace:*",
    "cookie-parser": "^1.4.7",
    "cors": "^2",
    "drizzle-orm": "catalog:",
    "express": "^5",
    "pino": "^9",
    "pino-http": "^10"
  },
  "devDependencies": {
    "@types/cookie-parser": "^1.4.10",
    "@types/cors": "^2.8.19",
    "@types/express": "^5.0.6",
    "@types/node": "catalog:",
    "esbuild": "^0.27.3",
    "esbuild-plugin-pino": "^2.3.3",
    "pino-pretty": "^13",
    "thread-stream": "3.1.0"
  }
}


// ============================================================
// FILE: artifacts/api-server/tsconfig.json
// ============================================================
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "dist",
    "rootDir": "src",
    "types": ["node"]
  },
  "include": ["src"],
  "references": [
    {
      "path": "../../lib/db"
    },
    {
      "path": "../../lib/api-zod"
    }
  ]
}


// ============================================================
// FILE: artifacts/sentinel-mesh/index.html
// ============================================================
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
    <title>SentinelMesh Security Platform</title>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>


// ============================================================
// FILE: artifacts/sentinel-mesh/vite.config.ts
// ============================================================
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import path from "path";
import runtimeErrorOverlay from "@replit/vite-plugin-runtime-error-modal";

const rawPort = process.env.PORT;

if (!rawPort) {
  throw new Error(
    "PORT environment variable is required but was not provided.",
  );
}

const port = Number(rawPort);

if (Number.isNaN(port) || port <= 0) {
  throw new Error(`Invalid PORT value: "${rawPort}"`);
}

const basePath = process.env.BASE_PATH;

if (!basePath) {
  throw new Error(
    "BASE_PATH environment variable is required but was not provided.",
  );
}

export default defineConfig({
  base: basePath,
  plugins: [
    react(),
    tailwindcss(),
    runtimeErrorOverlay(),
    ...(process.env.NODE_ENV !== "production" &&
    process.env.REPL_ID !== undefined
      ? [
          await import("@replit/vite-plugin-cartographer").then((m) =>
            m.cartographer({
              root: path.resolve(import.meta.dirname, ".."),
            }),
          ),
          await import("@replit/vite-plugin-dev-banner").then((m) =>
            m.devBanner(),
          ),
        ]
      : []),
  ],
  resolve: {
    alias: {
      "@": path.resolve(import.meta.dirname, "src"),
      "@assets": path.resolve(import.meta.dirname, "..", "..", "attached_assets"),
    },
    dedupe: ["react", "react-dom"],
  },
  root: path.resolve(import.meta.dirname),
  build: {
    outDir: path.resolve(import.meta.dirname, "dist/public"),
    emptyOutDir: true,
  },
  server: {
    port,
    host: "0.0.0.0",
    allowedHosts: true,
    fs: {
      strict: true,
      deny: ["**/.*"],
    },
  },
  preview: {
    port,
    host: "0.0.0.0",
    allowedHosts: true,
  },
});


// ============================================================
// FILE: artifacts/sentinel-mesh/tsconfig.json
// ============================================================
{
  "extends": "../../tsconfig.base.json",
  "include": ["src/**/*"],
  "exclude": ["node_modules", "build", "dist", "**/*.test.ts"],
  "compilerOptions": {
    "noEmit": true,
    "jsx": "preserve",
    "lib": ["esnext", "dom", "dom.iterable"],
    "resolveJsonModule": true,
    "allowImportingTsExtensions": true,
    "moduleResolution": "bundler",
    "types": ["node", "vite/client"],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "references": [
    {
      "path": "../../lib/api-client-react"
    }
  ]
}


// ============================================================
// FILE: artifacts/sentinel-mesh/package.json
// ============================================================
{
  "name": "@workspace/sentinel-mesh",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite --config vite.config.ts --host 0.0.0.0",
    "build": "vite build --config vite.config.ts",
    "serve": "vite preview --config vite.config.ts --host 0.0.0.0",
    "typecheck": "tsc -p tsconfig.json --noEmit"
  },
  "devDependencies": {
    "@hookform/resolvers": "^3.10.0",
    "@radix-ui/react-accordion": "^1.2.4",
    "@radix-ui/react-alert-dialog": "^1.1.7",
    "@radix-ui/react-aspect-ratio": "^1.1.3",
    "@radix-ui/react-avatar": "^1.1.4",
    "@radix-ui/react-checkbox": "^1.1.5",
    "@radix-ui/react-collapsible": "^1.1.4",
    "@radix-ui/react-context-menu": "^2.2.7",
    "@radix-ui/react-dialog": "^1.1.7",
    "@radix-ui/react-dropdown-menu": "^2.1.7",
    "@radix-ui/react-hover-card": "^1.1.7",
    "@radix-ui/react-label": "^2.1.3",
    "@radix-ui/react-menubar": "^1.1.7",
    "@radix-ui/react-navigation-menu": "^1.2.6",
    "@radix-ui/react-popover": "^1.1.7",
    "@radix-ui/react-progress": "^1.1.3",
    "@radix-ui/react-radio-group": "^1.2.4",
    "@radix-ui/react-scroll-area": "^1.2.4",
    "@radix-ui/react-select": "^2.1.7",
    "@radix-ui/react-separator": "^1.1.3",
    "@radix-ui/react-slider": "^1.2.4",
    "@radix-ui/react-slot": "^1.2.0",
    "@radix-ui/react-switch": "^1.1.4",
    "@radix-ui/react-tabs": "^1.1.4",
    "@radix-ui/react-toast": "^1.2.7",
    "@radix-ui/react-toggle": "^1.1.3",
    "@radix-ui/react-toggle-group": "^1.1.3",
    "@radix-ui/react-tooltip": "^1.2.0",
    "@replit/vite-plugin-cartographer": "catalog:",
    "@replit/vite-plugin-dev-banner": "catalog:",
    "@replit/vite-plugin-runtime-error-modal": "catalog:",
    "@tailwindcss/typography": "^0.5.15",
    "@tailwindcss/vite": "catalog:",
    "@tanstack/react-query": "catalog:",
    "@types/node": "catalog:",
    "@types/react": "catalog:",
    "@types/react-dom": "catalog:",
    "@vitejs/plugin-react": "catalog:",
    "@workspace/api-client-react": "workspace:*",
    "class-variance-authority": "catalog:",
    "clsx": "catalog:",
    "cmdk": "^1.1.1",
    "date-fns": "^3.6.0",
    "embla-carousel-react": "^8.6.0",
    "framer-motion": "catalog:",
    "input-otp": "^1.4.2",
    "lucide-react": "catalog:",
    "next-themes": "^0.4.6",
    "react": "catalog:",
    "react-day-picker": "^9.11.1",
    "react-dom": "catalog:",
    "react-hook-form": "^7.55.0",
    "react-icons": "^5.4.0",
    "react-resizable-panels": "^2.1.7",
    "recharts": "^2.15.2",
    "sonner": "^2.0.7",
    "tailwind-merge": "catalog:",
    "tailwindcss": "catalog:",
    "tw-animate-css": "^1.4.0",
    "vaul": "^1.1.2",
    "vite": "catalog:",
    "wouter": "^3.3.5",
    "zod": "catalog:"
  }
}


// ============================================================
// FILE: artifacts/sentinel-mesh/components.json
// ============================================================
{
    "$schema": "https://ui.shadcn.com/schema.json",
    "style": "new-york",
    "rsc": false,
    "tsx": true,
    "tailwind": {
      "config": "",
      "css": "src/index.css",
      "baseColor": "neutral",
      "cssVariables": true,
      "prefix": ""
    },
    "aliases": {
      "components": "@/components",
      "utils": "@/lib/utils",
      "ui": "@/components/ui",
      "lib": "@/lib",
      "hooks": "@/hooks"
    }
}

// ============================================================
// FILE: artifacts/sentinel-mesh/src/main.tsx
// ============================================================
import { createRoot } from "react-dom/client";
import App from "./App";
import "./index.css";

createRoot(document.getElementById("root")!).render(<App />);


// ============================================================
// FILE: artifacts/sentinel-mesh/src/App.tsx
// ============================================================
import { Switch, Route, Router as WouterRouter } from "wouter";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Toaster } from "@/components/ui/toaster";
import { TooltipProvider } from "@/components/ui/tooltip";
import NotFound from "@/pages/not-found";
import { AppShell } from "@/components/layout/app-shell";
import LandingPage from "@/pages/landing";

// Import pages
import Dashboard from "@/pages/dashboard";
import Threats from "@/pages/threats";
import Sessions from "@/pages/sessions";
import Honeypot from "@/pages/honeypot";
import Attackers from "@/pages/attackers";
import Canary from "@/pages/canary";
import Learning from "@/pages/learning";
import Onboarding from "@/pages/onboarding";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      staleTime: 1000 * 60 * 5, // 5 minutes
    },
  },
});

function Router() {
  return (
    <AppShell>
      <Switch>
        <Route path="/" component={LandingPage} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/threats" component={Threats} />
        <Route path="/sessions" component={Sessions} />
        <Route path="/honeypot" component={Honeypot} />
        <Route path="/attackers" component={Attackers} />
        <Route path="/canary" component={Canary} />
        <Route path="/learning" component={Learning} />
        <Route path="/setup" component={Onboarding} />
        <Route component={NotFound} />
      </Switch>
    </AppShell>
  );
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <TooltipProvider>
        <WouterRouter base={import.meta.env.BASE_URL.replace(/\/$/, "")}>
          <Router />
        </WouterRouter>
        <Toaster />
      </TooltipProvider>
    </QueryClientProvider>
  );
}

export default App;


// ============================================================
// FILE: artifacts/sentinel-mesh/src/index.css
// ============================================================
@import "tailwindcss";
@import "tw-animate-css";
@plugin "@tailwindcss/typography";

@custom-variant dark (&:is(.dark *));

@theme inline {
  --color-background: hsl(var(--background));
  --color-foreground: hsl(var(--foreground));
  --color-border: hsl(var(--border));
  --color-input: hsl(var(--input));
  --color-ring: hsl(var(--ring));

  --color-card: hsl(var(--card));
  --color-card-foreground: hsl(var(--card-foreground));
  --color-card-border: hsl(var(--card-border));

  --color-popover: hsl(var(--popover));
  --color-popover-foreground: hsl(var(--popover-foreground));
  --color-popover-border: hsl(var(--popover-border));

  --color-primary: hsl(var(--primary));
  --color-primary-foreground: hsl(var(--primary-foreground));

  --color-secondary: hsl(var(--secondary));
  --color-secondary-foreground: hsl(var(--secondary-foreground));

  --color-muted: hsl(var(--muted));
  --color-muted-foreground: hsl(var(--muted-foreground));

  --color-accent: hsl(var(--accent));
  --color-accent-foreground: hsl(var(--accent-foreground));

  --color-destructive: hsl(var(--destructive));
  --color-destructive-foreground: hsl(var(--destructive-foreground));

  --color-chart-1: hsl(var(--chart-1));
  --color-chart-2: hsl(var(--chart-2));
  --color-chart-3: hsl(var(--chart-3));
  --color-chart-4: hsl(var(--chart-4));
  --color-chart-5: hsl(var(--chart-5));

  --color-sidebar: hsl(var(--sidebar));
  --color-sidebar-foreground: hsl(var(--sidebar-foreground));
  --color-sidebar-border: hsl(var(--sidebar-border));
  --color-sidebar-primary: hsl(var(--sidebar-primary));
  --color-sidebar-primary-foreground: hsl(var(--sidebar-primary-foreground));
  --color-sidebar-accent: hsl(var(--sidebar-accent));
  --color-sidebar-accent-foreground: hsl(var(--sidebar-accent-foreground));
  --color-sidebar-ring: hsl(var(--sidebar-ring));

  --font-sans: var(--app-font-sans);
  --font-serif: var(--app-font-serif);
  --font-mono: var(--app-font-mono);

  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
}

:root {
  --background: 220 20% 4%;
  --foreground: 210 40% 98%;

  --card: 220 20% 6%;
  --card-foreground: 210 40% 98%;
  --card-border: 220 20% 12%;

  --popover: 220 20% 6%;
  --popover-foreground: 210 40% 98%;
  --popover-border: 220 20% 12%;

  --primary: 180 100% 45%;
  --primary-foreground: 220 20% 4%;

  --secondary: 220 20% 12%;
  --secondary-foreground: 210 40% 98%;

  --muted: 220 20% 12%;
  --muted-foreground: 215 20% 65%;

  --accent: 180 100% 45%;
  --accent-foreground: 220 20% 4%;

  --destructive: 0 84% 60%;
  --destructive-foreground: 210 40% 98%;

  --border: 220 20% 12%;
  --input: 220 20% 12%;
  --ring: 180 100% 45%;

  --chart-1: 180 100% 45%;
  --chart-2: 220 80% 50%;
  --chart-3: 280 80% 50%;
  --chart-4: 340 80% 50%;
  --chart-5: 40 80% 50%;

  --sidebar: 220 20% 4%;
  --sidebar-foreground: 210 40% 98%;
  --sidebar-border: 220 20% 12%;
  --sidebar-primary: 180 100% 45%;
  --sidebar-primary-foreground: 220 20% 4%;
  --sidebar-accent: 220 20% 12%;
  --sidebar-accent-foreground: 210 40% 98%;
  --sidebar-ring: 180 100% 45%;

  --app-font-sans: 'Inter', sans-serif;
  --app-font-mono: 'Fira Code', monospace;
  --radius: 0.25rem;
}

@layer base {
  * {
    @apply border-border;
  }

  body {
    @apply font-sans antialiased bg-background text-foreground;
  }
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/lib/utils.ts
// ============================================================
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/hooks/use-toast.ts
// ============================================================
import * as React from "react"

import type {
  ToastActionElement,
  ToastProps,
} from "@/components/ui/toast"

const TOAST_LIMIT = 1
const TOAST_REMOVE_DELAY = 1000000

type ToasterToast = ToastProps & {
  id: string
  title?: React.ReactNode
  description?: React.ReactNode
  action?: ToastActionElement
}

const actionTypes = {
  ADD_TOAST: "ADD_TOAST",
  UPDATE_TOAST: "UPDATE_TOAST",
  DISMISS_TOAST: "DISMISS_TOAST",
  REMOVE_TOAST: "REMOVE_TOAST",
} as const

let count = 0

function genId() {
  count = (count + 1) % Number.MAX_SAFE_INTEGER
  return count.toString()
}

type ActionType = typeof actionTypes

type Action =
  | {
      type: ActionType["ADD_TOAST"]
      toast: ToasterToast
    }
  | {
      type: ActionType["UPDATE_TOAST"]
      toast: Partial<ToasterToast>
    }
  | {
      type: ActionType["DISMISS_TOAST"]
      toastId?: ToasterToast["id"]
    }
  | {
      type: ActionType["REMOVE_TOAST"]
      toastId?: ToasterToast["id"]
    }

interface State {
  toasts: ToasterToast[]
}

const toastTimeouts = new Map<string, ReturnType<typeof setTimeout>>()

const addToRemoveQueue = (toastId: string) => {
  if (toastTimeouts.has(toastId)) {
    return
  }

  const timeout = setTimeout(() => {
    toastTimeouts.delete(toastId)
    dispatch({
      type: "REMOVE_TOAST",
      toastId: toastId,
    })
  }, TOAST_REMOVE_DELAY)

  toastTimeouts.set(toastId, timeout)
}

export const reducer = (state: State, action: Action): State => {
  switch (action.type) {
    case "ADD_TOAST":
      return {
        ...state,
        toasts: [action.toast, ...state.toasts].slice(0, TOAST_LIMIT),
      }

    case "UPDATE_TOAST":
      return {
        ...state,
        toasts: state.toasts.map((t) =>
          t.id === action.toast.id ? { ...t, ...action.toast } : t
        ),
      }

    case "DISMISS_TOAST": {
      const { toastId } = action

      // ! Side effects ! - This could be extracted into a dismissToast() action,
      // but I'll keep it here for simplicity
      if (toastId) {
        addToRemoveQueue(toastId)
      } else {
        state.toasts.forEach((toast) => {
          addToRemoveQueue(toast.id)
        })
      }

      return {
        ...state,
        toasts: state.toasts.map((t) =>
          t.id === toastId || toastId === undefined
            ? {
                ...t,
                open: false,
              }
            : t
        ),
      }
    }
    case "REMOVE_TOAST":
      if (action.toastId === undefined) {
        return {
          ...state,
          toasts: [],
        }
      }
      return {
        ...state,
        toasts: state.toasts.filter((t) => t.id !== action.toastId),
      }
  }
}

const listeners: Array<(state: State) => void> = []

let memoryState: State = { toasts: [] }

function dispatch(action: Action) {
  memoryState = reducer(memoryState, action)
  listeners.forEach((listener) => {
    listener(memoryState)
  })
}

type Toast = Omit<ToasterToast, "id">

function toast({ ...props }: Toast) {
  const id = genId()

  const update = (props: ToasterToast) =>
    dispatch({
      type: "UPDATE_TOAST",
      toast: { ...props, id },
    })
  const dismiss = () => dispatch({ type: "DISMISS_TOAST", toastId: id })

  dispatch({
    type: "ADD_TOAST",
    toast: {
      ...props,
      id,
      open: true,
      onOpenChange: (open) => {
        if (!open) dismiss()
      },
    },
  })

  return {
    id: id,
    dismiss,
    update,
  }
}

function useToast() {
  const [state, setState] = React.useState<State>(memoryState)

  React.useEffect(() => {
    listeners.push(setState)
    return () => {
      const index = listeners.indexOf(setState)
      if (index > -1) {
        listeners.splice(index, 1)
      }
    }
  }, [state])

  return {
    ...state,
    toast,
    dismiss: (toastId?: string) => dispatch({ type: "DISMISS_TOAST", toastId }),
  }
}

export { useToast, toast }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/hooks/use-mobile.tsx
// ============================================================
import * as React from "react"

const MOBILE_BREAKPOINT = 768

export function useIsMobile() {
  const [isMobile, setIsMobile] = React.useState<boolean | undefined>(undefined)

  React.useEffect(() => {
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`)
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    }
    mql.addEventListener("change", onChange)
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    return () => mql.removeEventListener("change", onChange)
  }, [])

  return !!isMobile
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/layout/app-shell.tsx
// ============================================================
import { Link, useLocation } from "wouter";
import { Shield, Activity, AlertTriangle, Users, Target, Network, BrainCircuit, Menu } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";

const NAV_ITEMS = [
  { href: "/dashboard", label: "SOC Dashboard", icon: Activity },
  { href: "/threats", label: "Threats", icon: AlertTriangle },
  { href: "/sessions", label: "Sessions", icon: Network },
  { href: "/honeypot", label: "Honeypot", icon: Shield },
  { href: "/attackers", label: "Attack Profiles", icon: Users },
  { href: "/canary", label: "Canary Tokens", icon: Target },
  { href: "/learning", label: "AI Learning", icon: BrainCircuit },
];

export function Sidebar() {
  const [location] = useLocation();

  const NavContent = () => (
    <div className="flex flex-col h-full bg-sidebar border-r border-sidebar-border">
      <div className="p-4 border-b border-sidebar-border">
        <Link href="/dashboard" className="flex items-center gap-2 font-bold text-lg text-sidebar-foreground">
          <div className="w-8 h-8 rounded bg-primary/20 flex items-center justify-center border border-primary/50 text-primary">
            <Shield className="w-5 h-5" />
          </div>
          SentinelMesh
        </Link>
      </div>
      <nav className="flex-1 py-4 flex flex-col gap-1 px-2">
        {NAV_ITEMS.map((item) => {
          const isActive = location === item.href || location.startsWith(item.href + "/");
          return (
            <Link key={item.href} href={item.href}>
              <div
                className={`flex items-center gap-3 px-3 py-2 rounded-md transition-colors text-sm font-medium ${
                  isActive
                    ? "bg-sidebar-accent text-sidebar-accent-foreground"
                    : "text-sidebar-foreground/70 hover:bg-sidebar-accent/50 hover:text-sidebar-foreground"
                }`}
              >
                <item.icon className={`w-4 h-4 ${isActive ? "text-primary" : ""}`} />
                {item.label}
              </div>
            </Link>
          );
        })}
      </nav>
    </div>
  );

  return (
    <>
      {/* Desktop Sidebar */}
      <div className="hidden md:flex w-64 flex-col fixed inset-y-0 left-0 z-50">
        <NavContent />
      </div>
      
      {/* Mobile Sidebar */}
      <div className="md:hidden flex items-center justify-between p-4 border-b border-border bg-background sticky top-0 z-40">
        <Link href="/dashboard" className="flex items-center gap-2 font-bold text-lg">
          <Shield className="w-5 h-5 text-primary" />
          SentinelMesh
        </Link>
        <Sheet>
          <SheetTrigger asChild>
            <Button variant="ghost" size="icon">
              <Menu className="w-5 h-5" />
            </Button>
          </SheetTrigger>
          <SheetContent side="left" className="p-0 w-64 border-r-border bg-sidebar">
            <NavContent />
          </SheetContent>
        </Sheet>
      </div>
    </>
  );
}

export function AppShell({ children }: { children: React.ReactNode }) {
  const [location] = useLocation();
  const isPublic = location === "/" || location === "/setup";

  if (isPublic) {
    return <div className="min-h-screen bg-background">{children}</div>;
  }

  return (
    <div className="min-h-screen bg-background">
      <Sidebar />
      <main className="md:pl-64 flex-1">
        <div className="p-6 md:p-8 max-w-7xl mx-auto">{children}</div>
      </main>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/layout/public-navbar.tsx
// ============================================================
import { Link } from "wouter";
import { Shield } from "lucide-react";
import { Button } from "@/components/ui/button";

export function PublicNavbar() {
  return (
    <header className="fixed top-0 inset-x-0 z-50 bg-background/80 backdrop-blur-md border-b border-border">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2 font-bold text-xl tracking-tight">
          <div className="w-8 h-8 rounded bg-primary/20 flex items-center justify-center border border-primary/50 text-primary">
            <Shield className="w-5 h-5" />
          </div>
          SentinelMesh
        </Link>
        <nav className="hidden md:flex items-center gap-6 text-sm font-medium text-muted-foreground">
          <a href="#how-it-works" className="hover:text-foreground transition-colors">How it Works</a>
          <a href="#features" className="hover:text-foreground transition-colors">Features</a>
          <a href="#pricing" className="hover:text-foreground transition-colors">Pricing</a>
          <Link href="/setup" className="hover:text-foreground transition-colors">Setup Guide</Link>
        </nav>
        <div className="flex items-center gap-4">
          <Link href="/dashboard">
            <Button variant="ghost" className="hidden sm:inline-flex">Sign In</Button>
          </Link>
          <Link href="/setup">
            <Button className="bg-primary text-primary-foreground hover:bg-primary/90">Get Started</Button>
          </Link>
        </div>
      </div>
    </header>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/landing.tsx
// ============================================================
import { PublicNavbar } from "@/components/layout/public-navbar";
import { Button } from "@/components/ui/button";
import { Link } from "wouter";
import { Shield, Network, Brain, Activity, ShieldAlert, Code2, Server, Target } from "lucide-react";
import { useListPricingPlans } from "@workspace/api-client-react";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";

export default function LandingPage() {
  const { data: pricingPlans, isLoading: pricingLoading } = useListPricingPlans();

  return (
    <div className="min-h-[100dvh] flex flex-col bg-background text-foreground overflow-hidden">
      <PublicNavbar />
      
      {/* Hero Section */}
      <section className="relative pt-32 pb-20 md:pt-48 md:pb-32 px-4">
        <div className="absolute inset-0 z-0">
          <img src="/hero-bg.png" alt="Cyber security network background" className="w-full h-full object-cover opacity-30" />
          <div className="absolute inset-0 bg-gradient-to-b from-background/80 via-background/90 to-background"></div>
        </div>
        
        <div className="container mx-auto relative z-10 text-center">
          <Badge variant="outline" className="mb-6 px-4 py-1 text-primary border-primary/30 bg-primary/10">
            Next-Gen API Protection
          </Badge>
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-6 max-w-4xl mx-auto">
            Trap Attackers in a <span className="text-primary">Convincing Illusion</span>
          </h1>
          <p className="text-lg md:text-xl text-muted-foreground max-w-2xl mx-auto mb-10">
            SentinelMesh silently routes malicious API requests into a high-fidelity fake server mid-session. We gather intelligence while they think they've breached your system.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link href="/setup">
              <Button size="lg" className="w-full sm:w-auto text-lg h-14 px-8 shadow-lg shadow-primary/20">
                Get Started — 15 min setup
              </Button>
            </Link>
            <Button size="lg" variant="outline" className="w-full sm:w-auto text-lg h-14 px-8">
              View Interactive Demo
            </Button>
          </div>
        </div>
      </section>

      {/* Architecture Section */}
      <section id="how-it-works" className="py-24 bg-card border-y border-border relative overflow-hidden">
        <div className="container mx-auto px-4 relative z-10">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">The Invisible Switch</h2>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Our AI gateway scores requests in real-time. When intent becomes malicious, we split the connection seamlessly.
            </p>
          </div>

          <div className="max-w-5xl mx-auto">
            <div className="grid grid-cols-1 md:grid-cols-5 gap-4 items-center">
              
              {/* Client */}
              <div className="flex flex-col items-center p-6 bg-background rounded-lg border border-border shadow-sm">
                <Code2 className="w-10 h-10 text-muted-foreground mb-3" />
                <span className="font-semibold">API Client</span>
              </div>

              <div className="hidden md:flex justify-center text-muted-foreground">
                →
              </div>

              {/* Gateway */}
              <div className="flex flex-col items-center p-6 bg-primary/10 rounded-lg border border-primary/30 shadow-[0_0_30px_rgba(0,255,255,0.1)]">
                <Brain className="w-10 h-10 text-primary mb-3" />
                <span className="font-semibold">Behavioral AI Score</span>
                <span className="text-xs text-muted-foreground mt-1">Cross-Key Correlation</span>
              </div>

              <div className="hidden md:flex flex-col justify-center text-muted-foreground gap-12">
                <div className="text-green-500">→</div>
                <div className="text-destructive">→</div>
              </div>

              {/* Destinations */}
              <div className="flex flex-col gap-4">
                <div className="flex flex-col items-center p-6 bg-background rounded-lg border border-border">
                  <Server className="w-8 h-8 text-green-500 mb-2" />
                  <span className="font-semibold">Real Server</span>
                  <span className="text-xs text-muted-foreground">Normal traffic</span>
                </div>
                <div className="flex flex-col items-center p-6 bg-destructive/10 rounded-lg border border-destructive/30">
                  <ShieldAlert className="w-8 h-8 text-destructive mb-2" />
                  <span className="font-semibold">Fake Server (Honeypot)</span>
                  <span className="text-xs text-muted-foreground">Malicious traffic</span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-24 bg-background">
        <div className="container mx-auto px-4">
          <div className="grid md:grid-cols-3 gap-8">
            <div className="p-6 bg-card rounded-xl border border-border">
              <Network className="w-12 h-12 text-primary mb-6" />
              <h3 className="text-xl font-bold mb-3">Live Session Cloning</h3>
              <p className="text-muted-foreground">
                Attackers are moved mid-session to a honeypot without dropping the connection. They never know they were caught.
              </p>
            </div>
            <div className="p-6 bg-card rounded-xl border border-border">
              <Activity className="w-12 h-12 text-primary mb-6" />
              <h3 className="text-xl font-bold mb-3">Forensic Profiling</h3>
              <p className="text-muted-foreground">
                We monitor the tools they use, their lateral movement attempts, and the fake data they try to exfiltrate to build a complete profile.
              </p>
            </div>
            <div className="p-6 bg-card rounded-xl border border-border">
              <Target className="w-12 h-12 text-primary mb-6" />
              <h3 className="text-xl font-bold mb-3">Canary Tokens</h3>
              <p className="text-muted-foreground">
                Deploy fake API keys, URLs, and records within your real application. If they get touched, the attacker is instantly isolated.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section id="pricing" className="py-24 bg-card border-t border-border">
        <div className="container mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Enterprise Grade, Priced for Small Business</h2>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Deploy a world-class SOC without the overhead. Transparent pricing based on traffic volume.
            </p>
          </div>

          {pricingLoading ? (
            <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
              {[1, 2, 3].map((i) => (
                <Card key={i} className="bg-background">
                  <CardHeader><Skeleton className="h-8 w-1/2 mb-2" /><Skeleton className="h-10 w-1/3" /></CardHeader>
                  <CardContent><Skeleton className="h-48 w-full" /></CardContent>
                </Card>
              ))}
            </div>
          ) : (
            <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
              {pricingPlans?.map((plan) => (
                <Card key={plan.id} className={`bg-background relative ${plan.recommended ? 'border-primary shadow-lg shadow-primary/10' : ''}`}>
                  {plan.recommended && (
                    <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-primary text-primary-foreground text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">
                      RECOMMENDED
                    </div>
                  )}
                  <CardHeader>
                    <CardTitle className="text-2xl">{plan.name}</CardTitle>
                    <CardDescription>{plan.description}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="mb-6">
                      <span className="text-4xl font-bold">${plan.monthlyPrice}</span>
                      <span className="text-muted-foreground">/mo</span>
                    </div>
                    <ul className="space-y-3 mb-6">
                      <li className="flex items-center text-sm text-muted-foreground">
                        <span className="w-1.5 h-1.5 bg-primary rounded-full mr-2"></span>
                        {plan.requestsPerMonth.toLocaleString()} Requests / mo
                      </li>
                      <li className="flex items-center text-sm text-muted-foreground">
                        <span className="w-1.5 h-1.5 bg-primary rounded-full mr-2"></span>
                        {plan.honeypotSessions.toLocaleString()} Honeypot Sessions
                      </li>
                      <li className="flex items-center text-sm text-muted-foreground">
                        <span className="w-1.5 h-1.5 bg-primary rounded-full mr-2"></span>
                        {plan.supportLevel} Support
                      </li>
                      {plan.features.map((feature, i) => (
                        <li key={i} className="flex items-center text-sm">
                          <span className="w-1.5 h-1.5 bg-primary/50 rounded-full mr-2"></span>
                          {feature}
                        </li>
                      ))}
                    </ul>
                  </CardContent>
                  <CardFooter>
                    <Button className={`w-full ${plan.recommended ? 'bg-primary' : 'bg-secondary text-secondary-foreground hover:bg-secondary/80'}`}>
                      Select Plan
                    </Button>
                  </CardFooter>
                </Card>
              ))}
            </div>
          )}
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 bg-background border-t border-border">
        <div className="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="flex items-center gap-2 font-bold">
            <Shield className="w-5 h-5 text-primary" />
            SentinelMesh
          </div>
          <div className="text-sm text-muted-foreground">
            © 2025 SentinelMesh Security. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/onboarding.tsx
// ============================================================
import { useState } from "react";
import { Link } from "wouter";
import { PublicNavbar } from "@/components/layout/public-navbar";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Shield,
  Server,
  Key,
  Globe,
  CheckCircle2,
  Circle,
  ChevronRight,
  Terminal,
  Copy,
  Check,
  Database,
  Lock,
  Zap,
  ArrowRight,
  AlertTriangle,
  BookOpen,
  LifeBuoy,
} from "lucide-react";

function CodeBlock({ code, language = "bash" }: { code: string; language?: string }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="relative rounded-lg bg-black/60 border border-border overflow-hidden">
      <div className="flex items-center justify-between px-4 py-2 border-b border-border bg-black/40">
        <span className="text-xs text-muted-foreground font-mono">{language}</span>
        <button
          onClick={handleCopy}
          className="flex items-center gap-1.5 text-xs text-muted-foreground hover:text-foreground transition-colors"
        >
          {copied ? <Check className="w-3.5 h-3.5 text-primary" /> : <Copy className="w-3.5 h-3.5" />}
          {copied ? "Copied" : "Copy"}
        </button>
      </div>
      <pre className="p-4 text-sm font-mono text-foreground/90 overflow-x-auto leading-relaxed whitespace-pre-wrap">{code}</pre>
    </div>
  );
}

const STEPS = [
  {
    number: 1,
    title: "Create your account and get your Gateway Key",
    icon: Key,
    time: "2 minutes",
    description:
      "Sign up and you will receive a unique Gateway Key. This is the only credential SentinelMesh needs. Your own database credentials never leave your infrastructure.",
  },
  {
    number: 2,
    title: "Tell SentinelMesh where your real server lives",
    icon: Server,
    time: "1 minute",
    description:
      "In your dashboard settings, enter your API server's upstream origin — the internal URL your server is already running on. SentinelMesh acts as an invisible proxy in front of it.",
  },
  {
    number: 3,
    title: "Route your API traffic through SentinelMesh",
    icon: Globe,
    time: "5–10 minutes",
    description:
      "Update your DNS record or load balancer so that incoming API traffic hits SentinelMesh first. Your server URL, database, and application code stay exactly as they are.",
  },
  {
    number: 4,
    title: "Verify the connection",
    icon: CheckCircle2,
    time: "1 minute",
    description:
      "Run a quick health check to confirm traffic is flowing through the gateway. Normal requests will be proxied to your real server with no added latency.",
  },
  {
    number: 5,
    title: "Deploy your first canary token",
    icon: Shield,
    time: "2 minutes",
    description:
      "Place a canary token inside one of your API responses — a fake record ID, a decoy API key, or a synthetic URL. The moment an attacker accesses it, their session is silently cloned to the fake server.",
  },
];

export default function Onboarding() {
  const [activeStep, setActiveStep] = useState(1);

  return (
    <div className="min-h-screen bg-background text-foreground">
      <PublicNavbar />

      <div className="pt-24 pb-20 px-4">
        <div className="max-w-4xl mx-auto">

          {/* Header */}
          <div className="text-center mb-14">
            <Badge variant="outline" className="border-primary/40 text-primary mb-4 text-xs tracking-widest uppercase">
              Integration Guide
            </Badge>
            <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight mb-4">
              Up and running in{" "}
              <span className="text-primary">under 15 minutes</span>
            </h1>
            <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
              SentinelMesh sits in front of your existing API. Your database, your server, and your application
              code do not change at all. No SDK to install. No schema migration. No downtime.
            </p>
          </div>

          {/* Key reassurance bar */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-14">
            {[
              { icon: Database, label: "Your database is never accessed", sub: "SentinelMesh never queries your DB" },
              { icon: Lock, label: "Zero credential sharing", sub: "Only your upstream URL is configured" },
              { icon: Zap, label: "No code changes required", sub: "Transparent proxy — your app is unaware" },
            ].map(({ icon: Icon, label, sub }) => (
              <div key={label} className="flex items-start gap-3 p-4 rounded-xl border border-border bg-card">
                <div className="w-8 h-8 rounded-md bg-primary/10 flex items-center justify-center shrink-0 mt-0.5">
                  <Icon className="w-4 h-4 text-primary" />
                </div>
                <div>
                  <p className="text-sm font-semibold">{label}</p>
                  <p className="text-xs text-muted-foreground mt-0.5">{sub}</p>
                </div>
              </div>
            ))}
          </div>

          {/* How the proxy works — visual diagram */}
          <div className="mb-14 p-6 rounded-xl border border-border bg-card">
            <h2 className="text-base font-semibold mb-1">How the proxy works</h2>
            <p className="text-sm text-muted-foreground mb-6">
              Traffic flows through SentinelMesh. Legitimate requests are passed straight through to your real server.
              Detected attackers are silently diverted to the fake server — your real server never sees them again.
            </p>
            <div className="flex flex-wrap items-center justify-center gap-2 text-sm font-mono">
              {[
                { label: "Client", bg: "bg-muted", text: "text-foreground" },
                null,
                { label: "SentinelMesh Gateway", bg: "bg-primary/20 border border-primary/40", text: "text-primary" },
                null,
                { label: "Your Real Server", bg: "bg-muted", text: "text-foreground" },
              ].map((item, i) =>
                item === null ? (
                  <ChevronRight key={i} className="w-4 h-4 text-muted-foreground" />
                ) : (
                  <div key={i} className={`px-3 py-1.5 rounded-md ${item.bg} ${item.text} text-xs`}>
                    {item.label}
                  </div>
                )
              )}
            </div>
            <div className="flex items-center justify-center gap-2 text-sm font-mono mt-3">
              <div className="w-[180px]" />
              <ChevronRight className="w-4 h-4 text-muted-foreground" />
              <div className="px-3 py-1.5 rounded-md bg-orange-500/20 border border-orange-500/40 text-orange-400 text-xs">
                Attacker detected
              </div>
              <ChevronRight className="w-4 h-4 text-muted-foreground" />
              <div className="px-3 py-1.5 rounded-md bg-red-900/30 border border-red-700/40 text-red-400 text-xs">
                Fake Server (decoy)
              </div>
            </div>
            <p className="text-center text-xs text-muted-foreground mt-3">
              Your real server's URL and database are never exposed to attackers after detection.
            </p>
          </div>

          {/* Step-by-step */}
          <div className="mb-14">
            <h2 className="text-xl font-bold mb-6">Step-by-step setup</h2>

            <div className="flex flex-col gap-3">
              {STEPS.map((step) => {
                const isActive = activeStep === step.number;
                const isDone = activeStep > step.number;
                const Icon = step.icon;

                return (
                  <div
                    key={step.number}
                    className={`rounded-xl border transition-all duration-200 overflow-hidden ${
                      isActive
                        ? "border-primary/50 bg-card"
                        : isDone
                        ? "border-border bg-card/60"
                        : "border-border bg-card/30"
                    }`}
                  >
                    {/* Step header — always visible */}
                    <button
                      onClick={() => setActiveStep(step.number)}
                      className="w-full flex items-center gap-4 p-4 text-left"
                    >
                      <div
                        className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 text-sm font-bold border transition-colors ${
                          isDone
                            ? "bg-primary/20 border-primary/40 text-primary"
                            : isActive
                            ? "bg-primary/20 border-primary/60 text-primary"
                            : "bg-muted/50 border-border text-muted-foreground"
                        }`}
                      >
                        {isDone ? <Check className="w-4 h-4" /> : step.number}
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center gap-2 flex-wrap">
                          <span
                            className={`font-semibold text-sm ${
                              isActive ? "text-foreground" : "text-foreground/70"
                            }`}
                          >
                            {step.title}
                          </span>
                          <span className="text-xs text-muted-foreground">· {step.time}</span>
                        </div>
                      </div>
                      <div className={`shrink-0 transition-transform ${isActive ? "rotate-90" : ""}`}>
                        <ChevronRight className="w-4 h-4 text-muted-foreground" />
                      </div>
                    </button>

                    {/* Step body — visible when active */}
                    {isActive && (
                      <div className="px-4 pb-5 space-y-4">
                        <div className="flex items-start gap-3 pl-12">
                          <p className="text-sm text-muted-foreground leading-relaxed">{step.description}</p>
                        </div>

                        <div className="pl-12 space-y-3">
                          {step.number === 1 && (
                            <>
                              <p className="text-xs text-muted-foreground font-medium uppercase tracking-wider">
                                Your credentials after signup
                              </p>
                              <CodeBlock
                                language="env"
                                code={`SENTINELMESH_GATEWAY_KEY=gw_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nSENTINELMESH_TENANT_ID=tnt_xxxxxxxxxxxxxxxxxxxxxxxx`}
                              />
                              <div className="flex items-start gap-2 p-3 rounded-lg bg-primary/5 border border-primary/20">
                                <Lock className="w-4 h-4 text-primary shrink-0 mt-0.5" />
                                <p className="text-xs text-muted-foreground">
                                  Store these in your environment variables or secret manager. SentinelMesh never
                                  asks for your database password, connection string, or any server credentials.
                                </p>
                              </div>
                            </>
                          )}

                          {step.number === 2 && (
                            <>
                              <p className="text-xs text-muted-foreground font-medium uppercase tracking-wider">
                                Dashboard configuration
                              </p>
                              <CodeBlock
                                language="json (tenant config)"
                                code={`{
  "upstreamOrigin": "https://api.yourdomain.internal",
  "highRiskThreshold": 55,
  "honeypotOrigin": "auto"
}`}
                              />
                              <div className="flex items-start gap-2 p-3 rounded-lg bg-orange-500/5 border border-orange-500/20">
                                <AlertTriangle className="w-4 h-4 text-orange-400 shrink-0 mt-0.5" />
                                <p className="text-xs text-muted-foreground">
                                  <strong className="text-foreground">upstreamOrigin</strong> is your existing API
                                  server — the URL your load balancer or DNS currently points to. This is the only
                                  setting that references your infrastructure.
                                </p>
                              </div>
                            </>
                          )}

                          {step.number === 3 && (
                            <>
                              <p className="text-xs text-muted-foreground font-medium uppercase tracking-wider">
                                Option A — DNS CNAME (recommended for most clients)
                              </p>
                              <CodeBlock
                                language="dns"
                                code={`# Before
api.yourdomain.com  CNAME  your-server.internal

# After — one record change
api.yourdomain.com  CNAME  gateway.sentinelmesh.io`}
                              />
                              <p className="text-xs text-muted-foreground font-medium uppercase tracking-wider pt-2">
                                Option B — Nginx / reverse proxy (zero DNS changes)
                              </p>
                              <CodeBlock
                                language="nginx"
                                code={`# Add this upstream block in your existing nginx config
upstream sentinelmesh {
  server gateway.sentinelmesh.io:443;
}

location /api/ {
  proxy_pass https://sentinelmesh;
  proxy_set_header Host gateway.sentinelmesh.io;
  proxy_set_header X-Gateway-Key gw_live_xxxxxxxxxxxx;
  proxy_set_header X-Forwarded-For $remote_addr;
}`}
                              />
                              <p className="text-xs text-muted-foreground font-medium uppercase tracking-wider pt-2">
                                Option C — AWS / GCP / Azure load balancer
                              </p>
                              <div className="p-3 rounded-lg bg-card border border-border text-xs text-muted-foreground space-y-1">
                                <p>1. Add <code className="text-primary">gateway.sentinelmesh.io</code> as a target in your load balancer pool</p>
                                <p>2. Set the forwarding rule to pass <code className="text-primary">X-Gateway-Key</code> as a header</p>
                                <p>3. Weight 100% of traffic to the SentinelMesh target</p>
                                <p>4. Your existing backend remains registered — SentinelMesh will forward clean traffic to it</p>
                              </div>
                            </>
                          )}

                          {step.number === 4 && (
                            <>
                              <p className="text-xs text-muted-foreground font-medium uppercase tracking-wider">
                                Verify traffic is flowing
                              </p>
                              <CodeBlock
                                language="bash"
                                code={`# Should return your real server's normal response
curl -H "X-Gateway-Key: gw_live_xxxxxxxxxxxx" \\
  https://api.yourdomain.com/healthz

# Check the SentinelMesh gateway status directly
curl https://gateway.sentinelmesh.io/status \\
  -H "X-Tenant-ID: tnt_xxxxxx" \\
  -H "Authorization: Bearer gw_live_xxxxxxxxxxxx"`}
                              />
                              <CodeBlock
                                language="expected response"
                                code={`{
  "status": "active",
  "upstream": "reachable",
  "requestsProxied": 1,
  "threatScore": 5,
  "route": "upstream"
}`}
                              />
                              <div className="flex items-start gap-2 p-3 rounded-lg bg-primary/5 border border-primary/20">
                                <CheckCircle2 className="w-4 h-4 text-primary shrink-0 mt-0.5" />
                                <p className="text-xs text-muted-foreground">
                                  A <code className="text-primary">route: "upstream"</code> response means your
                                  request was scored low-risk and passed directly to your real server. You will start
                                  seeing requests in the SOC Dashboard immediately.
                                </p>
                              </div>
                            </>
                          )}

                          {step.number === 5 && (
                            <>
                              <p className="text-xs text-muted-foreground font-medium uppercase tracking-wider">
                                Example — embed a canary in an API response
                              </p>
                              <CodeBlock
                                language="json (your API response — before)"
                                code={`{
  "id": "user_123",
  "name": "Acme Corp",
  "plan": "enterprise"
}`}
                              />
                              <CodeBlock
                                language="json (your API response — after, with canary)"
                                code={`{
  "id": "user_123",
  "name": "Acme Corp",
  "plan": "enterprise",
  "_ref": "cny_8f2a1c9d4b"   // <-- canary token ID from your dashboard
}`}
                              />
                              <p className="text-xs text-muted-foreground font-medium uppercase tracking-wider pt-2">
                                Or register a URL-based canary
                              </p>
                              <CodeBlock
                                language="json (your API response)"
                                code={`{
  "exportUrl": "https://api.yourdomain.com/exports/cny_8f2a1?token=trap"
}`}
                              />
                              <div className="flex items-start gap-2 p-3 rounded-lg bg-orange-500/5 border border-orange-500/20">
                                <Zap className="w-4 h-4 text-orange-400 shrink-0 mt-0.5" />
                                <p className="text-xs text-muted-foreground">
                                  The moment any client accesses a canary token URL or ID, SentinelMesh clones that
                                  session to the fake server in under 100ms — silently, mid-request. The attacker
                                  sees no interruption. You get an instant alert.
                                </p>
                              </div>
                            </>
                          )}
                        </div>

                        {/* Navigation buttons */}
                        <div className="pl-12 flex items-center gap-3 pt-2">
                          {step.number > 1 && (
                            <Button
                              variant="ghost"
                              size="sm"
                              onClick={() => setActiveStep(step.number - 1)}
                              className="text-xs"
                            >
                              Back
                            </Button>
                          )}
                          {step.number < STEPS.length ? (
                            <Button
                              size="sm"
                              onClick={() => setActiveStep(step.number + 1)}
                              className="text-xs bg-primary text-primary-foreground hover:bg-primary/90 gap-1.5"
                            >
                              Next: {STEPS[step.number].title.split(" ").slice(0, 4).join(" ")}…
                              <ArrowRight className="w-3.5 h-3.5" />
                            </Button>
                          ) : (
                            <Link href="/dashboard">
                              <Button
                                size="sm"
                                className="text-xs bg-primary text-primary-foreground hover:bg-primary/90 gap-1.5"
                              >
                                Open your dashboard
                                <ArrowRight className="w-3.5 h-3.5" />
                              </Button>
                            </Link>
                          )}
                        </div>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>

          {/* FAQ */}
          <div className="mb-14">
            <h2 className="text-xl font-bold mb-6">Common questions</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {[
                {
                  q: "Does SentinelMesh ever read from my database?",
                  a: "Never. SentinelMesh only sees the HTTP requests and responses flowing through the gateway. Your database connection string is never configured in SentinelMesh.",
                },
                {
                  q: "What happens to normal user requests?",
                  a: "Normal requests (scoring below your risk threshold) are proxied to your real server with a typical added latency of under 2ms. Your users will not notice SentinelMesh is there.",
                },
                {
                  q: "Where does the fake data come from?",
                  a: "SentinelMesh's fake data AI generates it synthetically — realistic names, invoice numbers, credentials, and records that look convincing but have no relation to your real data.",
                },
                {
                  q: "Can I set my own risk threshold?",
                  a: "Yes. The default threshold is 55 (out of 100). You can lower it for highly sensitive APIs (faster honeypotting) or raise it to reduce false positives. Per-path overrides are also supported.",
                },
                {
                  q: "What if the gateway goes down?",
                  a: "SentinelMesh runs on redundant infrastructure. In the event of a gateway outage, you can instantly revert your DNS/proxy config to point directly at your real server — no code to roll back.",
                },
                {
                  q: "Do I need to change my API clients or mobile apps?",
                  a: "No. The gateway operates transparently at the network layer. Your clients, mobile apps, and third-party integrations do not need any changes.",
                },
              ].map(({ q, a }) => (
                <div key={q} className="p-4 rounded-xl border border-border bg-card">
                  <p className="text-sm font-semibold mb-1.5">{q}</p>
                  <p className="text-sm text-muted-foreground leading-relaxed">{a}</p>
                </div>
              ))}
            </div>
          </div>

          {/* Footer CTA */}
          <div className="rounded-2xl border border-primary/30 bg-primary/5 p-8 text-center">
            <Shield className="w-10 h-10 text-primary mx-auto mb-4" />
            <h2 className="text-2xl font-bold mb-2">Ready to protect your API?</h2>
            <p className="text-muted-foreground text-sm mb-6 max-w-md mx-auto">
              Your database stays yours. Your code stays unchanged. SentinelMesh handles the rest.
            </p>
            <div className="flex flex-wrap items-center justify-center gap-3">
              <Link href="/dashboard">
                <Button className="bg-primary text-primary-foreground hover:bg-primary/90 gap-2">
                  Open Dashboard <ArrowRight className="w-4 h-4" />
                </Button>
              </Link>
              <a href="#pricing">
                <Button variant="outline" className="gap-2">
                  <BookOpen className="w-4 h-4" /> View Pricing
                </Button>
              </a>
              <a href="mailto:support@sentinelmesh.io">
                <Button variant="ghost" className="gap-2 text-muted-foreground">
                  <LifeBuoy className="w-4 h-4" /> Talk to an engineer
                </Button>
              </a>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/dashboard.tsx
// ============================================================
import { useGetDashboardSummary, useGetLiveFeed, useGetScoreTimeline } from "@workspace/api-client-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Activity, ShieldAlert, Network, Target, Brain, AlertTriangle } from "lucide-react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, AreaChart, Area } from "recharts";
import { format } from "date-fns";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";

export default function Dashboard() {
  const { data: summary, isLoading: summaryLoading } = useGetDashboardSummary();
  const { data: feed, isLoading: feedLoading } = useGetLiveFeed({ limit: 10 });
  const { data: timeline, isLoading: timelineLoading } = useGetScoreTimeline({ hours: 24 });

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold tracking-tight">Security Operations Center</h1>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Threats Today</CardTitle>
            <ShieldAlert className="h-4 w-4 text-destructive" />
          </CardHeader>
          <CardContent>
            {summaryLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-destructive">{summary?.totalThreatsToday.toLocaleString()}</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Actively mitigated or diverted</p>
          </CardContent>
        </Card>
        
        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Honeypotted Sessions</CardTitle>
            <Network className="h-4 w-4 text-primary" />
          </CardHeader>
          <CardContent>
            {summaryLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-primary">{summary?.honeypottedSessions.toLocaleString()}</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Attackers trapped in fake environment</p>
          </CardContent>
        </Card>

        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Active Attackers</CardTitle>
            <Target className="h-4 w-4 text-orange-500" />
          </CardHeader>
          <CardContent>
            {summaryLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-orange-500">{summary?.activeAttackers.toLocaleString()}</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Currently interacting with honeypot</p>
          </CardContent>
        </Card>

        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">AI Accuracy</CardTitle>
            <Brain className="h-4 w-4 text-green-500" />
          </CardHeader>
          <CardContent>
            {summaryLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-green-500">{(summary?.aiAccuracyRate ?? 0) * 100}%</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Behavioral classification confidence</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-6 md:grid-cols-7">
        <Card className="col-span-4 bg-card">
          <CardHeader>
            <CardTitle>Threat Score Timeline</CardTitle>
            <CardDescription>Average behavioral threat score over the last 24 hours</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="h-[300px] w-full">
              {timelineLoading ? <Skeleton className="h-full w-full" /> : (
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={timeline} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
                    <defs>
                      <linearGradient id="colorScore" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="hsl(var(--destructive))" stopOpacity={0.3}/>
                        <stop offset="95%" stopColor="hsl(var(--destructive))" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" vertical={false} />
                    <XAxis 
                      dataKey="timestamp" 
                      tickFormatter={(val) => format(new Date(val), "HH:mm")} 
                      stroke="hsl(var(--muted-foreground))"
                      fontSize={12}
                      tickLine={false}
                      axisLine={false}
                    />
                    <YAxis 
                      stroke="hsl(var(--muted-foreground))" 
                      fontSize={12}
                      tickLine={false}
                      axisLine={false}
                      domain={[0, 100]}
                    />
                    <Tooltip 
                      contentStyle={{ backgroundColor: 'hsl(var(--popover))', borderColor: 'hsl(var(--border))', color: 'hsl(var(--popover-foreground))' }}
                      labelFormatter={(val) => format(new Date(val), "MMM d, HH:mm")}
                    />
                    <Area 
                      type="monotone" 
                      dataKey="avgScore" 
                      stroke="hsl(var(--destructive))" 
                      fillOpacity={1} 
                      fill="url(#colorScore)" 
                      strokeWidth={2}
                    />
                  </AreaChart>
                </ResponsiveContainer>
              )}
            </div>
          </CardContent>
        </Card>

        <Card className="col-span-3 bg-card flex flex-col">
          <CardHeader>
            <CardTitle>Live Threat Feed</CardTitle>
            <CardDescription>Real-time security events</CardDescription>
          </CardHeader>
          <CardContent className="flex-1 overflow-auto pr-2">
            <div className="space-y-4">
              {feedLoading ? (
                Array(5).fill(0).map((_, i) => (
                  <div key={i} className="flex items-start gap-4">
                    <Skeleton className="h-8 w-8 rounded-full" />
                    <div className="space-y-2 flex-1">
                      <Skeleton className="h-4 w-full" />
                      <Skeleton className="h-3 w-2/3" />
                    </div>
                  </div>
                ))
              ) : (
                feed?.map((event) => (
                  <div key={event.id} className="flex items-start gap-4 group">
                    <div className={`mt-1 p-1.5 rounded-full shrink-0 ${
                      event.severity === 'critical' ? 'bg-destructive/20 text-destructive' :
                      event.severity === 'high' ? 'bg-orange-500/20 text-orange-500' :
                      event.severity === 'medium' ? 'bg-yellow-500/20 text-yellow-500' :
                      'bg-primary/20 text-primary'
                    }`}>
                      {event.type === 'honeypot_trip' ? <Network className="h-4 w-4" /> :
                       event.type === 'threat_detected' ? <ShieldAlert className="h-4 w-4" /> :
                       event.type === 'canary_fired' ? <Target className="h-4 w-4" /> :
                       <Activity className="h-4 w-4" />}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between gap-2">
                        <p className="text-sm font-medium leading-none text-foreground truncate">
                          {event.message}
                        </p>
                        <span className="text-xs text-muted-foreground whitespace-nowrap">
                          {format(new Date(event.timestamp), "HH:mm:ss")}
                        </span>
                      </div>
                      <div className="flex items-center gap-2 mt-1.5">
                        <Badge variant="outline" className="text-[10px] h-4 px-1.5 font-normal">
                          {event.ipAddress}
                        </Badge>
                        <Badge variant="outline" className={`text-[10px] h-4 px-1.5 font-normal ${
                          event.route === 'fake_server' ? 'text-destructive border-destructive/30' : 'text-green-500 border-green-500/30'
                        }`}>
                          {event.route === 'fake_server' ? 'Honeypot' : 'Real'}
                        </Badge>
                        <span className="text-xs text-muted-foreground ml-auto">
                          Score: {event.score}
                        </span>
                      </div>
                    </div>
                  </div>
                ))
              )}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/threats.tsx
// ============================================================
import { useListThreats, useGetThreat, useDismissThreat } from "@workspace/api-client-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { format } from "date-fns";
import { ShieldAlert, ShieldCheck, Fingerprint, MapPin, Globe, History, MoreHorizontal } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { useState } from "selected-react-hooks"; // Will use React hooks below
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import React from "react";

export default function Threats() {
  const [selectedId, setSelectedId] = React.useState<string | null>(null);
  const { data: threatData, isLoading } = useListThreats();
  
  const { data: detailData, isLoading: detailLoading } = useGetThreat(selectedId || "", {
    query: { enabled: !!selectedId }
  });

  const dismissMutation = useDismissThreat();

  const handleDismiss = (id: string) => {
    dismissMutation.mutate({ threatId: id }, {
      onSuccess: () => {
        setSelectedId(null);
        // Normally we'd invalidate queries here, but generated hook signatures might differ
      }
    });
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Threat Intelligence</h1>
          <p className="text-muted-foreground">Monitor and investigate detected threats across your infrastructure.</p>
        </div>
      </div>

      <Card className="bg-card">
        <Table>
          <TableHeader>
            <TableRow className="border-border hover:bg-transparent">
              <TableHead>IP Address</TableHead>
              <TableHead>Risk Score</TableHead>
              <TableHead>Technique</TableHead>
              <TableHead>Status</TableHead>
              <TableHead>Route</TableHead>
              <TableHead>Last Seen</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {isLoading ? (
              Array(5).fill(0).map((_, i) => (
                <TableRow key={i} className="border-border">
                  <TableCell><Skeleton className="h-5 w-24" /></TableCell>
                  <TableCell><Skeleton className="h-5 w-12" /></TableCell>
                  <TableCell><Skeleton className="h-5 w-32" /></TableCell>
                  <TableCell><Skeleton className="h-5 w-20" /></TableCell>
                  <TableCell><Skeleton className="h-5 w-20" /></TableCell>
                  <TableCell><Skeleton className="h-5 w-24" /></TableCell>
                  <TableCell><Skeleton className="h-8 w-8 ml-auto" /></TableCell>
                </TableRow>
              ))
            ) : (
              threatData?.threats.map((threat) => (
                <TableRow key={threat.id} className="border-border hover:bg-muted/50 cursor-pointer" onClick={() => setSelectedId(threat.id)}>
                  <TableCell className="font-mono text-sm">{threat.ipAddress}</TableCell>
                  <TableCell>
                    <div className="flex items-center gap-2">
                      <span className={`font-bold ${threat.score > 80 ? 'text-destructive' : threat.score > 50 ? 'text-orange-500' : 'text-yellow-500'}`}>
                        {threat.score}
                      </span>
                    </div>
                  </TableCell>
                  <TableCell>
                    <Badge variant="outline" className="font-mono text-xs">{threat.technique}</Badge>
                  </TableCell>
                  <TableCell>
                    <Badge variant={threat.status === 'active' ? 'destructive' : 'secondary'} className={threat.status === 'honeypotted' ? 'bg-primary text-primary-foreground hover:bg-primary/80' : ''}>
                      {threat.status}
                    </Badge>
                  </TableCell>
                  <TableCell>
                    <Badge variant="outline" className={threat.route === 'fake_server' ? 'border-primary/50 text-primary' : 'border-green-500/50 text-green-500'}>
                      {threat.route === 'fake_server' ? 'Honeypot' : 'Real Server'}
                    </Badge>
                  </TableCell>
                  <TableCell className="text-muted-foreground text-sm">
                    {format(new Date(threat.lastSeen), "MMM d, HH:mm")}
                  </TableCell>
                  <TableCell className="text-right">
                    <Button variant="ghost" size="icon" onClick={(e) => { e.stopPropagation(); setSelectedId(threat.id); }}>
                      <MoreHorizontal className="h-4 w-4" />
                    </Button>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </Card>

      <Dialog open={!!selectedId} onOpenChange={(open) => !open && setSelectedId(null)}>
        <DialogContent className="max-w-3xl bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-xl flex items-center gap-2">
              <ShieldAlert className="h-5 w-5 text-destructive" />
              Threat Investigation
            </DialogTitle>
            <DialogDescription>
              Detailed forensic analysis of suspicious activity.
            </DialogDescription>
          </DialogHeader>

          {detailLoading || !detailData ? (
            <div className="space-y-4 py-4">
              <Skeleton className="h-24 w-full" />
              <div className="grid grid-cols-2 gap-4">
                <Skeleton className="h-48 w-full" />
                <Skeleton className="h-48 w-full" />
              </div>
            </div>
          ) : (
            <div className="space-y-6">
              <div className="grid grid-cols-3 gap-4">
                <div className="p-4 bg-background border border-border rounded-lg">
                  <div className="text-sm text-muted-foreground mb-1">Actor IP</div>
                  <div className="text-lg font-mono font-bold flex items-center gap-2">
                    {detailData.ipAddress}
                    {detailData.isTor && <Badge variant="destructive" className="text-[10px]">TOR</Badge>}
                    {detailData.isVpn && <Badge variant="secondary" className="text-[10px]">VPN</Badge>}
                  </div>
                </div>
                <div className="p-4 bg-background border border-border rounded-lg">
                  <div className="text-sm text-muted-foreground mb-1">Geo-Location</div>
                  <div className="text-lg font-medium flex items-center gap-2">
                    <MapPin className="h-4 w-4 text-muted-foreground" />
                    {detailData.geoLocation}
                  </div>
                </div>
                <div className="p-4 bg-background border border-border rounded-lg">
                  <div className="text-sm text-muted-foreground mb-1">Threat Score</div>
                  <div className={`text-2xl font-bold ${detailData.score > 80 ? 'text-destructive' : 'text-orange-500'}`}>
                    {detailData.score} <span className="text-sm text-muted-foreground font-normal">/ 100</span>
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-6">
                <Card className="bg-background border-border shadow-none">
                  <CardHeader className="pb-3">
                    <CardTitle className="text-base">Score Breakdown</CardTitle>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div>
                      <div className="flex justify-between text-sm mb-1">
                        <span className="text-muted-foreground">Base Path/Body</span>
                        <span className="font-mono">{detailData.scoreComponents.basePathBody}</span>
                      </div>
                      <Progress value={detailData.scoreComponents.basePathBody} className="h-2" />
                    </div>
                    <div>
                      <div className="flex justify-between text-sm mb-1">
                        <span className="text-muted-foreground">Behavioral Memory</span>
                        <span className="font-mono">{detailData.scoreComponents.memoryBoost}</span>
                      </div>
                      <Progress value={detailData.scoreComponents.memoryBoost} className="h-2" />
                    </div>
                    <div>
                      <div className="flex justify-between text-sm mb-1">
                        <span className="text-muted-foreground">Cross-Key Correlation</span>
                        <span className="font-mono">{detailData.scoreComponents.correlationBoost}</span>
                      </div>
                      <Progress value={detailData.scoreComponents.correlationBoost} className="h-2" />
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-background border-border shadow-none">
                  <CardHeader className="pb-3">
                    <CardTitle className="text-base">Intelligence</CardTitle>
                  </CardHeader>
                  <CardContent className="space-y-4 text-sm">
                    <div className="space-y-1">
                      <span className="text-muted-foreground block text-xs uppercase tracking-wider">ATTACK TECHNIQUES</span>
                      <div className="flex flex-wrap gap-1">
                        {detailData.attackTechniques.map(t => (
                          <Badge key={t} variant="secondary" className="font-mono text-xs">{t}</Badge>
                        ))}
                      </div>
                    </div>
                    <div className="space-y-1">
                      <span className="text-muted-foreground block text-xs uppercase tracking-wider">USER AGENT</span>
                      <div className="font-mono text-xs break-all bg-muted/50 p-2 rounded">
                        {detailData.userAgent}
                      </div>
                    </div>
                    <div className="space-y-1">
                      <span className="text-muted-foreground block text-xs uppercase tracking-wider">ASN</span>
                      <div className="font-medium">
                        {detailData.asn}
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>

              <div className="flex justify-end gap-3 pt-4 border-t border-border">
                <Button variant="outline" onClick={() => setSelectedId(null)}>Close</Button>
                <Button variant="secondary" onClick={() => handleDismiss(detailData.id)} disabled={dismissMutation.isPending}>
                  {dismissMutation.isPending ? "Dismissing..." : "Dismiss (False Positive)"}
                </Button>
                <Button variant="destructive">Block IP Firmly</Button>
              </div>
            </div>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/sessions.tsx
// ============================================================
import { useListSessions, useGetSession } from "@workspace/api-client-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { format } from "date-fns";
import { Network, Activity, AlertTriangle, Route as RouteIcon, ShieldAlert } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import React from "react";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { LineChart, Line, XAxis, YAxis, ResponsiveContainer, CartesianGrid, Tooltip } from "recharts";

export default function Sessions() {
  const [selectedId, setSelectedId] = React.useState<string | null>(null);
  const { data: sessionData, isLoading } = useListSessions();
  const { data: detailData, isLoading: detailLoading } = useGetSession(selectedId || "", {
    query: { enabled: !!selectedId }
  });

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Live Session Monitor</h1>
          <p className="text-muted-foreground">Track active API sessions across real and honeypot environments.</p>
        </div>
      </div>

      <div className="grid gap-6">
        <Card className="bg-card">
          <Table>
            <TableHeader>
              <TableRow className="border-border">
                <TableHead>IP Address</TableHead>
                <TableHead>Type</TableHead>
                <TableHead>Requests</TableHead>
                <TableHead>Current Score</TableHead>
                <TableHead>Started At</TableHead>
                <TableHead>Last Activity</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {isLoading ? (
                Array(5).fill(0).map((_, i) => (
                  <TableRow key={i} className="border-border">
                    <TableCell><Skeleton className="h-5 w-32" /></TableCell>
                    <TableCell><Skeleton className="h-5 w-20" /></TableCell>
                    <TableCell><Skeleton className="h-5 w-12" /></TableCell>
                    <TableCell><Skeleton className="h-5 w-16" /></TableCell>
                    <TableCell><Skeleton className="h-5 w-24" /></TableCell>
                    <TableCell><Skeleton className="h-5 w-24" /></TableCell>
                  </TableRow>
                ))
              ) : (
                sessionData?.map((session) => (
                  <TableRow 
                    key={session.id} 
                    className="border-border hover:bg-muted/50 cursor-pointer"
                    onClick={() => setSelectedId(session.id)}
                  >
                    <TableCell className="font-mono text-sm">{session.ipAddress}</TableCell>
                    <TableCell>
                      <Badge variant="outline" className={
                        session.type === 'honeypot' ? 'border-destructive/50 text-destructive' : 
                        session.type === 'cloned' ? 'border-primary/50 text-primary' :
                        'border-green-500/50 text-green-500'
                      }>
                        {session.type.toUpperCase()}
                      </Badge>
                    </TableCell>
                    <TableCell className="font-mono">{session.requestCount}</TableCell>
                    <TableCell>
                      <span className={`font-bold ${session.currentScore > 80 ? 'text-destructive' : session.currentScore > 50 ? 'text-orange-500' : 'text-muted-foreground'}`}>
                        {session.currentScore}
                      </span>
                    </TableCell>
                    <TableCell className="text-muted-foreground text-sm">
                      {format(new Date(session.startedAt), "HH:mm:ss")}
                    </TableCell>
                    <TableCell className="text-muted-foreground text-sm">
                      {format(new Date(session.lastActivity), "HH:mm:ss")}
                    </TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </Card>
      </div>

      <Dialog open={!!selectedId} onOpenChange={(open) => !open && setSelectedId(null)}>
        <DialogContent className="max-w-4xl bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-xl flex items-center gap-2">
              <Network className="h-5 w-5 text-primary" />
              Session Inspection
            </DialogTitle>
            <DialogDescription>
              Real-time trajectory and request log for this session.
            </DialogDescription>
          </DialogHeader>

          {detailLoading || !detailData ? (
            <div className="space-y-4 py-4">
              <Skeleton className="h-32 w-full" />
              <Skeleton className="h-64 w-full" />
            </div>
          ) : (
            <div className="space-y-6">
              <div className="grid grid-cols-4 gap-4">
                <div className="p-3 bg-background border border-border rounded-lg">
                  <div className="text-xs text-muted-foreground mb-1">Status</div>
                  <Badge variant="outline" className={detailData.type === 'real' ? 'border-green-500 text-green-500' : 'border-destructive text-destructive'}>
                    {detailData.type === 'real' ? 'Trusted' : 'Honeypotted'}
                  </Badge>
                </div>
                {detailData.clonedToHoneypotAt && (
                  <div className="p-3 bg-background border border-border rounded-lg">
                    <div className="text-xs text-muted-foreground mb-1">Clone Latency</div>
                    <div className="font-mono text-lg font-bold text-primary">{detailData.cloneLatencyMs}ms</div>
                  </div>
                )}
                <div className="p-3 bg-background border border-border rounded-lg">
                  <div className="text-xs text-muted-foreground mb-1">Total Requests</div>
                  <div className="font-mono text-lg">{detailData.requestCount}</div>
                </div>
                <div className="p-3 bg-background border border-border rounded-lg">
                  <div className="text-xs text-muted-foreground mb-1">Final Score</div>
                  <div className="font-mono text-lg text-destructive">{detailData.currentScore}</div>
                </div>
              </div>

              <Card className="bg-background border-border shadow-none">
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm">Score Trajectory</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="h-[150px] w-full">
                    <ResponsiveContainer width="100%" height="100%">
                      <LineChart data={detailData.scoreHistory} margin={{ top: 5, right: 5, left: -20, bottom: 0 }}>
                        <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" vertical={false} />
                        <XAxis 
                          dataKey="timestamp" 
                          tickFormatter={(val) => format(new Date(val), "HH:mm:ss")} 
                          stroke="hsl(var(--muted-foreground))"
                          fontSize={10}
                        />
                        <YAxis stroke="hsl(var(--muted-foreground))" fontSize={10} domain={[0, 100]} />
                        <Tooltip 
                          contentStyle={{ backgroundColor: 'hsl(var(--popover))', borderColor: 'hsl(var(--border))' }}
                          labelFormatter={(val) => format(new Date(val), "HH:mm:ss")}
                        />
                        <Line type="stepAfter" dataKey="score" stroke="hsl(var(--destructive))" strokeWidth={2} dot={false} />
                      </LineChart>
                    </ResponsiveContainer>
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-background border-border shadow-none">
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm">Request Log</CardTitle>
                </CardHeader>
                <CardContent className="p-0">
                  <div className="max-h-[300px] overflow-auto">
                    <Table>
                      <TableHeader className="bg-muted/50 sticky top-0">
                        <TableRow className="border-border hover:bg-transparent">
                          <TableHead className="w-24">Time</TableHead>
                          <TableHead className="w-16">Method</TableHead>
                          <TableHead>Path</TableHead>
                          <TableHead className="w-16 text-right">Score</TableHead>
                          <TableHead className="w-24 text-right">Route</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        {detailData.requestLog.map((req, i) => (
                          <TableRow key={i} className="border-border">
                            <TableCell className="font-mono text-xs text-muted-foreground">
                              {format(new Date(req.timestamp), "HH:mm:ss.SSS")}
                            </TableCell>
                            <TableCell>
                              <Badge variant="outline" className="text-[10px] uppercase font-mono px-1">
                                {req.method}
                              </Badge>
                            </TableCell>
                            <TableCell className="font-mono text-xs text-muted-foreground truncate max-w-[200px]">
                              {req.path}
                            </TableCell>
                            <TableCell className="text-right font-mono text-xs">
                              <span className={req.score > 80 ? 'text-destructive' : 'text-muted-foreground'}>
                                {req.score}
                              </span>
                            </TableCell>
                            <TableCell className="text-right">
                              {req.servedBy === 'fake_server' ? (
                                <ShieldAlert className="h-4 w-4 text-destructive inline-block" />
                              ) : (
                                <Activity className="h-4 w-4 text-green-500 inline-block" />
                              )}
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </div>
                </CardContent>
              </Card>

            </div>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/honeypot.tsx
// ============================================================
import { useGetFakeServerStats, useListFakeRecords, useGetFakeServerInteractions } from "@workspace/api-client-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { format } from "date-fns";
import { Shield, Database, Activity, Clock, Zap } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import { Progress } from "@/components/ui/progress";

export default function Honeypot() {
  const { data: stats, isLoading: statsLoading } = useGetFakeServerStats();
  const { data: recordsData, isLoading: recordsLoading } = useListFakeRecords({ limit: 10 });
  const { data: interactionsData, isLoading: interactionsLoading } = useGetFakeServerInteractions({ limit: 15 });

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight flex items-center gap-3">
            <Shield className="h-8 w-8 text-primary" />
            Honeypot Core
          </h1>
          <p className="text-muted-foreground mt-1">Live overview of the fake server environment actively trapping attackers.</p>
        </div>
        <div className="flex items-center gap-2 px-3 py-1.5 bg-primary/10 text-primary border border-primary/30 rounded-full text-sm font-medium animate-pulse">
          <div className="w-2 h-2 rounded-full bg-primary"></div>
          Environment Active
        </div>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card className="bg-card border-primary/20 shadow-[0_0_15px_rgba(0,255,255,0.05)]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Total Interactions</CardTitle>
            <Activity className="h-4 w-4 text-primary" />
          </CardHeader>
          <CardContent>
            {statsLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-primary">{stats?.totalInteractions.toLocaleString()}</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Requests served by fake endpoints</p>
          </CardContent>
        </Card>
        
        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Avg Clone Latency</CardTitle>
            <Zap className="h-4 w-4 text-yellow-500" />
          </CardHeader>
          <CardContent>
            {statsLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-yellow-500">{stats?.avgCloneLatencyMs.toFixed(1)}ms</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Time to split session (Fastest: {stats?.fastestCloneMs}ms)</p>
          </CardContent>
        </Card>

        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Time in Honeypot</CardTitle>
            <Clock className="h-4 w-4 text-blue-500" />
          </CardHeader>
          <CardContent>
            {statsLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-blue-500">{stats?.avgTimeInHoneypotMinutes.toFixed(1)}m</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Average time spent before dropping</p>
          </CardContent>
        </Card>

        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Believability Rate</CardTitle>
            <Shield className="h-4 w-4 text-green-500" />
          </CardHeader>
          <CardContent>
            {statsLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-green-500">{(stats?.believabilityRate ?? 0).toFixed(1)}%</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Attackers continuing after fake data</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        <Card className="bg-card flex flex-col h-[500px]">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Database className="h-5 w-5 text-muted-foreground" />
              Dynamic Fake Records
            </CardTitle>
            <CardDescription>Generated synthetic data currently being served to attackers.</CardDescription>
          </CardHeader>
          <CardContent className="flex-1 overflow-auto p-0">
            <Table>
              <TableHeader className="bg-muted/50 sticky top-0 z-10">
                <TableRow className="border-border">
                  <TableHead className="pl-6">Type</TableHead>
                  <TableHead>Generated Payload (Excerpt)</TableHead>
                  <TableHead className="text-right pr-6">Served</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {recordsLoading ? (
                  Array(5).fill(0).map((_, i) => (
                    <TableRow key={i} className="border-border">
                      <TableCell className="pl-6"><Skeleton className="h-5 w-20" /></TableCell>
                      <TableCell><Skeleton className="h-5 w-48" /></TableCell>
                      <TableCell className="pr-6"><Skeleton className="h-5 w-8 ml-auto" /></TableCell>
                    </TableRow>
                  ))
                ) : (
                  recordsData?.records.map((record) => (
                    <TableRow key={record.id} className="border-border hover:bg-muted/30">
                      <TableCell className="pl-6">
                        <Badge variant="outline" className="uppercase text-[10px] tracking-wider">{record.type}</Badge>
                      </TableCell>
                      <TableCell className="font-mono text-xs text-muted-foreground truncate max-w-[200px]">
                        {JSON.stringify(record.data).substring(0, 60)}...
                      </TableCell>
                      <TableCell className="text-right pr-6 font-mono">
                        {record.servedTo}
                      </TableCell>
                    </TableRow>
                  ))
                )}
              </TableBody>
            </Table>
          </CardContent>
        </Card>

        <Card className="bg-card flex flex-col h-[500px]">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Activity className="h-5 w-5 text-muted-foreground" />
              Live Interactions
            </CardTitle>
            <CardDescription>Real-time log of requests hitting the fake server.</CardDescription>
          </CardHeader>
          <CardContent className="flex-1 overflow-auto p-0">
            <Table>
              <TableHeader className="bg-muted/50 sticky top-0 z-10">
                <TableRow className="border-border">
                  <TableHead className="pl-6">Time</TableHead>
                  <TableHead>Attacker IP</TableHead>
                  <TableHead>Endpoint Access</TableHead>
                  <TableHead className="text-center pr-6">Believed</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {interactionsLoading ? (
                  Array(5).fill(0).map((_, i) => (
                    <TableRow key={i} className="border-border">
                      <TableCell className="pl-6"><Skeleton className="h-5 w-16" /></TableCell>
                      <TableCell><Skeleton className="h-5 w-24" /></TableCell>
                      <TableCell><Skeleton className="h-5 w-32" /></TableCell>
                      <TableCell className="pr-6"><Skeleton className="h-5 w-12 mx-auto" /></TableCell>
                    </TableRow>
                  ))
                ) : (
                  interactionsData?.map((interaction) => (
                    <TableRow key={interaction.id} className="border-border hover:bg-muted/30">
                      <TableCell className="pl-6 text-xs text-muted-foreground whitespace-nowrap">
                        {format(new Date(interaction.timestamp), "HH:mm:ss")}
                      </TableCell>
                      <TableCell className="font-mono text-xs">
                        {interaction.attackerIp}
                      </TableCell>
                      <TableCell>
                        <div className="flex items-center gap-2">
                          <span className="text-[10px] text-muted-foreground font-mono uppercase">{interaction.method}</span>
                          <span className="font-mono text-xs truncate max-w-[120px]">{interaction.endpoint}</span>
                        </div>
                      </TableCell>
                      <TableCell className="text-center pr-6">
                        {interaction.attackerBelievedData ? (
                          <span className="inline-flex w-2 h-2 rounded-full bg-green-500"></span>
                        ) : (
                          <span className="inline-flex w-2 h-2 rounded-full bg-muted"></span>
                        )}
                      </TableCell>
                    </TableRow>
                  ))
                )}
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/attackers.tsx
// ============================================================
import { useListAttackProfiles, useGetAttackProfile, useGetAttackTechniques } from "@workspace/api-client-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { format } from "date-fns";
import { Users, Crosshair, Search, Fingerprint, MapPin, Database, Activity } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import React from "react";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from "recharts";

export default function Attackers() {
  const [selectedId, setSelectedId] = React.useState<string | null>(null);
  
  const { data: profilesData, isLoading: profilesLoading } = useListAttackProfiles();
  const { data: techniquesData, isLoading: techniquesLoading } = useGetAttackTechniques();
  
  const { data: detailData, isLoading: detailLoading } = useGetAttackProfile(selectedId || "", {
    query: { enabled: !!selectedId }
  });

  const COLORS = ['hsl(var(--chart-1))', 'hsl(var(--chart-2))', 'hsl(var(--chart-3))', 'hsl(var(--chart-4))', 'hsl(var(--chart-5))'];

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Attacker Profiles</h1>
          <p className="text-muted-foreground">Correlated identities across multiple IPs and sessions.</p>
        </div>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        <Card className="bg-card col-span-2 flex flex-col">
          <CardHeader>
            <CardTitle>Known Adversaries</CardTitle>
            <CardDescription>Entities mapped through behavioral fingerprints</CardDescription>
          </CardHeader>
          <CardContent className="flex-1 overflow-auto p-0">
            <Table>
              <TableHeader className="bg-muted/50 sticky top-0">
                <TableRow className="border-border">
                  <TableHead className="pl-6">Fingerprint</TableHead>
                  <TableHead>Intent</TableHead>
                  <TableHead>Primary Technique</TableHead>
                  <TableHead className="text-right">Time in Honeypot</TableHead>
                  <TableHead className="text-right pr-6">IPs</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {profilesLoading ? (
                  Array(5).fill(0).map((_, i) => (
                    <TableRow key={i} className="border-border">
                      <TableCell className="pl-6"><Skeleton className="h-5 w-24" /></TableCell>
                      <TableCell><Skeleton className="h-5 w-24" /></TableCell>
                      <TableCell><Skeleton className="h-5 w-32" /></TableCell>
                      <TableCell className="text-right"><Skeleton className="h-5 w-12 ml-auto" /></TableCell>
                      <TableCell className="text-right pr-6"><Skeleton className="h-5 w-8 ml-auto" /></TableCell>
                    </TableRow>
                  ))
                ) : (
                  profilesData?.map((profile) => (
                    <TableRow 
                      key={profile.id} 
                      className="border-border hover:bg-muted/50 cursor-pointer"
                      onClick={() => setSelectedId(profile.id)}
                    >
                      <TableCell className="pl-6 font-mono text-xs">{profile.fingerprint.substring(0, 12)}...</TableCell>
                      <TableCell>
                        <Badge variant="outline" className="border-orange-500/50 text-orange-500 bg-orange-500/10 text-[10px] uppercase">
                          {profile.intent.replace('_', ' ')}
                        </Badge>
                      </TableCell>
                      <TableCell className="text-sm">{profile.technique}</TableCell>
                      <TableCell className="text-right text-muted-foreground text-sm">{profile.honeypotTimeMinutes}m</TableCell>
                      <TableCell className="text-right pr-6 font-mono text-sm">{profile.ipAddresses.length}</TableCell>
                    </TableRow>
                  ))
                )}
              </TableBody>
            </Table>
          </CardContent>
        </Card>

        <Card className="bg-card">
          <CardHeader>
            <CardTitle>Technique Distribution</CardTitle>
            <CardDescription>Observed MITRE ATT&CK patterns</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="h-[300px] w-full">
              {techniquesLoading ? <Skeleton className="h-full w-full rounded-full" /> : (
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie
                      data={techniquesData}
                      cx="50%"
                      cy="50%"
                      innerRadius={60}
                      outerRadius={80}
                      paddingAngle={5}
                      dataKey="count"
                      nameKey="technique"
                    >
                      {techniquesData?.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                      ))}
                    </Pie>
                    <Tooltip 
                      contentStyle={{ backgroundColor: 'hsl(var(--popover))', borderColor: 'hsl(var(--border))', borderRadius: '8px' }}
                      itemStyle={{ color: 'hsl(var(--popover-foreground))' }}
                    />
                    <Legend verticalAlign="bottom" height={36} iconType="circle" wrapperStyle={{ fontSize: '12px' }} />
                  </PieChart>
                </ResponsiveContainer>
              )}
            </div>
          </CardContent>
        </Card>
      </div>

      <Dialog open={!!selectedId} onOpenChange={(open) => !open && setSelectedId(null)}>
        <DialogContent className="max-w-4xl bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-xl flex items-center gap-2">
              <Crosshair className="h-5 w-5 text-primary" />
              Forensic Profile
            </DialogTitle>
            <DialogDescription>
              Detailed behavioral analysis and intelligence gathered in honeypot.
            </DialogDescription>
          </DialogHeader>

          {detailLoading || !detailData ? (
            <div className="space-y-4 py-4">
              <Skeleton className="h-24 w-full" />
              <div className="grid grid-cols-2 gap-4">
                <Skeleton className="h-48 w-full" />
                <Skeleton className="h-48 w-full" />
              </div>
            </div>
          ) : (
            <div className="space-y-6">
              <div className="grid grid-cols-4 gap-4">
                <div className="p-3 bg-background border border-border rounded-lg">
                  <div className="text-xs text-muted-foreground mb-1">Actor Type</div>
                  <div className="font-semibold text-primary capitalize">{detailData.forensicReport.estimatedActorType.replace('_', ' ')}</div>
                </div>
                <div className="p-3 bg-background border border-border rounded-lg">
                  <div className="text-xs text-muted-foreground mb-1">Confidence</div>
                  <div className="font-semibold">{detailData.attributionConfidence}%</div>
                </div>
                <div className="p-3 bg-background border border-border rounded-lg">
                  <div className="text-xs text-muted-foreground mb-1">Total Requests</div>
                  <div className="font-semibold font-mono">{detailData.totalRequests}</div>
                </div>
                <div className="p-3 bg-background border border-border rounded-lg">
                  <div className="text-xs text-muted-foreground mb-1">Key Rotations</div>
                  <div className="font-semibold font-mono text-destructive">{detailData.apiKeyRotations}</div>
                </div>
              </div>

              <div className="p-4 bg-muted/20 border border-border rounded-lg text-sm leading-relaxed">
                <strong className="text-foreground block mb-2">AI Summary:</strong>
                <span className="text-muted-foreground">{detailData.forensicReport.summary}</span>
              </div>

              <div className="grid grid-cols-2 gap-6">
                <div className="space-y-4">
                  <h3 className="font-semibold flex items-center gap-2 text-sm border-b border-border pb-2">
                    <Search className="h-4 w-4" /> Observed Tooling & Indicators
                  </h3>
                  <div className="space-y-3">
                    <div>
                      <span className="text-xs text-muted-foreground block mb-1">IDENTIFIED TOOLS</span>
                      <div className="flex flex-wrap gap-1">
                        {detailData.forensicReport.toolsIdentified.map((t, i) => (
                          <Badge key={i} variant="secondary" className="font-mono text-[10px]">{t}</Badge>
                        ))}
                      </div>
                    </div>
                    <div>
                      <span className="text-xs text-muted-foreground block mb-1">MITRE TECHNIQUES</span>
                      <div className="flex flex-wrap gap-1">
                        {detailData.forensicReport.mitreTechniques.map((t, i) => (
                          <Badge key={i} variant="outline" className="font-mono text-[10px] border-primary/30 text-primary">{t}</Badge>
                        ))}
                      </div>
                    </div>
                    <div>
                      <span className="text-xs text-muted-foreground block mb-1">ROUTING CHAIN</span>
                      <div className="text-xs font-mono text-muted-foreground bg-background p-2 rounded border border-border">
                        {detailData.forensicReport.geolocationChain.join(" → ")}
                      </div>
                    </div>
                  </div>
                </div>

                <div className="space-y-4">
                  <h3 className="font-semibold flex items-center gap-2 text-sm border-b border-border pb-2">
                    <Activity className="h-4 w-4" /> Behavioral Map
                  </h3>
                  <div className="space-y-3 relative before:absolute before:inset-y-0 before:left-2 before:w-0.5 before:bg-border ml-2">
                    {detailData.behaviorMap.map((ev, i) => (
                      <div key={i} className="relative pl-6">
                        <span className={`absolute left-0 top-1.5 w-4 h-4 rounded-full border-4 border-card -translate-x-1.5 ${
                          ev.significance === 'high' ? 'bg-destructive' :
                          ev.significance === 'medium' ? 'bg-orange-500' : 'bg-primary'
                        }`} />
                        <div className="text-xs text-muted-foreground mb-0.5">{format(new Date(ev.timestamp), "HH:mm:ss")}</div>
                        <div className="text-sm font-medium">{ev.action}</div>
                        <div className="text-xs text-muted-foreground mt-0.5">{ev.detail}</div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/canary.tsx
// ============================================================
import { useListCanaryTokens, useCreateCanaryToken, useGetCanaryTokenTrips } from "@workspace/api-client-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { format } from "date-fns";
import { Target, Plus, AlertCircle, Key, Link as LinkIcon, Mail, Database, FileText } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import React from "react";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";

const formSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters."),
  type: z.enum(["api_key", "url", "email", "database_record", "file"]),
  location: z.string().min(2, "Location is required."),
});

export default function Canary() {
  const [selectedToken, setSelectedToken] = React.useState<string | null>(null);
  const [createOpen, setCreateOpen] = React.useState(false);
  
  const { data: tokens, isLoading: tokensLoading, refetch: refetchTokens } = useListCanaryTokens();
  const { data: tripsData, isLoading: tripsLoading } = useGetCanaryTokenTrips(selectedToken || "", {
    query: { enabled: !!selectedToken }
  });

  const createMutation = useCreateCanaryToken();

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      name: "",
      type: "api_key",
      location: "",
    },
  });

  function onSubmit(values: z.infer<typeof formSchema>) {
    createMutation.mutate({ data: values }, {
      onSuccess: () => {
        setCreateOpen(false);
        form.reset();
        refetchTokens();
      }
    });
  }

  const getTokenIcon = (type: string) => {
    switch(type) {
      case 'api_key': return <Key className="h-4 w-4" />;
      case 'url': return <LinkIcon className="h-4 w-4" />;
      case 'email': return <Mail className="h-4 w-4" />;
      case 'database_record': return <Database className="h-4 w-4" />;
      case 'file': return <FileText className="h-4 w-4" />;
      default: return <Target className="h-4 w-4" />;
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Canary Tokens</h1>
          <p className="text-muted-foreground">Deploy fake assets to instantly detect lateral movement and scraping.</p>
        </div>
        <Dialog open={createOpen} onOpenChange={setCreateOpen}>
          <DialogTrigger asChild>
            <Button className="bg-primary text-primary-foreground">
              <Plus className="h-4 w-4 mr-2" /> Deploy Token
            </Button>
          </DialogTrigger>
          <DialogContent className="bg-card border-border">
            <DialogHeader>
              <DialogTitle>Deploy New Canary Token</DialogTitle>
              <DialogDescription>
                Create a trackable fake asset. If anyone accesses this asset, SentinelMesh will instantly isolate their IP.
              </DialogDescription>
            </DialogHeader>
            <Form {...form}>
              <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                <FormField
                  control={form.control}
                  name="name"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Token Name / Description</FormLabel>
                      <FormControl>
                        <Input placeholder="e.g. Legacy DB Admin Key" {...field} className="bg-background" />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
                <FormField
                  control={form.control}
                  name="type"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Asset Type</FormLabel>
                      <Select onValueChange={field.onChange} defaultValue={field.value}>
                        <FormControl>
                          <SelectTrigger className="bg-background">
                            <SelectValue placeholder="Select type" />
                          </SelectTrigger>
                        </FormControl>
                        <SelectContent>
                          <SelectItem value="api_key">API Key (String)</SelectItem>
                          <SelectItem value="url">Hidden URL</SelectItem>
                          <SelectItem value="database_record">Database Record</SelectItem>
                          <SelectItem value="file">File Path</SelectItem>
                          <SelectItem value="email">Email Address</SelectItem>
                        </SelectContent>
                      </Select>
                      <FormMessage />
                    </FormItem>
                  )}
                />
                <FormField
                  control={form.control}
                  name="location"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Deployment Location (For your reference)</FormLabel>
                      <FormControl>
                        <Input placeholder="e.g. inside config.json on auth-server" {...field} className="bg-background" />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
                <Button type="submit" className="w-full mt-4" disabled={createMutation.isPending}>
                  {createMutation.isPending ? "Generating..." : "Generate Token"}
                </Button>
              </form>
            </Form>
          </DialogContent>
        </Dialog>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        <Card className="bg-card col-span-1 md:col-span-3">
          <Table>
            <TableHeader className="bg-muted/50">
              <TableRow className="border-border hover:bg-transparent">
                <TableHead className="pl-6">Token Name</TableHead>
                <TableHead>Type</TableHead>
                <TableHead>Location</TableHead>
                <TableHead>Status</TableHead>
                <TableHead className="text-right">Trips</TableHead>
                <TableHead className="text-right pr-6">Last Tripped</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {tokensLoading ? (
                Array(3).fill(0).map((_, i) => (
                  <TableRow key={i} className="border-border">
                    <TableCell className="pl-6"><Skeleton className="h-5 w-32" /></TableCell>
                    <TableCell><Skeleton className="h-5 w-20" /></TableCell>
                    <TableCell><Skeleton className="h-5 w-40" /></TableCell>
                    <TableCell><Skeleton className="h-5 w-16" /></TableCell>
                    <TableCell className="text-right"><Skeleton className="h-5 w-8 ml-auto" /></TableCell>
                    <TableCell className="text-right pr-6"><Skeleton className="h-5 w-24 ml-auto" /></TableCell>
                  </TableRow>
                ))
              ) : (
                tokens?.map((token) => (
                  <TableRow 
                    key={token.id} 
                    className="border-border hover:bg-muted/50 cursor-pointer"
                    onClick={() => setSelectedToken(token.id)}
                  >
                    <TableCell className="pl-6 font-medium flex items-center gap-2">
                      <div className="p-1.5 rounded-md bg-muted text-muted-foreground">
                        {getTokenIcon(token.type)}
                      </div>
                      {token.name}
                    </TableCell>
                    <TableCell>
                      <span className="text-xs uppercase tracking-wider text-muted-foreground">{token.type.replace('_', ' ')}</span>
                    </TableCell>
                    <TableCell className="text-sm text-muted-foreground">{token.location}</TableCell>
                    <TableCell>
                      <Badge variant={token.status === 'tripped' ? 'destructive' : 'secondary'} className={token.status === 'active' ? 'bg-green-500/10 text-green-500 hover:bg-green-500/20 border-green-500/20' : ''}>
                        {token.status}
                      </Badge>
                    </TableCell>
                    <TableCell className="text-right font-mono font-bold text-destructive">
                      {token.tripCount > 0 ? token.tripCount : '-'}
                    </TableCell>
                    <TableCell className="text-right pr-6 text-sm text-muted-foreground">
                      {token.lastTripped ? format(new Date(token.lastTripped), "MMM d, HH:mm") : 'Never'}
                    </TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </Card>
      </div>

      <Dialog open={!!selectedToken} onOpenChange={(open) => !open && setSelectedToken(null)}>
        <DialogContent className="max-w-3xl bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-xl flex items-center gap-2">
              <AlertCircle className="h-5 w-5 text-destructive" />
              Token Activation Log
            </DialogTitle>
            <DialogDescription>
              Every time this token was accessed, the attacker was instantly routed to the honeypot.
            </DialogDescription>
          </DialogHeader>

          {tripsLoading || !tripsData ? (
            <div className="py-8 flex justify-center"><Skeleton className="h-8 w-8 rounded-full" /></div>
          ) : tripsData.length === 0 ? (
            <div className="py-12 text-center text-muted-foreground border border-dashed border-border rounded-lg bg-background">
              <Target className="h-8 w-8 mx-auto mb-3 opacity-20" />
              <p>This token has not been tripped yet.</p>
            </div>
          ) : (
            <div className="space-y-4">
              <Table>
                <TableHeader className="bg-muted/50">
                  <TableRow className="border-border hover:bg-transparent">
                    <TableHead>Time</TableHead>
                    <TableHead>IP Address</TableHead>
                    <TableHead>User Agent</TableHead>
                    <TableHead className="text-right">Clone Latency</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {tripsData.map((trip) => (
                    <TableRow key={trip.id} className="border-border">
                      <TableCell className="text-sm font-mono text-muted-foreground whitespace-nowrap">
                        {format(new Date(trip.trippedAt), "MMM d, HH:mm:ss")}
                      </TableCell>
                      <TableCell className="font-mono text-xs">{trip.ipAddress}</TableCell>
                      <TableCell className="text-xs font-mono text-muted-foreground max-w-[200px] truncate">
                        {trip.userAgent}
                      </TableCell>
                      <TableCell className="text-right font-mono text-xs text-primary">
                        {trip.cloneLatencyMs}ms
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </div>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/learning.tsx
// ============================================================
import { useGetLearningMetrics, useGetLearningImprovements } from "@workspace/api-client-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { format } from "date-fns";
import { Brain, Zap, Target, Shield, Database, GitMerge } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";

export default function Learning() {
  const { data: metrics, isLoading: metricsLoading } = useGetLearningMetrics();
  const { data: improvements, isLoading: improvementsLoading } = useGetLearningImprovements({ limit: 20 });

  const getImprovementIcon = (type: string) => {
    switch(type) {
      case 'model_update': return <Brain className="h-4 w-4 text-primary" />;
      case 'canary_repositioned': return <Target className="h-4 w-4 text-orange-500" />;
      case 'fake_data_improved': return <Database className="h-4 w-4 text-blue-500" />;
      case 'threshold_adjusted': return <Shield className="h-4 w-4 text-green-500" />;
      case 'correlation_rule_added': return <GitMerge className="h-4 w-4 text-purple-500" />;
      default: return <Zap className="h-4 w-4" />;
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">AI Learning Loop</h1>
          <p className="text-muted-foreground">SentinelMesh improves itself automatically by analyzing attacks caught in the honeypot.</p>
        </div>
      </div>

      <div className="grid gap-4 md:grid-cols-4">
        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Model Accuracy</CardTitle>
            <Brain className="h-4 w-4 text-primary" />
          </CardHeader>
          <CardContent>
            {metricsLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-primary">{(metrics?.modelAccuracy ?? 0) * 100}%</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Based on recent validations</p>
          </CardContent>
        </Card>
        
        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">False Positives</CardTitle>
            <Shield className="h-4 w-4 text-green-500" />
          </CardHeader>
          <CardContent>
            {metricsLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-green-500">{(metrics?.falsePositiveRate ?? 0) * 100}%</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Legitimate traffic flagged</p>
          </CardContent>
        </Card>

        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Detection Speed</CardTitle>
            <Zap className="h-4 w-4 text-yellow-500" />
          </CardHeader>
          <CardContent>
            {metricsLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-yellow-500">{metrics?.avgDetectionTimeMs.toFixed(1)}ms</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Avg time to formulate score</p>
          </CardContent>
        </Card>

        <Card className="bg-card">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Attacks Learned</CardTitle>
            <Database className="h-4 w-4 text-blue-500" />
          </CardHeader>
          <CardContent>
            {metricsLoading ? <Skeleton className="h-8 w-20" /> : (
              <div className="text-2xl font-bold text-blue-500">{metrics?.attacksLearnedFrom.toLocaleString()}</div>
            )}
            <p className="text-xs text-muted-foreground mt-1">Unique patterns ingested</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        <Card className="bg-card col-span-2">
          <CardHeader>
            <CardTitle>Autonomous Improvements</CardTitle>
            <CardDescription>Recent adjustments made to the mesh based on attacker behavior.</CardDescription>
          </CardHeader>
          <CardContent>
            {improvementsLoading ? (
              <div className="space-y-4">
                {Array(4).fill(0).map((_, i) => (
                  <div key={i} className="flex gap-4"><Skeleton className="h-10 w-10 rounded" /><div className="flex-1 space-y-2"><Skeleton className="h-4 w-full" /><Skeleton className="h-3 w-1/2" /></div></div>
                ))}
              </div>
            ) : (
              <div className="relative space-y-0 before:absolute before:inset-y-0 before:left-[19px] before:w-px before:bg-border pl-1">
                {improvements?.map((imp, idx) => (
                  <div key={imp.id} className="relative flex gap-4 pt-0 pb-6 group last:pb-0">
                    <div className="absolute left-[15px] top-1 w-[9px] h-[9px] rounded-full bg-background border-2 border-primary group-hover:bg-primary transition-colors" />
                    <div className="w-8 shrink-0 flex justify-end mt-0.5" />
                    <div className="flex-1 bg-background border border-border p-4 rounded-lg shadow-sm group-hover:border-primary/30 transition-colors">
                      <div className="flex items-center justify-between mb-2">
                        <div className="flex items-center gap-2">
                          <div className="p-1.5 rounded-md bg-muted">
                            {getImprovementIcon(imp.type)}
                          </div>
                          <span className="font-semibold text-sm uppercase tracking-wider text-muted-foreground">{imp.type.replace(/_/g, ' ')}</span>
                        </div>
                        <span className="text-xs text-muted-foreground font-mono">{format(new Date(imp.timestamp), "MMM d, HH:mm")}</span>
                      </div>
                      <p className="text-sm font-medium mb-2">{imp.description}</p>
                      <div className="flex items-center gap-4 mt-3 pt-3 border-t border-border/50 text-xs">
                        <div className="text-muted-foreground">
                          Triggered by: <span className="font-mono text-foreground bg-muted px-1 py-0.5 rounded">{imp.triggeredBy}</span>
                        </div>
                        <Badge variant="outline" className={`ml-auto font-mono ${
                          imp.impactScore > 8 ? 'text-green-500 border-green-500/30' : 'text-blue-500 border-blue-500/30'
                        }`}>
                          Impact: +{imp.impactScore}
                        </Badge>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </CardContent>
        </Card>

        <Card className="bg-card flex flex-col">
          <CardHeader>
            <CardTitle>Training Context</CardTitle>
            <CardDescription>Current memory parameters</CardDescription>
          </CardHeader>
          <CardContent className="flex-1 space-y-6">
            <div>
              <div className="text-sm text-muted-foreground mb-1">Last Model Update</div>
              <div className="font-medium text-lg">
                {metricsLoading ? <Skeleton className="h-6 w-32" /> : 
                  metrics?.lastTrainedAt ? format(new Date(metrics.lastTrainedAt), "MMM d, yyyy HH:mm") : 'Never'
                }
              </div>
            </div>
            
            <div className="space-y-3">
              <h4 className="text-sm font-semibold border-b border-border pb-1">Optimization Stats</h4>
              <div className="flex justify-between text-sm">
                <span className="text-muted-foreground">Total Training Events</span>
                <span className="font-mono">{metrics?.totalTrainingEvents}</span>
              </div>
              <div className="flex justify-between text-sm">
                <span className="text-muted-foreground">Canary Repositions</span>
                <span className="font-mono text-orange-500">{metrics?.canaryPlacementUpdates}</span>
              </div>
              <div className="flex justify-between text-sm">
                <span className="text-muted-foreground">Fake Data Iterations</span>
                <span className="font-mono text-blue-500">{metrics?.fakeDataImprovements}</span>
              </div>
            </div>

            <div className="p-4 bg-primary/10 border border-primary/20 rounded-lg mt-auto">
              <h4 className="flex items-center gap-2 text-primary font-medium text-sm mb-2">
                <Brain className="h-4 w-4" /> System is Learning
              </h4>
              <p className="text-xs text-muted-foreground leading-relaxed">
                SentinelMesh actively analyzes lateral movement within the honeypot to generate more convincing fake data and adjust behavioral thresholds.
              </p>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/pages/not-found.tsx
// ============================================================
import { Card, CardContent } from "@/components/ui/card";
import { AlertCircle } from "lucide-react";

export default function NotFound() {
  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-gray-50">
      <Card className="w-full max-w-md mx-4">
        <CardContent className="pt-6">
          <div className="flex mb-4 gap-2">
            <AlertCircle className="h-8 w-8 text-red-500" />
            <h1 className="text-2xl font-bold text-gray-900">404 Page Not Found</h1>
          </div>

          <p className="mt-4 text-sm text-gray-600">
            Did you forget to add the page to the router?
          </p>
        </CardContent>
      </Card>
    </div>
  );
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/accordion.tsx
// ============================================================
import * as React from "react"
import * as AccordionPrimitive from "@radix-ui/react-accordion"
import { ChevronDown } from "lucide-react"

import { cn } from "@/lib/utils"

const Accordion = AccordionPrimitive.Root

const AccordionItem = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Item>
>(({ className, ...props }, ref) => (
  <AccordionPrimitive.Item
    ref={ref}
    className={cn("border-b", className)}
    {...props}
  />
))
AccordionItem.displayName = "AccordionItem"

const AccordionTrigger = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <AccordionPrimitive.Header className="flex">
    <AccordionPrimitive.Trigger
      ref={ref}
      className={cn(
        "flex flex-1 items-center justify-between py-4 text-sm font-medium transition-all hover:underline text-left [&[data-state=open]>svg]:rotate-180",
        className
      )}
      {...props}
    >
      {children}
      <ChevronDown className="h-4 w-4 shrink-0 text-muted-foreground transition-transform duration-200" />
    </AccordionPrimitive.Trigger>
  </AccordionPrimitive.Header>
))
AccordionTrigger.displayName = AccordionPrimitive.Trigger.displayName

const AccordionContent = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <AccordionPrimitive.Content
    ref={ref}
    className="overflow-hidden text-sm data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down"
    {...props}
  >
    <div className={cn("pb-4 pt-0", className)}>{children}</div>
  </AccordionPrimitive.Content>
))
AccordionContent.displayName = AccordionPrimitive.Content.displayName

export { Accordion, AccordionItem, AccordionTrigger, AccordionContent }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/alert-dialog.tsx
// ============================================================
import * as React from "react"
import * as AlertDialogPrimitive from "@radix-ui/react-alert-dialog"

import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"

const AlertDialog = AlertDialogPrimitive.Root

const AlertDialogTrigger = AlertDialogPrimitive.Trigger

const AlertDialogPortal = AlertDialogPrimitive.Portal

const AlertDialogOverlay = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Overlay
    className={cn(
      "fixed inset-0 z-50 bg-black/80 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
    ref={ref}
  />
))
AlertDialogOverlay.displayName = AlertDialogPrimitive.Overlay.displayName

const AlertDialogContent = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Content>
>(({ className, ...props }, ref) => (
  <AlertDialogPortal>
    <AlertDialogOverlay />
    <AlertDialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg",
        className
      )}
      {...props}
    />
  </AlertDialogPortal>
))
AlertDialogContent.displayName = AlertDialogPrimitive.Content.displayName

const AlertDialogHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-2 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
AlertDialogHeader.displayName = "AlertDialogHeader"

const AlertDialogFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
AlertDialogFooter.displayName = "AlertDialogFooter"

const AlertDialogTitle = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Title
    ref={ref}
    className={cn("text-lg font-semibold", className)}
    {...props}
  />
))
AlertDialogTitle.displayName = AlertDialogPrimitive.Title.displayName

const AlertDialogDescription = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Description>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
AlertDialogDescription.displayName =
  AlertDialogPrimitive.Description.displayName

const AlertDialogAction = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Action>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Action>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Action
    ref={ref}
    className={cn(buttonVariants(), className)}
    {...props}
  />
))
AlertDialogAction.displayName = AlertDialogPrimitive.Action.displayName

const AlertDialogCancel = React.forwardRef<
  React.ElementRef<typeof AlertDialogPrimitive.Cancel>,
  React.ComponentPropsWithoutRef<typeof AlertDialogPrimitive.Cancel>
>(({ className, ...props }, ref) => (
  <AlertDialogPrimitive.Cancel
    ref={ref}
    className={cn(
      buttonVariants({ variant: "outline" }),
      "mt-2 sm:mt-0",
      className
    )}
    {...props}
  />
))
AlertDialogCancel.displayName = AlertDialogPrimitive.Cancel.displayName

export {
  AlertDialog,
  AlertDialogPortal,
  AlertDialogOverlay,
  AlertDialogTrigger,
  AlertDialogContent,
  AlertDialogHeader,
  AlertDialogFooter,
  AlertDialogTitle,
  AlertDialogDescription,
  AlertDialogAction,
  AlertDialogCancel,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/alert.tsx
// ============================================================
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const alertVariants = cva(
  "relative w-full rounded-lg border px-4 py-3 text-sm [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4 [&>svg]:text-foreground [&>svg~*]:pl-7",
  {
    variants: {
      variant: {
        default: "bg-background text-foreground",
        destructive:
          "border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

const Alert = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & VariantProps<typeof alertVariants>
>(({ className, variant, ...props }, ref) => (
  <div
    ref={ref}
    role="alert"
    className={cn(alertVariants({ variant }), className)}
    {...props}
  />
))
Alert.displayName = "Alert"

const AlertTitle = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
  <h5
    ref={ref}
    className={cn("mb-1 font-medium leading-none tracking-tight", className)}
    {...props}
  />
))
AlertTitle.displayName = "AlertTitle"

const AlertDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm [&_p]:leading-relaxed", className)}
    {...props}
  />
))
AlertDescription.displayName = "AlertDescription"

export { Alert, AlertTitle, AlertDescription }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/aspect-ratio.tsx
// ============================================================
import * as AspectRatioPrimitive from "@radix-ui/react-aspect-ratio"

const AspectRatio = AspectRatioPrimitive.Root

export { AspectRatio }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/avatar.tsx
// ============================================================
"use client"

import * as React from "react"
import * as AvatarPrimitive from "@radix-ui/react-avatar"

import { cn } from "@/lib/utils"

const Avatar = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Root>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Root
    ref={ref}
    className={cn(
      "relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full",
      className
    )}
    {...props}
  />
))
Avatar.displayName = AvatarPrimitive.Root.displayName

const AvatarImage = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Image>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Image>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Image
    ref={ref}
    className={cn("aspect-square h-full w-full", className)}
    {...props}
  />
))
AvatarImage.displayName = AvatarPrimitive.Image.displayName

const AvatarFallback = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Fallback>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Fallback>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Fallback
    ref={ref}
    className={cn(
      "flex h-full w-full items-center justify-center rounded-full bg-muted",
      className
    )}
    {...props}
  />
))
AvatarFallback.displayName = AvatarPrimitive.Fallback.displayName

export { Avatar, AvatarImage, AvatarFallback }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/badge.tsx
// ============================================================
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const badgeVariants = cva(
  // @replit
  // Whitespace-nowrap: Badges should never wrap.
  "whitespace-nowrap inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2" +
  " hover-elevate ",
  {
    variants: {
      variant: {
        default:
          // @replit shadow-xs instead of shadow, no hover because we use hover-elevate
          "border-transparent bg-primary text-primary-foreground shadow-xs",
        secondary:
          // @replit no hover because we use hover-elevate
          "border-transparent bg-secondary text-secondary-foreground",
        destructive:
          // @replit shadow-xs instead of shadow, no hover because we use hover-elevate
          "border-transparent bg-destructive text-destructive-foreground shadow-xs",
          // @replit shadow-xs" - use badge outline variable
        outline: "text-foreground border [border-color:var(--badge-outline)]",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  )
}

export { Badge, badgeVariants }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/breadcrumb.tsx
// ============================================================
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { ChevronRight, MoreHorizontal } from "lucide-react"

import { cn } from "@/lib/utils"

const Breadcrumb = React.forwardRef<
  HTMLElement,
  React.ComponentPropsWithoutRef<"nav"> & {
    separator?: React.ReactNode
  }
>(({ ...props }, ref) => <nav ref={ref} aria-label="breadcrumb" {...props} />)
Breadcrumb.displayName = "Breadcrumb"

const BreadcrumbList = React.forwardRef<
  HTMLOListElement,
  React.ComponentPropsWithoutRef<"ol">
>(({ className, ...props }, ref) => (
  <ol
    ref={ref}
    className={cn(
      "flex flex-wrap items-center gap-1.5 break-words text-sm text-muted-foreground sm:gap-2.5",
      className
    )}
    {...props}
  />
))
BreadcrumbList.displayName = "BreadcrumbList"

const BreadcrumbItem = React.forwardRef<
  HTMLLIElement,
  React.ComponentPropsWithoutRef<"li">
>(({ className, ...props }, ref) => (
  <li
    ref={ref}
    className={cn("inline-flex items-center gap-1.5", className)}
    {...props}
  />
))
BreadcrumbItem.displayName = "BreadcrumbItem"

const BreadcrumbLink = React.forwardRef<
  HTMLAnchorElement,
  React.ComponentPropsWithoutRef<"a"> & {
    asChild?: boolean
  }
>(({ asChild, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "a"

  return (
    <Comp
      ref={ref}
      className={cn("transition-colors hover:text-foreground", className)}
      {...props}
    />
  )
})
BreadcrumbLink.displayName = "BreadcrumbLink"

const BreadcrumbPage = React.forwardRef<
  HTMLSpanElement,
  React.ComponentPropsWithoutRef<"span">
>(({ className, ...props }, ref) => (
  <span
    ref={ref}
    role="link"
    aria-disabled="true"
    aria-current="page"
    className={cn("font-normal text-foreground", className)}
    {...props}
  />
))
BreadcrumbPage.displayName = "BreadcrumbPage"

const BreadcrumbSeparator = ({
  children,
  className,
  ...props
}: React.ComponentProps<"li">) => (
  <li
    role="presentation"
    aria-hidden="true"
    className={cn("[&>svg]:w-3.5 [&>svg]:h-3.5", className)}
    {...props}
  >
    {children ?? <ChevronRight />}
  </li>
)
BreadcrumbSeparator.displayName = "BreadcrumbSeparator"

const BreadcrumbEllipsis = ({
  className,
  ...props
}: React.ComponentProps<"span">) => (
  <span
    role="presentation"
    aria-hidden="true"
    className={cn("flex h-9 w-9 items-center justify-center", className)}
    {...props}
  >
    <MoreHorizontal className="h-4 w-4" />
    <span className="sr-only">More</span>
  </span>
)
BreadcrumbEllipsis.displayName = "BreadcrumbElipssis"

export {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
  BreadcrumbEllipsis,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/button-group.tsx
// ============================================================
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"
import { Separator } from "@/components/ui/separator"

const buttonGroupVariants = cva(
  "flex w-fit items-stretch has-[>[data-slot=button-group]]:gap-2 [&>*]:focus-visible:relative [&>*]:focus-visible:z-10 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-md [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1",
  {
    variants: {
      orientation: {
        horizontal:
          "[&>*:not(:first-child)]:rounded-l-none [&>*:not(:first-child)]:border-l-0 [&>*:not(:last-child)]:rounded-r-none",
        vertical:
          "flex-col [&>*:not(:first-child)]:rounded-t-none [&>*:not(:first-child)]:border-t-0 [&>*:not(:last-child)]:rounded-b-none",
      },
    },
    defaultVariants: {
      orientation: "horizontal",
    },
  }
)

function ButtonGroup({
  className,
  orientation,
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof buttonGroupVariants>) {
  return (
    <div
      role="group"
      data-slot="button-group"
      data-orientation={orientation}
      className={cn(buttonGroupVariants({ orientation }), className)}
      {...props}
    />
  )
}

function ButtonGroupText({
  className,
  asChild = false,
  ...props
}: React.ComponentProps<"div"> & {
  asChild?: boolean
}) {
  const Comp = asChild ? Slot : "div"

  return (
    <Comp
      className={cn(
        "bg-muted shadow-xs flex items-center gap-2 rounded-md border px-4 text-sm font-medium [&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none",
        className
      )}
      {...props}
    />
  )
}

function ButtonGroupSeparator({
  className,
  orientation = "vertical",
  ...props
}: React.ComponentProps<typeof Separator>) {
  return (
    <Separator
      data-slot="button-group-separator"
      orientation={orientation}
      className={cn(
        "bg-input relative !m-0 self-stretch data-[orientation=vertical]:h-auto",
        className
      )}
      {...props}
    />
  )
}

export {
  ButtonGroup,
  ButtonGroupSeparator,
  ButtonGroupText,
  buttonGroupVariants,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/button.tsx
// ============================================================
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0" +
" hover-elevate active-elevate-2",
  {
    variants: {
      variant: {
        default:
           // @replit: no hover, and add primary border
           "bg-primary text-primary-foreground border border-primary-border",
        destructive:
          "bg-destructive text-destructive-foreground shadow-sm border-destructive-border",
        outline:
          // @replit Shows the background color of whatever card / sidebar / accent background it is inside of.
          // Inherits the current text color. Uses shadow-xs. no shadow on active
          // No hover state
          " border [border-color:var(--button-outline)] shadow-xs active:shadow-none ",
        secondary:
          // @replit border, no hover, no shadow, secondary border.
          "border bg-secondary text-secondary-foreground border border-secondary-border ",
        // @replit no hover, transparent border
        ghost: "border border-transparent",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        // @replit changed sizes
        default: "min-h-9 px-4 py-2",
        sm: "min-h-8 rounded-md px-3 text-xs",
        lg: "min-h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/calendar.tsx
// ============================================================
"use client"

import * as React from "react"
import {
  ChevronDownIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
} from "lucide-react"
import { DayButton, DayPicker, getDefaultClassNames } from "react-day-picker"

import { cn } from "@/lib/utils"
import { Button, buttonVariants } from "@/components/ui/button"

function Calendar({
  className,
  classNames,
  showOutsideDays = true,
  captionLayout = "label",
  buttonVariant = "ghost",
  formatters,
  components,
  ...props
}: React.ComponentProps<typeof DayPicker> & {
  buttonVariant?: React.ComponentProps<typeof Button>["variant"]
}) {
  const defaultClassNames = getDefaultClassNames()

  return (
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn(
        "bg-background group/calendar p-3 [--cell-size:2rem] [[data-slot=card-content]_&]:bg-transparent [[data-slot=popover-content]_&]:bg-transparent",
        String.raw`rtl:**:[.rdp-button\_next>svg]:rotate-180`,
        String.raw`rtl:**:[.rdp-button\_previous>svg]:rotate-180`,
        className
      )}
      captionLayout={captionLayout}
      formatters={{
        formatMonthDropdown: (date) =>
          date.toLocaleString("default", { month: "short" }),
        ...formatters,
      }}
      classNames={{
        root: cn("w-fit", defaultClassNames.root),
        months: cn(
          "relative flex flex-col gap-4 md:flex-row",
          defaultClassNames.months
        ),
        month: cn("flex w-full flex-col gap-4", defaultClassNames.month),
        nav: cn(
          "absolute inset-x-0 top-0 flex w-full items-center justify-between gap-1",
          defaultClassNames.nav
        ),
        button_previous: cn(
          buttonVariants({ variant: buttonVariant }),
          "h-[--cell-size] w-[--cell-size] select-none p-0 aria-disabled:opacity-50",
          defaultClassNames.button_previous
        ),
        button_next: cn(
          buttonVariants({ variant: buttonVariant }),
          "h-[--cell-size] w-[--cell-size] select-none p-0 aria-disabled:opacity-50",
          defaultClassNames.button_next
        ),
        month_caption: cn(
          "flex h-[--cell-size] w-full items-center justify-center px-[--cell-size]",
          defaultClassNames.month_caption
        ),
        dropdowns: cn(
          "flex h-[--cell-size] w-full items-center justify-center gap-1.5 text-sm font-medium",
          defaultClassNames.dropdowns
        ),
        dropdown_root: cn(
          "has-focus:border-ring border-input shadow-xs has-focus:ring-ring/50 has-focus:ring-[3px] relative rounded-md border",
          defaultClassNames.dropdown_root
        ),
        dropdown: cn(
          "bg-popover absolute inset-0 opacity-0",
          defaultClassNames.dropdown
        ),
        caption_label: cn(
          "select-none font-medium",
          captionLayout === "label"
            ? "text-sm"
            : "[&>svg]:text-muted-foreground flex h-8 items-center gap-1 rounded-md pl-2 pr-1 text-sm [&>svg]:size-3.5",
          defaultClassNames.caption_label
        ),
        table: "w-full border-collapse",
        weekdays: cn("flex", defaultClassNames.weekdays),
        weekday: cn(
          "text-muted-foreground flex-1 select-none rounded-md text-[0.8rem] font-normal",
          defaultClassNames.weekday
        ),
        week: cn("mt-2 flex w-full", defaultClassNames.week),
        week_number_header: cn(
          "w-[--cell-size] select-none",
          defaultClassNames.week_number_header
        ),
        week_number: cn(
          "text-muted-foreground select-none text-[0.8rem]",
          defaultClassNames.week_number
        ),
        day: cn(
          "group/day relative aspect-square h-full w-full select-none p-0 text-center [&:first-child[data-selected=true]_button]:rounded-l-md [&:last-child[data-selected=true]_button]:rounded-r-md",
          defaultClassNames.day
        ),
        range_start: cn(
          "bg-accent rounded-l-md",
          defaultClassNames.range_start
        ),
        range_middle: cn("rounded-none", defaultClassNames.range_middle),
        range_end: cn("bg-accent rounded-r-md", defaultClassNames.range_end),
        today: cn(
          "bg-accent text-accent-foreground rounded-md data-[selected=true]:rounded-none",
          defaultClassNames.today
        ),
        outside: cn(
          "text-muted-foreground aria-selected:text-muted-foreground",
          defaultClassNames.outside
        ),
        disabled: cn(
          "text-muted-foreground opacity-50",
          defaultClassNames.disabled
        ),
        hidden: cn("invisible", defaultClassNames.hidden),
        ...classNames,
      }}
      components={{
        Root: ({ className, rootRef, ...props }) => {
          return (
            <div
              data-slot="calendar"
              ref={rootRef}
              className={cn(className)}
              {...props}
            />
          )
        },
        Chevron: ({ className, orientation, ...props }) => {
          if (orientation === "left") {
            return (
              <ChevronLeftIcon className={cn("size-4", className)} {...props} />
            )
          }

          if (orientation === "right") {
            return (
              <ChevronRightIcon
                className={cn("size-4", className)}
                {...props}
              />
            )
          }

          return (
            <ChevronDownIcon className={cn("size-4", className)} {...props} />
          )
        },
        DayButton: CalendarDayButton,
        WeekNumber: ({ children, ...props }) => {
          return (
            <td {...props}>
              <div className="flex size-[--cell-size] items-center justify-center text-center">
                {children}
              </div>
            </td>
          )
        },
        ...components,
      }}
      {...props}
    />
  )
}

function CalendarDayButton({
  className,
  day,
  modifiers,
  ...props
}: React.ComponentProps<typeof DayButton>) {
  const defaultClassNames = getDefaultClassNames()

  const ref = React.useRef<HTMLButtonElement>(null)
  React.useEffect(() => {
    if (modifiers.focused) ref.current?.focus()
  }, [modifiers.focused])

  return (
    <Button
      ref={ref}
      variant="ghost"
      size="icon"
      data-day={day.date.toLocaleDateString()}
      data-selected-single={
        modifiers.selected &&
        !modifiers.range_start &&
        !modifiers.range_end &&
        !modifiers.range_middle
      }
      data-range-start={modifiers.range_start}
      data-range-end={modifiers.range_end}
      data-range-middle={modifiers.range_middle}
      className={cn(
        "data-[selected-single=true]:bg-primary data-[selected-single=true]:text-primary-foreground data-[range-middle=true]:bg-accent data-[range-middle=true]:text-accent-foreground data-[range-start=true]:bg-primary data-[range-start=true]:text-primary-foreground data-[range-end=true]:bg-primary data-[range-end=true]:text-primary-foreground group-data-[focused=true]/day:border-ring group-data-[focused=true]/day:ring-ring/50 flex aspect-square h-auto w-full min-w-[--cell-size] flex-col gap-1 font-normal leading-none data-[range-end=true]:rounded-md data-[range-middle=true]:rounded-none data-[range-start=true]:rounded-md group-data-[focused=true]/day:relative group-data-[focused=true]/day:z-10 group-data-[focused=true]/day:ring-[3px] [&>span]:text-xs [&>span]:opacity-70",
        defaultClassNames.day,
        className
      )}
      {...props}
    />
  )
}

export { Calendar, CalendarDayButton }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/card.tsx
// ============================================================
import * as React from "react"

import { cn } from "@/lib/utils"

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-xl border bg-card text-card-foreground shadow",
      className
    )}
    {...props}
  />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("font-semibold leading-none tracking-tight", className)}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex items-center p-6 pt-0", className)}
    {...props}
  />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/carousel.tsx
// ============================================================
import * as React from "react"
import useEmblaCarousel, {
  type UseEmblaCarouselType,
} from "embla-carousel-react"
import { ArrowLeft, ArrowRight } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"

type CarouselApi = UseEmblaCarouselType[1]
type UseCarouselParameters = Parameters<typeof useEmblaCarousel>
type CarouselOptions = UseCarouselParameters[0]
type CarouselPlugin = UseCarouselParameters[1]

type CarouselProps = {
  opts?: CarouselOptions
  plugins?: CarouselPlugin
  orientation?: "horizontal" | "vertical"
  setApi?: (api: CarouselApi) => void
}

type CarouselContextProps = {
  carouselRef: ReturnType<typeof useEmblaCarousel>[0]
  api: ReturnType<typeof useEmblaCarousel>[1]
  scrollPrev: () => void
  scrollNext: () => void
  canScrollPrev: boolean
  canScrollNext: boolean
} & CarouselProps

const CarouselContext = React.createContext<CarouselContextProps | null>(null)

function useCarousel() {
  const context = React.useContext(CarouselContext)

  if (!context) {
    throw new Error("useCarousel must be used within a <Carousel />")
  }

  return context
}

const Carousel = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & CarouselProps
>(
  (
    {
      orientation = "horizontal",
      opts,
      setApi,
      plugins,
      className,
      children,
      ...props
    },
    ref
  ) => {
    const [carouselRef, api] = useEmblaCarousel(
      {
        ...opts,
        axis: orientation === "horizontal" ? "x" : "y",
      },
      plugins
    )
    const [canScrollPrev, setCanScrollPrev] = React.useState(false)
    const [canScrollNext, setCanScrollNext] = React.useState(false)

    const onSelect = React.useCallback((api: CarouselApi) => {
      if (!api) {
        return
      }

      setCanScrollPrev(api.canScrollPrev())
      setCanScrollNext(api.canScrollNext())
    }, [])

    const scrollPrev = React.useCallback(() => {
      api?.scrollPrev()
    }, [api])

    const scrollNext = React.useCallback(() => {
      api?.scrollNext()
    }, [api])

    const handleKeyDown = React.useCallback(
      (event: React.KeyboardEvent<HTMLDivElement>) => {
        if (event.key === "ArrowLeft") {
          event.preventDefault()
          scrollPrev()
        } else if (event.key === "ArrowRight") {
          event.preventDefault()
          scrollNext()
        }
      },
      [scrollPrev, scrollNext]
    )

    React.useEffect(() => {
      if (!api || !setApi) {
        return
      }

      setApi(api)
    }, [api, setApi])

    React.useEffect(() => {
      if (!api) {
        return
      }

      onSelect(api)
      api.on("reInit", onSelect)
      api.on("select", onSelect)

      return () => {
        api?.off("select", onSelect)
      }
    }, [api, onSelect])

    return (
      <CarouselContext.Provider
        value={{
          carouselRef,
          api: api,
          opts,
          orientation:
            orientation || (opts?.axis === "y" ? "vertical" : "horizontal"),
          scrollPrev,
          scrollNext,
          canScrollPrev,
          canScrollNext,
        }}
      >
        <div
          ref={ref}
          onKeyDownCapture={handleKeyDown}
          className={cn("relative", className)}
          role="region"
          aria-roledescription="carousel"
          {...props}
        >
          {children}
        </div>
      </CarouselContext.Provider>
    )
  }
)
Carousel.displayName = "Carousel"

const CarouselContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => {
  const { carouselRef, orientation } = useCarousel()

  return (
    <div ref={carouselRef} className="overflow-hidden">
      <div
        ref={ref}
        className={cn(
          "flex",
          orientation === "horizontal" ? "-ml-4" : "-mt-4 flex-col",
          className
        )}
        {...props}
      />
    </div>
  )
})
CarouselContent.displayName = "CarouselContent"

const CarouselItem = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => {
  const { orientation } = useCarousel()

  return (
    <div
      ref={ref}
      role="group"
      aria-roledescription="slide"
      className={cn(
        "min-w-0 shrink-0 grow-0 basis-full",
        orientation === "horizontal" ? "pl-4" : "pt-4",
        className
      )}
      {...props}
    />
  )
})
CarouselItem.displayName = "CarouselItem"

const CarouselPrevious = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<typeof Button>
>(({ className, variant = "outline", size = "icon", ...props }, ref) => {
  const { orientation, scrollPrev, canScrollPrev } = useCarousel()

  return (
    <Button
      ref={ref}
      variant={variant}
      size={size}
      className={cn(
        "absolute  h-8 w-8 rounded-full",
        orientation === "horizontal"
          ? "-left-12 top-1/2 -translate-y-1/2"
          : "-top-12 left-1/2 -translate-x-1/2 rotate-90",
        className
      )}
      disabled={!canScrollPrev}
      onClick={scrollPrev}
      {...props}
    >
      <ArrowLeft className="h-4 w-4" />
      <span className="sr-only">Previous slide</span>
    </Button>
  )
})
CarouselPrevious.displayName = "CarouselPrevious"

const CarouselNext = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<typeof Button>
>(({ className, variant = "outline", size = "icon", ...props }, ref) => {
  const { orientation, scrollNext, canScrollNext } = useCarousel()

  return (
    <Button
      ref={ref}
      variant={variant}
      size={size}
      className={cn(
        "absolute h-8 w-8 rounded-full",
        orientation === "horizontal"
          ? "-right-12 top-1/2 -translate-y-1/2"
          : "-bottom-12 left-1/2 -translate-x-1/2 rotate-90",
        className
      )}
      disabled={!canScrollNext}
      onClick={scrollNext}
      {...props}
    >
      <ArrowRight className="h-4 w-4" />
      <span className="sr-only">Next slide</span>
    </Button>
  )
})
CarouselNext.displayName = "CarouselNext"

export {
  type CarouselApi,
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselPrevious,
  CarouselNext,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/chart.tsx
// ============================================================
import * as React from "react"
import * as RechartsPrimitive from "recharts"

import { cn } from "@/lib/utils"

// Format: { THEME_NAME: CSS_SELECTOR }
const THEMES = { light: "", dark: ".dark" } as const

export type ChartConfig = {
  [k in string]: {
    label?: React.ReactNode
    icon?: React.ComponentType
  } & (
    | { color?: string; theme?: never }
    | { color?: never; theme: Record<keyof typeof THEMES, string> }
  )
}

type ChartContextProps = {
  config: ChartConfig
}

const ChartContext = React.createContext<ChartContextProps | null>(null)

function useChart() {
  const context = React.useContext(ChartContext)

  if (!context) {
    throw new Error("useChart must be used within a <ChartContainer />")
  }

  return context
}

const ChartContainer = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    config: ChartConfig
    children: React.ComponentProps<
      typeof RechartsPrimitive.ResponsiveContainer
    >["children"]
  }
>(({ id, className, children, config, ...props }, ref) => {
  const uniqueId = React.useId()
  const chartId = `chart-${id || uniqueId.replace(/:/g, "")}`

  return (
    <ChartContext.Provider value={{ config }}>
      <div
        data-chart={chartId}
        ref={ref}
        className={cn(
          "flex aspect-video justify-center text-xs [&_.recharts-cartesian-axis-tick_text]:fill-muted-foreground [&_.recharts-cartesian-grid_line[stroke='#ccc']]:stroke-border/50 [&_.recharts-curve.recharts-tooltip-cursor]:stroke-border [&_.recharts-dot[stroke='#fff']]:stroke-transparent [&_.recharts-layer]:outline-none [&_.recharts-polar-grid_[stroke='#ccc']]:stroke-border [&_.recharts-radial-bar-background-sector]:fill-muted [&_.recharts-rectangle.recharts-tooltip-cursor]:fill-muted [&_.recharts-reference-line_[stroke='#ccc']]:stroke-border [&_.recharts-sector[stroke='#fff']]:stroke-transparent [&_.recharts-sector]:outline-none [&_.recharts-surface]:outline-none",
          className
        )}
        {...props}
      >
        <ChartStyle id={chartId} config={config} />
        <RechartsPrimitive.ResponsiveContainer>
          {children}
        </RechartsPrimitive.ResponsiveContainer>
      </div>
    </ChartContext.Provider>
  )
})
ChartContainer.displayName = "Chart"

const ChartStyle = ({ id, config }: { id: string; config: ChartConfig }) => {
  const colorConfig = Object.entries(config).filter(
    ([, config]) => config.theme || config.color
  )

  if (!colorConfig.length) {
    return null
  }

  return (
    <style
      dangerouslySetInnerHTML={{
        __html: Object.entries(THEMES)
          .map(
            ([theme, prefix]) => `
${prefix} [data-chart=${id}] {
${colorConfig
  .map(([key, itemConfig]) => {
    const color =
      itemConfig.theme?.[theme as keyof typeof itemConfig.theme] ||
      itemConfig.color
    return color ? `  --color-${key}: ${color};` : null
  })
  .join("\n")}
}
`
          )
          .join("\n"),
      }}
    />
  )
}

const ChartTooltip = RechartsPrimitive.Tooltip

const ChartTooltipContent = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<typeof RechartsPrimitive.Tooltip> &
    React.ComponentProps<"div"> & {
      hideLabel?: boolean
      hideIndicator?: boolean
      indicator?: "line" | "dot" | "dashed"
      nameKey?: string
      labelKey?: string
    }
>(
  (
    {
      active,
      payload,
      className,
      indicator = "dot",
      hideLabel = false,
      hideIndicator = false,
      label,
      labelFormatter,
      labelClassName,
      formatter,
      color,
      nameKey,
      labelKey,
    },
    ref
  ) => {
    const { config } = useChart()

    const tooltipLabel = React.useMemo(() => {
      if (hideLabel || !payload?.length) {
        return null
      }

      const [item] = payload
      const key = `${labelKey || item?.dataKey || item?.name || "value"}`
      const itemConfig = getPayloadConfigFromPayload(config, item, key)
      const value =
        !labelKey && typeof label === "string"
          ? config[label as keyof typeof config]?.label || label
          : itemConfig?.label

      if (labelFormatter) {
        return (
          <div className={cn("font-medium", labelClassName)}>
            {labelFormatter(value, payload)}
          </div>
        )
      }

      if (!value) {
        return null
      }

      return <div className={cn("font-medium", labelClassName)}>{value}</div>
    }, [
      label,
      labelFormatter,
      payload,
      hideLabel,
      labelClassName,
      config,
      labelKey,
    ])

    if (!active || !payload?.length) {
      return null
    }

    const nestLabel = payload.length === 1 && indicator !== "dot"

    return (
      <div
        ref={ref}
        className={cn(
          "grid min-w-[8rem] items-start gap-1.5 rounded-lg border border-border/50 bg-background px-2.5 py-1.5 text-xs shadow-xl",
          className
        )}
      >
        {!nestLabel ? tooltipLabel : null}
        <div className="grid gap-1.5">
          {payload
            .filter((item) => item.type !== "none")
            .map((item, index) => {
              const key = `${nameKey || item.name || item.dataKey || "value"}`
              const itemConfig = getPayloadConfigFromPayload(config, item, key)
              const indicatorColor = color || item.payload.fill || item.color

              return (
                <div
                  key={item.dataKey}
                  className={cn(
                    "flex w-full flex-wrap items-stretch gap-2 [&>svg]:h-2.5 [&>svg]:w-2.5 [&>svg]:text-muted-foreground",
                    indicator === "dot" && "items-center"
                  )}
                >
                  {formatter && item?.value !== undefined && item.name ? (
                    formatter(item.value, item.name, item, index, item.payload)
                  ) : (
                    <>
                      {itemConfig?.icon ? (
                        <itemConfig.icon />
                      ) : (
                        !hideIndicator && (
                          <div
                            className={cn(
                              "shrink-0 rounded-[2px] border-[--color-border] bg-[--color-bg]",
                              {
                                "h-2.5 w-2.5": indicator === "dot",
                                "w-1": indicator === "line",
                                "w-0 border-[1.5px] border-dashed bg-transparent":
                                  indicator === "dashed",
                                "my-0.5": nestLabel && indicator === "dashed",
                              }
                            )}
                            style={
                              {
                                "--color-bg": indicatorColor,
                                "--color-border": indicatorColor,
                              } as React.CSSProperties
                            }
                          />
                        )
                      )}
                      <div
                        className={cn(
                          "flex flex-1 justify-between leading-none",
                          nestLabel ? "items-end" : "items-center"
                        )}
                      >
                        <div className="grid gap-1.5">
                          {nestLabel ? tooltipLabel : null}
                          <span className="text-muted-foreground">
                            {itemConfig?.label || item.name}
                          </span>
                        </div>
                        {item.value && (
                          <span className="font-mono font-medium tabular-nums text-foreground">
                            {item.value.toLocaleString()}
                          </span>
                        )}
                      </div>
                    </>
                  )}
                </div>
              )
            })}
        </div>
      </div>
    )
  }
)
ChartTooltipContent.displayName = "ChartTooltip"

const ChartLegend = RechartsPrimitive.Legend

const ChartLegendContent = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> &
    Pick<RechartsPrimitive.LegendProps, "payload" | "verticalAlign"> & {
      hideIcon?: boolean
      nameKey?: string
    }
>(
  (
    { className, hideIcon = false, payload, verticalAlign = "bottom", nameKey },
    ref
  ) => {
    const { config } = useChart()

    if (!payload?.length) {
      return null
    }

    return (
      <div
        ref={ref}
        className={cn(
          "flex items-center justify-center gap-4",
          verticalAlign === "top" ? "pb-3" : "pt-3",
          className
        )}
      >
        {payload
          .filter((item) => item.type !== "none")
          .map((item) => {
            const key = `${nameKey || item.dataKey || "value"}`
            const itemConfig = getPayloadConfigFromPayload(config, item, key)

            return (
              <div
                key={item.value}
                className={cn(
                  "flex items-center gap-1.5 [&>svg]:h-3 [&>svg]:w-3 [&>svg]:text-muted-foreground"
                )}
              >
                {itemConfig?.icon && !hideIcon ? (
                  <itemConfig.icon />
                ) : (
                  <div
                    className="h-2 w-2 shrink-0 rounded-[2px]"
                    style={{
                      backgroundColor: item.color,
                    }}
                  />
                )}
                {itemConfig?.label}
              </div>
            )
          })}
      </div>
    )
  }
)
ChartLegendContent.displayName = "ChartLegend"

// Helper to extract item config from a payload.
function getPayloadConfigFromPayload(
  config: ChartConfig,
  payload: unknown,
  key: string
) {
  if (typeof payload !== "object" || payload === null) {
    return undefined
  }

  const payloadPayload =
    "payload" in payload &&
    typeof payload.payload === "object" &&
    payload.payload !== null
      ? payload.payload
      : undefined

  let configLabelKey: string = key

  if (
    key in payload &&
    typeof payload[key as keyof typeof payload] === "string"
  ) {
    configLabelKey = payload[key as keyof typeof payload] as string
  } else if (
    payloadPayload &&
    key in payloadPayload &&
    typeof payloadPayload[key as keyof typeof payloadPayload] === "string"
  ) {
    configLabelKey = payloadPayload[
      key as keyof typeof payloadPayload
    ] as string
  }

  return configLabelKey in config
    ? config[configLabelKey]
    : config[key as keyof typeof config]
}

export {
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
  ChartLegend,
  ChartLegendContent,
  ChartStyle,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/checkbox.tsx
// ============================================================
import * as React from "react"
import * as CheckboxPrimitive from "@radix-ui/react-checkbox"
import { Check } from "lucide-react"

import { cn } from "@/lib/utils"

const Checkbox = React.forwardRef<
  React.ElementRef<typeof CheckboxPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof CheckboxPrimitive.Root>
>(({ className, ...props }, ref) => (
  <CheckboxPrimitive.Root
    ref={ref}
    className={cn(
      "grid place-content-center peer h-4 w-4 shrink-0 rounded-sm border border-primary shadow focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground",
      className
    )}
    {...props}
  >
    <CheckboxPrimitive.Indicator
      className={cn("grid place-content-center text-current")}
    >
      <Check className="h-4 w-4" />
    </CheckboxPrimitive.Indicator>
  </CheckboxPrimitive.Root>
))
Checkbox.displayName = CheckboxPrimitive.Root.displayName

export { Checkbox }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/collapsible.tsx
// ============================================================
"use client"

import * as CollapsiblePrimitive from "@radix-ui/react-collapsible"

const Collapsible = CollapsiblePrimitive.Root

const CollapsibleTrigger = CollapsiblePrimitive.CollapsibleTrigger

const CollapsibleContent = CollapsiblePrimitive.CollapsibleContent

export { Collapsible, CollapsibleTrigger, CollapsibleContent }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/command.tsx
// ============================================================
"use client"

import * as React from "react"
import { type DialogProps } from "@radix-ui/react-dialog"
import { Command as CommandPrimitive } from "cmdk"
import { Search } from "lucide-react"

import { cn } from "@/lib/utils"
import { Dialog, DialogContent } from "@/components/ui/dialog"

const Command = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive>
>(({ className, ...props }, ref) => (
  <CommandPrimitive
    ref={ref}
    className={cn(
      "flex h-full w-full flex-col overflow-hidden rounded-md bg-popover text-popover-foreground",
      className
    )}
    {...props}
  />
))
Command.displayName = CommandPrimitive.displayName

const CommandDialog = ({ children, ...props }: DialogProps) => {
  return (
    <Dialog {...props}>
      <DialogContent className="overflow-hidden p-0">
        <Command className="[&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:font-medium [&_[cmdk-group-heading]]:text-muted-foreground [&_[cmdk-group]:not([hidden])_~[cmdk-group]]:pt-0 [&_[cmdk-group]]:px-2 [&_[cmdk-input-wrapper]_svg]:h-5 [&_[cmdk-input-wrapper]_svg]:w-5 [&_[cmdk-input]]:h-12 [&_[cmdk-item]]:px-2 [&_[cmdk-item]]:py-3 [&_[cmdk-item]_svg]:h-5 [&_[cmdk-item]_svg]:w-5">
          {children}
        </Command>
      </DialogContent>
    </Dialog>
  )
}

const CommandInput = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Input>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Input>
>(({ className, ...props }, ref) => (
  <div className="flex items-center border-b px-3" cmdk-input-wrapper="">
    <Search className="mr-2 h-4 w-4 shrink-0 opacity-50" />
    <CommandPrimitive.Input
      ref={ref}
      className={cn(
        "flex h-10 w-full rounded-md bg-transparent py-3 text-sm outline-none placeholder:text-muted-foreground disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    />
  </div>
))

CommandInput.displayName = CommandPrimitive.Input.displayName

const CommandList = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.List>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.List
    ref={ref}
    className={cn("max-h-[300px] overflow-y-auto overflow-x-hidden", className)}
    {...props}
  />
))

CommandList.displayName = CommandPrimitive.List.displayName

const CommandEmpty = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Empty>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Empty>
>((props, ref) => (
  <CommandPrimitive.Empty
    ref={ref}
    className="py-6 text-center text-sm"
    {...props}
  />
))

CommandEmpty.displayName = CommandPrimitive.Empty.displayName

const CommandGroup = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Group>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Group>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.Group
    ref={ref}
    className={cn(
      "overflow-hidden p-1 text-foreground [&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:py-1.5 [&_[cmdk-group-heading]]:text-xs [&_[cmdk-group-heading]]:font-medium [&_[cmdk-group-heading]]:text-muted-foreground",
      className
    )}
    {...props}
  />
))

CommandGroup.displayName = CommandPrimitive.Group.displayName

const CommandSeparator = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 h-px bg-border", className)}
    {...props}
  />
))
CommandSeparator.displayName = CommandPrimitive.Separator.displayName

const CommandItem = React.forwardRef<
  React.ElementRef<typeof CommandPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof CommandPrimitive.Item>
>(({ className, ...props }, ref) => (
  <CommandPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default gap-2 select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none data-[disabled=true]:pointer-events-none data-[selected=true]:bg-accent data-[selected=true]:text-accent-foreground data-[disabled=true]:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
      className
    )}
    {...props}
  />
))

CommandItem.displayName = CommandPrimitive.Item.displayName

const CommandShortcut = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) => {
  return (
    <span
      className={cn(
        "ml-auto text-xs tracking-widest text-muted-foreground",
        className
      )}
      {...props}
    />
  )
}
CommandShortcut.displayName = "CommandShortcut"

export {
  Command,
  CommandDialog,
  CommandInput,
  CommandList,
  CommandEmpty,
  CommandGroup,
  CommandItem,
  CommandShortcut,
  CommandSeparator,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/context-menu.tsx
// ============================================================
import * as React from "react"
import * as ContextMenuPrimitive from "@radix-ui/react-context-menu"
import { Check, ChevronRight, Circle } from "lucide-react"

import { cn } from "@/lib/utils"

const ContextMenu = ContextMenuPrimitive.Root

const ContextMenuTrigger = ContextMenuPrimitive.Trigger

const ContextMenuGroup = ContextMenuPrimitive.Group

const ContextMenuPortal = ContextMenuPrimitive.Portal

const ContextMenuSub = ContextMenuPrimitive.Sub

const ContextMenuRadioGroup = ContextMenuPrimitive.RadioGroup

const ContextMenuSubTrigger = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.SubTrigger> & {
    inset?: boolean
  }
>(({ className, inset, children, ...props }, ref) => (
  <ContextMenuPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground",
      inset && "pl-8",
      className
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto h-4 w-4" />
  </ContextMenuPrimitive.SubTrigger>
))
ContextMenuSubTrigger.displayName = ContextMenuPrimitive.SubTrigger.displayName

const ContextMenuSubContent = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <ContextMenuPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-lg data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-context-menu-content-transform-origin]",
      className
    )}
    {...props}
  />
))
ContextMenuSubContent.displayName = ContextMenuPrimitive.SubContent.displayName

const ContextMenuContent = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Content>
>(({ className, ...props }, ref) => (
  <ContextMenuPrimitive.Portal>
    <ContextMenuPrimitive.Content
      ref={ref}
      className={cn(
        "z-50 max-h-[--radix-context-menu-content-available-height] min-w-[8rem] overflow-y-auto overflow-x-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-context-menu-content-transform-origin]",
        className
      )}
      {...props}
    />
  </ContextMenuPrimitive.Portal>
))
ContextMenuContent.displayName = ContextMenuPrimitive.Content.displayName

const ContextMenuItem = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Item> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <ContextMenuPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
ContextMenuItem.displayName = ContextMenuPrimitive.Item.displayName

const ContextMenuCheckboxItem = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <ContextMenuPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <ContextMenuPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </ContextMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </ContextMenuPrimitive.CheckboxItem>
))
ContextMenuCheckboxItem.displayName =
  ContextMenuPrimitive.CheckboxItem.displayName

const ContextMenuRadioItem = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <ContextMenuPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <ContextMenuPrimitive.ItemIndicator>
        <Circle className="h-4 w-4 fill-current" />
      </ContextMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </ContextMenuPrimitive.RadioItem>
))
ContextMenuRadioItem.displayName = ContextMenuPrimitive.RadioItem.displayName

const ContextMenuLabel = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Label> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <ContextMenuPrimitive.Label
    ref={ref}
    className={cn(
      "px-2 py-1.5 text-sm font-semibold text-foreground",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
ContextMenuLabel.displayName = ContextMenuPrimitive.Label.displayName

const ContextMenuSeparator = React.forwardRef<
  React.ElementRef<typeof ContextMenuPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof ContextMenuPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <ContextMenuPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 my-1 h-px bg-border", className)}
    {...props}
  />
))
ContextMenuSeparator.displayName = ContextMenuPrimitive.Separator.displayName

const ContextMenuShortcut = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) => {
  return (
    <span
      className={cn(
        "ml-auto text-xs tracking-widest text-muted-foreground",
        className
      )}
      {...props}
    />
  )
}
ContextMenuShortcut.displayName = "ContextMenuShortcut"

export {
  ContextMenu,
  ContextMenuTrigger,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuCheckboxItem,
  ContextMenuRadioItem,
  ContextMenuLabel,
  ContextMenuSeparator,
  ContextMenuShortcut,
  ContextMenuGroup,
  ContextMenuPortal,
  ContextMenuSub,
  ContextMenuSubContent,
  ContextMenuSubTrigger,
  ContextMenuRadioGroup,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/dialog.tsx
// ============================================================
import * as React from "react"
import * as DialogPrimitive from "@radix-ui/react-dialog"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const Dialog = DialogPrimitive.Root

const DialogTrigger = DialogPrimitive.Trigger

const DialogPortal = DialogPrimitive.Portal

const DialogClose = DialogPrimitive.Close

const DialogOverlay = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Overlay
    ref={ref}
    className={cn(
      "fixed inset-0 z-50 bg-black/80  data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
  />
))
DialogOverlay.displayName = DialogPrimitive.Overlay.displayName

const DialogContent = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPortal>
    <DialogOverlay />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg",
        className
      )}
      {...props}
    >
      {children}
      <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </DialogPrimitive.Close>
    </DialogPrimitive.Content>
  </DialogPortal>
))
DialogContent.displayName = DialogPrimitive.Content.displayName

const DialogHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-1.5 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
DialogHeader.displayName = "DialogHeader"

const DialogFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
DialogFooter.displayName = "DialogFooter"

const DialogTitle = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Title
    ref={ref}
    className={cn(
      "text-lg font-semibold leading-none tracking-tight",
      className
    )}
    {...props}
  />
))
DialogTitle.displayName = DialogPrimitive.Title.displayName

const DialogDescription = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Description>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
DialogDescription.displayName = DialogPrimitive.Description.displayName

export {
  Dialog,
  DialogPortal,
  DialogOverlay,
  DialogTrigger,
  DialogClose,
  DialogContent,
  DialogHeader,
  DialogFooter,
  DialogTitle,
  DialogDescription,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/drawer.tsx
// ============================================================
import * as React from "react"
import { Drawer as DrawerPrimitive } from "vaul"

import { cn } from "@/lib/utils"

const Drawer = ({
  shouldScaleBackground = true,
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Root>) => (
  <DrawerPrimitive.Root
    shouldScaleBackground={shouldScaleBackground}
    {...props}
  />
)
Drawer.displayName = "Drawer"

const DrawerTrigger = DrawerPrimitive.Trigger

const DrawerPortal = DrawerPrimitive.Portal

const DrawerClose = DrawerPrimitive.Close

const DrawerOverlay = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DrawerPrimitive.Overlay
    ref={ref}
    className={cn("fixed inset-0 z-50 bg-black/80", className)}
    {...props}
  />
))
DrawerOverlay.displayName = DrawerPrimitive.Overlay.displayName

const DrawerContent = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DrawerPortal>
    <DrawerOverlay />
    <DrawerPrimitive.Content
      ref={ref}
      className={cn(
        "fixed inset-x-0 bottom-0 z-50 mt-24 flex h-auto flex-col rounded-t-[10px] border bg-background",
        className
      )}
      {...props}
    >
      <div className="mx-auto mt-4 h-2 w-[100px] rounded-full bg-muted" />
      {children}
    </DrawerPrimitive.Content>
  </DrawerPortal>
))
DrawerContent.displayName = "DrawerContent"

const DrawerHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn("grid gap-1.5 p-4 text-center sm:text-left", className)}
    {...props}
  />
)
DrawerHeader.displayName = "DrawerHeader"

const DrawerFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn("mt-auto flex flex-col gap-2 p-4", className)}
    {...props}
  />
)
DrawerFooter.displayName = "DrawerFooter"

const DrawerTitle = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DrawerPrimitive.Title
    ref={ref}
    className={cn(
      "text-lg font-semibold leading-none tracking-tight",
      className
    )}
    {...props}
  />
))
DrawerTitle.displayName = DrawerPrimitive.Title.displayName

const DrawerDescription = React.forwardRef<
  React.ElementRef<typeof DrawerPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof DrawerPrimitive.Description>
>(({ className, ...props }, ref) => (
  <DrawerPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
DrawerDescription.displayName = DrawerPrimitive.Description.displayName

export {
  Drawer,
  DrawerPortal,
  DrawerOverlay,
  DrawerTrigger,
  DrawerClose,
  DrawerContent,
  DrawerHeader,
  DrawerFooter,
  DrawerTitle,
  DrawerDescription,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/dropdown-menu.tsx
// ============================================================
"use client"

import * as React from "react"
import * as DropdownMenuPrimitive from "@radix-ui/react-dropdown-menu"
import { Check, ChevronRight, Circle } from "lucide-react"

import { cn } from "@/lib/utils"

const DropdownMenu = DropdownMenuPrimitive.Root

const DropdownMenuTrigger = DropdownMenuPrimitive.Trigger

const DropdownMenuGroup = DropdownMenuPrimitive.Group

const DropdownMenuPortal = DropdownMenuPrimitive.Portal

const DropdownMenuSub = DropdownMenuPrimitive.Sub

const DropdownMenuRadioGroup = DropdownMenuPrimitive.RadioGroup

const DropdownMenuSubTrigger = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubTrigger> & {
    inset?: boolean
  }
>(({ className, inset, children, ...props }, ref) => (
  <DropdownMenuPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent data-[state=open]:bg-accent [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
      inset && "pl-8",
      className
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto" />
  </DropdownMenuPrimitive.SubTrigger>
))
DropdownMenuSubTrigger.displayName =
  DropdownMenuPrimitive.SubTrigger.displayName

const DropdownMenuSubContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-lg data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-dropdown-menu-content-transform-origin]",
      className
    )}
    {...props}
  />
))
DropdownMenuSubContent.displayName =
  DropdownMenuPrimitive.SubContent.displayName

const DropdownMenuContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <DropdownMenuPrimitive.Portal>
    <DropdownMenuPrimitive.Content
      ref={ref}
      sideOffset={sideOffset}
      className={cn(
        "z-50 max-h-[var(--radix-dropdown-menu-content-available-height)] min-w-[8rem] overflow-y-auto overflow-x-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md",
        "data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-dropdown-menu-content-transform-origin]",
        className
      )}
      {...props}
    />
  </DropdownMenuPrimitive.Portal>
))
DropdownMenuContent.displayName = DropdownMenuPrimitive.Content.displayName

const DropdownMenuItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Item> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&>svg]:size-4 [&>svg]:shrink-0",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
DropdownMenuItem.displayName = DropdownMenuPrimitive.Item.displayName

const DropdownMenuCheckboxItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <DropdownMenuPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.CheckboxItem>
))
DropdownMenuCheckboxItem.displayName =
  DropdownMenuPrimitive.CheckboxItem.displayName

const DropdownMenuRadioItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <DropdownMenuPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Circle className="h-2 w-2 fill-current" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.RadioItem>
))
DropdownMenuRadioItem.displayName = DropdownMenuPrimitive.RadioItem.displayName

const DropdownMenuLabel = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Label> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Label
    ref={ref}
    className={cn(
      "px-2 py-1.5 text-sm font-semibold",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
DropdownMenuLabel.displayName = DropdownMenuPrimitive.Label.displayName

const DropdownMenuSeparator = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 my-1 h-px bg-muted", className)}
    {...props}
  />
))
DropdownMenuSeparator.displayName = DropdownMenuPrimitive.Separator.displayName

const DropdownMenuShortcut = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) => {
  return (
    <span
      className={cn("ml-auto text-xs tracking-widest opacity-60", className)}
      {...props}
    />
  )
}
DropdownMenuShortcut.displayName = "DropdownMenuShortcut"

export {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuCheckboxItem,
  DropdownMenuRadioItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuGroup,
  DropdownMenuPortal,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuRadioGroup,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/empty.tsx
// ============================================================
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

function Empty({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="empty"
      className={cn(
        "flex min-w-0 flex-1 flex-col items-center justify-center gap-6 text-balance rounded-lg border-dashed p-6 text-center md:p-12",
        className
      )}
      {...props}
    />
  )
}

function EmptyHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="empty-header"
      className={cn(
        "flex max-w-sm flex-col items-center gap-2 text-center",
        className
      )}
      {...props}
    />
  )
}

const emptyMediaVariants = cva(
  "mb-2 flex shrink-0 items-center justify-center [&_svg]:pointer-events-none [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        icon: "bg-muted text-foreground flex size-10 shrink-0 items-center justify-center rounded-lg [&_svg:not([class*='size-'])]:size-6",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

function EmptyMedia({
  className,
  variant = "default",
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof emptyMediaVariants>) {
  return (
    <div
      data-slot="empty-icon"
      data-variant={variant}
      className={cn(emptyMediaVariants({ variant, className }))}
      {...props}
    />
  )
}

function EmptyTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="empty-title"
      className={cn("text-lg font-medium tracking-tight", className)}
      {...props}
    />
  )
}

function EmptyDescription({ className, ...props }: React.ComponentProps<"p">) {
  return (
    <div
      data-slot="empty-description"
      className={cn(
        "text-muted-foreground [&>a:hover]:text-primary text-sm/relaxed [&>a]:underline [&>a]:underline-offset-4",
        className
      )}
      {...props}
    />
  )
}

function EmptyContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="empty-content"
      className={cn(
        "flex w-full min-w-0 max-w-sm flex-col items-center gap-4 text-balance text-sm",
        className
      )}
      {...props}
    />
  )
}

export {
  Empty,
  EmptyHeader,
  EmptyTitle,
  EmptyDescription,
  EmptyContent,
  EmptyMedia,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/field.tsx
// ============================================================
"use client"

import { useMemo } from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"
import { Label } from "@/components/ui/label"
import { Separator } from "@/components/ui/separator"

function FieldSet({ className, ...props }: React.ComponentProps<"fieldset">) {
  return (
    <fieldset
      data-slot="field-set"
      className={cn(
        "flex flex-col gap-6",
        "has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3",
        className
      )}
      {...props}
    />
  )
}

function FieldLegend({
  className,
  variant = "legend",
  ...props
}: React.ComponentProps<"legend"> & { variant?: "legend" | "label" }) {
  return (
    <legend
      data-slot="field-legend"
      data-variant={variant}
      className={cn(
        "mb-3 font-medium",
        "data-[variant=legend]:text-base",
        "data-[variant=label]:text-sm",
        className
      )}
      {...props}
    />
  )
}

function FieldGroup({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="field-group"
      className={cn(
        "group/field-group @container/field-group flex w-full flex-col gap-7 data-[slot=checkbox-group]:gap-3 [&>[data-slot=field-group]]:gap-4",
        className
      )}
      {...props}
    />
  )
}

const fieldVariants = cva(
  "group/field data-[invalid=true]:text-destructive flex w-full gap-3",
  {
    variants: {
      orientation: {
        vertical: ["flex-col [&>*]:w-full [&>.sr-only]:w-auto"],
        horizontal: [
          "flex-row items-center",
          "[&>[data-slot=field-label]]:flex-auto",
          "has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px has-[>[data-slot=field-content]]:items-start",
        ],
        responsive: [
          "@md/field-group:flex-row @md/field-group:items-center @md/field-group:[&>*]:w-auto flex-col [&>*]:w-full [&>.sr-only]:w-auto",
          "@md/field-group:[&>[data-slot=field-label]]:flex-auto",
          "@md/field-group:has-[>[data-slot=field-content]]:items-start @md/field-group:has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px",
        ],
      },
    },
    defaultVariants: {
      orientation: "vertical",
    },
  }
)

function Field({
  className,
  orientation = "vertical",
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof fieldVariants>) {
  return (
    <div
      role="group"
      data-slot="field"
      data-orientation={orientation}
      className={cn(fieldVariants({ orientation }), className)}
      {...props}
    />
  )
}

function FieldContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="field-content"
      className={cn(
        "group/field-content flex flex-1 flex-col gap-1.5 leading-snug",
        className
      )}
      {...props}
    />
  )
}

function FieldLabel({
  className,
  ...props
}: React.ComponentProps<typeof Label>) {
  return (
    <Label
      data-slot="field-label"
      className={cn(
        "group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50",
        "has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>[data-slot=field]]:p-4",
        "has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10",
        className
      )}
      {...props}
    />
  )
}

function FieldTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="field-label"
      className={cn(
        "flex w-fit items-center gap-2 text-sm font-medium leading-snug group-data-[disabled=true]/field:opacity-50",
        className
      )}
      {...props}
    />
  )
}

function FieldDescription({ className, ...props }: React.ComponentProps<"p">) {
  return (
    <p
      data-slot="field-description"
      className={cn(
        "text-muted-foreground text-sm font-normal leading-normal group-has-[[data-orientation=horizontal]]/field:text-balance",
        "nth-last-2:-mt-1 last:mt-0 [[data-variant=legend]+&]:-mt-1.5",
        "[&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4",
        className
      )}
      {...props}
    />
  )
}

function FieldSeparator({
  children,
  className,
  ...props
}: React.ComponentProps<"div"> & {
  children?: React.ReactNode
}) {
  return (
    <div
      data-slot="field-separator"
      data-content={!!children}
      className={cn(
        "relative -my-2 h-5 text-sm group-data-[variant=outline]/field-group:-mb-2",
        className
      )}
      {...props}
    >
      <Separator className="absolute inset-0 top-1/2" />
      {children && (
        <span
          className="bg-background text-muted-foreground relative mx-auto block w-fit px-2"
          data-slot="field-separator-content"
        >
          {children}
        </span>
      )}
    </div>
  )
}

function FieldError({
  className,
  children,
  errors,
  ...props
}: React.ComponentProps<"div"> & {
  errors?: Array<{ message?: string } | undefined>
}) {
  const content = useMemo(() => {
    if (children) {
      return children
    }

    if (!errors) {
      return null
    }

    if (errors?.length === 1 && errors[0]?.message) {
      return errors[0].message
    }

    return (
      <ul className="ml-4 flex list-disc flex-col gap-1">
        {errors.map(
          (error, index) =>
            error?.message && <li key={index}>{error.message}</li>
        )}
      </ul>
    )
  }, [children, errors])

  if (!content) {
    return null
  }

  return (
    <div
      role="alert"
      data-slot="field-error"
      className={cn("text-destructive text-sm font-normal", className)}
      {...props}
    >
      {content}
    </div>
  )
}

export {
  Field,
  FieldLabel,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLegend,
  FieldSeparator,
  FieldSet,
  FieldContent,
  FieldTitle,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/form.tsx
// ============================================================
import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"
import { Slot } from "@radix-ui/react-slot"
import {
  Controller,
  FormProvider,
  useFormContext,
  type ControllerProps,
  type FieldPath,
  type FieldValues,
} from "react-hook-form"

import { cn } from "@/lib/utils"
import { Label } from "@/components/ui/label"

const Form = FormProvider

type FormFieldContextValue<
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>
> = {
  name: TName
}

const FormFieldContext = React.createContext<FormFieldContextValue | null>(null)

const FormField = <
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>
>({
  ...props
}: ControllerProps<TFieldValues, TName>) => {
  return (
    <FormFieldContext.Provider value={{ name: props.name }}>
      <Controller {...props} />
    </FormFieldContext.Provider>
  )
}

const useFormField = () => {
  const fieldContext = React.useContext(FormFieldContext)
  const itemContext = React.useContext(FormItemContext)
  const { getFieldState, formState } = useFormContext()

  if (!fieldContext) {
    throw new Error("useFormField should be used within <FormField>")
  }

  if (!itemContext) {
    throw new Error("useFormField should be used within <FormItem>")
  }

  const fieldState = getFieldState(fieldContext.name, formState)

  const { id } = itemContext

  return {
    id,
    name: fieldContext.name,
    formItemId: `${id}-form-item`,
    formDescriptionId: `${id}-form-item-description`,
    formMessageId: `${id}-form-item-message`,
    ...fieldState,
  }
}

type FormItemContextValue = {
  id: string
}

const FormItemContext = React.createContext<FormItemContextValue | null>(null)

const FormItem = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => {
  const id = React.useId()

  return (
    <FormItemContext.Provider value={{ id }}>
      <div ref={ref} className={cn("space-y-2", className)} {...props} />
    </FormItemContext.Provider>
  )
})
FormItem.displayName = "FormItem"

const FormLabel = React.forwardRef<
  React.ElementRef<typeof LabelPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof LabelPrimitive.Root>
>(({ className, ...props }, ref) => {
  const { error, formItemId } = useFormField()

  return (
    <Label
      ref={ref}
      className={cn(error && "text-destructive", className)}
      htmlFor={formItemId}
      {...props}
    />
  )
})
FormLabel.displayName = "FormLabel"

const FormControl = React.forwardRef<
  React.ElementRef<typeof Slot>,
  React.ComponentPropsWithoutRef<typeof Slot>
>(({ ...props }, ref) => {
  const { error, formItemId, formDescriptionId, formMessageId } = useFormField()

  return (
    <Slot
      ref={ref}
      id={formItemId}
      aria-describedby={
        !error
          ? `${formDescriptionId}`
          : `${formDescriptionId} ${formMessageId}`
      }
      aria-invalid={!!error}
      {...props}
    />
  )
})
FormControl.displayName = "FormControl"

const FormDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => {
  const { formDescriptionId } = useFormField()

  return (
    <p
      ref={ref}
      id={formDescriptionId}
      className={cn("text-[0.8rem] text-muted-foreground", className)}
      {...props}
    />
  )
})
FormDescription.displayName = "FormDescription"

const FormMessage = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, children, ...props }, ref) => {
  const { error, formMessageId } = useFormField()
  const body = error ? String(error?.message ?? "") : children

  if (!body) {
    return null
  }

  return (
    <p
      ref={ref}
      id={formMessageId}
      className={cn("text-[0.8rem] font-medium text-destructive", className)}
      {...props}
    >
      {body}
    </p>
  )
})
FormMessage.displayName = "FormMessage"

export {
  useFormField,
  Form,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
  FormField,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/hover-card.tsx
// ============================================================
import * as React from "react"
import * as HoverCardPrimitive from "@radix-ui/react-hover-card"

import { cn } from "@/lib/utils"

const HoverCard = HoverCardPrimitive.Root

const HoverCardTrigger = HoverCardPrimitive.Trigger

const HoverCardContent = React.forwardRef<
  React.ElementRef<typeof HoverCardPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof HoverCardPrimitive.Content>
>(({ className, align = "center", sideOffset = 4, ...props }, ref) => (
  <HoverCardPrimitive.Content
    ref={ref}
    align={align}
    sideOffset={sideOffset}
    className={cn(
      "z-50 w-64 rounded-md border bg-popover p-4 text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-hover-card-content-transform-origin]",
      className
    )}
    {...props}
  />
))
HoverCardContent.displayName = HoverCardPrimitive.Content.displayName

export { HoverCard, HoverCardTrigger, HoverCardContent }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/input-group.tsx
// ============================================================
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"

function InputGroup({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="input-group"
      role="group"
      className={cn(
        "group/input-group border-input dark:bg-input/30 shadow-xs relative flex w-full items-center rounded-md border outline-none transition-[color,box-shadow]",
        "h-9 has-[>textarea]:h-auto",

        // Variants based on alignment.
        "has-[>[data-align=inline-start]]:[&>input]:pl-2",
        "has-[>[data-align=inline-end]]:[&>input]:pr-2",
        "has-[>[data-align=block-start]]:h-auto has-[>[data-align=block-start]]:flex-col has-[>[data-align=block-start]]:[&>input]:pb-3",
        "has-[>[data-align=block-end]]:h-auto has-[>[data-align=block-end]]:flex-col has-[>[data-align=block-end]]:[&>input]:pt-3",

        // Focus state.
        "has-[[data-slot=input-group-control]:focus-visible]:ring-ring has-[[data-slot=input-group-control]:focus-visible]:ring-1",

        // Error state.
        "has-[[data-slot][aria-invalid=true]]:ring-destructive/20 has-[[data-slot][aria-invalid=true]]:border-destructive dark:has-[[data-slot][aria-invalid=true]]:ring-destructive/40",

        className
      )}
      {...props}
    />
  )
}

const inputGroupAddonVariants = cva(
  "text-muted-foreground flex h-auto cursor-text select-none items-center justify-center gap-2 py-1.5 text-sm font-medium group-data-[disabled=true]/input-group:opacity-50 [&>kbd]:rounded-[calc(var(--radius)-5px)] [&>svg:not([class*='size-'])]:size-4",
  {
    variants: {
      align: {
        "inline-start":
          "order-first pl-3 has-[>button]:ml-[-0.45rem] has-[>kbd]:ml-[-0.35rem]",
        "inline-end":
          "order-last pr-3 has-[>button]:mr-[-0.4rem] has-[>kbd]:mr-[-0.35rem]",
        "block-start":
          "[.border-b]:pb-3 order-first w-full justify-start px-3 pt-3 group-has-[>input]/input-group:pt-2.5",
        "block-end":
          "[.border-t]:pt-3 order-last w-full justify-start px-3 pb-3 group-has-[>input]/input-group:pb-2.5",
      },
    },
    defaultVariants: {
      align: "inline-start",
    },
  }
)

function InputGroupAddon({
  className,
  align = "inline-start",
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof inputGroupAddonVariants>) {
  return (
    <div
      role="group"
      data-slot="input-group-addon"
      data-align={align}
      className={cn(inputGroupAddonVariants({ align }), className)}
      onClick={(e) => {
        if ((e.target as HTMLElement).closest("button")) {
          return
        }
        e.currentTarget.parentElement?.querySelector("input")?.focus()
      }}
      {...props}
    />
  )
}

const inputGroupButtonVariants = cva(
  "flex items-center gap-2 text-sm shadow-none",
  {
    variants: {
      size: {
        xs: "h-6 gap-1 rounded-[calc(var(--radius)-5px)] px-2 has-[>svg]:px-2 [&>svg:not([class*='size-'])]:size-3.5",
        sm: "h-8 gap-1.5 rounded-md px-2.5 has-[>svg]:px-2.5",
        "icon-xs":
          "size-6 rounded-[calc(var(--radius)-5px)] p-0 has-[>svg]:p-0",
        "icon-sm": "size-8 p-0 has-[>svg]:p-0",
      },
    },
    defaultVariants: {
      size: "xs",
    },
  }
)

function InputGroupButton({
  className,
  type = "button",
  variant = "ghost",
  size = "xs",
  ...props
}: Omit<React.ComponentProps<typeof Button>, "size"> &
  VariantProps<typeof inputGroupButtonVariants>) {
  return (
    <Button
      type={type}
      data-size={size}
      variant={variant}
      className={cn(inputGroupButtonVariants({ size }), className)}
      {...props}
    />
  )
}

function InputGroupText({ className, ...props }: React.ComponentProps<"span">) {
  return (
    <span
      className={cn(
        "text-muted-foreground flex items-center gap-2 text-sm [&_svg:not([class*='size-'])]:size-4 [&_svg]:pointer-events-none",
        className
      )}
      {...props}
    />
  )
}

function InputGroupInput({
  className,
  ...props
}: React.ComponentProps<"input">) {
  return (
    <Input
      data-slot="input-group-control"
      className={cn(
        "flex-1 rounded-none border-0 bg-transparent shadow-none focus-visible:ring-0 dark:bg-transparent",
        className
      )}
      {...props}
    />
  )
}

function InputGroupTextarea({
  className,
  ...props
}: React.ComponentProps<"textarea">) {
  return (
    <Textarea
      data-slot="input-group-control"
      className={cn(
        "flex-1 resize-none rounded-none border-0 bg-transparent py-3 shadow-none focus-visible:ring-0 dark:bg-transparent",
        className
      )}
      {...props}
    />
  )
}

export {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupText,
  InputGroupInput,
  InputGroupTextarea,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/input-otp.tsx
// ============================================================
import * as React from "react"
import { OTPInput, OTPInputContext } from "input-otp"
import { Minus } from "lucide-react"

import { cn } from "@/lib/utils"

const InputOTP = React.forwardRef<
  React.ElementRef<typeof OTPInput>,
  React.ComponentPropsWithoutRef<typeof OTPInput>
>(({ className, containerClassName, ...props }, ref) => (
  <OTPInput
    ref={ref}
    containerClassName={cn(
      "flex items-center gap-2 has-[:disabled]:opacity-50",
      containerClassName
    )}
    className={cn("disabled:cursor-not-allowed", className)}
    {...props}
  />
))
InputOTP.displayName = "InputOTP"

const InputOTPGroup = React.forwardRef<
  React.ElementRef<"div">,
  React.ComponentPropsWithoutRef<"div">
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("flex items-center", className)} {...props} />
))
InputOTPGroup.displayName = "InputOTPGroup"

const InputOTPSlot = React.forwardRef<
  React.ElementRef<"div">,
  React.ComponentPropsWithoutRef<"div"> & { index: number }
>(({ index, className, ...props }, ref) => {
  const inputOTPContext = React.useContext(OTPInputContext)
  const { char, hasFakeCaret, isActive } = inputOTPContext.slots[index]

  return (
    <div
      ref={ref}
      className={cn(
        "relative flex h-9 w-9 items-center justify-center border-y border-r border-input text-sm shadow-sm transition-all first:rounded-l-md first:border-l last:rounded-r-md",
        isActive && "z-10 ring-1 ring-ring",
        className
      )}
      {...props}
    >
      {char}
      {hasFakeCaret && (
        <div className="pointer-events-none absolute inset-0 flex items-center justify-center">
          <div className="h-4 w-px animate-caret-blink bg-foreground duration-1000" />
        </div>
      )}
    </div>
  )
})
InputOTPSlot.displayName = "InputOTPSlot"

const InputOTPSeparator = React.forwardRef<
  React.ElementRef<"div">,
  React.ComponentPropsWithoutRef<"div">
>(({ ...props }, ref) => (
  <div ref={ref} role="separator" {...props}>
    <Minus />
  </div>
))
InputOTPSeparator.displayName = "InputOTPSeparator"

export { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/input.tsx
// ============================================================
import * as React from "react"

import { cn } from "@/lib/utils"

const Input = React.forwardRef<HTMLInputElement, React.ComponentProps<"input">>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = "Input"

export { Input }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/item.tsx
// ============================================================
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"
import { Separator } from "@/components/ui/separator"

function ItemGroup({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      role="list"
      data-slot="item-group"
      className={cn("group/item-group flex flex-col", className)}
      {...props}
    />
  )
}

function ItemSeparator({
  className,
  ...props
}: React.ComponentProps<typeof Separator>) {
  return (
    <Separator
      data-slot="item-separator"
      orientation="horizontal"
      className={cn("my-0", className)}
      {...props}
    />
  )
}

const itemVariants = cva(
  "group/item [a]:hover:bg-accent/50 focus-visible:border-ring focus-visible:ring-ring/50 [a]:transition-colors flex flex-wrap items-center rounded-md border border-transparent text-sm outline-none transition-colors duration-100 focus-visible:ring-[3px]",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        outline: "border-border",
        muted: "bg-muted/50",
      },
      size: {
        default: "gap-4 p-4 ",
        sm: "gap-2.5 px-4 py-3",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Item({
  className,
  variant = "default",
  size = "default",
  asChild = false,
  ...props
}: React.ComponentProps<"div"> &
  VariantProps<typeof itemVariants> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "div"
  return (
    <Comp
      data-slot="item"
      data-variant={variant}
      data-size={size}
      className={cn(itemVariants({ variant, size, className }))}
      {...props}
    />
  )
}

const itemMediaVariants = cva(
  "flex shrink-0 items-center justify-center gap-2 group-has-[[data-slot=item-description]]/item:translate-y-0.5 group-has-[[data-slot=item-description]]/item:self-start [&_svg]:pointer-events-none",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        icon: "bg-muted size-8 rounded-sm border [&_svg:not([class*='size-'])]:size-4",
        image:
          "size-10 overflow-hidden rounded-sm [&_img]:size-full [&_img]:object-cover",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

function ItemMedia({
  className,
  variant = "default",
  ...props
}: React.ComponentProps<"div"> & VariantProps<typeof itemMediaVariants>) {
  return (
    <div
      data-slot="item-media"
      data-variant={variant}
      className={cn(itemMediaVariants({ variant, className }))}
      {...props}
    />
  )
}

function ItemContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="item-content"
      className={cn(
        "flex flex-1 flex-col gap-1 [&+[data-slot=item-content]]:flex-none",
        className
      )}
      {...props}
    />
  )
}

function ItemTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="item-title"
      className={cn(
        "flex w-fit items-center gap-2 text-sm font-medium leading-snug",
        className
      )}
      {...props}
    />
  )
}

function ItemDescription({ className, ...props }: React.ComponentProps<"p">) {
  return (
    <p
      data-slot="item-description"
      className={cn(
        "text-muted-foreground line-clamp-2 text-balance text-sm font-normal leading-normal",
        "[&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4",
        className
      )}
      {...props}
    />
  )
}

function ItemActions({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="item-actions"
      className={cn("flex items-center gap-2", className)}
      {...props}
    />
  )
}

function ItemHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="item-header"
      className={cn(
        "flex basis-full items-center justify-between gap-2",
        className
      )}
      {...props}
    />
  )
}

function ItemFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="item-footer"
      className={cn(
        "flex basis-full items-center justify-between gap-2",
        className
      )}
      {...props}
    />
  )
}

export {
  Item,
  ItemMedia,
  ItemContent,
  ItemActions,
  ItemGroup,
  ItemSeparator,
  ItemTitle,
  ItemDescription,
  ItemHeader,
  ItemFooter,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/kbd.tsx
// ============================================================
import { cn } from "@/lib/utils"

function Kbd({ className, ...props }: React.ComponentProps<"kbd">) {
  return (
    <kbd
      data-slot="kbd"
      className={cn(
        "bg-muted text-muted-foreground pointer-events-none inline-flex h-5 w-fit min-w-5 select-none items-center justify-center gap-1 rounded-sm px-1 font-sans text-xs font-medium",
        "[&_svg:not([class*='size-'])]:size-3",
        "[[data-slot=tooltip-content]_&]:bg-background/20 [[data-slot=tooltip-content]_&]:text-background dark:[[data-slot=tooltip-content]_&]:bg-background/10",
        className
      )}
      {...props}
    />
  )
}

function KbdGroup({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <kbd
      data-slot="kbd-group"
      className={cn("inline-flex items-center gap-1", className)}
      {...props}
    />
  )
}

export { Kbd, KbdGroup }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/label.tsx
// ============================================================
"use client"

import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const labelVariants = cva(
  "text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
)

const Label = React.forwardRef<
  React.ElementRef<typeof LabelPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof LabelPrimitive.Root> &
    VariantProps<typeof labelVariants>
>(({ className, ...props }, ref) => (
  <LabelPrimitive.Root
    ref={ref}
    className={cn(labelVariants(), className)}
    {...props}
  />
))
Label.displayName = LabelPrimitive.Root.displayName

export { Label }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/menubar.tsx
// ============================================================
import * as React from "react"
import * as MenubarPrimitive from "@radix-ui/react-menubar"
import { Check, ChevronRight, Circle } from "lucide-react"

import { cn } from "@/lib/utils"

function MenubarMenu({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Menu>) {
  return <MenubarPrimitive.Menu {...props} />
}

function MenubarGroup({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Group>) {
  return <MenubarPrimitive.Group {...props} />
}

function MenubarPortal({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Portal>) {
  return <MenubarPrimitive.Portal {...props} />
}

function MenubarRadioGroup({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.RadioGroup>) {
  return <MenubarPrimitive.RadioGroup {...props} />
}

function MenubarSub({
  ...props
}: React.ComponentProps<typeof MenubarPrimitive.Sub>) {
  return <MenubarPrimitive.Sub data-slot="menubar-sub" {...props} />
}

const Menubar = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Root>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.Root
    ref={ref}
    className={cn(
      "flex h-9 items-center space-x-1 rounded-md border bg-background p-1 shadow-sm",
      className
    )}
    {...props}
  />
))
Menubar.displayName = MenubarPrimitive.Root.displayName

const MenubarTrigger = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.Trigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-3 py-1 text-sm font-medium outline-none focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground",
      className
    )}
    {...props}
  />
))
MenubarTrigger.displayName = MenubarPrimitive.Trigger.displayName

const MenubarSubTrigger = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.SubTrigger> & {
    inset?: boolean
  }
>(({ className, inset, children, ...props }, ref) => (
  <MenubarPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground",
      inset && "pl-8",
      className
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto h-4 w-4" />
  </MenubarPrimitive.SubTrigger>
))
MenubarSubTrigger.displayName = MenubarPrimitive.SubTrigger.displayName

const MenubarSubContent = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-lg data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-menubar-content-transform-origin]",
      className
    )}
    {...props}
  />
))
MenubarSubContent.displayName = MenubarPrimitive.SubContent.displayName

const MenubarContent = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Content>
>(
  (
    { className, align = "start", alignOffset = -4, sideOffset = 8, ...props },
    ref
  ) => (
    <MenubarPrimitive.Portal>
      <MenubarPrimitive.Content
        ref={ref}
        align={align}
        alignOffset={alignOffset}
        sideOffset={sideOffset}
        className={cn(
          "z-50 min-w-[12rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-menubar-content-transform-origin]",
          className
        )}
        {...props}
      />
    </MenubarPrimitive.Portal>
  )
)
MenubarContent.displayName = MenubarPrimitive.Content.displayName

const MenubarItem = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Item> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <MenubarPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
MenubarItem.displayName = MenubarPrimitive.Item.displayName

const MenubarCheckboxItem = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <MenubarPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <MenubarPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </MenubarPrimitive.ItemIndicator>
    </span>
    {children}
  </MenubarPrimitive.CheckboxItem>
))
MenubarCheckboxItem.displayName = MenubarPrimitive.CheckboxItem.displayName

const MenubarRadioItem = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <MenubarPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <MenubarPrimitive.ItemIndicator>
        <Circle className="h-4 w-4 fill-current" />
      </MenubarPrimitive.ItemIndicator>
    </span>
    {children}
  </MenubarPrimitive.RadioItem>
))
MenubarRadioItem.displayName = MenubarPrimitive.RadioItem.displayName

const MenubarLabel = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Label> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <MenubarPrimitive.Label
    ref={ref}
    className={cn(
      "px-2 py-1.5 text-sm font-semibold",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
MenubarLabel.displayName = MenubarPrimitive.Label.displayName

const MenubarSeparator = React.forwardRef<
  React.ElementRef<typeof MenubarPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof MenubarPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <MenubarPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 my-1 h-px bg-muted", className)}
    {...props}
  />
))
MenubarSeparator.displayName = MenubarPrimitive.Separator.displayName

const MenubarShortcut = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) => {
  return (
    <span
      className={cn(
        "ml-auto text-xs tracking-widest text-muted-foreground",
        className
      )}
      {...props}
    />
  )
}
MenubarShortcut.displayname = "MenubarShortcut"

export {
  Menubar,
  MenubarMenu,
  MenubarTrigger,
  MenubarContent,
  MenubarItem,
  MenubarSeparator,
  MenubarLabel,
  MenubarCheckboxItem,
  MenubarRadioGroup,
  MenubarRadioItem,
  MenubarPortal,
  MenubarSubContent,
  MenubarSubTrigger,
  MenubarGroup,
  MenubarSub,
  MenubarShortcut,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/navigation-menu.tsx
// ============================================================
import * as React from "react"
import * as NavigationMenuPrimitive from "@radix-ui/react-navigation-menu"
import { cva } from "class-variance-authority"
import { ChevronDown } from "lucide-react"

import { cn } from "@/lib/utils"

const NavigationMenu = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Root>
>(({ className, children, ...props }, ref) => (
  <NavigationMenuPrimitive.Root
    ref={ref}
    className={cn(
      "relative z-10 flex max-w-max flex-1 items-center justify-center",
      className
    )}
    {...props}
  >
    {children}
    <NavigationMenuViewport />
  </NavigationMenuPrimitive.Root>
))
NavigationMenu.displayName = NavigationMenuPrimitive.Root.displayName

const NavigationMenuList = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.List>
>(({ className, ...props }, ref) => (
  <NavigationMenuPrimitive.List
    ref={ref}
    className={cn(
      "group flex flex-1 list-none items-center justify-center space-x-1",
      className
    )}
    {...props}
  />
))
NavigationMenuList.displayName = NavigationMenuPrimitive.List.displayName

const NavigationMenuItem = NavigationMenuPrimitive.Item

const navigationMenuTriggerStyle = cva(
  "group inline-flex h-9 w-max items-center justify-center rounded-md bg-background px-4 py-2 text-sm font-medium transition-colors hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground focus:outline-none disabled:pointer-events-none disabled:opacity-50 data-[state=open]:text-accent-foreground data-[state=open]:bg-accent/50 data-[state=open]:hover:bg-accent data-[state=open]:focus:bg-accent"
)

const NavigationMenuTrigger = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <NavigationMenuPrimitive.Trigger
    ref={ref}
    className={cn(navigationMenuTriggerStyle(), "group", className)}
    {...props}
  >
    {children}{" "}
    <ChevronDown
      className="relative top-[1px] ml-1 h-3 w-3 transition duration-300 group-data-[state=open]:rotate-180"
      aria-hidden="true"
    />
  </NavigationMenuPrimitive.Trigger>
))
NavigationMenuTrigger.displayName = NavigationMenuPrimitive.Trigger.displayName

const NavigationMenuContent = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Content>
>(({ className, ...props }, ref) => (
  <NavigationMenuPrimitive.Content
    ref={ref}
    className={cn(
      "left-0 top-0 w-full data-[motion^=from-]:animate-in data-[motion^=to-]:animate-out data-[motion^=from-]:fade-in data-[motion^=to-]:fade-out data-[motion=from-end]:slide-in-from-right-52 data-[motion=from-start]:slide-in-from-left-52 data-[motion=to-end]:slide-out-to-right-52 data-[motion=to-start]:slide-out-to-left-52 md:absolute md:w-auto ",
      className
    )}
    {...props}
  />
))
NavigationMenuContent.displayName = NavigationMenuPrimitive.Content.displayName

const NavigationMenuLink = NavigationMenuPrimitive.Link

const NavigationMenuViewport = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Viewport>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Viewport>
>(({ className, ...props }, ref) => (
  <div className={cn("absolute left-0 top-full flex justify-center")}>
    <NavigationMenuPrimitive.Viewport
      className={cn(
        "origin-top-center relative mt-1.5 h-[var(--radix-navigation-menu-viewport-height)] w-full overflow-hidden rounded-md border bg-popover text-popover-foreground shadow data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-90 md:w-[var(--radix-navigation-menu-viewport-width)]",
        className
      )}
      ref={ref}
      {...props}
    />
  </div>
))
NavigationMenuViewport.displayName =
  NavigationMenuPrimitive.Viewport.displayName

const NavigationMenuIndicator = React.forwardRef<
  React.ElementRef<typeof NavigationMenuPrimitive.Indicator>,
  React.ComponentPropsWithoutRef<typeof NavigationMenuPrimitive.Indicator>
>(({ className, ...props }, ref) => (
  <NavigationMenuPrimitive.Indicator
    ref={ref}
    className={cn(
      "top-full z-[1] flex h-1.5 items-end justify-center overflow-hidden data-[state=visible]:animate-in data-[state=hidden]:animate-out data-[state=hidden]:fade-out data-[state=visible]:fade-in",
      className
    )}
    {...props}
  >
    <div className="relative top-[60%] h-2 w-2 rotate-45 rounded-tl-sm bg-border shadow-md" />
  </NavigationMenuPrimitive.Indicator>
))
NavigationMenuIndicator.displayName =
  NavigationMenuPrimitive.Indicator.displayName

export {
  navigationMenuTriggerStyle,
  NavigationMenu,
  NavigationMenuList,
  NavigationMenuItem,
  NavigationMenuContent,
  NavigationMenuTrigger,
  NavigationMenuLink,
  NavigationMenuIndicator,
  NavigationMenuViewport,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/pagination.tsx
// ============================================================
import * as React from "react"
import { ChevronLeft, ChevronRight, MoreHorizontal } from "lucide-react"

import { cn } from "@/lib/utils"
import { ButtonProps, buttonVariants } from "@/components/ui/button"

const Pagination = ({ className, ...props }: React.ComponentProps<"nav">) => (
  <nav
    role="navigation"
    aria-label="pagination"
    className={cn("mx-auto flex w-full justify-center", className)}
    {...props}
  />
)
Pagination.displayName = "Pagination"

const PaginationContent = React.forwardRef<
  HTMLUListElement,
  React.ComponentProps<"ul">
>(({ className, ...props }, ref) => (
  <ul
    ref={ref}
    className={cn("flex flex-row items-center gap-1", className)}
    {...props}
  />
))
PaginationContent.displayName = "PaginationContent"

const PaginationItem = React.forwardRef<
  HTMLLIElement,
  React.ComponentProps<"li">
>(({ className, ...props }, ref) => (
  <li ref={ref} className={cn("", className)} {...props} />
))
PaginationItem.displayName = "PaginationItem"

type PaginationLinkProps = {
  isActive?: boolean
} & Pick<ButtonProps, "size"> &
  React.ComponentProps<"a">

const PaginationLink = ({
  className,
  isActive,
  size = "icon",
  ...props
}: PaginationLinkProps) => (
  <a
    aria-current={isActive ? "page" : undefined}
    className={cn(
      buttonVariants({
        variant: isActive ? "outline" : "ghost",
        size,
      }),
      className
    )}
    {...props}
  />
)
PaginationLink.displayName = "PaginationLink"

const PaginationPrevious = ({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) => (
  <PaginationLink
    aria-label="Go to previous page"
    size="default"
    className={cn("gap-1 pl-2.5", className)}
    {...props}
  >
    <ChevronLeft className="h-4 w-4" />
    <span>Previous</span>
  </PaginationLink>
)
PaginationPrevious.displayName = "PaginationPrevious"

const PaginationNext = ({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) => (
  <PaginationLink
    aria-label="Go to next page"
    size="default"
    className={cn("gap-1 pr-2.5", className)}
    {...props}
  >
    <span>Next</span>
    <ChevronRight className="h-4 w-4" />
  </PaginationLink>
)
PaginationNext.displayName = "PaginationNext"

const PaginationEllipsis = ({
  className,
  ...props
}: React.ComponentProps<"span">) => (
  <span
    aria-hidden
    className={cn("flex h-9 w-9 items-center justify-center", className)}
    {...props}
  >
    <MoreHorizontal className="h-4 w-4" />
    <span className="sr-only">More pages</span>
  </span>
)
PaginationEllipsis.displayName = "PaginationEllipsis"

export {
  Pagination,
  PaginationContent,
  PaginationLink,
  PaginationItem,
  PaginationPrevious,
  PaginationNext,
  PaginationEllipsis,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/popover.tsx
// ============================================================
import * as React from "react"
import * as PopoverPrimitive from "@radix-ui/react-popover"

import { cn } from "@/lib/utils"

const Popover = PopoverPrimitive.Root

const PopoverTrigger = PopoverPrimitive.Trigger

const PopoverAnchor = PopoverPrimitive.Anchor

const PopoverContent = React.forwardRef<
  React.ElementRef<typeof PopoverPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof PopoverPrimitive.Content>
>(({ className, align = "center", sideOffset = 4, ...props }, ref) => (
  <PopoverPrimitive.Portal>
    <PopoverPrimitive.Content
      ref={ref}
      align={align}
      sideOffset={sideOffset}
      className={cn(
        "z-50 w-72 rounded-md border bg-popover p-4 text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-popover-content-transform-origin]",
        className
      )}
      {...props}
    />
  </PopoverPrimitive.Portal>
))
PopoverContent.displayName = PopoverPrimitive.Content.displayName

export { Popover, PopoverTrigger, PopoverContent, PopoverAnchor }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/progress.tsx
// ============================================================
"use client"

import * as React from "react"
import * as ProgressPrimitive from "@radix-ui/react-progress"

import { cn } from "@/lib/utils"

const Progress = React.forwardRef<
  React.ElementRef<typeof ProgressPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ProgressPrimitive.Root>
>(({ className, value, ...props }, ref) => (
  <ProgressPrimitive.Root
    ref={ref}
    className={cn(
      "relative h-2 w-full overflow-hidden rounded-full bg-primary/20",
      className
    )}
    {...props}
  >
    <ProgressPrimitive.Indicator
      className="h-full w-full flex-1 bg-primary transition-all"
      style={{ transform: `translateX(-${100 - (value || 0)}%)` }}
    />
  </ProgressPrimitive.Root>
))
Progress.displayName = ProgressPrimitive.Root.displayName

export { Progress }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/radio-group.tsx
// ============================================================
import * as React from "react"
import * as RadioGroupPrimitive from "@radix-ui/react-radio-group"
import { Circle } from "lucide-react"

import { cn } from "@/lib/utils"

const RadioGroup = React.forwardRef<
  React.ElementRef<typeof RadioGroupPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof RadioGroupPrimitive.Root>
>(({ className, ...props }, ref) => {
  return (
    <RadioGroupPrimitive.Root
      className={cn("grid gap-2", className)}
      {...props}
      ref={ref}
    />
  )
})
RadioGroup.displayName = RadioGroupPrimitive.Root.displayName

const RadioGroupItem = React.forwardRef<
  React.ElementRef<typeof RadioGroupPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof RadioGroupPrimitive.Item>
>(({ className, ...props }, ref) => {
  return (
    <RadioGroupPrimitive.Item
      ref={ref}
      className={cn(
        "aspect-square h-4 w-4 rounded-full border border-primary text-primary shadow focus:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    >
      <RadioGroupPrimitive.Indicator className="flex items-center justify-center">
        <Circle className="h-3.5 w-3.5 fill-primary" />
      </RadioGroupPrimitive.Indicator>
    </RadioGroupPrimitive.Item>
  )
})
RadioGroupItem.displayName = RadioGroupPrimitive.Item.displayName

export { RadioGroup, RadioGroupItem }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/resizable.tsx
// ============================================================
"use client"

import { GripVertical } from "lucide-react"
import * as ResizablePrimitive from "react-resizable-panels"

import { cn } from "@/lib/utils"

const ResizablePanelGroup = ({
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelGroup>) => (
  <ResizablePrimitive.PanelGroup
    className={cn(
      "flex h-full w-full data-[panel-group-direction=vertical]:flex-col",
      className
    )}
    {...props}
  />
)

const ResizablePanel = ResizablePrimitive.Panel

const ResizableHandle = ({
  withHandle,
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelResizeHandle> & {
  withHandle?: boolean
}) => (
  <ResizablePrimitive.PanelResizeHandle
    className={cn(
      "relative flex w-px items-center justify-center bg-border after:absolute after:inset-y-0 after:left-1/2 after:w-1 after:-translate-x-1/2 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring focus-visible:ring-offset-1 data-[panel-group-direction=vertical]:h-px data-[panel-group-direction=vertical]:w-full data-[panel-group-direction=vertical]:after:left-0 data-[panel-group-direction=vertical]:after:h-1 data-[panel-group-direction=vertical]:after:w-full data-[panel-group-direction=vertical]:after:-translate-y-1/2 data-[panel-group-direction=vertical]:after:translate-x-0 [&[data-panel-group-direction=vertical]>div]:rotate-90",
      className
    )}
    {...props}
  >
    {withHandle && (
      <div className="z-10 flex h-4 w-3 items-center justify-center rounded-sm border bg-border">
        <GripVertical className="h-2.5 w-2.5" />
      </div>
    )}
  </ResizablePrimitive.PanelResizeHandle>
)

export { ResizablePanelGroup, ResizablePanel, ResizableHandle }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/scroll-area.tsx
// ============================================================
import * as React from "react"
import * as ScrollAreaPrimitive from "@radix-ui/react-scroll-area"

import { cn } from "@/lib/utils"

const ScrollArea = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.Root>
>(({ className, children, ...props }, ref) => (
  <ScrollAreaPrimitive.Root
    ref={ref}
    className={cn("relative overflow-hidden", className)}
    {...props}
  >
    <ScrollAreaPrimitive.Viewport className="h-full w-full rounded-[inherit]">
      {children}
    </ScrollAreaPrimitive.Viewport>
    <ScrollBar />
    <ScrollAreaPrimitive.Corner />
  </ScrollAreaPrimitive.Root>
))
ScrollArea.displayName = ScrollAreaPrimitive.Root.displayName

const ScrollBar = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>
>(({ className, orientation = "vertical", ...props }, ref) => (
  <ScrollAreaPrimitive.ScrollAreaScrollbar
    ref={ref}
    orientation={orientation}
    className={cn(
      "flex touch-none select-none transition-colors",
      orientation === "vertical" &&
        "h-full w-2.5 border-l border-l-transparent p-[1px]",
      orientation === "horizontal" &&
        "h-2.5 flex-col border-t border-t-transparent p-[1px]",
      className
    )}
    {...props}
  >
    <ScrollAreaPrimitive.ScrollAreaThumb className="relative flex-1 rounded-full bg-border" />
  </ScrollAreaPrimitive.ScrollAreaScrollbar>
))
ScrollBar.displayName = ScrollAreaPrimitive.ScrollAreaScrollbar.displayName

export { ScrollArea, ScrollBar }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/select.tsx
// ============================================================
"use client"

import * as React from "react"
import * as SelectPrimitive from "@radix-ui/react-select"
import { Check, ChevronDown, ChevronUp } from "lucide-react"

import { cn } from "@/lib/utils"

const Select = SelectPrimitive.Root

const SelectGroup = SelectPrimitive.Group

const SelectValue = SelectPrimitive.Value

const SelectTrigger = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Trigger
    ref={ref}
    className={cn(
      "flex h-9 w-full items-center justify-between whitespace-nowrap rounded-md border border-input bg-transparent px-3 py-2 text-sm shadow-sm ring-offset-background data-[placeholder]:text-muted-foreground focus:outline-none focus:ring-1 focus:ring-ring disabled:cursor-not-allowed disabled:opacity-50 [&>span]:line-clamp-1",
      className
    )}
    {...props}
  >
    {children}
    <SelectPrimitive.Icon asChild>
      <ChevronDown className="h-4 w-4 opacity-50" />
    </SelectPrimitive.Icon>
  </SelectPrimitive.Trigger>
))
SelectTrigger.displayName = SelectPrimitive.Trigger.displayName

const SelectScrollUpButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollUpButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollUpButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollUpButton
    ref={ref}
    className={cn(
      "flex cursor-default items-center justify-center py-1",
      className
    )}
    {...props}
  >
    <ChevronUp className="h-4 w-4" />
  </SelectPrimitive.ScrollUpButton>
))
SelectScrollUpButton.displayName = SelectPrimitive.ScrollUpButton.displayName

const SelectScrollDownButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollDownButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollDownButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollDownButton
    ref={ref}
    className={cn(
      "flex cursor-default items-center justify-center py-1",
      className
    )}
    {...props}
  >
    <ChevronDown className="h-4 w-4" />
  </SelectPrimitive.ScrollDownButton>
))
SelectScrollDownButton.displayName =
  SelectPrimitive.ScrollDownButton.displayName

const SelectContent = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Content>
>(({ className, children, position = "popper", ...props }, ref) => (
  <SelectPrimitive.Portal>
    <SelectPrimitive.Content
      ref={ref}
      className={cn(
        "relative z-50 max-h-[--radix-select-content-available-height] min-w-[8rem] overflow-y-auto overflow-x-hidden rounded-md border bg-popover text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-select-content-transform-origin]",
        position === "popper" &&
          "data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1",
        className
      )}
      position={position}
      {...props}
    >
      <SelectScrollUpButton />
      <SelectPrimitive.Viewport
        className={cn(
          "p-1",
          position === "popper" &&
            "h-[var(--radix-select-trigger-height)] w-full min-w-[var(--radix-select-trigger-width)]"
        )}
      >
        {children}
      </SelectPrimitive.Viewport>
      <SelectScrollDownButton />
    </SelectPrimitive.Content>
  </SelectPrimitive.Portal>
))
SelectContent.displayName = SelectPrimitive.Content.displayName

const SelectLabel = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Label>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Label
    ref={ref}
    className={cn("px-2 py-1.5 text-sm font-semibold", className)}
    {...props}
  />
))
SelectLabel.displayName = SelectPrimitive.Label.displayName

const SelectItem = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Item>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex w-full cursor-default select-none items-center rounded-sm py-1.5 pl-2 pr-8 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute right-2 flex h-3.5 w-3.5 items-center justify-center">
      <SelectPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </SelectPrimitive.ItemIndicator>
    </span>
    <SelectPrimitive.ItemText>{children}</SelectPrimitive.ItemText>
  </SelectPrimitive.Item>
))
SelectItem.displayName = SelectPrimitive.Item.displayName

const SelectSeparator = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 my-1 h-px bg-muted", className)}
    {...props}
  />
))
SelectSeparator.displayName = SelectPrimitive.Separator.displayName

export {
  Select,
  SelectGroup,
  SelectValue,
  SelectTrigger,
  SelectContent,
  SelectLabel,
  SelectItem,
  SelectSeparator,
  SelectScrollUpButton,
  SelectScrollDownButton,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/separator.tsx
// ============================================================
import * as React from "react"
import * as SeparatorPrimitive from "@radix-ui/react-separator"

import { cn } from "@/lib/utils"

const Separator = React.forwardRef<
  React.ElementRef<typeof SeparatorPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof SeparatorPrimitive.Root>
>(
  (
    { className, orientation = "horizontal", decorative = true, ...props },
    ref
  ) => (
    <SeparatorPrimitive.Root
      ref={ref}
      decorative={decorative}
      orientation={orientation}
      className={cn(
        "shrink-0 bg-border",
        orientation === "horizontal" ? "h-[1px] w-full" : "h-full w-[1px]",
        className
      )}
      {...props}
    />
  )
)
Separator.displayName = SeparatorPrimitive.Root.displayName

export { Separator }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/sheet.tsx
// ============================================================
"use client"

import * as React from "react"
import * as SheetPrimitive from "@radix-ui/react-dialog"
import { cva, type VariantProps } from "class-variance-authority"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const Sheet = SheetPrimitive.Root

const SheetTrigger = SheetPrimitive.Trigger

const SheetClose = SheetPrimitive.Close

const SheetPortal = SheetPrimitive.Portal

const SheetOverlay = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Overlay
    className={cn(
      "fixed inset-0 z-50 bg-black/80  data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
    ref={ref}
  />
))
SheetOverlay.displayName = SheetPrimitive.Overlay.displayName

const sheetVariants = cva(
  "fixed z-50 gap-4 bg-background p-6 shadow-lg transition ease-in-out data-[state=closed]:duration-300 data-[state=open]:duration-500 data-[state=open]:animate-in data-[state=closed]:animate-out",
  {
    variants: {
      side: {
        top: "inset-x-0 top-0 border-b data-[state=closed]:slide-out-to-top data-[state=open]:slide-in-from-top",
        bottom:
          "inset-x-0 bottom-0 border-t data-[state=closed]:slide-out-to-bottom data-[state=open]:slide-in-from-bottom",
        left: "inset-y-0 left-0 h-full w-3/4 border-r data-[state=closed]:slide-out-to-left data-[state=open]:slide-in-from-left sm:max-w-sm",
        right:
          "inset-y-0 right-0 h-full w-3/4 border-l data-[state=closed]:slide-out-to-right data-[state=open]:slide-in-from-right sm:max-w-sm",
      },
    },
    defaultVariants: {
      side: "right",
    },
  }
)

interface SheetContentProps
  extends React.ComponentPropsWithoutRef<typeof SheetPrimitive.Content>,
    VariantProps<typeof sheetVariants> {}

const SheetContent = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Content>,
  SheetContentProps
>(({ side = "right", className, children, ...props }, ref) => (
  <SheetPortal>
    <SheetOverlay />
    <SheetPrimitive.Content
      ref={ref}
      className={cn(sheetVariants({ side }), className)}
      {...props}
    >
      <SheetPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-secondary">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </SheetPrimitive.Close>
      {children}
    </SheetPrimitive.Content>
  </SheetPortal>
))
SheetContent.displayName = SheetPrimitive.Content.displayName

const SheetHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-2 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
SheetHeader.displayName = "SheetHeader"

const SheetFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
SheetFooter.displayName = "SheetFooter"

const SheetTitle = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Title>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Title
    ref={ref}
    className={cn("text-lg font-semibold text-foreground", className)}
    {...props}
  />
))
SheetTitle.displayName = SheetPrimitive.Title.displayName

const SheetDescription = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Description>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
SheetDescription.displayName = SheetPrimitive.Description.displayName

export {
  Sheet,
  SheetPortal,
  SheetOverlay,
  SheetTrigger,
  SheetClose,
  SheetContent,
  SheetHeader,
  SheetFooter,
  SheetTitle,
  SheetDescription,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/sidebar.tsx
// ============================================================
"use client"

import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, VariantProps } from "class-variance-authority"
import { PanelLeftIcon } from "lucide-react"

import { useIsMobile } from "@/hooks/use-mobile"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Separator } from "@/components/ui/separator"
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet"
import { Skeleton } from "@/components/ui/skeleton"
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

const SIDEBAR_COOKIE_NAME = "sidebar_state"
const SIDEBAR_COOKIE_MAX_AGE = 60 * 60 * 24 * 7
const SIDEBAR_WIDTH = "16rem"
const SIDEBAR_WIDTH_MOBILE = "18rem"
const SIDEBAR_WIDTH_ICON = "3rem"
const SIDEBAR_KEYBOARD_SHORTCUT = "b"

type SidebarContextProps = {
  state: "expanded" | "collapsed"
  open: boolean
  setOpen: (open: boolean) => void
  openMobile: boolean
  setOpenMobile: (open: boolean) => void
  isMobile: boolean
  toggleSidebar: () => void
}

const SidebarContext = React.createContext<SidebarContextProps | null>(null)

function useSidebar() {
  const context = React.useContext(SidebarContext)
  if (!context) {
    throw new Error("useSidebar must be used within a SidebarProvider.")
  }

  return context
}

function SidebarProvider({
  defaultOpen = true,
  open: openProp,
  onOpenChange: setOpenProp,
  className,
  style,
  children,
  ...props
}: React.ComponentProps<"div"> & {
  defaultOpen?: boolean
  open?: boolean
  onOpenChange?: (open: boolean) => void
}) {
  const isMobile = useIsMobile()
  const [openMobile, setOpenMobile] = React.useState(false)

  // This is the internal state of the sidebar.
  // We use openProp and setOpenProp for control from outside the component.
  const [_open, _setOpen] = React.useState(defaultOpen)
  const open = openProp ?? _open
  const setOpen = React.useCallback(
    (value: boolean | ((value: boolean) => boolean)) => {
      const openState = typeof value === "function" ? value(open) : value
      if (setOpenProp) {
        setOpenProp(openState)
      } else {
        _setOpen(openState)
      }

      // This sets the cookie to keep the sidebar state.
      document.cookie = `${SIDEBAR_COOKIE_NAME}=${openState}; path=/; max-age=${SIDEBAR_COOKIE_MAX_AGE}`
    },
    [setOpenProp, open]
  )

  // Helper to toggle the sidebar.
  const toggleSidebar = React.useCallback(() => {
    return isMobile ? setOpenMobile((open) => !open) : setOpen((open) => !open)
  }, [isMobile, setOpen, setOpenMobile])

  // Adds a keyboard shortcut to toggle the sidebar.
  React.useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (
        event.key === SIDEBAR_KEYBOARD_SHORTCUT &&
        (event.metaKey || event.ctrlKey)
      ) {
        event.preventDefault()
        toggleSidebar()
      }
    }

    window.addEventListener("keydown", handleKeyDown)
    return () => window.removeEventListener("keydown", handleKeyDown)
  }, [toggleSidebar])

  // We add a state so that we can do data-state="expanded" or "collapsed".
  // This makes it easier to style the sidebar with Tailwind classes.
  const state = open ? "expanded" : "collapsed"

  const contextValue = React.useMemo<SidebarContextProps>(
    () => ({
      state,
      open,
      setOpen,
      isMobile,
      openMobile,
      setOpenMobile,
      toggleSidebar,
    }),
    [state, open, setOpen, isMobile, openMobile, setOpenMobile, toggleSidebar]
  )

  return (
    <SidebarContext.Provider value={contextValue}>
      <TooltipProvider delayDuration={0}>
        <div
          data-slot="sidebar-wrapper"
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH,
              "--sidebar-width-icon": SIDEBAR_WIDTH_ICON,
              ...style,
            } as React.CSSProperties
          }
          className={cn(
            "group/sidebar-wrapper has-data-[variant=inset]:bg-sidebar flex min-h-svh w-full",
            className
          )}
          {...props}
        >
          {children}
        </div>
      </TooltipProvider>
    </SidebarContext.Provider>
  )
}

function Sidebar({
  side = "left",
  variant = "sidebar",
  collapsible = "offcanvas",
  className,
  children,
  ...props
}: React.ComponentProps<"div"> & {
  side?: "left" | "right"
  variant?: "sidebar" | "floating" | "inset"
  collapsible?: "offcanvas" | "icon" | "none"
}) {
  const { isMobile, state, openMobile, setOpenMobile } = useSidebar()

  if (collapsible === "none") {
    return (
      <div
        data-slot="sidebar"
        className={cn(
          "bg-sidebar text-sidebar-foreground flex h-full w-[var(--sidebar-width)] flex-col",
          className
        )}
        {...props}
      >
        {children}
      </div>
    )
  }

  if (isMobile) {
    return (
      <Sheet open={openMobile} onOpenChange={setOpenMobile} {...props}>
        <SheetContent
          data-sidebar="sidebar"
          data-slot="sidebar"
          data-mobile="true"
          className="bg-sidebar text-sidebar-foreground w-[var(--sidebar-width)] p-0 [&>button]:hidden"
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH_MOBILE,
            } as React.CSSProperties
          }
          side={side}
        >
          <SheetHeader className="sr-only">
            <SheetTitle>Sidebar</SheetTitle>
            <SheetDescription>Displays the mobile sidebar.</SheetDescription>
          </SheetHeader>
          <div className="flex h-full w-full flex-col">{children}</div>
        </SheetContent>
      </Sheet>
    )
  }

  return (
    <div
      className="group peer text-sidebar-foreground hidden md:block"
      data-state={state}
      data-collapsible={state === "collapsed" ? collapsible : ""}
      data-variant={variant}
      data-side={side}
      data-slot="sidebar"
    >
      {/* This is what handles the sidebar gap on desktop */}
      <div
        data-slot="sidebar-gap"
        className={cn(
          "relative w-[var(--sidebar-width)] bg-transparent transition-[width] duration-200 ease-linear",
          "group-data-[collapsible=offcanvas]:w-0",
          "group-data-[side=right]:rotate-180",
          variant === "floating" || variant === "inset"
            ? "group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)+var(--spacing-4))]"
            : "group-data-[collapsible=icon]:w-[var(--sidebar-width-icon)]"
        )}
      />
      <div
        data-slot="sidebar-container"
        className={cn(
          "fixed inset-y-0 z-10 hidden h-svh w-[var(--sidebar-width)] transition-[left,right,width] duration-200 ease-linear md:flex",
          side === "left"
            ? "left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]"
            : "right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
          // Adjust the padding for floating and inset variants.
          variant === "floating" || variant === "inset"
            ? "p-2 group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)+var(--spacing-4)+2px)]"
            : "group-data-[collapsible=icon]:w-[var(--sidebar-width-icon)] group-data-[side=left]:border-r group-data-[side=right]:border-l",
          className
        )}
        {...props}
      >
        <div
          data-sidebar="sidebar"
          data-slot="sidebar-inner"
          className="bg-sidebar group-data-[variant=floating]:border-sidebar-border flex h-full w-full flex-col group-data-[variant=floating]:rounded-lg group-data-[variant=floating]:border group-data-[variant=floating]:shadow-sm"
        >
          {children}
        </div>
      </div>
    </div>
  )
}

function SidebarTrigger({
  className,
  onClick,
  ...props
}: React.ComponentProps<typeof Button>) {
  const { toggleSidebar } = useSidebar()

  return (
    <Button
      data-sidebar="trigger"
      data-slot="sidebar-trigger"
      variant="ghost"
      size="icon"
      className={cn("h-7 w-7", className)}
      onClick={(event) => {
        onClick?.(event)
        toggleSidebar()
      }}
      {...props}
    >
      <PanelLeftIcon />
      <span className="sr-only">Toggle Sidebar</span>
    </Button>
  )
}

function SidebarRail({ className, ...props }: React.ComponentProps<"button">) {
  const { toggleSidebar } = useSidebar()

  // Note: Tailwind v3.4 doesn't support "in-" selectors. So the rail won't work perfectly.
  return (
    <button
      data-sidebar="rail"
      data-slot="sidebar-rail"
      aria-label="Toggle Sidebar"
      tabIndex={-1}
      onClick={toggleSidebar}
      title="Toggle Sidebar"
      className={cn(
        "hover:after:bg-sidebar-border absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear group-data-[side=left]:-right-4 group-data-[side=right]:left-0 after:absolute after:inset-y-0 after:left-1/2 after:w-[2px] sm:flex",
        "in-data-[side=left]:cursor-w-resize in-data-[side=right]:cursor-e-resize",
        "[[data-side=left][data-state=collapsed]_&]:cursor-e-resize [[data-side=right][data-state=collapsed]_&]:cursor-w-resize",
        "hover:group-data-[collapsible=offcanvas]:bg-sidebar group-data-[collapsible=offcanvas]:translate-x-0 group-data-[collapsible=offcanvas]:after:left-full",
        "[[data-side=left][data-collapsible=offcanvas]_&]:-right-2",
        "[[data-side=right][data-collapsible=offcanvas]_&]:-left-2",
        className
      )}
      {...props}
    />
  )
}

function SidebarInset({ className, ...props }: React.ComponentProps<"main">) {
  return (
    <main
      data-slot="sidebar-inset"
      className={cn(
        "bg-background relative flex w-full flex-1 flex-col",
        "md:peer-data-[variant=inset]:m-2 md:peer-data-[variant=inset]:ml-0 md:peer-data-[variant=inset]:rounded-xl md:peer-data-[variant=inset]:shadow-sm md:peer-data-[variant=inset]:peer-data-[state=collapsed]:ml-2",
        className
      )}
      {...props}
    />
  )
}

function SidebarInput({
  className,
  ...props
}: React.ComponentProps<typeof Input>) {
  return (
    <Input
      data-slot="sidebar-input"
      data-sidebar="input"
      className={cn("bg-background h-8 w-full shadow-none", className)}
      {...props}
    />
  )
}

function SidebarHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-header"
      data-sidebar="header"
      className={cn("flex flex-col gap-2 p-2", className)}
      {...props}
    />
  )
}

function SidebarFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-footer"
      data-sidebar="footer"
      className={cn("flex flex-col gap-2 p-2", className)}
      {...props}
    />
  )
}

function SidebarSeparator({
  className,
  ...props
}: React.ComponentProps<typeof Separator>) {
  return (
    <Separator
      data-slot="sidebar-separator"
      data-sidebar="separator"
      className={cn("bg-sidebar-border mx-2 w-auto", className)}
      {...props}
    />
  )
}

function SidebarContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-content"
      data-sidebar="content"
      className={cn(
        "flex min-h-0 flex-1 flex-col gap-2 overflow-auto group-data-[collapsible=icon]:overflow-hidden",
        className
      )}
      {...props}
    />
  )
}

function SidebarGroup({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-group"
      data-sidebar="group"
      className={cn("relative flex w-full min-w-0 flex-col p-2", className)}
      {...props}
    />
  )
}

function SidebarGroupLabel({
  className,
  asChild = false,
  ...props
}: React.ComponentProps<"div"> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "div"

  return (
    <Comp
      data-slot="sidebar-group-label"
      data-sidebar="group-label"
      className={cn(
        "text-sidebar-foreground/70 ring-sidebar-ring flex h-8 shrink-0 items-center rounded-md px-2 text-xs font-medium outline-hidden transition-[margin,opacity] duration-200 ease-linear focus-visible:ring-2 [&>svg]:h-4 [&>svg]:w-4 [&>svg]:shrink-0",
        "group-data-[collapsible=icon]:-mt-8 group-data-[collapsible=icon]:opacity-0",
        className
      )}
      {...props}
    />
  )
}

function SidebarGroupAction({
  className,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="sidebar-group-action"
      data-sidebar="group-action"
      className={cn(
        "text-sidebar-foreground ring-sidebar-ring hover:bg-sidebar-accent hover:text-sidebar-accent-foreground absolute top-3.5 right-3 flex aspect-square w-5 items-center justify-center rounded-md p-0 outline-hidden transition-transform focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
        // Increases the hit area of the button on mobile.
        "after:absolute after:-inset-2 md:after:hidden",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
}

function SidebarGroupContent({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-group-content"
      data-sidebar="group-content"
      className={cn("w-full text-sm", className)}
      {...props}
    />
  )
}

function SidebarMenu({ className, ...props }: React.ComponentProps<"ul">) {
  return (
    <ul
      data-slot="sidebar-menu"
      data-sidebar="menu"
      className={cn("flex w-full min-w-0 flex-col gap-1", className)}
      {...props}
    />
  )
}

function SidebarMenuItem({ className, ...props }: React.ComponentProps<"li">) {
  return (
    <li
      data-slot="sidebar-menu-item"
      data-sidebar="menu-item"
      className={cn("group/menu-item relative", className)}
      {...props}
    />
  )
}

const sidebarMenuButtonVariants = cva(
  "peer/menu-button flex w-full items-center gap-2 overflow-hidden rounded-md p-2 text-left text-sm outline-hidden ring-sidebar-ring transition-[width,height,padding] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 group-has-data-[sidebar=menu-action]/menu-item:pr-8 aria-disabled:pointer-events-none aria-disabled:opacity-50 data-[active=true]:bg-sidebar-accent data-[active=true]:font-medium data-[active=true]:text-sidebar-accent-foreground data-[state=open]:hover:bg-sidebar-accent data-[state=open]:hover:text-sidebar-accent-foreground group-data-[collapsible=icon]:w-8! group-data-[collapsible=icon]:h-8! group-data-[collapsible=icon]:p-2! [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
        outline:
          "bg-background shadow-[0_0_0_1px_hsl(var(--sidebar-border))] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground hover:shadow-[0_0_0_1px_hsl(var(--sidebar-accent))]",
      },
      size: {
        default: "h-8 text-sm",
        sm: "h-7 text-xs",
        lg: "h-12 text-sm group-data-[collapsible=icon]:p-0!",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function SidebarMenuButton({
  asChild = false,
  isActive = false,
  variant = "default",
  size = "default",
  tooltip,
  className,
  ...props
}: React.ComponentProps<"button"> & {
  asChild?: boolean
  isActive?: boolean
  tooltip?: string | React.ComponentProps<typeof TooltipContent>
} & VariantProps<typeof sidebarMenuButtonVariants>) {
  const Comp = asChild ? Slot : "button"
  const { isMobile, state } = useSidebar()

  const button = (
    <Comp
      data-slot="sidebar-menu-button"
      data-sidebar="menu-button"
      data-size={size}
      data-active={isActive}
      className={cn(sidebarMenuButtonVariants({ variant, size }), className)}
      {...props}
    />
  )

  if (!tooltip) {
    return button
  }

  if (typeof tooltip === "string") {
    tooltip = {
      children: tooltip,
    }
  }

  return (
    <Tooltip>
      <TooltipTrigger asChild>{button}</TooltipTrigger>
      <TooltipContent
        side="right"
        align="center"
        hidden={state !== "collapsed" || isMobile}
        {...tooltip}
      />
    </Tooltip>
  )
}

function SidebarMenuAction({
  className,
  asChild = false,
  showOnHover = false,
  ...props
}: React.ComponentProps<"button"> & {
  asChild?: boolean
  showOnHover?: boolean
}) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="sidebar-menu-action"
      data-sidebar="menu-action"
      className={cn(
        "text-sidebar-foreground ring-sidebar-ring hover:bg-sidebar-accent hover:text-sidebar-accent-foreground peer-hover/menu-button:text-sidebar-accent-foreground absolute top-1.5 right-1 flex aspect-square w-5 items-center justify-center rounded-md p-0 outline-hidden transition-transform focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
        // Increases the hit area of the button on mobile.
        "after:absolute after:-inset-2 md:after:hidden",
        "peer-data-[size=sm]/menu-button:top-1",
        "peer-data-[size=default]/menu-button:top-1.5",
        "peer-data-[size=lg]/menu-button:top-2.5",
        "group-data-[collapsible=icon]:hidden",
        showOnHover &&
          "peer-data-[active=true]/menu-button:text-sidebar-accent-foreground group-focus-within/menu-item:opacity-100 group-hover/menu-item:opacity-100 data-[state=open]:opacity-100 md:opacity-0",
        className
      )}
      {...props}
    />
  )
}

function SidebarMenuBadge({
  className,
  ...props
}: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="sidebar-menu-badge"
      data-sidebar="menu-badge"
      className={cn(
        "text-sidebar-foreground pointer-events-none absolute right-1 flex h-5 min-w-5 items-center justify-center rounded-md px-1 text-xs font-medium tabular-nums select-none",
        "peer-hover/menu-button:text-sidebar-accent-foreground peer-data-[active=true]/menu-button:text-sidebar-accent-foreground",
        "peer-data-[size=sm]/menu-button:top-1",
        "peer-data-[size=default]/menu-button:top-1.5",
        "peer-data-[size=lg]/menu-button:top-2.5",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
}

function SidebarMenuSkeleton({
  className,
  showIcon = false,
  ...props
}: React.ComponentProps<"div"> & {
  showIcon?: boolean
}) {
  // Random width between 50 to 90%.
  const width = React.useMemo(() => {
    return `${Math.floor(Math.random() * 40) + 50}%`
  }, [])

  return (
    <div
      data-slot="sidebar-menu-skeleton"
      data-sidebar="menu-skeleton"
      className={cn("flex h-8 items-center gap-2 rounded-md px-2", className)}
      {...props}
    >
      {showIcon && (
        <Skeleton
          className="size-4 rounded-md"
          data-sidebar="menu-skeleton-icon"
        />
      )}
      <Skeleton
        className="h-4 max-w-[var(--skeleton-width)] flex-1"
        data-sidebar="menu-skeleton-text"
        style={
          {
            "--skeleton-width": width,
          } as React.CSSProperties
        }
      />
    </div>
  )
}

function SidebarMenuSub({ className, ...props }: React.ComponentProps<"ul">) {
  return (
    <ul
      data-slot="sidebar-menu-sub"
      data-sidebar="menu-sub"
      className={cn(
        "border-sidebar-border mx-3.5 flex min-w-0 translate-x-px flex-col gap-1 border-l px-2.5 py-0.5",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
}

function SidebarMenuSubItem({
  className,
  ...props
}: React.ComponentProps<"li">) {
  return (
    <li
      data-slot="sidebar-menu-sub-item"
      data-sidebar="menu-sub-item"
      className={cn("group/menu-sub-item relative", className)}
      {...props}
    />
  )
}

function SidebarMenuSubButton({
  asChild = false,
  size = "md",
  isActive = false,
  className,
  ...props
}: React.ComponentProps<"a"> & {
  asChild?: boolean
  size?: "sm" | "md"
  isActive?: boolean
}) {
  const Comp = asChild ? Slot : "a"

  return (
    <Comp
      data-slot="sidebar-menu-sub-button"
      data-sidebar="menu-sub-button"
      data-size={size}
      data-active={isActive}
      className={cn(
        "text-sidebar-foreground ring-sidebar-ring hover:bg-sidebar-accent hover:text-sidebar-accent-foreground active:bg-sidebar-accent active:text-sidebar-accent-foreground [&>svg]:text-sidebar-accent-foreground flex h-7 min-w-0 -translate-x-px items-center gap-2 overflow-hidden rounded-md px-2 outline outline-2 outline-transparent outline-offset-2 focus-visible:ring-2 disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none aria-disabled:opacity-50 [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0",
        "data-[active=true]:bg-sidebar-accent data-[active=true]:text-sidebar-accent-foreground",
        size === "sm" && "text-xs",
        size === "md" && "text-sm",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
}

export {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupAction,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarInput,
  SidebarInset,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuBadge,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSkeleton,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  SidebarProvider,
  SidebarRail,
  SidebarSeparator,
  SidebarTrigger,
  useSidebar,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/skeleton.tsx
// ============================================================
import { cn } from "@/lib/utils"

function Skeleton({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn("animate-pulse rounded-md bg-primary/10", className)}
      {...props}
    />
  )
}

export { Skeleton }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/slider.tsx
// ============================================================
import * as React from "react"
import * as SliderPrimitive from "@radix-ui/react-slider"

import { cn } from "@/lib/utils"

const Slider = React.forwardRef<
  React.ElementRef<typeof SliderPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof SliderPrimitive.Root>
>(({ className, ...props }, ref) => (
  <SliderPrimitive.Root
    ref={ref}
    className={cn(
      "relative flex w-full touch-none select-none items-center",
      className
    )}
    {...props}
  >
    <SliderPrimitive.Track className="relative h-1.5 w-full grow overflow-hidden rounded-full bg-primary/20">
      <SliderPrimitive.Range className="absolute h-full bg-primary" />
    </SliderPrimitive.Track>
    <SliderPrimitive.Thumb className="block h-4 w-4 rounded-full border border-primary/50 bg-background shadow transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50" />
  </SliderPrimitive.Root>
))
Slider.displayName = SliderPrimitive.Root.displayName

export { Slider }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/sonner.tsx
// ============================================================
"use client"

import { useTheme } from "next-themes"
import { Toaster as Sonner } from "sonner"

type ToasterProps = React.ComponentProps<typeof Sonner>

const Toaster = ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme()

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      className="toaster group"
      toastOptions={{
        classNames: {
          toast:
            "group toast group-[.toaster]:bg-background group-[.toaster]:text-foreground group-[.toaster]:border-border group-[.toaster]:shadow-lg",
          description: "group-[.toast]:text-muted-foreground",
          actionButton:
            "group-[.toast]:bg-primary group-[.toast]:text-primary-foreground",
          cancelButton:
            "group-[.toast]:bg-muted group-[.toast]:text-muted-foreground",
        },
      }}
      {...props}
    />
  )
}

export { Toaster }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/spinner.tsx
// ============================================================
import { Loader2Icon } from "lucide-react"

import { cn } from "@/lib/utils"

function Spinner({ className, ...props }: React.ComponentProps<"svg">) {
  return (
    <Loader2Icon
      role="status"
      aria-label="Loading"
      className={cn("size-4 animate-spin", className)}
      {...props}
    />
  )
}

export { Spinner }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/switch.tsx
// ============================================================
import * as React from "react"
import * as SwitchPrimitives from "@radix-ui/react-switch"

import { cn } from "@/lib/utils"

const Switch = React.forwardRef<
  React.ElementRef<typeof SwitchPrimitives.Root>,
  React.ComponentPropsWithoutRef<typeof SwitchPrimitives.Root>
>(({ className, ...props }, ref) => (
  <SwitchPrimitives.Root
    className={cn(
      "peer inline-flex h-5 w-9 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=unchecked]:bg-input",
      className
    )}
    {...props}
    ref={ref}
  >
    <SwitchPrimitives.Thumb
      className={cn(
        "pointer-events-none block h-4 w-4 rounded-full bg-background shadow-lg ring-0 transition-transform data-[state=checked]:translate-x-4 data-[state=unchecked]:translate-x-0"
      )}
    />
  </SwitchPrimitives.Root>
))
Switch.displayName = SwitchPrimitives.Root.displayName

export { Switch }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/table.tsx
// ============================================================
import * as React from "react"

import { cn } from "@/lib/utils"

const Table = React.forwardRef<
  HTMLTableElement,
  React.HTMLAttributes<HTMLTableElement>
>(({ className, ...props }, ref) => (
  <div className="relative w-full overflow-auto">
    <table
      ref={ref}
      className={cn("w-full caption-bottom text-sm", className)}
      {...props}
    />
  </div>
))
Table.displayName = "Table"

const TableHeader = React.forwardRef<
  HTMLTableSectionElement,
  React.HTMLAttributes<HTMLTableSectionElement>
>(({ className, ...props }, ref) => (
  <thead ref={ref} className={cn("[&_tr]:border-b", className)} {...props} />
))
TableHeader.displayName = "TableHeader"

const TableBody = React.forwardRef<
  HTMLTableSectionElement,
  React.HTMLAttributes<HTMLTableSectionElement>
>(({ className, ...props }, ref) => (
  <tbody
    ref={ref}
    className={cn("[&_tr:last-child]:border-0", className)}
    {...props}
  />
))
TableBody.displayName = "TableBody"

const TableFooter = React.forwardRef<
  HTMLTableSectionElement,
  React.HTMLAttributes<HTMLTableSectionElement>
>(({ className, ...props }, ref) => (
  <tfoot
    ref={ref}
    className={cn(
      "border-t bg-muted/50 font-medium [&>tr]:last:border-b-0",
      className
    )}
    {...props}
  />
))
TableFooter.displayName = "TableFooter"

const TableRow = React.forwardRef<
  HTMLTableRowElement,
  React.HTMLAttributes<HTMLTableRowElement>
>(({ className, ...props }, ref) => (
  <tr
    ref={ref}
    className={cn(
      "border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted",
      className
    )}
    {...props}
  />
))
TableRow.displayName = "TableRow"

const TableHead = React.forwardRef<
  HTMLTableCellElement,
  React.ThHTMLAttributes<HTMLTableCellElement>
>(({ className, ...props }, ref) => (
  <th
    ref={ref}
    className={cn(
      "h-10 px-2 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0 [&>[role=checkbox]]:translate-y-[2px]",
      className
    )}
    {...props}
  />
))
TableHead.displayName = "TableHead"

const TableCell = React.forwardRef<
  HTMLTableCellElement,
  React.TdHTMLAttributes<HTMLTableCellElement>
>(({ className, ...props }, ref) => (
  <td
    ref={ref}
    className={cn(
      "p-2 align-middle [&:has([role=checkbox])]:pr-0 [&>[role=checkbox]]:translate-y-[2px]",
      className
    )}
    {...props}
  />
))
TableCell.displayName = "TableCell"

const TableCaption = React.forwardRef<
  HTMLTableCaptionElement,
  React.HTMLAttributes<HTMLTableCaptionElement>
>(({ className, ...props }, ref) => (
  <caption
    ref={ref}
    className={cn("mt-4 text-sm text-muted-foreground", className)}
    {...props}
  />
))
TableCaption.displayName = "TableCaption"

export {
  Table,
  TableHeader,
  TableBody,
  TableFooter,
  TableHead,
  TableRow,
  TableCell,
  TableCaption,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/tabs.tsx
// ============================================================
import * as React from "react"
import * as TabsPrimitive from "@radix-ui/react-tabs"

import { cn } from "@/lib/utils"

const Tabs = TabsPrimitive.Root

const TabsList = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.List>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.List
    ref={ref}
    className={cn(
      "inline-flex h-9 items-center justify-center rounded-lg bg-muted p-1 text-muted-foreground",
      className
    )}
    {...props}
  />
))
TabsList.displayName = TabsPrimitive.List.displayName

const TabsTrigger = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Trigger
    ref={ref}
    className={cn(
      "inline-flex items-center justify-center whitespace-nowrap rounded-md px-3 py-1 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow",
      className
    )}
    {...props}
  />
))
TabsTrigger.displayName = TabsPrimitive.Trigger.displayName

const TabsContent = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Content>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Content
    ref={ref}
    className={cn(
      "mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
      className
    )}
    {...props}
  />
))
TabsContent.displayName = TabsPrimitive.Content.displayName

export { Tabs, TabsList, TabsTrigger, TabsContent }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/textarea.tsx
// ============================================================
import * as React from "react"

import { cn } from "@/lib/utils"

const Textarea = React.forwardRef<
  HTMLTextAreaElement,
  React.ComponentProps<"textarea">
>(({ className, ...props }, ref) => {
  return (
    <textarea
      className={cn(
        "flex min-h-[60px] w-full rounded-md border border-input bg-transparent px-3 py-2 text-base shadow-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
        className
      )}
      ref={ref}
      {...props}
    />
  )
})
Textarea.displayName = "Textarea"

export { Textarea }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/toaster.tsx
// ============================================================
import { useToast } from "@/hooks/use-toast"
import {
  Toast,
  ToastClose,
  ToastDescription,
  ToastProvider,
  ToastTitle,
  ToastViewport,
} from "@/components/ui/toast"

export function Toaster() {
  const { toasts } = useToast()

  return (
    <ToastProvider>
      {toasts.map(function ({ id, title, description, action, ...props }) {
        return (
          <Toast key={id} {...props}>
            <div className="grid gap-1">
              {title && <ToastTitle>{title}</ToastTitle>}
              {description && (
                <ToastDescription>{description}</ToastDescription>
              )}
            </div>
            {action}
            <ToastClose />
          </Toast>
        )
      })}
      <ToastViewport />
    </ToastProvider>
  )
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/toast.tsx
// ============================================================
import * as React from "react"
import * as ToastPrimitives from "@radix-ui/react-toast"
import { cva, type VariantProps } from "class-variance-authority"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const ToastProvider = ToastPrimitives.Provider

const ToastViewport = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Viewport>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Viewport>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Viewport
    ref={ref}
    className={cn(
      "fixed top-0 z-[100] flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-0 sm:right-0 sm:top-auto sm:flex-col md:max-w-[420px]",
      className
    )}
    {...props}
  />
))
ToastViewport.displayName = ToastPrimitives.Viewport.displayName

const toastVariants = cva(
  "group pointer-events-auto relative flex w-full items-center justify-between space-x-4 overflow-hidden rounded-md border p-6 pr-8 shadow-lg transition-all data-[swipe=cancel]:translate-x-0 data-[swipe=end]:translate-x-[var(--radix-toast-swipe-end-x)] data-[swipe=move]:translate-x-[var(--radix-toast-swipe-move-x)] data-[swipe=move]:transition-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[swipe=end]:animate-out data-[state=closed]:fade-out-80 data-[state=closed]:slide-out-to-right-full data-[state=open]:slide-in-from-top-full data-[state=open]:sm:slide-in-from-bottom-full",
  {
    variants: {
      variant: {
        default: "border bg-background text-foreground",
        destructive:
          "destructive group border-destructive bg-destructive text-destructive-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

const Toast = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Root>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Root> &
    VariantProps<typeof toastVariants>
>(({ className, variant, ...props }, ref) => {
  return (
    <ToastPrimitives.Root
      ref={ref}
      className={cn(toastVariants({ variant }), className)}
      {...props}
    />
  )
})
Toast.displayName = ToastPrimitives.Root.displayName

const ToastAction = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Action>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Action>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Action
    ref={ref}
    className={cn(
      "inline-flex h-8 shrink-0 items-center justify-center rounded-md border bg-transparent px-3 text-sm font-medium ring-offset-background transition-colors hover:bg-secondary focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 group-[.destructive]:border-muted/40 group-[.destructive]:hover:border-destructive/30 group-[.destructive]:hover:bg-destructive group-[.destructive]:hover:text-destructive-foreground group-[.destructive]:focus:ring-destructive",
      className
    )}
    {...props}
  />
))
ToastAction.displayName = ToastPrimitives.Action.displayName

const ToastClose = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Close>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Close>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Close
    ref={ref}
    className={cn(
      "absolute right-2 top-2 rounded-md p-1 text-foreground/50 opacity-0 transition-opacity hover:text-foreground focus:opacity-100 focus:outline-none focus:ring-2 group-hover:opacity-100 group-[.destructive]:text-red-300 group-[.destructive]:hover:text-red-50 group-[.destructive]:focus:ring-red-400 group-[.destructive]:focus:ring-offset-red-600",
      className
    )}
    toast-close=""
    {...props}
  >
    <X className="h-4 w-4" />
  </ToastPrimitives.Close>
))
ToastClose.displayName = ToastPrimitives.Close.displayName

const ToastTitle = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Title>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Title>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Title
    ref={ref}
    className={cn("text-sm font-semibold", className)}
    {...props}
  />
))
ToastTitle.displayName = ToastPrimitives.Title.displayName

const ToastDescription = React.forwardRef<
  React.ElementRef<typeof ToastPrimitives.Description>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitives.Description>
>(({ className, ...props }, ref) => (
  <ToastPrimitives.Description
    ref={ref}
    className={cn("text-sm opacity-90", className)}
    {...props}
  />
))
ToastDescription.displayName = ToastPrimitives.Description.displayName

type ToastProps = React.ComponentPropsWithoutRef<typeof Toast>

type ToastActionElement = React.ReactElement<typeof ToastAction>

export {
  type ToastProps,
  type ToastActionElement,
  ToastProvider,
  ToastViewport,
  Toast,
  ToastTitle,
  ToastDescription,
  ToastClose,
  ToastAction,
}


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/toggle-group.tsx
// ============================================================
"use client"

import * as React from "react"
import * as ToggleGroupPrimitive from "@radix-ui/react-toggle-group"
import { type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"
import { toggleVariants } from "@/components/ui/toggle"

const ToggleGroupContext = React.createContext<
  VariantProps<typeof toggleVariants>
>({
  size: "default",
  variant: "default",
})

const ToggleGroup = React.forwardRef<
  React.ElementRef<typeof ToggleGroupPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ToggleGroupPrimitive.Root> &
    VariantProps<typeof toggleVariants>
>(({ className, variant, size, children, ...props }, ref) => (
  <ToggleGroupPrimitive.Root
    ref={ref}
    className={cn("flex items-center justify-center gap-1", className)}
    {...props}
  >
    <ToggleGroupContext.Provider value={{ variant, size }}>
      {children}
    </ToggleGroupContext.Provider>
  </ToggleGroupPrimitive.Root>
))

ToggleGroup.displayName = ToggleGroupPrimitive.Root.displayName

const ToggleGroupItem = React.forwardRef<
  React.ElementRef<typeof ToggleGroupPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof ToggleGroupPrimitive.Item> &
    VariantProps<typeof toggleVariants>
>(({ className, children, variant, size, ...props }, ref) => {
  const context = React.useContext(ToggleGroupContext)

  return (
    <ToggleGroupPrimitive.Item
      ref={ref}
      className={cn(
        toggleVariants({
          variant: context.variant || variant,
          size: context.size || size,
        }),
        className
      )}
      {...props}
    >
      {children}
    </ToggleGroupPrimitive.Item>
  )
})

ToggleGroupItem.displayName = ToggleGroupPrimitive.Item.displayName

export { ToggleGroup, ToggleGroupItem }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/toggle.tsx
// ============================================================
import * as React from "react"
import * as TogglePrimitive from "@radix-ui/react-toggle"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const toggleVariants = cva(
  "inline-flex items-center justify-center gap-2 rounded-md text-sm font-medium transition-colors hover:bg-muted hover:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 data-[state=on]:bg-accent data-[state=on]:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        outline:
          "border border-input bg-transparent shadow-sm hover:bg-accent hover:text-accent-foreground",
      },
      size: {
        default: "h-9 px-2 min-w-9",
        sm: "h-8 px-1.5 min-w-8",
        lg: "h-10 px-2.5 min-w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

const Toggle = React.forwardRef<
  React.ElementRef<typeof TogglePrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof TogglePrimitive.Root> &
    VariantProps<typeof toggleVariants>
>(({ className, variant, size, ...props }, ref) => (
  <TogglePrimitive.Root
    ref={ref}
    className={cn(toggleVariants({ variant, size, className }))}
    {...props}
  />
))

Toggle.displayName = TogglePrimitive.Root.displayName

export { Toggle, toggleVariants }


// ============================================================
// FILE: artifacts/sentinel-mesh/src/components/ui/tooltip.tsx
// ============================================================
"use client"

import * as React from "react"
import * as TooltipPrimitive from "@radix-ui/react-tooltip"

import { cn } from "@/lib/utils"

const TooltipProvider = TooltipPrimitive.Provider

const Tooltip = TooltipPrimitive.Root

const TooltipTrigger = TooltipPrimitive.Trigger

const TooltipContent = React.forwardRef<
  React.ElementRef<typeof TooltipPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TooltipPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <TooltipPrimitive.Portal>
    <TooltipPrimitive.Content
      ref={ref}
      sideOffset={sideOffset}
      className={cn(
        "z-50 overflow-hidden rounded-md bg-primary px-3 py-1.5 text-xs text-primary-foreground animate-in fade-in-0 zoom-in-95 data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 origin-[--radix-tooltip-content-transform-origin]",
        className
      )}
      {...props}
    />
  </TooltipPrimitive.Portal>
))
TooltipContent.displayName = TooltipPrimitive.Content.displayName

export { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider }


// ============================================================
// END OF FILE
// ============================================================
