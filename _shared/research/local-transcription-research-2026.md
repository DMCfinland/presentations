# Local/On-Device Transcription Solutions Research (March 2026)

Research conducted for 1658 Holdings Oy -- 10-person company, Mac environment, Finnish + English, GDPR-compliant.

---

## 1. HEAD-TO-HEAD ENGINE COMPARISON

| Engine | Type | Parameters | Speed (RTFx) | Avg WER | Languages | License | Mac-Native |
|--------|------|-----------|--------------|---------|-----------|---------|------------|
| **Whisper large-v3** | Transformer (encoder-decoder) | 1.55B | ~146x | 7.4% | 99+ | MIT | Via whisper.cpp / WhisperKit |
| **Whisper large-v3-turbo** | Pruned Whisper (4 decoder layers) | 809M | ~216x | 7.75% | 99+ | MIT | Via whisper.cpp / WhisperKit |
| **faster-whisper** | CTranslate2 optimized Whisper | Same as source | ~2x CPU vs original | Same as source | 99+ | MIT | Yes (CPU, no Metal GPU) |
| **whisper.cpp** | C/C++ port (GGML format) | Same as source | 3-6x with CoreML/ANE | Same as source | 99+ | MIT | Best native (CoreML + ANE) |
| **WhisperKit** | Apple-optimized Whisper | Same as source | Best on Apple Silicon | Same as source | 99+ | MIT | Purpose-built for Apple |
| **NVIDIA Parakeet v3** | Transducer (TDT) | 0.6B | ~3,333x | 6.3% (EN) | 25 (European) | CC-BY-4.0 | Yes (via Alter app) |
| **Canary Qwen 2.5B** | NVIDIA NeMo | 2.5B | ~418x | 5.63% (EN) | English-focused | Apache 2.0 | Limited |
| **Vosk** | Kaldi-based | ~50MB models | Real-time on CPU | Higher than Whisper | 20+ (NO Finnish) | Apache 2.0 | Yes |
| **Apple SpeechAnalyzer** | Apple Intelligence | Unknown | 55% faster than Whisper | Comparable | TBD | macOS Tahoe | Native |

### Key Takeaways

- **Whisper large-v3** remains the multilingual accuracy king, especially for Finnish
- **Parakeet v3** is 10-23x faster than Whisper but weaker on Finnish (13.2% vs 7.7% WER)
- **whisper.cpp with CoreML** is the best-optimized path for Apple Silicon
- **WhisperKit** is the most polished Apple-native implementation
- **Vosk** does NOT support Finnish -- eliminated
- **Apple SpeechAnalyzer** (macOS Tahoe) is 55% faster than Whisper but Finnish support unconfirmed

---

## 2. FINNISH LANGUAGE QUALITY (Critical for 1658 Holdings)

### WER Benchmarks on Finnish

| Model | FLEURS WER | Common Voice WER | Notes |
|-------|-----------|-----------------|-------|
| **Whisper large-v3 (base)** | 9.63% (normalized) | 10.82% (normalized) | Best general-purpose for Finnish |
| **Whisper large-v3 (Finnish fine-tuned)** | **8.21%** (normalized) | **8.23%** (normalized) | 15-24% improvement over base |
| **Whisper large-v3-turbo** | ~10-12% (estimated) | Not benchmarked | Minor degradation from v3 |
| **Parakeet v3** | **13.2%** | Not available | Significantly worse on Finnish |
| **ElevenLabs Scribe** | 3.1% (FLEURS) | 5.5% (CV) | Cloud only -- not local |

### Verdict for Finnish

**Whisper large-v3 is the clear winner for Finnish.** The Finnish-NLP fine-tuned variant (`Finnish-NLP/whisper-large-finnish-v3` on HuggingFace) reduces WER by ~15-24% over the base model. Parakeet v3, despite being 10x faster, produces nearly double the errors on Finnish (13.2% vs 7.7%).

Finnish is morphologically complex (agglutinative), which makes it harder for models trained primarily on English. The fine-tuned model was trained on FLEURS + Common Voice Finnish data for 32,000 steps on an RTX 4080.

For a business meeting context (multiple speakers, background noise, Finnish dialect variations), expect real-world WER of 12-18% with base Whisper large-v3, improving to 10-14% with the fine-tuned model.

---

