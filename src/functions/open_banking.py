import requests

import config
from repositories.participants_repository import ParticipantsRepository


def _build_upsert_filters(org_document: dict):
    return {'organization_id': org_document.get('OrganisationId')}


def _build_doc_fields(org_document: dict):
    return {'set__organization_id': org_document.get('OrganisationId'),
            'set__organization_name': org_document.get('OrganisationName'),
            'set__discovery_url': org_document.get('AuthorisationServers', [{}])[0].get('OpenIDDiscoveryDocument')}


def retrieve_all_organizations():
    api_response = requests.get(config.OPEN_BANKING_API_URL)
    return api_response.json()


def save_organizations(repository: ParticipantsRepository):
    documents = retrieve_all_organizations()

    for document in documents:
        filters = _build_upsert_filters(document)
        fields = _build_doc_fields(document)

        repository.upsert_one(object=fields, filter=filters)
