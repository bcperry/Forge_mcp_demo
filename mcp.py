from typing import Any
from enum import Enum
import httpx
import logging
from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Optional, Annotated
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from stubapi.models import (
    ActivityApprovalStatusDto,
ActivityInitialInsightsDto,
ActivityNotesDto,
ActivityPlanningTimelineDto,
ActivityRecommendationsDto,
AssessmentAccessRequestDto,
AssessmentClaDto,
AssessmentGapRsaDto,
AssessmentGeneralInformationDto,
AssessmentTcbaProjectCreateDto,
ClaDto,
CommentDto,
ConceptCommandPostDto,
ConceptEnablerDto,
ConceptEquipCapabilityChangesDto,
ConceptEquipmentMappingDto,
ConceptGeneralInformationDto,
ConceptLearningEventMappingDto,
ConceptLitLibraryDocumentsDto,
ConceptMeasurementDto,
ConceptNotionDto,
ConceptScenarioMappingDto,
ConceptScienceTechMappingDto,
ConceptTaskMappingDto,
CrcMappingDto,
CrcSolutionSetMappingDto,
DataGridChangeDto,
DataSourceLoadOptions,
DiscriminatorDto,
DocumentSearchSortOrder,
DynamicTableColumnDto,
DynamicTableColumnLookupDto,
DynamicTableDto,
DynamicTableEditingOptionsDto,
EeaDto,
ForgeFileDto,
GapDraftDto,
GapWorkflowStep,
GapWorksheetDto,
GroupingInfo,
GuidLookupDto,
Int32FileMetadataDto,
InterdependenciesDto,
LdResponseMappingDto,
LdResponsesReviewDto,
LearningActivityDocumentFileDto,
LearningActivityDto,
LearningActivityGeneralInformationDto,
LearningDemandDto,
LearningDemandEeaMappingDto,
LearningDemandGenInfoDto,
LearningDemandRequiredCapabilityDto,
LearningDemandTddDto,
LearningEventDto,
LearningTddType,
MeasureCategoryDto,
MeasureDto,
MilestoneDto,
MilestoneTemplateDto,
ModernizationImpactDto,
MyProfileDto,
ReferenceTable,
RequiredCapabilitiesDto,
ResourcesNewViewDto,
RoleDto,
RsaSolutionIdeaDto,
ScienceTechnologyDto,
SecureNetwork,
SolutionIdeaAcquisitionDto,
SolutionIdeaDto,
SolutionIdeaFeasibilityDto,
SolutionIdeaGeneralInformationDto,
SolutionIdeaPocDto,
SolutionIdeaPriorityDto,
SolutionIdeaReadinessDto,
SolutionPriorityAlgorithm,
SolutionReviewGridDto,
SolutionSetDto,
SortingInfo,
SummaryInfo,
TaskMappingCreateUserDefinedDto,
TcbaLookupTable,
TddAdministrativeFormDto,
TddClosureDto,
TddCreateDto,
TddDto,
TddLearningDemandMappingDto,
TddProblemDispositionFormDto,
UserInfoDto,
)

mcp = FastMCP("Forge")

# bare bones example of a FastMCP streamable-http server

class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"

# Add MCP functionality with decorators
# Constants
FORGE_API_BASE = "https://localhost:8042"  # Changed to HTTPS for self-signed cert
USER_AGENT = "Army-Forge-mcp/0.1"