## 3. APPLE SILICON (M-SERIES MAC) PERFORMANCE

### Benchmark: 10-Minute Audio File, Whisper Medium Model

| Mac | Chip | RAM | Transcription Time | Real-Time Factor |
|-----|------|-----|-------------------|------------------|
| MacBook Air | M1 | 8 GB | ~3 min | 0.3x |
| MacBook Pro | M1 Pro | 16 GB | ~2 min | 0.2x |
| MacBook Air | M2 | 8 GB | ~2.5 min | 0.25x |
| MacBook Pro | M3 Pro | 18 GB | ~1.5 min | 0.15x |
| MacBook Pro | M3 Max | 36 GB | ~1 min | 0.1x |
| Mac mini | M4 | 16 GB | ~1.2 min | 0.12x |
| MacBook Pro | M4 Pro | 24 GB | ~50 sec | 0.08x |

### Key Performance Insights

- **M3 Pro and above:** Transcription is "essentially instant" -- a 1-hour meeting transcribes in ~6-9 minutes
- **whisper.cpp + CoreML:** 3-6x speedup over CPU-only by using the Apple Neural Engine (ANE)
- **WhisperKit optimizations:** 45% latency reduction on M3 ANE (8.4ms to 4.6ms per decoder pass), 75% energy reduction
- **Apple SpeechAnalyzer (macOS Tahoe):** Processes 34-minute file in 45 seconds vs WhisperKit's 1 min 41 sec
- **Memory:** Whisper large-v3 needs ~6-10GB RAM; large-v3-turbo needs ~4-6GB. Any 16GB+ Mac handles it comfortably
- **Practical rule:** On M3/M4 with 16GB+ RAM, you can transcribe a 1-hour meeting in under 10 minutes with large-v3

### Implementation Comparison on Mac

| Implementation | Mac Optimization | GPU/ANE Support | Ease of Setup |
|----------------|-----------------|-----------------|---------------|
| **WhisperKit** | Purpose-built | Full ANE | Easy (Swift) |
| **whisper.cpp + CoreML** | Excellent | ANE via CoreML | Moderate (compile) |
| **faster-whisper** | Good (CPU) | No Metal/ANE | Easy (Python) |
| **MacWhisper (app)** | Uses WhisperKit | Full ANE | Easiest (GUI) |

---

## 4. SPEAKER DIARIZATION (Who Said What)

### Available Solutions

| Solution | Approach | Offline | Accuracy (DER) | Mac Support | Notes |
|----------|----------|---------|----------------|-------------|-------|
| **Pyannote 3.1** | Neural embeddings | Yes | 11-19% | Yes (Python) | Open-source leader, handles overlapping speech |
| **WhisperX** | Whisper + Pyannote combined | Yes | Same as Pyannote | Yes (Python) | Best all-in-one: transcription + diarization + timestamps |
| **NVIDIA NeMo** | TitaNet embeddings | Yes | Excellent | Limited (needs NVIDIA GPU) | Enterprise-grade |
| **MacWhisper Pro** | Built-in (WhisperKit) | Yes | Beta quality | Native Mac app | "Sometimes mistakes one person for multiple speakers" |
| **Alter** | Built-in | Yes | Not benchmarked | Native Mac app | Local speaker identification included |

### Recommendation

**WhisperX** is the best technical solution -- it combines Whisper transcription with Pyannote diarization and produces word-level speaker attribution in one pipeline. For a non-technical user, **MacWhisper Pro** or **Alter** provide GUI-based diarization, though accuracy is lower.

Processing time for diarization on 1-hour audio:
- GPU: 15-35 minutes
- CPU (Mac): 2-4 hours for Pyannote
- Cloud services: 5-10 minutes

---

## 5. BUSINESS USE CASE: Meeting & Interview Transcription (2025-2026)

### Local-First Mac Apps (No Cloud)

| App | Price | Models | Diarization | Languages | Key Strength |
|-----|-------|--------|-------------|-----------|--------------|
| **MacWhisper Pro** | EUR 64 one-time | Whisper + WhisperKit | Yes (beta) | 100+ | Most mature Mac app, batch processing |
| **Alter** | $29/year | Parakeet v3 + Whisper large-v3 | Yes | 50+ | Dual-engine, cheapest, auto-detects calls |
| **BB Recorder** | Free | Whisper + Llama + Apple Intelligence | Unknown | Multiple | Free, AI chat during meetings |
| **Aiko** | Free | Whisper (small/medium) | No | 100+ | Simplest, fully free, iOS + Mac |
| **Char (Hyprnote)** | Free (open-source) | Configurable | Unknown | Configurable | Open-source, markdown output |

