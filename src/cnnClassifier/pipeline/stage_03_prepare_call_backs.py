from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.components.prepare_call_backs import PrepareCallback




STAGE_NAME = "Prepare Call Backs"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    
    
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
        
        
if __name__ == '__main__':
    try:
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
    except Exception as e:
        logger.exception(e)
        raise e