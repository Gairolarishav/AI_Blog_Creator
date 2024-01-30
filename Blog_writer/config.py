OPENAI_API_KEY =  "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"

class Config(object):
    Debug =True
    Testing = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"

Config = {
    'development' : DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production' : DevelopmentConfig
}