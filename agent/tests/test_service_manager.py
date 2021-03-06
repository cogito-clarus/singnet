#
# tests/test_service_manager.py - unit test for the service manager.
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

import logging

import pytest

import demo
from sn_agent import ontology
from sn_agent.log import setup_logging
from sn_agent.service_adapter import setup_service_manager, ServiceManager
from sn_agent.test.mocks import MockApp

log = logging.getLogger(__name__)


@pytest.fixture
def app():
    app = MockApp()
    ontology.setup_ontology(app)
    return app


def check_adapter(service_manager: ServiceManager, service_id: int, klass):
    service_adapter = service_manager.get_service_adapter_for_id(service_id)
    assert (not service_adapter is None)
    assert (isinstance(service_adapter, klass))


def test_service_manager(app):
    print()
    setup_logging()
    log.debug("--- test_service_manager ---")
    setup_service_manager(app)

    # Excercise the service manager methods.
    assert (not app['service_manager'] is None)
    service_manager = app['service_manager']

    check_adapter(service_manager, ontology.DOCUMENT_SUMMARIZER_ID, demo.document_summarizer.DocumentSummarizer)
    check_adapter(service_manager, ontology.ENTITY_EXTRACTER_ID, demo.entity_extracter.EntityExtracter)
    check_adapter(service_manager, ontology.FACE_RECOGNIZER_ID, demo.face_recognizer.FaceRecognizer)
    check_adapter(service_manager, ontology.TEXT_SUMMARIZER_ID, demo.text_summarizer.TextSummarizer)
    check_adapter(service_manager, ontology.VIDEO_SUMMARIZER_ID, demo.video_summarizer.VideoSummarizer)
    check_adapter(service_manager, ontology.WORD_SENSE_DISAMBIGUATER_ID, demo.word_sense_disambiguater.WordSenseDisambiguater)

    service_adapter = service_manager.get_service_adapter_for_id(ontology.DOCUMENT_SUMMARIZER_ID)
    assert (not service_adapter is None)
    assert (isinstance(service_adapter, demo.document_summarizer.DocumentSummarizer))

    service_adapter = service_manager.get_service_adapter_for_id(ontology.ENTITY_EXTRACTER_ID)
    assert (not service_adapter is None)
    assert (isinstance(service_adapter, demo.entity_extracter.EntityExtracter))

    service_adapter = service_manager.get_service_adapter_for_id(ontology.FACE_RECOGNIZER_ID)
    assert (not service_adapter is None)
    assert (isinstance(service_adapter, demo.face_recognizer.FaceRecognizer))

    service_adapter = service_manager.get_service_adapter_for_id(ontology.TEXT_SUMMARIZER_ID)
    assert (not service_adapter is None)
    assert (isinstance(service_adapter, demo.text_summarizer.TextSummarizer))

    service_adapter = service_manager.get_service_adapter_for_id(ontology.VIDEO_SUMMARIZER_ID)
    assert (not service_adapter is None)
    assert (isinstance(service_adapter, demo.video_summarizer.VideoSummarizer))

    service_adapter = service_manager.get_service_adapter_for_id(ontology.WORD_SENSE_DISAMBIGUATER_ID)
    assert (not service_adapter is None)
    assert (isinstance(service_adapter, demo.word_sense_disambiguater.WordSenseDisambiguater))


def test_start_stop_services(app):
    print()
    setup_logging()
    log.debug("")
    log.debug("--- test_start_stop_services ---")
    setup_service_manager(app)

    # Start and stop some services.
    assert (not app['service_manager'] is None)
    service_manager = app['service_manager']
    service_manager.start(ontology.DOCUMENT_SUMMARIZER_ID)
    service_manager.start(ontology.WORD_SENSE_DISAMBIGUATER_ID)
    service_manager.start(ontology.ENTITY_EXTRACTER_ID)

    service_manager.stop(ontology.ENTITY_EXTRACTER_ID)
    service_manager.stop(ontology.WORD_SENSE_DISAMBIGUATER_ID)
    service_manager.stop(ontology.DOCUMENT_SUMMARIZER_ID)