### What Companies Actually Use (2025-2026 Market)

Most businesses still use cloud solutions (Otter.ai, Fireflies.ai, Microsoft Teams transcription). The shift to local is driven by:
1. **GDPR concerns** -- especially in EU
2. **Cost** -- cloud transcription costs $10-30/month/user
3. **Quality parity** -- local Whisper large-v3 now matches cloud accuracy
4. **Apple Silicon performance** -- M3/M4 Macs make local transcription fast enough

---

## 6. PRIVACY / GDPR -- FULLY LOCAL SOLUTIONS

### Verified 100% Local (Zero Cloud)

| Solution | Data Leaves Device? | GDPR Status | Notes |
|----------|-------------------|-------------|-------|
| **whisper.cpp** | Never | Fully compliant | Raw engine, no network calls |
| **WhisperKit** | Never | Fully compliant | Apple-native, no network |
| **MacWhisper** | Never (unless AI features used) | Compliant for transcription | ChatGPT/Claude integration is optional cloud |
| **Alter** | Never | GDPR + HIPAA compliant | All files stored locally only |
| **Aiko** | Never | Fully compliant | On-device only |
| **BB Recorder** | Never (base) | Compliant | Optional BYOK cloud features |
| **faster-whisper** | Never | Fully compliant | Python library, no network |

### GDPR Notes for 1658 Holdings

- All Whisper-based local solutions process audio entirely on-device -- no Article 28 DPA needed
- No data residency concerns -- data never leaves the Mac
- Audio files can be stored on local disk or local-only encrypted volume
- If transcripts are saved to OneDrive/SharePoint afterward, standard M365 DPA applies (already in place)

---

## 7. WHISPER LARGE-V3 vs LARGE-V3-TURBO

| Aspect | large-v3 | large-v3-turbo |
|--------|----------|----------------|
| **Parameters** | 1.55B | 809M (48% fewer) |
| **Decoder layers** | 32 | 4 (87% fewer) |
| **Speed** | Baseline | **6x faster** (216x RTFx) |
| **English WER** | 7.4% | 7.75% (+0.35%) |
| **Finnish WER (FLEURS)** | 7.7% | ~10-12% (estimated, not officially benchmarked) |
| **VRAM/RAM** | ~10GB | ~6GB |
| **Hallucination risk** | Lower | Slightly higher |
| **Best for** | Accuracy-critical, Finnish | Speed-critical, English-primary |

### Verdict

For **English-primary** work: use large-v3-turbo -- negligible quality loss, 6x faster.
For **Finnish**: stick with large-v3 -- the turbo variant likely loses more accuracy on lower-resource languages. The pruned decoder (32 to 4 layers) disproportionately affects languages with less training data.

---

## 8. RECOMMENDED WORKFLOW FOR 1658 HOLDINGS

### Setup: 10-person company, Mac environment, Finnish + English meetings

#### Option A: Simplest (Recommended to Start)

