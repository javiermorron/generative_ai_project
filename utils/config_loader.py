import yaml
import os

class Config:
    def __init__(self, path='config/model_config.yaml'):
        with open(path, 'r') as f:
            raw_config = yaml.safe_load(f)
        self.llms = self._inject_env(raw_config.get('llms', {}))
        self.image_models = self._inject_env(raw_config.get('image_models', {}))
        self.audio_models = self._inject_env(raw_config.get('audio_models', {}))

    def _inject_env(self, section):
        # Reemplaza variables tipo ${VAR_NAME} por os.environ['VAR_NAME']
        if isinstance(section, dict):
            return {k: self._inject_env(v) for k, v in section.items()}
        elif isinstance(section, list):
            return [self._inject_env(item) for item in section]
        elif isinstance(section, str) and section.startswith("${") and section.endswith("}"):
            var_name = section[2:-1]
            return os.getenv(var_name, f"<<MISSING ENV: {var_name}>>")
        return section

# Ejemplo de uso
if __name__ == "__main__":
    config = Config()
    print("GPT Model:", config.llms['gpt']['model'])
    print("Claude Endpoint:", config.llms['claude']['endpoint'])
