import os

import hydra
from omegaconf import DictConfig
from pytorch_lightning import (
    LightningDataModule,
    LightningModule,
    Trainer,
    seed_everything,
)

from src import utils

# Get logger
log = utils.get_logger(__name__)


def test(config: DictConfig) -> None:
    """Evaluates given checkpoint on a testset.

    Args:
        config (DictConfig): Configuration composed by Hydra.

    Returns:
        None
    """

    # Set seed for random number generators in pytorch, numpy and python.random
    if config.get("seed"):
        seed_everything(config.seed, workers=True)

    # Convert relative ckpt path to absolute path if necessary
    if not os.path.isabs(config.ckpt_path):
        config.ckpt_path = os.path.join(
            hydra.utils.get_original_cwd(), config.ckpt_path
        )

    # Init lightning datamodule
    log.info(f"Instantiating datamodule <{config.datamodule._target_}>")
    datamodule: LightningDataModule = hydra.utils.instantiate(config.datamodule)

    # Init lightning model
    log.info(f"Instantiating model <{config.litmodule._target_}>")
    litmodule: LightningModule = hydra.utils.instantiate(config.litmodule)

    # Init lightning loggers List[LightningLoggerBase]
    logger = []
    if "logger" in config:
        for _, lg_conf in config.logger.items():
            if "_target_" in lg_conf:
                log.info(f"Instantiating logger <{lg_conf._target_}>")
                logger.append(hydra.utils.instantiate(lg_conf))

    # Init lightning trainer
    log.info(f"Instantiating trainer <{config.trainer._target_}>")
    trainer: Trainer = hydra.utils.instantiate(config.trainer, logger=logger)

    # Log hyperparameters
    if trainer.logger:
        trainer.logger.log_hyperparams({"ckpt_path": config.ckpt_path})

    log.info("Starting testing!")
    trainer.test(model=litmodule, datamodule=datamodule, ckpt_path=config.ckpt_path)