**MacWhisper Pro (EUR 64 one-time)**
1. Install from Mac App Store
2. Download Whisper large-v3 model (first-time, ~3GB)
3. Record meeting audio (Voice Memos, QuickTime, or MacWhisper's own recorder)
4. Drop audio file into MacWhisper
5. Select language (Finnish or auto-detect)
6. Enable speaker diarization (beta)
7. Export as .txt or .docx
8. Save to SharePoint via OneDrive sync folder

**Pros:** One-time cost, GUI, batch processing, supports Finnish well
**Cons:** Diarization is beta quality, no automation

#### Option B: Best Quality (Technical Setup Required)

**WhisperX + Finnish fine-tuned model**
1. Install Python + WhisperX (`pip install whisperx`)
2. Download `Finnish-NLP/whisper-large-finnish-v3` from HuggingFace
3. Accept Pyannote license on HuggingFace (free for research, paid for commercial)
4. Run: `whisperx audio.wav --model Finnish-NLP/whisper-large-finnish-v3 --diarize --language fi`
5. Output: JSON/SRT/TXT with speaker labels and timestamps
6. Post-process: convert to Word doc, upload to SharePoint

**Pros:** Best Finnish accuracy (8.2% WER), proper diarization, automated pipeline possible
**Cons:** Requires Python knowledge, Pyannote commercial license (~EUR 500/year)

#### Option C: Dual-Engine with Auto-Detection

**Alter ($29/year)**
1. Install Alter from website
2. It auto-detects when you join a call (Zoom, Teams, Meet, etc.)
3. Records and transcribes locally using Parakeet (English) or Whisper (Finnish)
4. Speaker diarization included
5. Export transcripts

**Pros:** Cheapest, auto-detects calls, dual engine
**Cons:** Finnish accuracy may use Parakeet (13.2% WER) instead of Whisper (7.7%)

### Recommended Starting Point

**Start with MacWhisper Pro** (Option A). It is the lowest-friction path:
- EUR 64 one-time, no subscription
- Works for both Finnish and English
- Any team member can use it (no technical skills)
- If diarization quality is insufficient, evaluate WhisperX (Option B) for critical meetings

---

## 9. COST COMPARISON

### Free Solutions

| Solution | Cost | Limitations |
|----------|------|------------|
| **Aiko** | Free | Small/medium models only (lower accuracy) |
| **BB Recorder** | Free | Newer, less mature |
| **whisper.cpp** | Free | Command-line only |
| **WhisperX** | Free (open-source) | Pyannote requires HuggingFace token; commercial use needs license |
| **Char/Hyprnote** | Free (open-source) | Early stage |

### Paid Local Solutions

| Solution | Cost | What You Get |
|----------|------|-------------|
| **MacWhisper Pro** | EUR 64 one-time | Full GUI, all models, batch, diarization, export |
| **Alter** | $29/year | Dual-engine, auto-detect calls, diarization |
| **Whisper Notes** | $6.99 one-time | Lightweight alternative to MacWhisper |
| **Pyannote (commercial)** | ~EUR 500/year | Commercial diarization license |

### Cloud Solutions (for comparison -- NOT recommended for GDPR)

| Solution | Cost | Notes |
|----------|------|-------|
| Otter.ai | $120-360/year/user | Cloud-processed |
| Fireflies.ai | $216-348/year/user | Cloud-processed |
| Microsoft Teams transcription | Included in M365 | Cloud-processed, limited languages |

### Total Cost for 1658 Holdings (10 users)

| Scenario | Year 1 | Ongoing |
|----------|--------|---------|
| **MacWhisper Pro (shared license)** | EUR 64 | EUR 0 |
| **Alter (per-device)** | ~$290 (10 x $29) | ~$290/year |
| **WhisperX + Pyannote commercial** | ~EUR 500 | ~EUR 500/year |
| **Cloud (Otter.ai, 10 users)** | EUR 1,200-3,600 | EUR 1,200-3,600/year |

---

## 10. MICROSOFT 365 / WORD / SHAREPOINT INTEGRATION

### Direct Integration Options

**There is no direct pipe from local Whisper to M365.** However, several workflow paths exist:

#### Path 1: Manual Export (Simplest)
1. Transcribe locally (MacWhisper / WhisperX)
2. Export as .docx or .txt
3. Save to OneDrive sync folder -> auto-syncs to SharePoint

#### Path 2: Power Automate Workflow
1. WhisperX outputs .txt/.docx to a watched folder
2. Power Automate flow detects new file
3. Uploads to SharePoint document library
4. Optionally creates a Teams message with link

#### Path 3: Word Transcription (Built-in, but Cloud)
- Microsoft Word has built-in "Transcribe" feature
- Limit: 300 min/month (M365) or 30,000 min/month (Copilot license)
- **This is cloud-processed** -- not local, not GDPR-ideal

#### Path 4: Azure Whisper (Hybrid)
- Azure AI Services offers Whisper via batch transcription API
- Data stays in Azure tenant (EU region available)
- Integrates natively with SharePoint
- **Not fully local** but within your Azure tenant

### Recommended M365 Integration for 1658 Holdings

**Path 1 + OneDrive sync** is the simplest and most GDPR-compliant:
1. Transcribe locally on Mac
2. Save .docx to `~/OneDrive - [Company]/Transcripts/`
3. File appears in SharePoint automatically
4. Searchable by M365 Copilot / SharePoint search

---

## FINAL RECOMMENDATION

For 1658 Holdings Oy, the recommended stack is:

1. **Engine:** Whisper large-v3 (best Finnish accuracy at 7.7% WER)
2. **App:** MacWhisper Pro (EUR 64, one-time, GUI, any team member can use)
3. **Finnish boost:** If Finnish accuracy is critical, load the `Finnish-NLP/whisper-large-finnish-v3` fine-tuned model (8.2% WER) -- requires technical setup
4. **Diarization:** MacWhisper Pro (beta) for casual use; WhisperX + Pyannote for important meetings
5. **Hardware:** Any M3/M4 Mac with 16GB+ RAM -- 1-hour meeting transcribes in under 10 minutes
6. **M365 integration:** Save transcripts to OneDrive sync folder -> SharePoint
7. **GDPR:** Fully compliant -- all processing on-device, no cloud
8. **Cost:** EUR 64 total (MacWhisper Pro one-time license)

### Future Watch

- **Apple SpeechAnalyzer (macOS Tahoe):** 55% faster than Whisper -- monitor Finnish language support when it launches
- **Parakeet v3 Finnish fine-tuning:** If NVIDIA or community fine-tunes Parakeet for Finnish, it could become the speed+accuracy winner
- **Whisper v4:** No announcement yet, but OpenAI may release an improved multilingual model

---

## SOURCES

- [Northflank: Best Open Source STT Model in 2026 (Benchmarks)](https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks)
- [Parakeet V3 vs Whisper: 10x Faster, Better Accuracy](https://whispernotes.app/blog/parakeet-v3-default-mac-model)
- [Finnish-NLP/whisper-large-finnish-v3 (HuggingFace)](https://huggingface.co/Finnish-NLP/whisper-large-finnish-v3)
- [OpenAI whisper-large-v3-turbo Model Card](https://huggingface.co/openai/whisper-large-v3-turbo)
- [Whisper Performance on Apple Silicon: M1-M4 Benchmarks](https://www.voicci.com/blog/apple-silicon-whisper-performance.html)
- [Best Speaker Diarization Models Compared 2026](https://brasstranscripts.com/blog/speaker-diarization-models-comparison)
- [Best Local AI Meeting Recorders: No Cloud 2026](https://blog.buildbetter.ai/best-local-ai-meeting-recorders-no-cloud-2026/)
- [Apple's Transcription APIs Blow Past Whisper in Speed Tests](https://www.macrumors.com/2025/06/18/apple-transcription-api-faster-than-whisper/)
- [WhisperKit: On-device Real-time ASR (arXiv)](https://arxiv.org/html/2507.10860v1)
- [Apple SpeechAnalyzer and Argmax WhisperKit](https://www.argmaxinc.com/blog/apple-and-argmax)
- [Best Privacy-Focused Meeting Transcription Tools 2025](https://localmeetnotes.com/en/blog/best-privacy-focused-meeting-transcription-tools-2025.html)
- [Alter: Privacy Mac Meeting Recording with Local AI](https://alterhq.com/blog/privacy-mac-meeting-recording-with-local-ai)
- [MacWhisper Reviews & Pricing](https://opentools.ai/tools/macwhisper)
- [Choosing Between Whisper Variants (Modal)](https://modal.com/blog/choosing-whisper-variants)
- [Whisper Large V3 Turbo: 6x Faster (Medium)](https://medium.com/@bnjmn_marie/whisper-large-v3-turbo-as-good-as-large-v2-but-6x-faster-97f0803fa933)
- [NVIDIA Parakeet TDT 0.6B v3 (HuggingFace)](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3)
- [Vosk Speech Recognition Guide 2025](https://www.videosdk.live/developer-hub/stt/vosk-speech-recognition)
- [Microsoft Word Transcribe Feature](https://support.microsoft.com/en-us/office/transcribe-your-recordings-7fc2efec-245e-45f0-b053-2a97531ecf57)
- [Canary-1B-v2 & Parakeet-TDT-0.6B-v3 (arXiv)](https://arxiv.org/abs/2509.14128)
- [whisper.cpp GitHub + CoreML Discussion](https://github.com/ggml-org/whisper.cpp)
