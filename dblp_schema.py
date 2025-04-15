dblp_schema = {
  "ontology": {
    "title": "dblp RDF schema",
    "description": "This ontology describes the RDF representation of the contents of the dblp computer science bibliography.",
    "creator": "https://dblp.org",
    "abstract": "The dblp RDF schema is an ontology that models the semantic contents of the dblp computer science bibliography.",
    "versionIRI": "https://dblp.org/rdf/schema-2024-06-14",
    "versionInfo": "Fri 14 Jun 2024",
    "priorVersion": "https://dblp.org/rdf/schema-2023-10-17"
  },
  "classes": {
    "Entity": {
      "label": "Entity",
      "comment": "An abstract, identifiable entity in dblp.",
      "subClassOf": [
        "http://www.w3.org/2002/07/owl#Thing",
        "https://schema.org/Thing",
        "http://www.wikidata.org/entity/Q35120"
      ]
    },
    "Creator": {
      "label": "Creator",
      "comment": "A creator of a publication.",
      "subClassOf": [
        "#Entity",
        "http://id.loc.gov/ontologies/bibframe/Agent",
        "http://dbpedia.org/ontology/Agent",
        "http://purl.org/dc/terms/Agent",
        "http://xmlns.com/foaf/0.1/Agent",
        "http://www.wikidata.org/entity/Q24229398"
      ]
    },
    "AmbiguousCreator": {
      "label": "AmbiguousCreator",
      "comment": "Not an actual creator, but an ambiguous proxy for an unknown number of unrelated actual creators of the same name.",
      "subClassOf": [
        "#Creator",
        "http://www.wikidata.org/entity/Q48522"
      ]
    },
    "Person": {
      "label": "Person",
      "comment": "An actual person, who is a creator of a publication.",
      "subClassOf": [
        "#Creator"
      ],
      "equivalentClass": [
        "http://id.loc.gov/ontologies/bibframe/Person",
        "http://dbpedia.org/ontology/Person",
        "http://xmlns.com/foaf/0.1/Person",
        "https://schema.org/Person",
        "http://www.wikidata.org/entity/Q5"
      ]
    },
    "Group": {
      "label": "Group",
      "comment": "A creator alias used by a group or consortium of persons.",
      "subClassOf": [
        "#Creator"
      ],
      "equivalentClass": [
        "http://id.loc.gov/ontologies/bibframe/Organisation",
        "http://dbpedia.org/ontology/Organisation",
        "http://xmlns.com/foaf/0.1/Group",
        "https://schema.org/Organization",
        "http://www.wikidata.org/entity/Q43229"
      ]
    },
    "Signature": {
      "label": "Signature",
      "comment": "The information that links a publication to a creator."
    },
    "AuthorSignature": {
      "label": "AuthorSignature",
      "comment": "The information that links a publication to an author.",
      "subClassOf": [
        "#Signature"
      ]
    },
    "EditorSignature": {
      "label": "EditorSignature",
      "comment": "The information that links a publication to an editor.",
      "subClassOf": [
        "#Signature"
      ]
    },
    "Publication": {
      "label": "Publication",
      "comment": "A publication.",
      "subClassOf": [
        "#Entity",
        "http://id.loc.gov/ontologies/bibframe/Work",
        "http://dbpedia.org/ontology/WrittenWork",
        "http://purl.org/dc/terms/BibliographicResource",
        "http://purl.org/ontology/bibo/Document",
        "http://xmlns.com/foaf/0.1/Document",
        "https://schema.org/CreativeWork"
      ],
      "equivalentClass": [
        "http://www.wikidata.org/entity/Q591041"
      ]
    },
    "Book": {
      "label": "Book",
      "comment": "A book or a thesis.",
      "subClassOf": [
        "#Publication"
      ],
      "equivalentClass": [
        "http://dbpedia.org/ontology/Book",
        "https://schema.org/Book",
        "http://www.wikidata.org/entity/Q571",
        "http://purl.org/ontology/bibo/Book"
      ]
    },
    "Article": {
      "label": "Article",
      "comment": "A journal article.",
      "subClassOf": [
        "#Publication",
        "https://schema.org/Article",
        "http://www.wikidata.org/entity/Q13442814",
        "http://purl.org/ontology/bibo/AcademicArticle"
      ],
      "equivalentClass": [
        "http://dbpedia.org/ontology/Article"
      ]
    },
    "Inproceedings": {
      "label": "Inproceedings",
      "comment": "A conference or workshop paper.",
      "subClassOf": [
        "#Publication",
        "https://schema.org/Chapter",
        "http://www.wikidata.org/entity/Q13442814",
        "http://purl.org/ontology/bibo/AcademicArticle"
      ]
    },
    "Incollection": {
      "label": "Incollection",
      "comment": "A part/chapter in a book or a collection.",
      "subClassOf": [
        "#Publication",
        "https://schema.org/Chapter",
        "http://www.wikidata.org/entity/Q13442814",
        "http://purl.org/ontology/bibo/AcademicArticle"
      ]
    },
    "Editorship": {
      "label": "Editorship",
      "comment": "An edited publication.",
      "subClassOf": [
        "#Publication"
      ]
    },
    "Reference": {
      "label": "Reference",
      "comment": "A reference work entry.",
      "subClassOf": [
        "#Publication"
      ],
      "equivalentClass": [
        "http://www.wikidata.org/entity/Q10389811",
        "http://purl.org/ontology/bibo/ReferenceSource"
      ]
    },
    "Data": {
      "label": "Data",
      "comment": "Research data or artifacts.",
      "subClassOf": [
        "#Publication"
      ],
      "equivalentClass": [
        "https://schema.org/Dataset",
        "http://www.wikidata.org/entity/Q17051824"
      ]
    },
    "Informal": {
      "label": "Informal",
      "comment": "An informal or other publication.",
      "subClassOf": [
        "#Publication"
      ],
      "equivalentClass": [
        "http://www.wikidata.org/entity/Q1148359"
      ]
    },
    "Withdrawn": {
      "label": "Withdrawn",
      "comment": "A withdrawn publication item.",
      "subClassOf": [
        "#Publication"
      ],
      "equivalentClass": [
        "http://www.wikidata.org/entity/Q45182324"
      ]
    },
    "VersionRelation": {
      "label": "VersionRelation",
      "comment": "The information that links an (instanced) publication version to its general (concept) publication."
    },
    "Stream": {
      "label": "Stream",
      "comment": "A publication stream, i.e., a venue or source for publications.",
      "subClassOf": [
        "#Entity",
        "https://schema.org/CreativeWorkSeries"
      ]
    },
    "Conference": {
      "label": "Conference",
      "comment": "A conference or workshop series.",
      "subClassOf": [
        "#Stream"
      ],
      "equivalentClass": [
        "http://www.wikidata.org/entity/Q47258130"
      ]
    },
    "Journal": {
      "label": "Journal",
      "comment": "A periodically published journal.",
      "subClassOf": [
        "#Stream",
        "https://schema.org/Periodical"
      ],
      "equivalentClass": [
        "http://www.wikidata.org/entity/Q5633421"
      ]
    },
    "Series": {
      "label": "Series",
      "comment": "A published series of volumes.",
      "subClassOf": [
        "#Stream"
      ],
      "equivalentClass": [
        "http://www.wikidata.org/entity/Q2217301"
      ]
    },
    "Repository": {
      "label": "Repository",
      "comment": "A source of data and/or artifact publications.",
      "subClassOf": [
        "#Stream"
      ],
      "equivalentClass": [
        "http://www.wikidata.org/entity/Q5227240"
      ]
    }
  },
  "properties": {
    "identifier": {
      "label": "identifier",
      "comment": "An abstract identifier.",
      "domain": "#Entity",
      "range": "http://www.w3.org/2001/XMLSchema#anyUri",
      "equivalentProperty": [
        "http://id.loc.gov/vocabulary/identifiers/id"
      ]
    },
    "wikidata": {
      "label": "wikidata",
      "comment": "A wikidata item.",
      "domain": "#Entity",
      "range": "http://www.w3.org/2001/XMLSchema#anyUri",
      "subPropertyOf": [
        "#identifier"
      ],
      "equivalentProperty": [
        "http://purl.org/spar/datacite/wikidata",
        "http://id.loc.gov/vocabulary/identifiers/wikidata"
      ]
    },
    "webpage": {
      "label": "webpage",
      "comment": "The URL of a web page about this item.",
      "domain": "#Entity",
      "range": "http://xmlns.com/foaf/0.1/Document",
      "subPropertyOf": [
        "https://schema.org/url",
        "http://www.wikidata.org/entity/P2699"
      ],
      "equivalentProperty": [
        "http://xmlns.com/foaf/0.1/page"
      ]
    },
    "archivedWebpage": {
      "label": "archivedWebpage",
      "comment": "The URL of an archived web page about this item, which may no longer be available in the web.",
      "domain": "#Entity",
      "range": "http://xmlns.com/foaf/0.1/Document",
      "subPropertyOf": [
        "#webpage"
      ]
    },
    "wikipedia": {
      "label": "wikipedia",
      "comment": "The URL of an (English) Wikipedia article about this item.",
      "domain": "#Entity",
      "range": "http://xmlns.com/foaf/0.1/Document",
      "subPropertyOf": [
        "#webpage"
      ]
    },
    "orcid": {
      "label": "orcid",
      "comment": "An Open Researcher and Contributor ID.",
      "domain": "#Creator",
      "range": "http://www.w3.org/2001/XMLSchema#anyUri",
      "subPropertyOf": [
        "#identifier"
      ],
      "equivalentProperty": [
        "http://purl.org/spar/datacite/orcid",
        "http://id.loc.gov/vocabulary/identifiers/orcid"
      ]
    },
    "creatorName": {
      "label": "creatorname",
      "comment": "The full name of the creator.",
      "domain": "#Creator",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "http://xmlns.com/foaf/0.1/name",
        "https://schema.org/name",
        "http://www.wikidata.org/entity/P2561"
      ]
    },
    "primaryCreatorName": {
      "label": "primaryCreatorName",
      "comment": "The primary full name of the creator.",
      "domain": "#Creator",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "#creatorName",
        "http://dbpedia.org/ontology/commonName"
      ]
    },
    "creatorNote": {
      "label": "creatorNote",
      "comment": "An additional note about the creator.",
      "domain": "#Creator",
      "range": "http://www.w3.org/2001/XMLSchema#string"
    },
    "affiliation": {
      "label": "affiliation",
      "comment": "A (past or present) affiliation of the creator.",
      "domain": "#Creator",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "#creatorNote"
      ],
      "equivalentProperty": [
        "http://dbpedia.org/ontology/affiliation",
        "https://schema.org/affiliation",
        "http://www.wikidata.org/entity/P1416"
      ]
    },
    "primaryAffiliation": {
      "label": "primaryAffiliation",
      "comment": "The primary affiliation of the creator.",
      "domain": "#Creator",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "#affiliation"
      ]
    },
    "awardWebpage": {
      "label": "awardwebpage",
      "comment": "The URL of a web page about an award received by this creator.",
      "domain": "#Creator",
      "range": "http://xmlns.com/foaf/0.1/Document",
      "subPropertyOf": [
        "#webpage"
      ]
    },
    "homepage": {
      "label": "homepage",
      "comment": "The URL of an academic homepage of this creator.",
      "domain": "#Creator",
      "range": "http://xmlns.com/foaf/0.1/Document",
      "subPropertyOf": [
        "#webpage"
      ],
      "equivalentProperty": [
        "http://xmlns.com/foaf/0.1/homepage",
        "http://www.wikidata.org/entity/P856"
      ]
    },
    "primaryHomepage": {
      "label": "primaryHomepage",
      "comment": "The primary URL of an academic homepage of this creator.",
      "domain": "#Creator",
      "range": "http://xmlns.com/foaf/0.1/Document",
      "subPropertyOf": [
        "#homepage"
      ]
    },
    "creatorOf": {
      "label": "creatorOf",
      "comment": "The creator of the publication.",
      "domain": "#Creator",
      "range": "#Publication",
      "inverseOf": "#createdBy",
      "subPropertyOf": [
        "http://xmlns.com/foaf/0.1/made"
      ]
    },
    "authorOf": {
      "label": "authorOf",
      "comment": "The creator is the author of the publication.",
      "domain": "#Creator",
      "range": "#Publication",
      "subPropertyOf": [
        "#creatorOf"
      ],
      "inverseOf": "#authoredBy"
    },
    "editorOf": {
      "label": "editorOf",
      "comment": "The creator is the editor of the publication.",
      "domain": "#Creator",
      "range": "#Publication",
      "subPropertyOf": [
        "#creatorOf"
      ],
      "inverseOf": "#editedBy"
    },
    "coCreatorWith": {
      "label": "coCreatorWith",
      "comment": "The creator is co-creator with the other creator.",
      "domain": "#Creator",
      "range": "#Creator",
      "subPropertyOf": [
        "http://xmlns.com/foaf/0.1/knows"
      ],
      "type": "http://www.w3.org/2002/07/owl#SymmetricProperty"
    },
    "coAuthorWith": {
      "label": "coAuthorWith",
      "comment": "The creator is co-author with the other creator.",
      "domain": "#Creator",
      "range": "#Creator",
      "subPropertyOf": [
        "#coCreatorWith"
      ],
      "type": "http://www.w3.org/2002/07/owl#SymmetricProperty"
    },
    "coEditorWith": {
      "label": "coEditorWith",
      "comment": "The creator is co-editor with the other creator.",
      "domain": "#Creator",
      "range": "#Creator",
      "subPropertyOf": [
        "#coCreatorWith"
      ],
      "type": "http://www.w3.org/2002/07/owl#SymmetricProperty"
    },
    "homonymousCreator": {
      "label": "homonymousCreator",
      "comment": "This creator shares a homonymous name with the other creator.",
      "domain": "#Creator",
      "range": "#Creator",
      "type": "http://www.w3.org/2002/07/owl#SymmetricProperty"
    },
    "possibleActualCreator": {
      "label": "possibleActualCreator",
      "comment": "This ambiguous creator may be (or may be not) just a disambiguation proxy for the other creator.",
      "domain": "#AmbiguousCreator",
      "range": "#Creator",
      "inverseOf": "#proxyAmbiguousCreator",
      "subPropertyOf": [
        "#homonymousCreator"
      ]
    },
    "proxyAmbiguousCreator": {
      "label": "proxyAmbiguousCreator",
      "comment": "This creator ... is also represented by the given ambiguous creator ...",
      "domain": "#Creator",
      "range": "#AmbiguousCreator",
      "subPropertyOf": [
        "#homonymousCreator"
      ],
      "inverseOf": "#possibleActualCreator"
    },
    "signatureCreator": {
      "label": "signatureCreator",
      "comment": "A linked creator of the publication.",
      "domain": "#Signature",
      "range": "#Creator"
    },
    "signatureDblpName": {
      "label": "signatureDblpName",
      "comment": "A dblp name that links the publication to a creator.",
      "domain": "#Signature",
      "range": "http://www.w3.org/2001/XMLSchema#string"
    },
    "signatureOrcid": {
      "label": "signatureOrcid",
      "comment": "An ORCID that links the publication to a creator.",
      "domain": "#Signature",
      "range": "http://www.w3.org/2001/XMLSchema#anyUri"
    },
    "signatureOrdinal": {
      "label": "signatureOrdinal",
      "comment": "The ordinal number of this signature for the publication.",
      "domain": "#Signature",
      "range": "http://www.w3.org/2001/XMLSchema#integer"
    },
    "signaturePublication": {
      "label": "signaturePublication",
      "comment": "The publication of this signature.",
      "domain": "#Signature",
      "range": "#Publication",
      "inverseOf": "#hasSignature"
    },
    "doi": {
      "label": "doi",
      "comment": "A Digital Object Identifier.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#anyUri",
      "subPropertyOf": [
        "#identifier"
      ],
      "equivalentProperty": [
        "http://purl.org/spar/datacite/doi",
        "http://id.loc.gov/vocabulary/identifiers/doi"
      ]
    },
    "isbn": {
      "label": "isbn",
      "comment": "An International Standard Book Number.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#anyUri",
      "subPropertyOf": [
        "#identifier"
      ],
      "equivalentProperty": [
        "http://purl.org/spar/datacite/isbn",
        "http://id.loc.gov/vocabulary/identifiers/isbn"
      ]
    },
    "omid": {
      "label": "omid",
      "comment": "An OpenCitations Meta Identifier.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#anyUri",
      "subPropertyOf": [
        "#identifier"
      ],
      "equivalentProperty": [
        "http://purl.org/spar/datacite/omid"
      ]
    },
    "title": {
      "label": "title",
      "comment": "The title of the publication.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "http://purl.org/dc/elements/1.1/title",
        "https://schema.org/name"
      ],
      "equivalentProperty": [
        "http://purl.org/dc/terms/title",
        "http://www.wikidata.org/entity/P1476"
      ]
    },
    "bibtexType": {
      "label": "bibtexType",
      "comment": "The bibtex type of the publication, e.g. book, inproceedings, etc.",
      "domain": "#Publication",
      "range": "http://purl.org/net/nknouf/ns/bibtex#Entry"
    },
    "createdBy": {
      "label": "createdBy",
      "comment": "The publication is created by the creator.",
      "domain": "#Publication",
      "range": "#Creator",
      "subPropertyOf": [
        "http://purl.org/dc/elements/1.1/creator",
        "http://xmlns.com/foaf/0.1/maker"
      ],
      "inverseOf": "#creatorOf",
      "equivalentProperty": [
        "http://purl.org/dc/terms/creator",
        "http://id.loc.gov/vocabulary/relators/cre",
        "https://schema.org/creator",
        "http://www.wikidata.org/entity/P170"
      ]
    },
    "authoredBy": {
      "label": "authoredBy",
      "comment": "The publication is authored by the creator.",
      "domain": "#Publication",
      "range": "#Creator",
      "subPropertyOf": [
        "#createdBy"
      ],
      "inverseOf": "#authorOf",
      "equivalentProperty": [
        "http://dbpedia.org/ontology/author",
        "http://id.loc.gov/vocabulary/relators/aut",
        "https://schema.org/author",
        "http://www.wikidata.org/entity/P50"
      ]
    },
    "editedBy": {
      "label": "editedBy",
      "comment": "The publication is edited by the creator.",
      "domain": "#Publication",
      "range": "#Creator",
      "subPropertyOf": [
        "#createdBy"
      ],
      "inverseOf": "#editorOf",
      "equivalentProperty": [
        "http://dbpedia.org/ontology/editor",
        "http://id.loc.gov/vocabulary/relators/edt",
        "https://schema.org/editor",
        "http://www.wikidata.org/entity/P98",
        "http://purl.org/ontology/bibo/editor"
      ]
    },
    "numberOfCreators": {
      "label": "numberOfCreators",
      "comment": "The number of creators who created this publication.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#integer"
    },
    "hasSignature": {
      "label": "hasSignature",
      "comment": "A signature that links this publication to a creator.",
      "domain": "#Publication",
      "range": "#Signature",
      "inverseOf": "#signaturePublication"
    },
    "documentPage": {
      "label": "documentPage",
      "comment": "The URL of the electronic edition of the publication.",
      "domain": "#Publication",
      "range": "http://xmlns.com/foaf/0.1/Document",
      "subPropertyOf": [
        "#webpage"
      ],
      "equivalentProperty": [
        "http://id.loc.gov/ontologies/bibframe/electronicLocator",
        "http://purl.org/ontology/bibo/uri"
      ]
    },
    "primaryDocumentPage": {
      "label": "primaryDocumentPage",
      "comment": "The primary URL of the electronic edition of the publication.",
      "domain": "#Publication",
      "range": "http://xmlns.com/foaf/0.1/Document",
      "subPropertyOf": [
        "#documentPage"
      ]
    },
    "listedOnTocPage": {
      "label": "listedOnTocPage",
      "comment": "The url of the dblp table of contents page listing this publication.",
      "domain": "#Publication",
      "range": "http://xmlns.com/foaf/0.1/Document"
    },
    "publishedInStream": {
      "label": "publishedInStream",
      "comment": "The conference series, the journal, or the repository in which the publication has been published.",
      "domain": "#Publication",
      "range": "#Stream",
      "subPropertyOf": [
        "https://schema.org/isPartOf",
        "http://www.wikidata.org/entity/P1433"
      ]
    },
    "publishedIn": {
      "label": "publishedIn",
      "comment": "The name of the series, the journal, or the book in which the publication has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "https://schema.org/isPartOf",
        "http://www.wikidata.org/entity/P1433"
      ]
    },
    "publishedInSeries": {
      "label": "publishedInSeries",
      "comment": "The name of the series in which the publication has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "#publishedIn"
      ]
    },
    "publishedInSeriesVolume": {
      "label": "publishedInSeriesVolume",
      "comment": "The volume of the series in which the publication has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "https://schema.org/volumeNumber",
        "http://www.wikidata.org/entity/P478"
      ],
      "equivalentProperty": [
        "http://purl.org/ontology/bibo/volume"
      ]
    },
    "publishedInJournal": {
      "label": "publishedInJournal",
      "comment": "The name of the journal in which the publication has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "#publishedIn"
      ]
    },
    "publishedInJournalVolume": {
      "label": "publishedInJournalVolume",
      "comment": "The volume of the journal in which the publication has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "https://schema.org/volumeNumber",
        "http://www.wikidata.org/entity/P478"
      ],
      "equivalentProperty": [
        "http://purl.org/ontology/bibo/volume"
      ]
    },
    "publishedInJournalVolumeIssue": {
      "label": "publishedInJournalIssue",
      "comment": "The issue of the journal in which the publication has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "https://schema.org/issueNumber",
        "http://www.wikidata.org/entity/P433"
      ],
      "equivalentProperty": [
        "http://purl.org/ontology/bibo/issue"
      ]
    },
    "publishedInBook": {
      "label": "publishedInBook",
      "comment": "The name of the book in which the publication has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "#publishedIn"
      ]
    },
    "publishedInBookChapter": {
      "label": "publishedInBookChapter",
      "comment": "The chapter of the book in which the publication has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "https://schema.org/position",
        "http://www.wikidata.org/entity/P792"
      ],
      "equivalentProperty": [
        "http://purl.org/ontology/bibo/chapter"
      ]
    },
    "pagination": {
      "label": "pagination",
      "comment": "The page numbers where the publication can be found.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "equivalentProperty": [
        "https://schema.org/pagination",
        "http://www.wikidata.org/entity/P304",
        "http://purl.org/ontology/bibo/pages"
      ]
    },
    "yearOfEvent": {
      "label": "yearOfEvent",
      "comment": "The year the conference or workshop contribution has been presented.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#gYear"
    },
    "yearOfPublication": {
      "label": "yearOfPublication",
      "comment": "The year the publication's issue or volume has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#gYear",
      "equivalentProperty": [
        "http://dbpedia.org/ontology/publicationDate",
        "http://purl.org/dc/terms/issued",
        "https://schema.org/publication",
        "http://www.wikidata.org/entity/P577"
      ]
    },
    "monthOfPublication": {
      "label": "monthOfPublication",
      "comment": "The month the publication has been published.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#gMonth",
      "subPropertyOf": [
        "http://www.wikidata.org/entity/P2922"
      ]
    },
    "publishedBy": {
      "label": "publishedBy",
      "comment": "The publisher of the publication.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "http://purl.org/dc/elements/1.1/publisher"
      ],
      "equivalentProperty": [
        "http://purl.org/dc/terms/publisher",
        "https://schema.org/publisher",
        "http://www.wikidata.org/entity/P123"
      ]
    },
    "publishersAddress": {
      "label": "publishersAddress",
      "comment": "The address of the publisher.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string"
    },
    "thesisAcceptedBySchool": {
      "label": "thesisAcceptedBySchool",
      "comment": "The school where the publication (typically a thesis) has been accepted.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string"
    },
    "publicationNote": {
      "label": "publicationNote",
      "comment": "An additional note to the publication.",
      "domain": "#Publication",
      "range": "http://www.w3.org/2001/XMLSchema#string"
    },
    "publishedAsPartOf": {
      "label": "publishedAsPartOf",
      "comment": "The publication has been published as a part of the other publication.",
      "domain": "#Publication",
      "range": "#Publication",
      "subPropertyOf": [
        "https://schema.org/isPartOf",
        "http://www.wikidata.org/entity/P1433"
      ],
      "type": "http://www.w3.org/2002/07/owl#TransitiveProperty"
    },
    "hasVersion": {
      "label": "hasVersion",
      "comment": "The publication has a different, more specific (instance) publication as its version.",
      "domain": "#Publication",
      "range": "#VersionRelation",
      "inverseOf": "#versionConcept"
    },
    "isVersion": {
      "label": "isVersion",
      "comment": "The publication is a version of another, more general (concept) publication.",
      "domain": "#Publication",
      "range": "#VersionRelation",
      "inverseOf": "#versionInstance"
    },
    "isVersionOf": {
      "label": "isVersionOf",
      "comment": "The publication is a version of another, more general (concept) publication.",
      "domain": "#Publication",
      "range": "#Publication",
      "equivalentProperty": [
        "http://www.wikidata.org/entity/P747"
      ],
      "type": "http://www.w3.org/2002/07/owl#TransitiveProperty"
    },
    "versionConcept": {
      "label": "versionConcept",
      "comment": "The linked general (concept) publication.",
      "domain": "#VersionRelation",
      "range": "#Publication"
    },
    "versionInstance": {
      "label": "versionInstance",
      "comment": "The linked specific (instance) publication version.",
      "domain": "#VersionRelation",
      "range": "#Publication"
    },
    "versionUri": {
      "label": "versionUri",
      "comment": "An (optional) URI of identifying the linked specific (instance) publication version.",
      "domain": "#VersionRelation",
      "range": "http://www.w3.org/2001/XMLSchema#anyUri"
    },
    "versionLabel": {
      "label": "versionLabel",
      "comment": "The human-readable version label of the specific (instance) publication version.",
      "domain": "#VersionRelation",
      "range": "http://www.w3.org/2001/XMLSchema#string"
    },
    "versionOrdinal": {
      "label": "versionOrdinal",
      "comment": "The ordinal number of the specific (instance) publication version.",
      "domain": "#VersionRelation",
      "range": "http://www.w3.org/2001/XMLSchema#integer"
    },
    "streamTitle": {
      "label": "streamTitle",
      "comment": "A title of the stream.",
      "domain": "#Stream",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "http://xmlns.com/foaf/0.1/name",
        "https://schema.org/name",
        "http://www.wikidata.org/entity/P2561"
      ]
    },
    "primaryStreamTitle": {
      "label": "primaryStreamTitle",
      "comment": "The primary title of the stream.",
      "domain": "#Stream",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "#streamTitle",
        "http://dbpedia.org/ontology/commonName"
      ]
    },
    "formerStreamTitle": {
      "label": "formerStreamTitle",
      "comment": "A former title of the stream.",
      "domain": "#Stream",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "subPropertyOf": [
        "#streamTitle"
      ]
    },
    "issn": {
      "label": "issn",
      "comment": "An International Standard Serial Number.",
      "domain": "#Stream",
      "range": "http://www.w3.org/2001/XMLSchema#anyUri",
      "subPropertyOf": [
        "#identifier"
      ],
      "equivalentProperty": [
        "http://purl.org/spar/datacite/issn",
        "http://id.loc.gov/vocabulary/identifiers/issn"
      ]
    },
    "iso4": {
      "label": "iso4",
      "comment": "The stream's ISO4 abbreviation.",
      "domain": "#Stream",
      "range": "http://www.w3.org/2001/XMLSchema#string",
      "equivalentProperty": [
        "http://www.wikidata.org/entity/P1160"
      ]
    },
    "indexPage": {
      "label": "indexPage",
      "comment": "The URL of the dblp stream index page for this stream.",
      "domain": "#Stream",
      "range": "http://xmlns.com/foaf/0.1/Document"
    },
    "relatedStream": {
      "label": "relatedStream",
      "comment": "This stream is related to the other stream in some unspecified way.",
      "domain": "#Stream",
      "range": "#Stream",
      "type": "http://www.w3.org/2002/07/owl#SymmetricProperty"
    },
    "superStream": {
      "label": "superStream",
      "comment": "This stream has (or had) the other stream as a part.",
      "domain": "#Stream",
      "range": "#Stream",
      "subPropertyOf": [
        "#relatedStream"
      ],
      "inverseOf": "#subStream"
    },
    "subStream": {
      "label": "subStream",
      "comment": "This stream is (or was) a part of the other stream.",
      "domain": "#Stream",
      "range": "#Stream",
      "subPropertyOf": [
        "#relatedStream"
      ],
      "inverseOf": "#superStream"
    },
    "predecessorStream": {
      "label": "predecessorStream",
      "comment": "This stream is a predecessor of the other stream.",
      "domain": "#Stream",
      "range": "#Stream",
      "subPropertyOf": [
        "#relatedStream"
      ],
      "inverseOf": "#successorStream"
    },
    "successorStream": {
      "label": "successorStream",
      "comment": "This stream is a successor of the other stream.",
      "domain": "#Stream",
      "range": "#Stream",
      "subPropertyOf": [
        "#relatedStream"
      ],
      "inverseOf": "#predecessorStream"
    }
  }
}
classes_uri = {
    "AmbiguousCreator": "https://dblp.org/rdf/schema#AmbiguousCreator",
    "Article": "https://dblp.org/rdf/schema#Article",
    "AuthorSignature": "https://dblp.org/rdf/schema#AuthorSignature",
    "Book": "https://dblp.org/rdf/schema#Book",
    "Conference": "https://dblp.org/rdf/schema#Conference",
    "Creator": "https://dblp.org/rdf/schema#Creator",
    "Data": "https://dblp.org/rdf/schema#Data",
    "EditorSignature": "https://dblp.org/rdf/schema#EditorSignature",
    "Editorship": "https://dblp.org/rdf/schema#Editorship",
    "Entity": "https://dblp.org/rdf/schema#Entity",
    "Group": "https://dblp.org/rdf/schema#Group",
    "Incollection": "https://dblp.org/rdf/schema#Incollection",
    "Informal": "https://dblp.org/rdf/schema#Informal",
    "Inproceedings": "https://dblp.org/rdf/schema#Inproceedings",
    "Journal": "https://dblp.org/rdf/schema#Journal",
    "Person": "https://dblp.org/rdf/schema#Person",
    "Publication": "https://dblp.org/rdf/schema#Publication",
    "Reference": "https://dblp.org/rdf/schema#Reference",
    "Repository": "https://dblp.org/rdf/schema#Repository",
    "Series": "https://dblp.org/rdf/schema#Series",
    "Signature": "https://dblp.org/rdf/schema#Signature",
    "Stream": "https://dblp.org/rdf/schema#Stream",
    "VersionRelation": "https://dblp.org/rdf/schema#VersionRelation",
    "Withdrawn": "https://dblp.org/rdf/schema#Withdrawn"
  }

