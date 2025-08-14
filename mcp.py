from typing import Any
from enum import Enum
import httpx
from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Optional, Annotated

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
FORGE_API_BASE = "http://localhost:8042"
USER_AGENT = "Army-Forge-mcp/0.1"

async def make_request(url: str, method: HttpMethod, params: dict[str, Any] | None = None) -> str | None:
    """Make a request to the Army publications API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    async with httpx.AsyncClient() as client:
        try:
            print(f"(make_request) Sending request to Forge API: {url}")
            if method == HttpMethod.GET:
                response = await client.get(url, headers=headers, params=params, timeout=30.0)
            elif method == HttpMethod.POST:
                response = await client.post(url, headers=headers, json=params, timeout=30.0)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            print(f"(make_request) Response status code: {response.status_code}")
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"(make_request) Error making request: {e}")
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
        print(f"Creating concept with data: {concept_dict}")
        response = await make_request(f"{FORGE_API_BASE}{TOOL_ENDPOINT}", method=HttpMethod.POST, params=concept_dict)
        return response
    except Exception as e:
        print(f"Error creating concept: {e}")
        return f"Error creating concept: {e}"





if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8000)