async def make_request(url: str, method: HttpMethod, params: dict[str, Any] | None = None) -> str | None:
    """Make a request to the Forge API with proper error handling and SSL verification disabled for self-signed certs."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    # Disable SSL verification for self-signed certificates
    async with httpx.AsyncClient(verify=False) as client:
        try:
            logger.info(f"(make_request) Sending request to Forge API: {url}")
            if method == HttpMethod.GET:
                response = await client.get(url, headers=headers, params=params, timeout=30.0)
            elif method == HttpMethod.POST:
                response = await client.post(url, headers=headers, json=params, timeout=30.0)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            logger.info(f"(make_request) Response status code: {response.status_code}")
            response.raise_for_status()
            return response.text
        except Exception as e:
            logger.error(f"(make_request) Error making request: {e}")
            return e

@mcp.tool()
# async def create_concept(concept: ConceptGeneralInformationDto) -> list[dict[str, Any]]:  This should work, but it seems to be a bug in FastMCP
async def create_concept(PocId: Annotated[str, Field(description="Point of Contact ID")],
    DiscoverabilityGuid: Annotated[str, Field(description="Discoverability GUID")],
    StatusId: Annotated[str, Field(description="Status ID")],
    AocYear: Annotated[str, Field(description="Area of Concern Year")],
    TypeGuid: Annotated[str, Field(description="Type GUID")],
    LeadOrganizationId: Annotated[str, Field(description="Lead Organization ID")],
    Id: Annotated[int, Field(description="ID")],
    Name: Annotated[str, Field(min_length=5)],
    StatusDescription: Annotated[str, Field(description="Status Description")] = None,
    AocYearString: Annotated[str, Field(description="Area of Concern Year (in YYYY)") ] = None,
    LearningYear: Annotated[str, Field(description="Learning Year (in YYYY)")] = None,
    LearningYearString: Annotated[str, Field(description="Learning Year String (ex. FEB061991)")] = None,
    AdditionalLeadOrganizations: Annotated[list, Field(description="A comma separated list of additional Lead Organizations, provided in square brackets ex: [<ID1>, <ID2>]")] = None,
    SupportingOrganizationId: Annotated[str, Field(description="Supporting Organization ID")] = None,
    AdditionalSupportingOrganizations: Annotated[list, Field(description="A comma separated list of additional Supporting Organizations, provided in square brackets ex: [<ID1>, <ID2>]")] = None,
    FormationIds: Annotated[list, Field(description="Formation IDs")] = None,
    OrganizationDescription: Annotated[str, Field(description="Organization Description")] = None,
    OperationalChanges: Annotated[str, Field(description="Operational Changes")] = None,
    Mission: Annotated[str, Field(description="Mission")] = None,
    Hypothesis: Annotated[str, Field(description="Hypothesis")] = None,
    Purpose: Annotated[str, Field(description="Purpose")] = None,
    Scope: Annotated[str, Field(description="Scope")] = None,
    Image: Annotated[str, Field(description="Image")] = None,
    ModifiedDate: Annotated[str, Field(description="Modified Date")] = None,
    LastModifiedDate: Annotated[str, Field(description="Last Modified Date")] = None,
    CreatorName: Annotated[str, Field(description="Creator Name")] = None,
    CreatorEmail: Annotated[str, Field(description="Creator Email")] = None,
    CreatorPhone: Annotated[str, Field(description="Creator Phone")] = None,
    PocName: Annotated[str, Field(description="Point of Contact Name")] = None,
    PocEmail: Annotated[str, Field(description="Point of Contact Email")] = None,
    PocPhone: Annotated[str, Field(description="Point of Contact Phone")] = None,
    OrganizationSize: Annotated[int, Field(description="Organization Size integer to the nearest 1000")] = None,
    ConceptNotionTypeId: Annotated[str, Field(description="Concept Notion Type ID")] = None,
    ShortTitle: Annotated[str, Field(description="Short Title")] = None,
    IsFcw: bool = False) -> str | None:
    """Create a concept for use in the Forge application.
    """

    concept = ConceptGeneralInformationDto(
        Id=Id,
        Name=Name,
        DiscoverabilityGuid=DiscoverabilityGuid,
        StatusId=StatusId,
        StatusDescription=StatusDescription,
        AocYear=AocYear,
        AocYearString=AocYearString,
        LearningYear=LearningYear,
        LearningYearString=LearningYearString,
        TypeGuid=TypeGuid,
        LeadOrganizationId=LeadOrganizationId,
        AdditionalLeadOrganizations=AdditionalLeadOrganizations,
        SupportingOrganizationId=SupportingOrganizationId,
        AdditionalSupportingOrganizations=AdditionalSupportingOrganizations,
        FormationIds=FormationIds,
        OrganizationDescription=OrganizationDescription,
        OperationalChanges=OperationalChanges,
        Mission=Mission,
        Hypothesis=Hypothesis,
        Purpose=Purpose,
        Scope=Scope,
        Image=Image,
        ModifiedDate=ModifiedDate,
        LastModifiedDate=LastModifiedDate,
        CreatorName=CreatorName,
        CreatorEmail=CreatorEmail,
        CreatorPhone=CreatorPhone,
        PocId=PocId,
        PocName=PocName,
        PocEmail=PocEmail,
        PocPhone=PocPhone,
        OrganizationSize=OrganizationSize,
        ConceptNotionTypeId=ConceptNotionTypeId,
        ShortTitle=ShortTitle,
        IsFcw=IsFcw
    )


    TOOL_ENDPOINT = "/api/Concept/Create"
    try:
        # Convert Pydantic model to dictionary for JSON serialization
        concept_dict = concept.model_dump()
        logger.info(f"Creating concept with data: {concept_dict}")
        response = await make_request(f"{FORGE_API_BASE}{TOOL_ENDPOINT}", method=HttpMethod.POST, params=concept_dict)
        return response
    except Exception as e:
        logger.error(f"Error creating concept: {e}")
        return f"Error creating concept: {e}"

@mcp.tool()
async def create_solution_idea(
    MappingId: Annotated[str, Field(description="Mapping ID")] = None,
    RsaId: Annotated[int, Field(description="RSA ID")] = None,
    SolutionIdeaId: Annotated[str, Field(description="Solution Idea ID")] = None,
    GapCodeId: Annotated[str, Field(description="Gap Code ID")] = None,
    ShortName: Annotated[str, Field(description="Short name of the solution idea")] = None,
    Description: Annotated[str, Field(description="Description of the solution idea")] = None,
    Domain: Annotated[str, Field(description="Domain of the solution")] = None,
    OprProponent: Annotated[str, Field(description="Operational proponent")] = None,
    Comments: Annotated[str, Field(description="Comments about the solution idea")] = None,
    TechnicalRisk: Annotated[str, Field(description="Technical risk assessment")] = None,
    Supportability: Annotated[str, Field(description="Supportability assessment")] = None,
    Affordability: Annotated[str, Field(description="Affordability assessment")] = None,
    Availability: Annotated[str, Field(description="Availability assessment")] = None,
    ApprovedToRsa: Annotated[bool, Field(description="Whether approved to RSA")] = None,
    StudyLead: Annotated[str, Field(description="Study lead contact")] = None,
    StudyLeadComment: Annotated[str, Field(description="Study lead comments")] = None,
    MitigationExtentId: Annotated[str, Field(description="Mitigation extent ID")] = None,
    MitigationExtent: Annotated[str, Field(description="Mitigation extent description")] = None,
    MitigationExtentOrderNbr: Annotated[int, Field(description="Mitigation extent order number")] = None,
    CdidSolutionPriority: Annotated[int, Field(description="CDID solution priority number")] = None,
    TechnicalReadinessLevel: Annotated[str, Field(description="Technical readiness level")] = None,
    FeasibilityDegree: Annotated[str, Field(description="Feasibility degree assessment")] = None,
    MappedGaps: Annotated[list, Field(description="List of mapped gaps")] = None,
    MappedGapNames: Annotated[str, Field(description="Names of mapped gaps")] = None
) -> str | None:
    """Create a solution idea in the Forge Pathfinder system.
    
    This tool creates a new solution idea with RSA (Requirements Solution Analysis) mapping
    that can be used to address capability gaps identified in assessments. Ensure that you have retrieved the
    mandatory solution information before using this tool, and only use that data as inputs.
    """
    
    solution_idea = RsaSolutionIdeaDto(
        MappingId=MappingId,
        RsaId=RsaId,
        SolutionIdeaId=SolutionIdeaId,
        GapCodeId=GapCodeId,
        ShortName=ShortName,
        Description=Description,
        Domain=Domain,
        OprProponent=OprProponent,
        Comments=Comments,
        TechnicalRisk=TechnicalRisk,
        Supportability=Supportability,
        Affordability=Affordability,
        Availability=Availability,
        ApprovedToRsa=ApprovedToRsa,
        StudyLead=StudyLead,
        StudyLeadComment=StudyLeadComment,
        MitigationExtentId=MitigationExtentId,
        MitigationExtent=MitigationExtent,
        MitigationExtentOrderNbr=MitigationExtentOrderNbr,
        CdidSolutionPriority=CdidSolutionPriority,
        TechnicalReadinessLevel=TechnicalReadinessLevel,
        FeasibilityDegree=FeasibilityDegree,
        MappedGaps=MappedGaps,
        MappedGapNames=MappedGapNames
    )

    TOOL_ENDPOINT = "/api/pathfinder/SolutionIdeas"
    try:
        # Convert Pydantic model to dictionary for JSON serialization
        solution_idea_dict = solution_idea.model_dump()
        logger.info(f"Creating solution idea with data: {solution_idea_dict}")
        response = await make_request(f"{FORGE_API_BASE}{TOOL_ENDPOINT}", method=HttpMethod.POST, params=solution_idea_dict)
        return response
    except Exception as e:
        logger.error(f"Error creating solution idea: {e}")
        return f"Error creating solution idea: {e}"

@mcp.tool()
async def get_required_solution_idea_data() -> dict | None:
    """Get organization, idea type, and warfighting gap data for solution ideas from the Forge API.
    
    Returns a dictionary containing:
    - organizations: List of organization objects with OrganizationGuid, OrganizationName, etc.
    - ideaTypes: List of domain/idea type objects with DomainId, DomainCode, DomainText, etc.
    - warfightingGaps: List of warfighting gap categories with Key, Value, Code
    """
    OPR_OCR_ENDPOINT = "/api/lookuptables/organizations"
    IDEA_TYPE_ENDPOINT = "/api/lookuptables/ideaTypes"
    WAR_FIGHTING_GAP_CATEGORIES_ENDPOINT = "/api/lookuptables/listwarfightinggapcategories"
    
    try:
        import json
        
        # Fetch organizations data
        opr_response = await make_request(f"{FORGE_API_BASE}{OPR_OCR_ENDPOINT}", method=HttpMethod.GET)
        organizations = []
        if opr_response and isinstance(opr_response, str):
            parsed_opr_response = json.loads(opr_response)
            if "data" in parsed_opr_response and "data" in parsed_opr_response["data"]:
                organizations = parsed_opr_response["data"]["data"]
            else:
                logger.warning("Unexpected organization response structure")
        
        # Fetch idea types data
        idea_type_response = await make_request(f"{FORGE_API_BASE}{IDEA_TYPE_ENDPOINT}", method=HttpMethod.GET)
        idea_types = []
        if idea_type_response and isinstance(idea_type_response, str):
            parsed_idea_response = json.loads(idea_type_response)
            if "data" in parsed_idea_response and "data" in parsed_idea_response["data"]:
                idea_types = parsed_idea_response["data"]["data"]
            else:
                logger.warning("Unexpected idea type response structure")
        
        # Fetch warfighting gap categories data
        warfighting_gap_response = await make_request(f"{FORGE_API_BASE}{WAR_FIGHTING_GAP_CATEGORIES_ENDPOINT}", method=HttpMethod.GET)
        warfighting_gaps = []
        if warfighting_gap_response and isinstance(warfighting_gap_response, str):
            parsed_gap_response = json.loads(warfighting_gap_response)
            if "data" in parsed_gap_response and "data" in parsed_gap_response["data"]:
                warfighting_gaps = parsed_gap_response["data"]["data"]
            else:
                logger.warning("Unexpected warfighting gap response structure")
        
        # Return combined data
        return {
            "organizations": organizations,
            "ideaTypes": idea_types,
            "warfightingGaps": warfighting_gaps
        }
        
    except Exception as e:
        logger.error(f"Error fetching solution idea data: {e}")
        return None
    



if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8000)