prefixes = {
    "bf": "http://id.loc.gov/ontologies/bibframe/",
    "bibo": "http://purl.org/ontology/bibo/",
    "bibtex": "http://purl.org/net/nknouf/ns/bibtex#",
    "cito": "http://purl.org/spar/cito/",
    "datacite": "http://purl.org/spar/datacite/",
    "dblp": "https://dblp.org/rdf/schema#",
    "dbo": "http://dbpedia.org/ontology/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dct": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "litre": "http://purl.org/spar/literal/",
    "locid": "http://id.loc.gov/vocabulary/identifiers/",
    "locrel": "http://id.loc.gov/vocabulary/relators/",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "schema": "https://schema.org/",
    "wd": "http://www.wikidata.org/entity/",
    "wdt": "http://www.wikidata.org/prop/direct/",
    "xml": "http://www.w3.org/XML/1998/namespace",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
}

properties_uri = {
"affiliation": "https://dblp.org/rdf/schema#affiliation",
    "archivedWebpage": "https://dblp.org/rdf/schema#archivedWebpage",
    "authorOf": "https://dblp.org/rdf/schema#authorOf",
    "authoredBy": "https://dblp.org/rdf/schema#authoredBy",
    "awardWebpage": "https://dblp.org/rdf/schema#awardWebpage",
    "bibtexType": "https://dblp.org/rdf/schema#bibtexType",
    "coAuthorWith": "https://dblp.org/rdf/schema#coAuthorWith",
    "coCreatorWith": "https://dblp.org/rdf/schema#coCreatorWith",
    "coEditorWith": "https://dblp.org/rdf/schema#coEditorWith",
    "createdBy": "https://dblp.org/rdf/schema#createdBy",
    "creatorName": "https://dblp.org/rdf/schema#creatorName",
    "creatorNote": "https://dblp.org/rdf/schema#creatorNote",
    "creatorOf": "https://dblp.org/rdf/schema#creatorOf",
    "documentPage": "https://dblp.org/rdf/schema#documentPage",
    "doi": "https://dblp.org/rdf/schema#doi",
    "editedBy": "https://dblp.org/rdf/schema#editedBy",
    "editorOf": "https://dblp.org/rdf/schema#editorOf",
    "formerStreamTitle": "https://dblp.org/rdf/schema#formerStreamTitle",
    "hasSignature": "https://dblp.org/rdf/schema#hasSignature",
    "hasVersion": "https://dblp.org/rdf/schema#hasVersion",
    "homepage": "https://dblp.org/rdf/schema#homepage",
    "homonymousCreator": "https://dblp.org/rdf/schema#homonymousCreator",
    "identifier": "https://dblp.org/rdf/schema#identifier",
    "indexPage": "https://dblp.org/rdf/schema#indexPage",
    "isVersion": "https://dblp.org/rdf/schema#isVersion",
    "isVersionOf": "https://dblp.org/rdf/schema#isVersionOf",
    "isbn": "https://dblp.org/rdf/schema#isbn",
    "iso4": "https://dblp.org/rdf/schema#iso4",
    "issn": "https://dblp.org/rdf/schema#issn",
    "listedOnTocPage": "https://dblp.org/rdf/schema#listedOnTocPage",
    "monthOfPublication": "https://dblp.org/rdf/schema#monthOfPublication",
    "numberOfCreators": "https://dblp.org/rdf/schema#numberOfCreators",
    "omid": "https://dblp.org/rdf/schema#omid",
    "orcid": "https://dblp.org/rdf/schema#orcid",
    "pagination": "https://dblp.org/rdf/schema#pagination",
    "possibleActualCreator": "https://dblp.org/rdf/schema#possibleActualCreator",
    "predecessorStream": "https://dblp.org/rdf/schema#predecessorStream",
    "primaryAffiliation": "https://dblp.org/rdf/schema#primaryAffiliation",
    "primaryCreatorName": "https://dblp.org/rdf/schema#primaryCreatorName",
    "primaryDocumentPage": "https://dblp.org/rdf/schema#primaryDocumentPage",
    "primaryHomepage": "https://dblp.org/rdf/schema#primaryHomepage",
    "primaryStreamTitle": "https://dblp.org/rdf/schema#primaryStreamTitle",
    "proxyAmbiguousCreator": "https://dblp.org/rdf/schema#proxyAmbiguousCreator",
    "publicationNote": "https://dblp.org/rdf/schema#publicationNote",
    "publishedAsPartOf": "https://dblp.org/rdf/schema#publishedAsPartOf",
    "publishedBy": "https://dblp.org/rdf/schema#publishedBy",
    "publishedIn": "https://dblp.org/rdf/schema#publishedIn",
    "publishedInBook": "https://dblp.org/rdf/schema#publishedInBook",
    "publishedInBookChapter": "https://dblp.org/rdf/schema#publishedInBookChapter",
    "publishedInJournal": "https://dblp.org/rdf/schema#publishedInJournal",
    "publishedInJournalVolume": "https://dblp.org/rdf/schema#publishedInJournalVolume",
    "publishedInJournalVolumeIssue": "https://dblp.org/rdf/schema#publishedInJournalVolumeIssue",
    "publishedInSeries": "https://dblp.org/rdf/schema#publishedInSeries",
    "publishedInSeriesVolume": "https://dblp.org/rdf/schema#publishedInSeriesVolume",
    "publishedInStream": "https://dblp.org/rdf/schema#publishedInStream",
    "publishersAddress": "https://dblp.org/rdf/schema#publishersAddress",
    "relatedStream": "https://dblp.org/rdf/schema#relatedStream",
    "signatureCreator": "https://dblp.org/rdf/schema#signatureCreator",
    "signatureDblpName": "https://dblp.org/rdf/schema#signatureDblpName",
    "signatureOrcid": "https://dblp.org/rdf/schema#signatureOrcid",
    "signatureOrdinal": "https://dblp.org/rdf/schema#signatureOrdinal",
    "signaturePublication": "https://dblp.org/rdf/schema#signaturePublication",
    "streamTitle": "https://dblp.org/rdf/schema#streamTitle",
    "subStream": "https://dblp.org/rdf/schema#subStream",
    "successorStream": "https://dblp.org/rdf/schema#successorStream",
    "superStream": "https://dblp.org/rdf/schema#superStream",
    "thesisAcceptedBySchool": "https://dblp.org/rdf/schema#thesisAcceptedBySchool",
    "title": "https://dblp.org/rdf/schema#title",
    "versionConcept": "https://dblp.org/rdf/schema#versionConcept",
    "versionInstance": "https://dblp.org/rdf/schema#versionInstance",
    "versionLabel": "https://dblp.org/rdf/schema#versionLabel",
    "versionOrdinal": "https://dblp.org/rdf/schema#versionOrdinal",
    "versionUri": "https://dblp.org/rdf/schema#versionUri",
    "webpage": "https://dblp.org/rdf/schema#webpage",
    "wikidata": "https://dblp.org/rdf/schema#wikidata",
    "wikipedia": "https://dblp.org/rdf/schema#wikipedia",
    "yearOfEvent": "https://dblp.org/rdf/schema#yearOfEvent",
    "yearOfPublication": "https://dblp.org/rdf/schema#yearOfPublication"
}

