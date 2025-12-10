"""
Constants for Fastkoko TTS custom component
"""

DOMAIN = "fastkoko_tts"
CONF_API_KEY = "api_key"
CONF_DEFAULT_LANGUAGE = "default_language"
CONF_MODEL = "model"
CONF_VOICE = "voice"
CONF_SPEED = "speed"
CONF_URL = "url"
DEFAULT_URL = "https://kokoro-tts:8880/v1/audio/speech"
UNIQUE_ID = "unique_id"

LANGUAGES = {
    "es": "e",
    "en": "a",
    "fr": "f",
    "hi": "h",
    "it": "i",
    "pt": "p",
    "ja": "j",
    "zh": "z"
}
MODELS = ["kokoro"]
VOICES = [
    "af_alloy",
    "af_aoede",
    "af_bella",
    "af_heart",
    "af_jadzia",
    "af_jessica",
    "af_kore",
    "af_nicole",
    "af_nova",
    "af_river",
    "af_sarah",
    "af_sky",
    "af_v0",
    "af_v0bella",
    "af_v0irulan",
    "af_v0nicole",
    "af_v0sarah",
    "af_v0sky",
    "am_adam",
    "am_echo",
    "am_eric",
    "am_fenrir",
    "am_liam",
    "am_michael",
    "am_onyx",
    "am_puck",
    "am_santa",
    "am_v0adam",
    "am_v0gurney",
    "am_v0michael",
    "bf_alice",
    "bf_emma",
    "bf_lily",
    "bf_v0emma",
    "bf_v0isabella",
    "bm_daniel",
    "bm_fable",
    "bm_george",
    "bm_lewis",
    "bm_v0george",
    "bm_v0lewis",
    "ef_dora",
    "em_alex",
    "em_santa",
    "ff_siwis",
    "hf_alpha",
    "hf_beta",
    "hm_omega",
    "hm_psi",
    "if_sara",
    "im_nicola",
    "jf_alpha",
    "jf_gongitsune",
    "jf_nezumi",
    "jf_tebukuro",
    "jm_kumo",
    "pf_dora",
    "pm_alex",
    "pm_santa",
    "zf_xiaobei",
    "zf_xiaoni",
    "zf_xiaoxiao",
    "zf_xiaoyi",
    "zm_yunjian",
    "zm_yunxi",
    "zm_yunxia",
    "zm_yunyang"
]

# Supported languages (OpenAI TTS auto-detects from text, this list is for HA UI)
# Based on OpenAI Whisper model language support
SUPPORTED_LANGUAGES = [
    "af",  # Afrikaans
    "ar",  # Arabic
    "bg",  # Bulgarian
    "bn",  # Bengali
    "bs",  # Bosnian
    "ca",  # Catalan
    "cs",  # Czech
    "cy",  # Welsh
    "da",  # Danish
    "de",  # German
    "el",  # Greek
    "en",  # English
    "es",  # Spanish
    "et",  # Estonian
    "fa",  # Persian
    "fi",  # Finnish
    "fr",  # French
    "gl",  # Galician
    "he",  # Hebrew
    "hi",  # Hindi
    "hr",  # Croatian
    "hu",  # Hungarian
    "id",  # Indonesian
    "is",  # Icelandic
    "it",  # Italian
    "ja",  # Japanese
    "kk",  # Kazakh
    "ko",  # Korean
    "lt",  # Lithuanian
    "lv",  # Latvian
    "mk",  # Macedonian
    "ml",  # Malayalam
    "mr",  # Marathi
    "ms",  # Malay
    "nb",  # Norwegian Bokmål
    "nl",  # Dutch
    "pl",  # Polish
    "pt",  # Portuguese
    "ro",  # Romanian
    "ru",  # Russian
    "sk",  # Slovak
    "sl",  # Slovenian
    "sr",  # Serbian
    "sv",  # Swedish
    "sw",  # Swahili
    "ta",  # Tamil
    "te",  # Telugu
    "th",  # Thai
    "tl",  # Tagalog
    "tr",  # Turkish
    "uk",  # Ukrainian
    "ur",  # Urdu
    "vi",  # Vietnamese
    "zh",  # Chinese
]

CONF_CHIME_ENABLE = "chime"
CONF_CHIME_SOUND = "chime_sound"
CONF_NORMALIZE_AUDIO = "normalize_audio"
CONF_INSTRUCTIONS = "instructions"

# Toggle to snapshot & restore volumes
CONF_VOLUME_RESTORE = "volume_restore"

# Toggle to pause/resume media playback
CONF_PAUSE_PLAYBACK = "pause_playback"

# Profile name for sub-entries
CONF_PROFILE_NAME = "profile_name"

# Key for storing message-to-duration cache in hass.data
MESSAGE_DURATIONS_KEY = "message_durations"