properties = {
  "affiliation": {
      "IRI": "https://dblp.org/rdf/schema#affiliation",
      "description": "A (past or present) affiliation of the creator. (Remark: This property currently just gives literal xsd:string values until institutions are modelled as proper entities.)",
      "equivalentTo": ["affiliation", "P1416", "affiliation"],
      "superProperties": ["creatorNote"],
      "subProperties": ["primaryAffiliation"],
      "domains": ["Creator c"],
      "range": "string"
    },
    "archivedWebpage": {
      "IRI": "https://dblp.org/rdf/schema#archivedWebpage",
      "description": "The URL of an archived web page about this item, which may no longer be available in the web.",
      "superProperties": ["webpage"],
      "domains": ["Entity c"],
      "range": "Document c"
    },
    "authorOf": {
      "IRI": "https://dblp.org/rdf/schema#authorOf",
      "description": "The creator is the author of the publication.",
      "superProperties": ["creatorOf"],
      "domains": ["Creator c"],
      "range": "Publication c",
      "inverseOf": "authoredBy"
    },
    "authoredBy": {
      "IRI": "https://dblp.org/rdf/schema#authoredBy",
      "description": "The publication is authored by the creator.",
      "equivalentTo": ["author", "aut", "P50", "author"],
      "superProperties": ["createdBy"],
      "domains": ["Publication c"],
      "range": "Creator c",
      "inverseOf": "authorOf"
    },
    "awardwebpage": {
      "IRI": "https://dblp.org/rdf/schema#awardWebpage",
      "description": "The URL of a web page about an award received by this creator.",
      "superProperties": ["webpage"],
      "domains": ["Creator c"],
      "range": "Document c"
    },
    "bibtexType": {
      "IRI": "https://dblp.org/rdf/schema#bibtexType",
      "description": "The bibtex type of the publication, e.g., book, inproceedings, etc.",
      "domains": ["Publication c"],
      "range": "Entry c"
    },
    "coAuthorWith": {
      "IRI": "https://dblp.org/rdf/schema#coAuthorWith",
      "description": "The creator is co-author with the other creator.",
      "superProperties": ["coCreatorWith"],
      "domains": ["Creator c"],
      "range": "Creator c"
    },
    "coCreatorWith": {
      "IRI": "https://dblp.org/rdf/schema#coCreatorWith",
      "description": "The creator is co-creator with the other creator.",
      "superProperties": ["knows"],
      "subProperties": ["coAuthorWith", "coEditorWith"],
      "domains": ["Creator c"],
      "range": "Creator c"
    },
    "coEditorWith": {
      "IRI": "https://dblp.org/rdf/schema#coEditorWith",
      "description": "The creator is co-editor with the other creator.",
      "superProperties": ["coCreatorWith"],
      "domains": ["Creator c"],
      "range": "Creator c"
    },
    "createdBy": {
      "IRI": "https://dblp.org/rdf/schema#createdBy",
      "description": "The publication is created by the creator.",
      "equivalentTo": ["cre", "Creator", "P170", "creator"],
      "superProperties": ["Creator", "maker"],
      "subProperties": ["authoredBy", "editedBy"],
      "domains": ["Publication c"],
      "range": "Creator c",
      "inverseOf": "creatorOf"
    },
    "creatorname": {
      "IRI": "https://dblp.org/rdf/schema#creatorName",
      "description": "The full name of the creator.",
      "superProperties": ["P2561", "name", "name"],
      "subProperties": ["primaryCreatorName"],
      "domains": ["Creator c"],
      "range": "string"
    },
    "creatorNote": {
      "IRI": "https://dblp.org/rdf/schema#creatorNote",
      "description": "An additional note about the creator.",
      "subProperties": ["affiliation"],
      "domains": ["Creator c"],
      "range": "string"
    },
    "creatorOf": {
      "IRI": "https://dblp.org/rdf/schema#creatorOf",
      "description": "The creator of the publication.",
      "superProperties": ["made"],
      "subProperties": ["authorOf", "editorOf"],
      "domains": ["Creator c"],
      "range": "Publication c",
      "inverseOf": "createdBy"
    },
    "documentPage": {
      "IRI": "https://dblp.org/rdf/schema#documentPage",
      "description": "The URL of the electronic edition of the publication.",
      "equivalentTo": ["Electronic location", "uri"],
      "superProperties": ["webpage"],
      "subProperties": ["primaryDocumentPage"],
      "domains": ["Publication c"],
      "range": "Document c"
    },
    "doi": {
      "IRI": "https://dblp.org/rdf/schema#doi",
      "description": "A Digital Object Identifier.",
      "equivalentTo": ["doi", "doi"],
      "superProperties": ["identifier"],
      "domains": ["Publication c"],
      "range": "anyUri"
    },
    "editedBy": {
      "IRI": "https://dblp.org/rdf/schema#editedBy",
      "description": "The publication is edited by the creator.",
      "equivalentTo": ["editor", "edt", "editor", "P98", "editor"],
      "superProperties": ["createdBy"],
      "domains": ["Publication c"],
      "range": "Creator c",
      "inverseOf": "editorOf"
    },
    "editorOf": {
      "IRI": "https://dblp.org/rdf/schema#editorOf",
      "description": "The creator is the editor of the publication.",
      "superProperties": ["creatorOf"],
      "domains": ["Creator c"],
      "range": "Publication c",
      "inverseOf": "editedBy"
    },
    "formerStreamTitle": {
      "IRI": "https://dblp.org/rdf/schema#formerStreamTitle",
      "description": "A former title of the stream.",
      "superProperties": ["streamTitle"],
      "domains": ["Stream c"],
      "range": "string"
    },
    "hasSignature": {
      "IRI": "https://dblp.org/rdf/schema#hasSignature",
      "description": "A signature that links this publication to an creator.",
      "domains": ["Publication c"],
      "range": "Signature c",
      "inverseOf": "signaturePublication"
    },
    "hasVersion": {
      "IRI": "https://dblp.org/rdf/schema#hasVersion",
      "description": "The publication has a different, more specific (instance) publication as its version.",
      "domains": ["Publication c"],
      "range": "VersionRelation c",
      "inverseOf": "versionConcept"
    },
    "homepage": {
      "IRI": "https://dblp.org/rdf/schema#homepage",
      "description": "The URL of an academic homepage of this creator.",
      "equivalentTo": ["P856", "homepage"],
      "superProperties": ["webpage"],
      "subProperties": ["primaryHomepage"],
      "domains": ["Creator c"],
      "range": "Document c"
    },
    "homonymousCreator": {
      "IRI": "https://dblp.org/rdf/schema#homonymousCreator",
      "description": "This creator shares a homonymous name with the other creator.",
      "subProperties": ["possibleActualCreator", "proxyAmbiguousCreator"],
      "domains": ["Creator c"],
      "range": "Creator c"
    },
    "identifier": {
      "IRI": "https://dblp.org/rdf/schema#identifier",
      "description": "An abstract identifier.",
      "equivalentTo": ["id"],
      "subProperties": ["doi", "isbn", "issn", "omid", "orcid", "wikidata"],
      "domains": ["Entity c"],
      "range": "anyUri"
    },
    "indexPage": {
      "IRI": "https://dblp.org/rdf/schema#indexPage",
      "description": "The URL of the dblp stream index page for this stream.",
      "domains": ["Stream c"],
      "range": "Document c"
    },
    "isVersion": {
      "IRI": "https://dblp.org/rdf/schema#isVersion",
      "description": "The publication is a version of another, more general (concept) publication.",
      "domains": ["Publication c"],
      "range": "VersionRelation c",
      "inverseOf": "versionInstance"
    },
    "isVersionOf": {
      "IRI": "https://dblp.org/rdf/schema#isVersionOf",
      "description": "The publication is a version of another, more general (concept) publication.",
      "equivalentTo": ["P747"],
      "domains": ["Publication c"],
      "range": "Publication c"
    },
    "isbn": {
      "IRI": "https://dblp.org/rdf/schema#isbn",
      "description": "An International Standard Book Number.",
      "equivalentTo": ["isbn", "isbn"],
      "superProperties": ["identifier"],
      "domains": ["Publication c"],
      "range": "anyUri"
    },
    "iso4": {
      "IRI": "https://dblp.org/rdf/schema#iso4",
      "description": "The stream's ISO4 abbreviation.",
      "equivalentTo": ["P1160"],
      "domains": ["Stream c"],
      "range": "string"
    },
    "issn": {
      "IRI": "https://dblp.org/rdf/schema#issn",
      "description": "An International Standard Serial Number.",
      "equivalentTo": ["issn", "issn"],
      "superProperties": ["identifier"],
      "domains": ["Stream c"],
      "range": "anyUri"
    },
    "listedOnTocPage": {
      "IRI": "https://dblp.org/rdf/schema#listedOnTocPage",
      "description": "The url of the dblp table of contents page listing this publication.",
      "domains": ["Publication c"],
      "range": "Document c"
    },
    "monthOfPublication": {
      "IRI": "https://dblp.org/rdf/schema#monthOfPublication",
      "description": "The month the publication has been published.",
      "superProperties": ["P2922"],
      "domains": ["Publication c"],
      "range": "gMonth"
    },
    "numberOfCreators": {
      "IRI": "https://dblp.org/rdf/schema#numberOfCreators",
      "description": "The number of creators who created this publication.",
      "domains": ["Publication c"],
      "range": "integer"
    },
    "omid": {
      "IRI": "https://dblp.org/rdf/schema#omid",
      "description": "An OpenCitations Meta Identifier.",
      "equivalentTo": ["omid"],
      "superProperties": ["identifier"],
      "domains": ["Publication c"],
      "range": "anyUri"
    },
    "orcid": {
      "IRI": "https://dblp.org/rdf/schema#orcid",
      "description": "An Open Researcher and Contributor ID.",
      "equivalentTo": ["orcid", "orcid"],
      "superProperties": ["identifier"],
      "domains": ["Creator c"],
      "range": "anyUri"
    },
    "pagination": {
      "IRI": "https://dblp.org/rdf/schema#pagination",
      "description": "The page numbers where the publication can be found.",
      "equivalentTo": ["pages", "P304", "pagination"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "possibleActualCreator": {
      "IRI": "https://dblp.org/rdf/schema#possibleActualCreator",
      "description": "This ambiguous creator may be (or may be not) just a disambiguation proxy for the other creator. Further actual creator candidates are possible.",
      "superProperties": ["homonymousCreator"],
      "domains": ["AmbiguousCreator c"],
      "range": "Creator c",
      "inverseOf": "proxyAmbiguousCreator"
    },
    "predecessorStream": {
      "IRI": "https://dblp.org/rdf/schema#predecessorStream",
      "description": "This stream is a predecessor of the other stream.",
      "superProperties": ["relatedStream"],
      "domains": ["Stream c"],
      "range": "Stream c",
      "inverseOf": "successorStream"
    },
    "primaryAffiliation": {
      "IRI": "https://dblp.org/rdf/schema#primaryAffiliation",
      "description": "The primary affiliation of the creator. (Remark: This property currently just gives literal xsd:string values until institutions are modelled as proper entities.)",
      "superProperties": ["affiliation"],
      "domains": ["Creator c"],
      "range": "string"
    },
    "primaryCreatorName": {
      "IRI": "https://dblp.org/rdf/schema#primaryCreatorName",
      "description": "The primary full name of the creator.",
      "superProperties": ["commonName", "creatorname"],
      "domains": ["Creator c"],
      "range": "string"
    },
    "primaryDocumentPage": {
      "IRI": "https://dblp.org/rdf/schema#primaryDocumentPage",
      "description": "The primary URL of the electronic edition of the publication.",
      "superProperties": ["documentPage"],
      "domains": ["Publication c"],
      "range": "Document c"
    },
    "primaryHomepage": {
      "IRI": "https://dblp.org/rdf/schema#primaryHomepage",
      "description": "The primary URL of an academic homepage of this creator.",
      "superProperties": ["homepage"],
      "domains": ["Creator c"],
      "range": "Document c"
    },
    "primaryStreamTitle": {
      "IRI": "https://dblp.org/rdf/schema#primaryStreamTitle",
      "description": "The primary title of the stream.",
      "superProperties": ["commonName", "streamTitle"],
      "domains": ["Stream c"],
      "range": "string"
    },
    "proxyAmbiguousCreator": {
      "IRI": "https://dblp.org/rdf/schema#proxyAmbiguousCreator",
      "description": "This creator (and any of her fellow homonymous creators) is also represented by the given ambiguous creator in cases where the authorship of a publication is undetermined.",
      "superProperties": ["homonymousCreator"],
      "domains": ["Creator c"],
      "range": "AmbiguousCreator c",
      "inverseOf": "possibleActualCreator"
    },
    "publicationNote": {
      "IRI": "https://dblp.org/rdf/schema#publicationNote",
      "description": "An additional note to the publication.",
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedAsPartOf": {
      "IRI": "https://dblp.org/rdf/schema#publishedAsPartOf",
      "description": "The publication has been published as a part of the other publication.",
      "superProperties": ["P1433", "isPartOf"],
      "domains": ["Publication c"],
      "range": "Publication c"
    },
    "publishedBy": {
      "IRI": "https://dblp.org/rdf/schema#publishedBy",
      "description": "The publisher of the publication. (Remark: This property currently just gives literal xsd:string values until publishers are modelled as proper entities.)",
      "equivalentTo": ["Publisher", "P123", "publisher"],
      "superProperties": ["Publisher"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedIn": {
      "IRI": "https://dblp.org/rdf/schema#publishedIn",
      "description": "The name of the series, the journal, or the book in which the publication has been published. (Remark: This property currently just gives literal xsd:string values until journals and conference series are modelled as proper entities.)",
      "superProperties": ["P1433", "isPartOf"],
      "subProperties": ["publishedInBook", "publishedInJournal", "publishedInSeries"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedInBook": {
      "IRI": "https://dblp.org/rdf/schema#publishedInBook",
      "description": "The name of the book in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)",
      "superProperties": ["publishedIn"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedInBookChapter": {
      "IRI": "https://dblp.org/rdf/schema#publishedInBookChapter",
      "description": "The chapter of the book in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)",
      "equivalentTo": ["chapter"],
      "superProperties": ["P792", "position"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedInJournal": {
      "IRI": "https://dblp.org/rdf/schema#publishedInJournal",
      "description": "The name of the journal in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)",
      "superProperties": ["publishedIn"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedInJournalVolume": {
      "IRI": "https://dblp.org/rdf/schema#publishedInJournalVolume",
      "description": "The volume of the journal in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)",
      "equivalentTo": ["volume"],
      "superProperties": ["P478", "volumeNumber"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedInJournalIssue": {
      "IRI": "https://dblp.org/rdf/schema#publishedInJournalVolumeIssue",
      "description": "The issue of the journal in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)",
      "equivalentTo": ["issue"],
      "superProperties": ["P433", "issueNumber"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedInSeries": {
      "IRI": "https://dblp.org/rdf/schema#publishedInSeries",
      "description": "The name of the series in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)",
      "superProperties": ["publishedIn"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedInSeriesVolume": {
      "IRI": "https://dblp.org/rdf/schema#publishedInSeriesVolume",
      "description": "The volume of the series in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)",
      "equivalentTo": ["volume"],
      "superProperties": ["P478", "volumeNumber"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "publishedInStream": {
      "IRI": "https://dblp.org/rdf/schema#publishedInStream",
      "description": "The conference series, the journal, or the repository in which the publication has been published.",
      "superProperties": ["P1433", "isPartOf"],
      "domains": ["Publication c"],
      "range": "Stream c"
    },
    "publishersAddress": {
      "IRI": "https://dblp.org/rdf/schema#publishersAddress",
      "description": "The address of the publisher. (Remark: This is currently an intermediate property that will be removed once publishers are modelled as proper entities.)",
      "domains": ["Publication c"],
      "range": "string"
    },
    "relatedStream": {
      "IRI": "https://dblp.org/rdf/schema#relatedStream",
      "description": "This stream is related to the other stream in some unspecified way.",
      "subProperties": ["predecessorStream", "subStream", "successorStream", "superStream"],
      "domains": ["Stream c"],
      "range": "Stream c"
    },
    "signatureCreator": {
      "IRI": "https://dblp.org/rdf/schema#signatureCreator",
      "description": "A linked creator of the publication.",
      "domains": ["Signature c"],
      "range": "Creator c"
    },
    "signatureDblpName": {
      "IRI": "https://dblp.org/rdf/schema#signatureDblpName",
      "description": "A dblp name (including any possible trailing homonym number) that links the publication to a creator.",
      "domains": ["Signature c"],
      "range": "string"
    },
    "signatureOrcid": {
      "IRI": "https://dblp.org/rdf/schema#signatureOrcid",
      "description": "An ORCID that links the publication to a creator.",
      "domains": ["Signature c"],
      "range": "anyUri"
    },
    "signatureOrdinal": {
      "IRI": "https://dblp.org/rdf/schema#signatureOrdinal",
      "description": "The ordinal number of this signature for the publication, starting with 1.",
      "domains": ["Signature c"],
      "range": "integer"
    },
    "signaturePublication": {
      "IRI": "https://dblp.org/rdf/schema#signaturePublication",
      "description": "The publication of this signature.",
      "domains": ["Signature c"],
      "range": "Publication c",
      "inverseOf": "hasSignature"
    },
    "streamTitle": {
      "IRI": "https://dblp.org/rdf/schema#streamTitle",
      "description": "A title of the stream.",
      "superProperties": ["P2561", "name", "name"],
      "subProperties": ["formerStreamTitle", "primaryStreamTitle"],
      "domains": ["Stream c"],
      "range": "string"
    },
    "subStream": {
      "IRI": "https://dblp.org/rdf/schema#subStream",
      "description": "This stream is (or was) a part of the other stream.",
      "superProperties": ["relatedStream"],
      "domains": ["Stream c"],
      "range": "Stream c",
      "inverseOf": "superStream"
    },
    "successorStream": {
      "IRI": "https://dblp.org/rdf/schema#successorStream",
      "description": "This stream is a successor of the other stream.",
      "superProperties": ["relatedStream"],
      "domains": ["Stream c"],
      "range": "Stream c",
      "inverseOf": "predecessorStream"
    },
    "superStream": {
      "IRI": "https://dblp.org/rdf/schema#superStream",
      "description": "This stream has (or had) the other stream as a part.",
      "superProperties": ["relatedStream"],
      "domains": ["Stream c"],
      "range": "Stream c",
      "inverseOf": "subStream"
    },
    "thesisAcceptedBySchool": {
      "IRI": "https://dblp.org/rdf/schema#thesisAcceptedBySchool",
      "description": "The school where the publication (typically a thesis) has been accepted. (Remark: This property currently just gives literal xsd:string values until institutions are modelled as proper entities.)",
      "domains": ["Publication c"],
      "range": "string"
    },
    "title": {
      "IRI": "https://dblp.org/rdf/schema#title",
      "description": "The title of the publication.",
      "equivalentTo": ["Title", "P1476"],
      "superProperties": ["Title", "name"],
      "domains": ["Publication c"],
      "range": "string"
    },
    "versionConcept": {
      "IRI": "https://dblp.org/rdf/schema#versionConcept",
      "description": "The linked general (concept) publication.",
      "domains": ["VersionRelation c"],
      "range": "Publication c",
      "inverseOf": "hasVersion"
    },
    "versionInstance": {
      "IRI": "https://dblp.org/rdf/schema#versionInstance",
      "description": "The linked specific (instance) publication version.",
      "domains": ["VersionRelation c"],
      "range": "Publication c",
      "inverseOf": "isVersion"
    },
    "versionLabel": {
      "IRI": "https://dblp.org/rdf/schema#versionLabel",
      "description": "The human-readable version label of the specific (instance) publication version.",
      "domains": ["VersionRelation c"],
      "range": "string"
    },
    "versionOrdinal": {
      "IRI": "https://dblp.org/rdf/schema#versionOrdinal",
      "description": "The ordinal number of the specific (instance) publication version. This number is solely intended for sorting purposes: bigger numbers indicate later versions. Version ordinals do not need to describe a complete number range, nor is there a necessary relationship to the version labels.",
      "domains": ["VersionRelation c"],
      "range": "integer"
    },
    "versionUri": {
      "IRI": "https://dblp.org/rdf/schema#versionUri",
      "description": "An (optional) URI of identifying the linked specific (instance) publication version.",
      "domains": ["VersionRelation c"],
      "range": "anyUri"
    },
    "webpage": {
      "IRI": "https://dblp.org/rdf/schema#webpage",
      "description": "The URL of a web page about this item.",
      "equivalentTo": ["page"],
      "superProperties": ["P2699", "url"],
      "subProperties": ["archivedWebpage", "awardwebpage", "documentPage", "homepage", "wikipedia"],
      "domains": ["Entity c"],
      "range": "Document c"
    },
    "wikidata": {
      "IRI": "https://dblp.org/rdf/schema#wikidata",
      "description": "A wikidata item.",
      "equivalentTo": ["wikidata", "wikidata"],
      "superProperties": ["identifier"],
      "domains": ["Entity c"],
      "range": "anyUri"
    },
    "wikipedia": {
      "IRI": "https://dblp.org/rdf/schema#wikipedia",
      "description": "The URL of an (English) Wikipedia article about this item.",
      "superProperties": ["webpage"],
      "domains": ["Entity c"],
      "range": "Document c"
    },
    "yearOfEvent": {
      "IRI": "https://dblp.org/rdf/schema#yearOfEvent",
      "description": "The year the conference or workshop contribution has been presented.",
      "domains": ["Publication c"],
      "range": "gYear"
    },
    "yearOfPublication": {
      "IRI": "https://dblp.org/rdf/schema#yearOfPublication",
      "description": "The year the publication's issue or volume has been published.",
      "equivalentTo": ["publicationDate", "Date Issued", "P577", "publication"],
      "domains": ["Publication c"],
      "range": "gYear"
    }
  }

# deleted_from = {"authorOf": {
#   "IRI": "https://dblp.org/rdf/schema#authorOf",
#   "description": "The creator is the author of the publication."
# },
# "creatorOf": {
#     "IRI": "https://dblp.org/rdf/schema#creatorOf",
#     "description": "The creator of the publication."
#   },
#   "editorOf": {
#     "IRI": "https://dblp.org/rdf/schema#editorOf",
#     "description": "The creator is the editor of the publication."
#   }
# }

properties_uri_and_description = {
  "affiliation": {
    "IRI": "https://dblp.org/rdf/schema#affiliation",
    "description": "A (past or present) affiliation of the creator. (Remark: This property currently just gives literal xsd:string values until institutions are modelled as proper entities.)"
  },
  "archivedWebpage": {
    "IRI": "https://dblp.org/rdf/schema#archivedWebpage",
    "description": "The URL of an archived web page about this item, which may no longer be available in the web."
  },
  "authoredBy": {
    "IRI": "https://dblp.org/rdf/schema#authoredBy",
    "description": "The publication is authored by the creator."
  },
  "awardwebpage": {
    "IRI": "https://dblp.org/rdf/schema#awardWebpage",
    "description": "The URL of a web page about an award received by this creator."
  },
  "bibtexType": {
    "IRI": "https://dblp.org/rdf/schema#bibtexType",
    "description": "The bibtex type of the publication, e.g., book, inproceedings, etc."
  },
  "coAuthorWith": {
    "IRI": "https://dblp.org/rdf/schema#coAuthorWith",
    "description": "The creator is co-author with the other creator."
  },
  "coCreatorWith": {
    "IRI": "https://dblp.org/rdf/schema#coCreatorWith",
    "description": "The creator is co-creator with the other creator."
  },
  "coEditorWith": {
    "IRI": "https://dblp.org/rdf/schema#coEditorWith",
    "description": "The creator is co-editor with the other creator."
  },
  "createdBy": {
    "IRI": "https://dblp.org/rdf/schema#createdBy",
    "description": "The publication is created by the creator."
  },
  "creatorname": {
    "IRI": "https://dblp.org/rdf/schema#creatorName",
    "description": "The full name of the creator."
  },
  "creatorNote": {
    "IRI": "https://dblp.org/rdf/schema#creatorNote",
    "description": "An additional note about the creator."
  },
  "documentPage": {
    "IRI": "https://dblp.org/rdf/schema#documentPage",
    "description": "The URL of the electronic edition of the publication."
  },
  "doi": {
    "IRI": "https://dblp.org/rdf/schema#doi",
    "description": "A Digital Object Identifier."
  },
  "editedBy": {
    "IRI": "https://dblp.org/rdf/schema#editedBy",
    "description": "The publication is edited by the creator."
  },
  "formerStreamTitle": {
    "IRI": "https://dblp.org/rdf/schema#formerStreamTitle",
    "description": "A former title of the stream."
  },
  "hasSignature": {
    "IRI": "https://dblp.org/rdf/schema#hasSignature",
    "description": "A signature that links this publication to an creator."
  },
  "hasVersion": {
    "IRI": "https://dblp.org/rdf/schema#hasVersion",
    "description": "The publication has a different, more specific (instance) publication as its version."
  },
  "homepage": {
    "IRI": "https://dblp.org/rdf/schema#homepage",
    "description": "The URL of an academic homepage of this creator."
  },
  "homonymousCreator": {
    "IRI": "https://dblp.org/rdf/schema#homonymousCreator",
    "description": "This creator shares a homonymous name with the other creator."
  },
  "identifier": {
    "IRI": "https://dblp.org/rdf/schema#identifier",
    "description": "An abstract identifier."
  },
  "indexPage": {
    "IRI": "https://dblp.org/rdf/schema#indexPage",
    "description": "The URL of the dblp stream index page for this stream."
  },
  "isVersion": {
    "IRI": "https://dblp.org/rdf/schema#isVersion",
    "description": "The publication is a version of another, more general (concept) publication."
  },
  "isVersionOf": {
    "IRI": "https://dblp.org/rdf/schema#isVersionOf",
    "description": "The publication is a version of another, more general (concept) publication."
  },
  "isbn": {
    "IRI": "https://dblp.org/rdf/schema#isbn",
    "description": "An International Standard Book Number."
  },
  "iso4": {
    "IRI": "https://dblp.org/rdf/schema#iso4",
    "description": "The stream's ISO4 abbreviation."
  },
  "issn": {
    "IRI": "https://dblp.org/rdf/schema#issn",
    "description": "An International Standard Serial Number."
  },
  "listedOnTocPage": {
    "IRI": "https://dblp.org/rdf/schema#listedOnTocPage",
    "description": "The url of the dblp table of contents page listing this publication."
  },
  "monthOfPublication": {
    "IRI": "https://dblp.org/rdf/schema#monthOfPublication",
    "description": "The month the publication has been published."
  },
  "numberOfCreators": {
    "IRI": "https://dblp.org/rdf/schema#numberOfCreators",
    "description": "The number of creators who created this publication."
  },
  "omid": {
    "IRI": "https://dblp.org/rdf/schema#omid",
    "description": "An OpenCitations Meta Identifier."
  },
  "orcid": {
    "IRI": "https://dblp.org/rdf/schema#orcid",
    "description": "An Open Researcher and Contributor ID."
  },
  "pagination": {
    "IRI": "https://dblp.org/rdf/schema#pagination",
    "description": "The page numbers where the publication can be found."
  },
  "possibleActualCreator": {
    "IRI": "https://dblp.org/rdf/schema#possibleActualCreator",
    "description": "This ambiguous creator may be (or may be not) just a disambiguation proxy for the other creator. Further actual creator candidates are possible."
  },
  "predecessorStream": {
    "IRI": "https://dblp.org/rdf/schema#predecessorStream",
    "description": "This stream is a predecessor of the other stream."
  },
  "primaryAffiliation": {
    "IRI": "https://dblp.org/rdf/schema#primaryAffiliation",
    "description": "The primary affiliation of the creator. (Remark: This property currently just gives literal xsd:string values until institutions are modelled as proper entities.)"
  },
  "primaryCreatorName": {
    "IRI": "https://dblp.org/rdf/schema#primaryCreatorName",
    "description": "The primary full name of the creator."
  },
  "primaryDocumentPage": {
    "IRI": "https://dblp.org/rdf/schema#primaryDocumentPage",
    "description": "The primary URL of the electronic edition of the publication."
  },
  "primaryHomepage": {
    "IRI": "https://dblp.org/rdf/schema#primaryHomepage",
    "description": "The primary URL of an academic homepage of this creator."
  },
  "primaryStreamTitle": {
    "IRI": "https://dblp.org/rdf/schema#primaryStreamTitle",
    "description": "The primary title of the stream."
  },
  "proxyAmbiguousCreator": {
    "IRI": "https://dblp.org/rdf/schema#proxyAmbiguousCreator",
    "description": "This creator (and any of her fellow homonymous creators) is also represented by the given ambiguous creator in cases where the authorship of a publication is undetermined."
  },
  "publicationNote": {
    "IRI": "https://dblp.org/rdf/schema#publicationNote",
    "description": "An additional note to the publication."
  },
  "publishedAsPartOf": {
    "IRI": "https://dblp.org/rdf/schema#publishedAsPartOf",
    "description": "The publication has been published as a part of the other publication."
  },
  "publishedBy": {
    "IRI": "https://dblp.org/rdf/schema#publishedBy",
    "description": "The publisher of the publication. (Remark: This property currently just gives literal xsd:string values until publishers are modelled as proper entities.)"
  },
  "publishedIn": {
    "IRI": "https://dblp.org/rdf/schema#publishedIn",
    "description": "The name of the series, the journal, or the book in which the publication has been published. (Remark: This property currently just gives literal xsd:string values until journals and conference series are modelled as proper entities.)"
  },
  "publishedInBook": {
    "IRI": "https://dblp.org/rdf/schema#publishedInBook",
    "description": "The name of the book in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)"
  },
  "publishedInBookChapter": {
    "IRI": "https://dblp.org/rdf/schema#publishedInBookChapter",
    "description": "The chapter of the book in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)"
  },
  "publishedInJournal": {
    "IRI": "https://dblp.org/rdf/schema#publishedInJournal",
    "description": "The name of the journal in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)"
  },
  "publishedInJournalVolume": {
    "IRI": "https://dblp.org/rdf/schema#publishedInJournalVolume",
    "description": "The volume of the journal in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)"
  },
  "publishedInJournalIssue": {
    "IRI": "https://dblp.org/rdf/schema#publishedInJournalVolumeIssue",
    "description": "The issue of the journal in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)"
  },
  "publishedInSeries": {
    "IRI": "https://dblp.org/rdf/schema#publishedInSeries",
    "description": "The name of the series in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)"
  },
  "publishedInSeriesVolume": {
    "IRI": "https://dblp.org/rdf/schema#publishedInSeriesVolume",
    "description": "The volume of the series in which the publication has been published. (Remark: This is currently an intermediate property that will be removed once journals and conference series are modelled as proper entities.)"
  },
  "publishedInStream": {
    "IRI": "https://dblp.org/rdf/schema#publishedInStream",
    "description": "The conference series, the journal, or the repository in which the publication has been published."
  },
  "publishersAddress": {
    "IRI": "https://dblp.org/rdf/schema#publishersAddress",
    "description": "The address of the publisher. (Remark: This is currently an intermediate property that will be removed once publishers are modelled as proper entities.)"
  },
  "relatedStream": {
    "IRI": "https://dblp.org/rdf/schema#relatedStream",
    "description": "This stream is related to the other stream in some unspecified way."
  },
  "signatureCreator": {
    "IRI": "https://dblp.org/rdf/schema#signatureCreator",
    "description": "A linked creator of the publication."
  },
  "signatureDblpName": {
    "IRI": "https://dblp.org/rdf/schema#signatureDblpName",
    "description": "A dblp name (including any possible trailing homonym number) that links the publication to a creator."
  },
  "signatureOrcid": {
    "IRI": "https://dblp.org/rdf/schema#signatureOrcid",
    "description": "An ORCID that links the publication to a creator."
  },
  "signatureOrdinal": {
    "IRI": "https://dblp.org/rdf/schema#signatureOrdinal",
    "description": "The ordinal number of this signature for the publication, starting with 1."
  },
  "signaturePublication": {
    "IRI": "https://dblp.org/rdf/schema#signaturePublication",
    "description": "The publication of this signature."
  },
  "streamTitle": {
    "IRI": "https://dblp.org/rdf/schema#streamTitle",
    "description": "A title of the stream."
  },
  "subStream": {
    "IRI": "https://dblp.org/rdf/schema#subStream",
    "description": "This stream is (or was) a part of the other stream."
  },
  "successorStream": {
    "IRI": "https://dblp.org/rdf/schema#successorStream",
    "description": "This stream is a successor of the other stream."
  },
  "superStream": {
    "IRI": "https://dblp.org/rdf/schema#superStream",
    "description": "This stream has (or had) the other stream as a part."
  },
  "thesisAcceptedBySchool": {
    "IRI": "https://dblp.org/rdf/schema#thesisAcceptedBySchool",
    "description": "The school where the publication (typically a thesis) has been accepted. (Remark: This property currently just gives literal xsd:string values until institutions are modelled as proper entities.)"
  },
  "title": {
    "IRI": "https://dblp.org/rdf/schema#title",
    "description": "The title of the publication."
  },
  "versionConcept": {
    "IRI": "https://dblp.org/rdf/schema#versionConcept",
    "description": "The linked general (concept) publication."
  },
  "versionInstance": {
    "IRI": "https://dblp.org/rdf/schema#versionInstance",
    "description": "The linked specific (instance) publication version."
  },
  "versionLabel": {
    "IRI": "https://dblp.org/rdf/schema#versionLabel",
    "description": "The human-readable version label of the specific (instance) publication version."
  },
  "versionOrdinal": {
    "IRI": "https://dblp.org/rdf/schema#versionOrdinal",
    "description": "The ordinal number of the specific (instance) publication version. This number is solely intended for sorting purposes: bigger numbers indicate later versions. Version ordinals do not need to describe a complete number range, nor is there a necessary relationship to the version labels."
  },
  "versionUri": {
    "IRI": "https://dblp.org/rdf/schema#versionUri",
    "description": "An (optional) URI of identifying the linked specific (instance) publication version."
  },
  "webpage": {
    "IRI": "https://dblp.org/rdf/schema#webpage",
    "description": "The URL of a web page about this item."
  },
  "wikidata": {
    "IRI": "https://dblp.org/rdf/schema#wikidata",
    "description": "A wikidata item."
  },
  "wikipedia": {
    "IRI": "https://dblp.org/rdf/schema#wikipedia",
    "description": "The URL of an (English) Wikipedia article about this item."
  },
  "yearOfEvent": {
    "IRI": "https://dblp.org/rdf/schema#yearOfEvent",
    "description": "The year the conference or workshop contribution has been presented."
  },
  "yearOfPublication": {
    "IRI": "https://dblp.org/rdf/schema#yearOfPublication",
    "description": "The year the publication's issue or volume has been published."
  }
}