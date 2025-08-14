from fastapi import FastAPI, HTTPException, Query, Path, Body
from fastapi.responses import JSONResponse
from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from enum import Enum, IntEnum
from .models import (
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


import json

# Initialize FastAPI app
app = FastAPI(
    title="FORGE API",
    description="FORGE API Stub Implementation",
    version="v1",
    contact={
        "name": "FORGE Contact",
        "email": "forge@army.mil"
    }
)





@app.post('/api/AiAssistant/CompleteForm', tags=['AiAssistantApi'])
async def post_api_AiAssistant_CompleteForm(body: str) -> dict:
    """
    Prompts the AI assistant to complete a form
    
    Tags: AiAssistantApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/AiAssistant/SummarizeDocument', tags=['AiAssistantApi'])
async def get_api_AiAssistant_SummarizeDocument(filepath: Optional[str] = None) -> dict:
    """
    Prompts the AI assistant to summarize a file by its path
    
    Tags: AiAssistantApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/AiAssistant/SummarizeDocument/{fileId}', tags=['AiAssistantApi'])
async def get_api_AiAssistant_SummarizeDocument(fileId: str) -> dict:
    """
    Prompts the AI assistant to summarize a file by its ID
    
    Tags: AiAssistantApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/AiChatBot/Message', tags=['AiChatBotApi'])
async def post_api_AiChatBot_Message(usermessage: Optional[str] = None) -> dict:
    """
    Sends a user message to the chatbot and retrieves a response.
    
    Tags: AiChatBotApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.delete('/api/assessments/{id}', tags=['AssessmentApi'])
async def delete_api_assessments(id: str) -> dict:
    """
    Delete an Assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/assessments/AccessRequests', tags=['AssessmentApi'])
async def get_api_assessments_AccessRequests(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns list of access requests on the assessment's admin page
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/assessments/AccessRequests', tags=['AssessmentApi'])
async def post_api_assessments_AccessRequests(body: AssessmentAccessRequestDto) -> dict:
    """
    Creates an assessment permissions request
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.put('/api/assessments/AccessRequests/{id}', tags=['AssessmentApi'])
async def put_api_assessments_AccessRequests(id: str, body: List[AssessmentAccessRequestDto]) -> dict:
    """
    Save updates to assessment access requests (approve/deny)
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/assessments/AllGaps', tags=['AssessmentApi'])
async def get_api_assessments_AllGaps(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets all gaps for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/ApprovedGaps', tags=['AssessmentApi'])
async def get_api_assessments_ApprovedGaps(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets approved gaps for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/ApprovedUnmappedGaps', tags=['AssessmentApi'])
async def get_api_assessments_ApprovedUnmappedGaps(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets approved, unmapped gaps for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/AssessmentFileExists/{id}', tags=['AssessmentApi'])
async def get_api_assessments_AssessmentFileExists(id: str, relativepath: Optional[str] = None) -> dict:
    """
    Checks if an Assessment file exists
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/AssessmentGapMapping/{id}', tags=['AssessmentApi'])
async def post_api_assessments_AssessmentGapMapping(id: str, gapcodeid: Optional[str] = None) -> dict:
    """
    Maps a gap to an assessment from another assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.delete('/api/assessments/AssessmentGapMappingDelete/{id}', tags=['AssessmentApi'])
async def delete_api_assessments_AssessmentGapMappingDelete(id: str, gapcodeid: Optional[str] = None) -> dict:
    """
    Maps a gap to an assessment from another assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/assessments/AssessmentGaps', tags=['AssessmentApi'])
async def get_api_assessments_AssessmentGaps(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets all gaps for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/CgApprovalMemoFile/{id}', tags=['AssessmentApi'])
async def post_api_assessments_CgApprovalMemoFile(id: str) -> dict:
    """
    Save posted Cg approval memo file to the blob storage and return file id.
The file is posted as multipart/form-data to this method
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/Clas', tags=['AssessmentApi'])
async def get_api_assessments_Clas(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of CLAs for a specific Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/Clas/{id}', tags=['AssessmentApi'])
async def post_api_assessments_Clas(id: str, body: List[AssessmentClaDto], query_id: Optional[int] = None) -> dict:
    """
    Endpoint responsible for saving CLA changes for an
Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/assessments/Clas/{id}', tags=['AssessmentApi'])
async def delete_api_assessments_Clas(id: str, query_id: Optional[int] = None, claids: Optional[List[dict]] = None) -> dict:
    """
    Delete a list of Assessment CLAs
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/assessments/CreateProject', tags=['AssessmentApi'])
async def post_api_assessments_CreateProject(body: AssessmentTcbaProjectCreateDto) -> dict:
    """
    Endpoint responsible for saving new Tcba Project.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/assessments/DegreeOfFeasibility', tags=['AssessmentApi'])
async def get_api_assessments_DegreeOfFeasibility(technicalriskid: Optional[str] = None, supportabilityid: Optional[str] = None, affordabilityid: Optional[str] = None) -> dict:
    """
    Calculates degree of feasibility based on technical risk, supportability and affordability
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/DocumentSearch', tags=['AssessmentApi'])
async def get_api_assessments_DocumentSearch(searchterm: Optional[str] = None, indexname: Optional[str] = None, sortorder: Optional[DocumentSearchSortOrder] = None, filters: Optional[str] = None) -> dict:
    """
    Search the blob storage files for the search term in the assessments search index
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/DownloadFile', tags=['AssessmentApi'])
async def get_api_assessments_DownloadFile(id: Optional[int] = None, fileid: Optional[int] = None) -> dict:
    """
    Download file associated with the Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/exportassessmentquadcharts/{id}', tags=['AssessmentApi'])
async def get_api_assessments_exportassessmentquadcharts(id: str) -> dict:
    """
    Calls service method to export Gap Quad Charts for an Assessment to PowerPoint
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/exportindividualquadcharts', tags=['AssessmentApi'])
async def get_api_assessments_exportindividualquadcharts(guidsstring: Optional[str] = None) -> dict:
    """
    Calls service method to export Gap Quad Charts identified by GUID to PowerPoint
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/FailedTaskGaps', tags=['AssessmentApi'])
async def get_api_assessments_FailedTaskGaps(id: Optional[int] = None, failedgaps: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets failed task gaps for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/FileHasOtherReferences/{id}', tags=['AssessmentApi'])
async def get_api_assessments_FileHasOtherReferences(id: str, fileid: Optional[int] = None) -> dict:
    """
    Endpoint for checking for multiple file references.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/FileMappings/{id}', tags=['AssessmentApi'])
async def post_api_assessments_FileMappings(id: str, fileid: Optional[int] = None) -> dict:
    """
    Map a file to the Assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/Files', tags=['AssessmentApi'])
async def get_api_assessments_Files(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Endpoint for listing files associated with this assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/Files/{id}', tags=['AssessmentApi'])
async def post_api_assessments_Files(id: str) -> dict:
    """
    Upload a file to the assessment.  File metadata should be posted
as part of the FormData as Forge.Core.DTO.FileMetadataDto`1
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/assessments/Files/{id}', tags=['AssessmentApi'])
async def delete_api_assessments_Files(id: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Delete file mappings for the Assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/assessments/Gap', tags=['AssessmentApi'])
async def get_api_assessments_Gap(gapcodeguid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a Gap by Gap Code GUID
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/GapApproval/{id}', tags=['AssessmentApi'])
async def post_api_assessments_GapApproval(id: str, gapcodeid: Optional[str] = None, workflowstep: Optional[GapWorkflowStep] = None) -> dict:
    """
    Records the approval of a gap
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/GapApprovalCgApprovalMemo/{id}', tags=['AssessmentApi'])
async def post_api_assessments_GapApprovalCgApprovalMemo(id: str, body: List[dict], fileid: Optional[int] = None) -> dict:
    """
    Records the approval of a gap with a Cg Approval Memo Upload
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/assessments/GapDrafts', tags=['AssessmentApi'])
async def get_api_assessments_GapDrafts(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List all draft gaps for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/GapDrafts/{id}', tags=['AssessmentApi'])
async def post_api_assessments_GapDrafts(id: str, body: GapDraftDto) -> dict:
    """
    Creates a new gap or updates and existing draft gap mapped to an Assessment Unit/Task/Scenario/Contition combo.
Permissions checks are performed in the service
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/assessments/GapFileExists', tags=['AssessmentApi'])
async def get_api_assessments_GapFileExists(gapcodeid: Optional[str] = None, relativepath: Optional[str] = None) -> dict:
    """
    Checks if a Gap file exists
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/GapLinkedLearningDemands', tags=['AssessmentApi'])
async def get_api_assessments_GapLinkedLearningDemands(id: Optional[int] = None, gapcodeguid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get the linked Learning Demands for a gap
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/GapOv1File/{gapCodeId}', tags=['AssessmentApi'])
async def post_api_assessments_GapOv1File(gapCodeId: str) -> dict:
    """
    Save posted OV1 file to associated with the gap.
The file is posted as multipart/form-data to this method
Permissions are checked in the service
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/GapRsas', tags=['AssessmentApi'])
async def get_api_assessments_GapRsas(id: Optional[int] = None, gapcodeid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets RSAs for a specified Gap.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/GapRsas/{id}', tags=['AssessmentApi'])
async def post_api_assessments_GapRsas(id: str, body: AssessmentGapRsaDto) -> dict:
    """
    Create a new RSA or save risk management level and workflow step.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/assessments/GapRsas/{id}', tags=['AssessmentApi'])
async def delete_api_assessments_GapRsas(id: str, rsaid: Optional[int] = None) -> dict:
    """
    Deletes an RSA in a gap for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/assessments/GapWorksheet', tags=['AssessmentApi'])
async def post_api_assessments_GapWorksheet(body: GapWorksheetDto) -> dict:
    """
    Creates a new gap or updates and existing draft gap mapped to an assessment.
Permissions checks are performed in the service
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/assessments/GapWorksheetGapMitigation', tags=['AssessmentApi'])
async def get_api_assessments_GapWorksheetGapMitigation(gapcodeid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of solution ideas for a gap on gap worksheet page
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/GeneralInformation/{id}', tags=['AssessmentApi'])
async def post_api_assessments_GeneralInformation(id: str, body: AssessmentGeneralInformationDto) -> dict:
    """
    Updates the General Information for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/assessments/GetApprovedSolutions', tags=['AssessmentApi'])
async def get_api_assessments_GetApprovedSolutions(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of AFC-approved RSAs mapped to the Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/ImpactSolutionsByTier1GapCategory', tags=['AssessmentApi'])
async def get_api_assessments_ImpactSolutionsByTier1GapCategory(tier1gapcategoryid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List Solution Ideas for a Tier 1 Gap Category ordered by priority score/ranking
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/LearningDemandExport/{id}', tags=['AssessmentApi'])
async def get_api_assessments_LearningDemandExport(id: str) -> dict:
    """
    Retrieve data needed to export Gaps and Learning Demands for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/LearningDemands/{id}', tags=['AssessmentApi'])
async def post_api_assessments_LearningDemands(id: str, gapcodeguid: Optional[str] = None, ldid: Optional[int] = None) -> dict:
    """
    Endpoint for saving new Learning Demand mappings
for the Gap.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/assessments/LearningDemands/{id}', tags=['AssessmentApi'])
async def delete_api_assessments_LearningDemands(id: str, ldid: Optional[int] = None, gapcodeguid: Optional[str] = None) -> dict:
    """
    Endpoint for deleting Learning Demand mappings
for the Gap.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/assessments/LinkableGapLearningDemands', tags=['AssessmentApi'])
async def get_api_assessments_LinkableGapLearningDemands(id: Optional[int] = None, gapcodeguid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get Learning Demands that have not been linked to a gap
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/lookuptables/{lookupTable}', tags=['AssessmentApi'])
async def get_api_assessments_lookuptables(lookupTable: str) -> dict:
    """
    Get properties and data for the requested lookup table
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/assessments/lookuptables/{lookupTable}', tags=['AssessmentApi'])
async def post_api_assessments_lookuptables(lookupTable: str, body: List[DataGridChangeDto]) -> dict:
    """
    Saves changes for a lookup table.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/assessments/MitigationGaps', tags=['AssessmentApi'])
async def get_api_assessments_MitigationGaps(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets gaps that can be mitigated for an assessment.  Must be Approved or CDID Approved
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/NonApprovedGaps', tags=['AssessmentApi'])
async def get_api_assessments_NonApprovedGaps(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets non approved gaps for an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/NonApprovedGapsCgApproval', tags=['AssessmentApi'])
async def get_api_assessments_NonApprovedGapsCgApproval(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets non approved gaps for an assessment for cg approval upload
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/NonEmptySolutionSets', tags=['AssessmentApi'])
async def get_api_assessments_NonEmptySolutionSets(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of all unmapped solution sets.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/OtherFileMappings', tags=['AssessmentApi'])
async def get_api_assessments_OtherFileMappings(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Endpoint for listing file mappings associated with other Assessments,
excluding the current Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/RequiredCapabilities', tags=['AssessmentApi'])
async def get_api_assessments_RequiredCapabilities(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of mapped required capabilities for an assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/RequiredCapabilities/{id}', tags=['AssessmentApi'])
async def post_api_assessments_RequiredCapabilities(id: str, crcid: Optional[int] = None) -> dict:
    """
    Endpoint for mapping a Required Capability to the Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/assessments/RequiredCapabilities/{id}', tags=['AssessmentApi'])
async def delete_api_assessments_RequiredCapabilities(id: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Endpoint for removing a mapping for the Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/assessments/RsaApproval/{id}', tags=['AssessmentApi'])
async def post_api_assessments_RsaApproval(id: str, rsaid: Optional[int] = None, approve: Optional[bool] = None) -> dict:
    """
    Approves a Gap's RSA in an Assessment at the AFC level.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.put('/api/assessments/RsaSolutionIdeaApproval/{id}', tags=['AssessmentApi'])
async def put_api_assessments_RsaSolutionIdeaApproval(id: str, mappingid: Optional[str] = None, approve: Optional[bool] = None) -> dict:
    """
    Approves an solution idea on an RSA for a gap in an assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/RsaSolutionIdeas', tags=['AssessmentApi'])
async def get_api_assessments_RsaSolutionIdeas(id: Optional[int] = None, rsaid: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets solution ideas mapped to in an RSA for a gap.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.put('/api/assessments/RsaSolutionIdeas/{id}', tags=['AssessmentApi'])
async def put_api_assessments_RsaSolutionIdeas(id: str, rsaid: Optional[int] = None, solutionideaid: Optional[str] = None) -> dict:
    """
    Links an unmapped solution idea to an RSA in a gap.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/assessments/RsaSolutionIdeas/{id}', tags=['AssessmentApi'])
async def post_api_assessments_RsaSolutionIdeas(id: str, body: RsaSolutionIdeaDto) -> dict:
    """
    Updates an RSA/Solution Idea mapping with study lead changes or risk mitigation level
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/assessments/RsaSolutionIdeas/{id}', tags=['AssessmentApi'])
async def delete_api_assessments_RsaSolutionIdeas(id: str, mappingid: Optional[str] = None) -> dict:
    """
    Removes a Solution Idea from the RSA for a gap in an assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/assessments/RsaSolutions', tags=['AssessmentApi'])
async def get_api_assessments_RsaSolutions(id: Optional[int] = None, rsaid: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of Solutions for the specified Gap in an Assessment's RSA.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/RsaSolutions/{id}', tags=['AssessmentApi'])
async def post_api_assessments_RsaSolutions(id: str, body: RsaSolutionIdeaDto) -> dict:
    """
    Updates an RSA under Review for a gap in an Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/assessments/RsaSolutionSets/{id}', tags=['AssessmentApi'])
async def post_api_assessments_RsaSolutionSets(id: str, rsaid: Optional[int] = None, solutionsetid: Optional[str] = None) -> dict:
    """
    Adds all the solution ideas to the RSA from the selected solution set
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/SolutionIdeaPriorityDiscriminatorParams', tags=['AssessmentApi'])
async def post_api_assessments_SolutionIdeaPriorityDiscriminatorParams(body: SolutionIdeaPriorityDto) -> dict:
    """
    Saves Solution Idea Priority Discriminator values via JSON.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/assessments/SolutionPriority', tags=['AssessmentApi'])
async def get_api_assessments_SolutionPriority(algorithm: Optional[SolutionPriorityAlgorithm] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of calculated top priorities for solution ideas in RSAs.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/SolutionPriorityAll', tags=['AssessmentApi'])
async def get_api_assessments_SolutionPriorityAll(algorithm: Optional[SolutionPriorityAlgorithm] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of priorities for solution ideas for each assigned gap.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/SolutionPriorityAllGapSelectionOptions', tags=['AssessmentApi'])
async def get_api_assessments_SolutionPriorityAllGapSelectionOptions(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of gaps for the Solution Priority (all) gap selection functionality
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/SolutionPriorityGapSelectionOptions', tags=['AssessmentApi'])
async def get_api_assessments_SolutionPriorityGapSelectionOptions(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of gaps for the Solution Priority gap selection functionality
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/SolutionReview', tags=['AssessmentApi'])
async def get_api_assessments_SolutionReview(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of Gaps with RSAs in an Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/SolutionReview/{id}', tags=['AssessmentApi'])
async def post_api_assessments_SolutionReview(id: str, body: SolutionReviewGridDto) -> dict:
    """
    Updates an Solution under Review for a Proponent and Gap in an Assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/assessments/SolutionReviewExport/{id}', tags=['AssessmentApi'])
async def get_api_assessments_SolutionReviewExport(id: str, proponentid: Optional[str] = None) -> dict:
    """
    Retrieve all solutions for the assessment
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/SolutionReviewProponents', tags=['AssessmentApi'])
async def get_api_assessments_SolutionReviewProponents(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of Proponents.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/assessments/UndoGapApproval/{id}', tags=['AssessmentApi'])
async def post_api_assessments_UndoGapApproval(id: str, gapcodeid: Optional[str] = None, workflowstep: Optional[GapWorkflowStep] = None) -> dict:
    """
    Undo/revert the approval of a gap
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/UnmappedRequiredCapabilities', tags=['AssessmentApi'])
async def get_api_assessments_UnmappedRequiredCapabilities(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of all required capabilities that have not already been mapped to an assessment.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/assessments/UnmappedRsaSolutionIdeas', tags=['AssessmentApi'])
async def get_api_assessments_UnmappedRsaSolutionIdeas(id: Optional[int] = None, rsaid: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of all unmapped solution ideas for a particular RSA.
    
    Tags: AssessmentApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept', tags=['ConceptApi'])
async def get_api_Concept(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get version history for this concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.delete('/api/Concept/{id}', tags=['ConceptApi'])
async def delete_api_Concept(id: str) -> dict:
    """
    Delete a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/AllFiles', tags=['ConceptApi'])
async def get_api_Concept_AllFiles() -> dict:
    """
    Retrieves all files uploaded from a concept 
or the concept literature library
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/AssessedTasks', tags=['ConceptApi'])
async def get_api_Concept_AssessedTasks(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of tasks associated with this concept through an assessment
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/AvailableFormations', tags=['ConceptApi'])
async def get_api_Concept_AvailableFormations(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets details from ArCADIE of FORDESA formations that are available to be mapped to a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/BaselineEquipment', tags=['ConceptApi'])
async def get_api_Concept_BaselineEquipment(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of baseline equipment for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/BaselineEquipment/{id}', tags=['ConceptApi'])
async def post_api_Concept_BaselineEquipment(id: str, body: List[ConceptEquipmentMappingDto]) -> dict:
    """
    Create or update concept baseline equipment
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/BaselineEquipment/{id}', tags=['ConceptApi'])
async def delete_api_Concept_BaselineEquipment(id: str, equipmentmappingids: Optional[List[dict]] = None) -> dict:
    """
    Remove baseline equipment that was mapped to a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/Clas', tags=['ConceptApi'])
async def get_api_Concept_Clas(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Return list of CLAs for a specific concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/Clas/{id}', tags=['ConceptApi'])
async def post_api_Concept_Clas(id: str, body: List[ClaDto]) -> dict:
    """
    Post changed data from related concept CLAs
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Concept/CommandPosts', tags=['ConceptApi'])
async def get_api_Concept_CommandPosts(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of command posts for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/CommandPosts/{id}', tags=['ConceptApi'])
async def post_api_Concept_CommandPosts(id: str, body: List[ConceptCommandPostDto]) -> dict:
    """
    Create or update concept command posts
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/CommandPosts/{id}', tags=['ConceptApi'])
async def delete_api_Concept_CommandPosts(id: str, commandpostids: Optional[List[dict]] = None) -> dict:
    """
    Delete command posts from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/Comments', tags=['ConceptApi'])
async def get_api_Concept_Comments(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of comments for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/Comments/{id}', tags=['ConceptApi'])
async def post_api_Concept_Comments(id: str, body: List[CommentDto]) -> dict:
    """
    Save comments
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/Comments/{id}', tags=['ConceptApi'])
async def delete_api_Concept_Comments(id: str, commentids: Optional[List[dict]] = None) -> dict:
    """
    Delete comments from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/ConceptRequiredCapabilities', tags=['ConceptApi'])
async def get_api_Concept_ConceptRequiredCapabilities(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Endpoint for getting list of Required Capability Mappings
for the Concept.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/ConceptRequiredCapabilities/{id}', tags=['ConceptApi'])
async def post_api_Concept_ConceptRequiredCapabilities(id: str, crcid: Optional[int] = None) -> dict:
    """
    Endpoint for saving new CRC Mappings
for the Concept.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/Concept/ConceptRequiredCapabilities/{id}', tags=['ConceptApi'])
async def delete_api_Concept_ConceptRequiredCapabilities(id: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Endpoint for removing existing Required Capability
Mappings by id.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/ConceptScienceTech', tags=['ConceptApi'])
async def get_api_Concept_ConceptScienceTech(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of science and technology items mapped to this concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/ConceptScienceTech/{id}', tags=['ConceptApi'])
async def post_api_Concept_ConceptScienceTech(id: str, body: List[ConceptScienceTechMappingDto]) -> dict:
    """
    Save science and tech mappings
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/ConceptScienceTech/{id}', tags=['ConceptApi'])
async def delete_api_Concept_ConceptScienceTech(id: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Delete science and tech mappings from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/Concept/CopyLiteratureLibraryDocument', tags=['ConceptApi'])
async def post_api_Concept_CopyLiteratureLibraryDocument() -> dict:
    """
    Copy the Blob Document
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/Create', tags=['ConceptApi'])
async def post_api_Concept_Create(body: ConceptGeneralInformationDto) -> dict:
    """
    Create Concept with General Information
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {"status": "created"}
@app.post('/api/Concept/CreateLiteratureLibraryDirectory', tags=['ConceptApi'])
async def post_api_Concept_CreateLiteratureLibraryDirectory() -> dict:
    """
    Create a new Directory in Blob Storage
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/DeleteClas/{id}', tags=['ConceptApi'])
async def post_api_Concept_DeleteClas(id: str, body: List[dict]) -> dict:
    """
    Delete a list of concept CLAs
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Concept/DeleteLiteratureLibraryDocument', tags=['ConceptApi'])
async def post_api_Concept_DeleteLiteratureLibraryDocument() -> dict:
    """
    Delete the Blob Document
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/DocumentMappings', tags=['ConceptApi'])
async def get_api_Concept_DocumentMappings(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieves literature library document mappings for a concept.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/DocumentMappings/{id}', tags=['ConceptApi'])
async def post_api_Concept_DocumentMappings(id: str, body: List[ConceptLitLibraryDocumentsDto]) -> dict:
    """
    Save document mappings for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/DocumentMappings/{id}', tags=['ConceptApi'])
async def delete_api_Concept_DocumentMappings(id: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Delete a mapped document from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/DocumentSearch', tags=['ConceptApi'])
async def get_api_Concept_DocumentSearch(searchterm: Optional[str] = None, indexname: Optional[str] = None, sortorder: Optional[DocumentSearchSortOrder] = None, filters_conceptname: Optional[str] = None, filters_concepttypeguid: Optional[str] = None, filters_statusid: Optional[str] = None, filters_aocyear: Optional[int] = None, filters_documentversion: Optional[str] = None, filters_documenttypeid: Optional[int] = None, filters_documentstatus: Optional[str] = None, filters_documentname: Optional[str] = None) -> dict:
    """
    Search the blob storage files for the search term
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/Enablers', tags=['ConceptApi'])
async def get_api_Concept_Enablers(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of concept enablers
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/Enablers/{id}', tags=['ConceptApi'])
async def post_api_Concept_Enablers(id: str, body: List[ConceptEnablerDto]) -> dict:
    """
    Save enablers
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/Enablers/{id}', tags=['ConceptApi'])
async def delete_api_Concept_Enablers(id: str, enablerids: Optional[List[dict]] = None) -> dict:
    """
    Delete enablers from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/EquipmentCapabilityChanges', tags=['ConceptApi'])
async def get_api_Concept_EquipmentCapabilityChanges(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of equipment capability changes for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/EquipmentCapabilityChanges/{id}', tags=['ConceptApi'])
async def post_api_Concept_EquipmentCapabilityChanges(id: str, body: List[ConceptEquipCapabilityChangesDto]) -> dict:
    """
    Create or update concept equipment capability change
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/EquipmentCapabilityChanges/{id}', tags=['ConceptApi'])
async def delete_api_Concept_EquipmentCapabilityChanges(id: str, capabilitychangeids: Optional[List[dict]] = None) -> dict:
    """
    Delete equipment capability changes from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/FileExists/{id}', tags=['ConceptApi'])
async def get_api_Concept_FileExists(id: str, relativepath: Optional[str] = None) -> dict:
    """
    Checks if a file exists
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/Files', tags=['ConceptApi'])
async def get_api_Concept_Files(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieves a list of files and documents for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/Files/{id}', tags=['ConceptApi'])
async def post_api_Concept_Files(id: str) -> dict:
    """
    Create a concept file.  File metadata should be in the format of Forge.Core.DTO.FileMetadataDto`1
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/Concept/Files/{id}', tags=['ConceptApi'])
async def delete_api_Concept_Files(id: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Delete concept files
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/Concept/FordesaFormations/{id}', tags=['ConceptApi'])
async def post_api_Concept_FordesaFormations(id: str, fordesaprojectid: Optional[int] = None) -> dict:
    """
    Endpoint for saving new formation for the Concept.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/Concept/FordesaFormations/{id}', tags=['ConceptApi'])
async def delete_api_Concept_FordesaFormations(id: str, projids: Optional[List[dict]] = None) -> dict:
    """
    Endpoint for removing existing ForDesA formation projects mapped to a concept.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/Formations', tags=['ConceptApi'])
async def get_api_Concept_Formations(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets details from ArCADIE of FORDESA formations mapped to a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/GeneralInformation/{id}', tags=['ConceptApi'])
async def post_api_Concept_GeneralInformation(id: str, body: ConceptGeneralInformationDto) -> dict:
    """
    Endpoint for saving the data for the Concept.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Concept/GeneralInformationLogo/{id}', tags=['ConceptApi'])
async def post_api_Concept_GeneralInformationLogo(id: str) -> dict:
    """
    Endpoint for saving the logo for the Concept.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/Concept/GeneralInformationLogo/{id}', tags=['ConceptApi'])
async def delete_api_Concept_GeneralInformationLogo(id: str, delete: Optional[bool] = None) -> dict:
    """
    Endpoint for deleting the logo for the Concept.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/GetLiteratureLibraryItems', tags=['ConceptApi'])
async def get_api_Concept_GetLiteratureLibraryItems(folderpath: Optional[str] = None) -> dict:
    """
    Retrieves items for the concepts literature library
for the specified folder path
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/Interdependencies', tags=['ConceptApi'])
async def get_api_Concept_Interdependencies(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Return a list of interdependencies for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/Interdependencies/{id}', tags=['ConceptApi'])
async def post_api_Concept_Interdependencies(id: str, body: List[InterdependenciesDto]) -> dict:
    """
    Save interdependencies
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/Interdependencies/{id}', tags=['ConceptApi'])
async def delete_api_Concept_Interdependencies(id: str, interdependencyids: Optional[List[dict]] = None) -> dict:
    """
    Delete interdependencies from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/LearningEventMappings', tags=['ConceptApi'])
async def get_api_Concept_LearningEventMappings(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of learning events (activities) mapped to a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/LearningEventMappings/{id}', tags=['ConceptApi'])
async def post_api_Concept_LearningEventMappings(id: str, body: List[ConceptLearningEventMappingDto]) -> dict:
    """
    Save learning events
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/LearningEventMappings/{id}', tags=['ConceptApi'])
async def delete_api_Concept_LearningEventMappings(id: str, learningeventids: Optional[List[dict]] = None) -> dict:
    """
    Delete learning events from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/List', tags=['ConceptApi'])
async def get_api_Concept_List(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List Concepts
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/MeasureCategories', tags=['ConceptApi'])
async def get_api_Concept_MeasureCategories(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieves a list of measure categories
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/Concept/MeasureCategories', tags=['ConceptApi'])
async def post_api_Concept_MeasureCategories(body: MeasureCategoryDto) -> dict:
    """
    Save measure categories
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/MeasureCategories', tags=['ConceptApi'])
async def delete_api_Concept_MeasureCategories(measurecategoryids: Optional[List[dict]] = None) -> dict:
    """
    Delete measure categories
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/Measures', tags=['ConceptApi'])
async def get_api_Concept_Measures(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieves a list of measures
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/Concept/Measures', tags=['ConceptApi'])
async def post_api_Concept_Measures(body: MeasureDto) -> dict:
    """
    Save measures
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/Measures', tags=['ConceptApi'])
async def delete_api_Concept_Measures(measureids: Optional[List[dict]] = None) -> dict:
    """
    Delete measures
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/MeasuresByCategory', tags=['ConceptApi'])
async def get_api_Concept_MeasuresByCategory(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieves a list of measures by category
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/MigrateConceptFiles', tags=['ConceptApi'])
async def get_api_Concept_MigrateConceptFiles() -> dict:
    """
    Moves all concept files into a 
concepts/uploads/[concept_id]/ directory structure
to allow loading from the updated concept literature library
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/MigrateLiteratureLibrary', tags=['ConceptApi'])
async def get_api_Concept_MigrateLiteratureLibrary() -> dict:
    """
    Moves existing directories and creates new directories in blob storage
to produce the concept literature library structure requested by users
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/ModernizationImpact', tags=['ConceptApi'])
async def get_api_Concept_ModernizationImpact(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get modernization impact records for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/ModernizationImpact/{id}', tags=['ConceptApi'])
async def post_api_Concept_ModernizationImpact(id: str, body: List[ModernizationImpactDto]) -> dict:
    """
    Save a modernization impact record for the concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/ModernizationImpact/{id}', tags=['ConceptApi'])
async def delete_api_Concept_ModernizationImpact(id: str, modernizationimpactids: Optional[List[dict]] = None) -> dict:
    """
    Delete modernization impact records from the concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/Concept/MoveLiteratureLibraryDocument', tags=['ConceptApi'])
async def post_api_Concept_MoveLiteratureLibraryDocument() -> dict:
    """
    Move the Blob Document
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/PerformanceMeasures', tags=['ConceptApi'])
async def get_api_Concept_PerformanceMeasures(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieves a list of performance measures for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/PerformanceMeasures/{id}', tags=['ConceptApi'])
async def post_api_Concept_PerformanceMeasures(id: str, body: List[ConceptMeasurementDto]) -> dict:
    """
    Save a performance measurement for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/PerformanceMeasures/{id}', tags=['ConceptApi'])
async def delete_api_Concept_PerformanceMeasures(id: str, performancemeasureids: Optional[List[dict]] = None) -> dict:
    """
    Delete performance measurements from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/RecentlyAddedDocuments', tags=['ConceptApi'])
async def get_api_Concept_RecentlyAddedDocuments(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Generates table summarizing recently-added concept documents.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/RecentlyUpdatedConcepts', tags=['ConceptApi'])
async def get_api_Concept_RecentlyUpdatedConcepts(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Generates table summarizing recently-updated concept.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/SaveLiteratureLibraryDocument', tags=['ConceptApi'])
async def post_api_Concept_SaveLiteratureLibraryDocument() -> dict:
    """
    Save File for Literature Library.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/ScenarioMappings', tags=['ConceptApi'])
async def get_api_Concept_ScenarioMappings(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of scenarios mapped to a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/ScenarioMappings/{id}', tags=['ConceptApi'])
async def post_api_Concept_ScenarioMappings(id: str, body: List[ConceptScenarioMappingDto]) -> dict:
    """
    Save scenarios
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/ScenarioMappings/{id}', tags=['ConceptApi'])
async def delete_api_Concept_ScenarioMappings(id: str, scenarioids: Optional[List[dict]] = None) -> dict:
    """
    Delete scenarios from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/Concept/ScienceTechnology', tags=['ConceptApi'])
async def post_api_Concept_ScienceTechnology(body: ScienceTechnologyDto, conceptid: Optional[int] = None) -> dict:
    """
    Method to Save new Science and Technology
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Concept/ScienceTechnologyFile', tags=['ConceptApi'])
async def post_api_Concept_ScienceTechnologyFile(sntid: Optional[int] = None) -> dict:
    """
    Method to Save new Science and Technology file
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Concept/SupplyConsiderations', tags=['ConceptApi'])
async def get_api_Concept_SupplyConsiderations(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieves a list of supply considerations for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/SupplyConsiderations/{id}', tags=['ConceptApi'])
async def post_api_Concept_SupplyConsiderations(id: str, body: List[ConceptMeasurementDto]) -> dict:
    """
    Save a supply consideration for a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/SupplyConsiderations/{id}', tags=['ConceptApi'])
async def delete_api_Concept_SupplyConsiderations(id: str, supplyconsiderationids: Optional[List[dict]] = None) -> dict:
    """
    Delete supply considerations from a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/TaskMappings', tags=['ConceptApi'])
async def get_api_Concept_TaskMappings(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of tasks mapped to this concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/TaskMappings/{id}', tags=['ConceptApi'])
async def post_api_Concept_TaskMappings(id: str, body: List[ConceptTaskMappingDto]) -> dict:
    """
    Save task mappings
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Concept/TaskMappings/{id}', tags=['ConceptApi'])
async def delete_api_Concept_TaskMappings(id: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Delete tasks mapped to a concept
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Concept/UnmappedRequiredCapabilities', tags=['ConceptApi'])
async def get_api_Concept_UnmappedRequiredCapabilities(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Endpoint for getting list of Required Capabilities.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Concept/UserDefinedTask/{id}', tags=['ConceptApi'])
async def post_api_Concept_UserDefinedTask(id: str, body: TaskMappingCreateUserDefinedDto) -> dict:
    """
    Creates a new User Defined Task.
    
    Tags: ConceptApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/crc/Dependencies', tags=['CrcApi'])
async def get_api_crc_Dependencies(id: Optional[int] = None) -> dict:
    """
    Get the mapped solution sets and their CRC mappings for a given CRC
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/crc/Dependencies', tags=['CrcApi'])
async def post_api_crc_Dependencies(body: RequiredCapabilitiesDto) -> dict:
    """
    Update the mapped solution sets with other dependencies
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/crc/LinkableSolutionSets', tags=['CrcApi'])
async def get_api_crc_LinkableSolutionSets(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieves a list of available solution sets that can be linked to a CRC
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/crc/RequiredCapabilities', tags=['CrcApi'])
async def get_api_crc_RequiredCapabilities(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get a list of Required Capabilities.
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/crc/RequiredCapabilities', tags=['CrcApi'])
async def post_api_crc_RequiredCapabilities(body: RequiredCapabilitiesDto) -> dict:
    """
    Create or update a Required Capability
Any concept contributor can create a draft CRC.  Only module managers can approve a draft.
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/crc/RequiredCapabilities', tags=['CrcApi'])
async def delete_api_crc_RequiredCapabilities(crcid: Optional[int] = None) -> dict:
    """
    Delete a Concept Required Capability and
all associated mappings.
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/crc/RequiredCapabilityFiles', tags=['CrcApi'])
async def post_api_crc_RequiredCapabilityFiles(crcid: Optional[int] = None) -> dict:
    """
    Saves the file for the Required Capability.
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/crc/RequiredCapabilityFiles', tags=['CrcApi'])
async def delete_api_crc_RequiredCapabilityFiles(crcid: Optional[int] = None, removefile: Optional[bool] = None) -> dict:
    """
    Deletes the file from the Required Capability.
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/crc/SolutionSetExport/{id}', tags=['CrcApi'])
async def get_api_crc_SolutionSetExport(id: str) -> dict:
    """
    Retrieve data needed to export Solution Sets and Solution Ideas for a Concept Required Capability
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/crc/SolutionSets', tags=['CrcApi'])
async def get_api_crc_SolutionSets(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get the linked Solution Set mappings for a CRC
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/crc/SolutionSets', tags=['CrcApi'])
async def post_api_crc_SolutionSets(crcid: Optional[int] = None, ssid: Optional[str] = None) -> dict:
    """
    Saves CRC Solution Set mapping
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/crc/SolutionSets', tags=['CrcApi'])
async def delete_api_crc_SolutionSets(mappingid: Optional[str] = None) -> dict:
    """
    Delete CRC Solution Set mapping
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/crc/SolutionSetSolutionIdeas', tags=['CrcApi'])
async def get_api_crc_SolutionSetSolutionIdeas(id: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get the solution ideas for a CRCs Solution Sets
    
    Tags: CrcApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/general/librarypermissionrequest', tags=['GeneralApi'])
async def post_api_general_librarypermissionrequest(body: RoleDto) -> dict:
    """
    Request rename, copy, move, delete or upload permission for a literature library
    
    Tags: GeneralApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/general/referencetables/{referenceTable}', tags=['GeneralApi'])
async def get_api_general_referencetables(referenceTable: str) -> DynamicTableDto:
    """
    Get properties and data for the requested reference table
    
    Tags: GeneralApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/general/unreadusernotificationscount', tags=['GeneralApi'])
async def get_api_general_unreadusernotificationscount() -> dict:
    """
    Returns a list of unread user notifications
    
    Tags: GeneralApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/general/userinformation', tags=['GeneralApi'])
async def get_api_general_userinformation() -> dict:
    """
    Returns the current user's information
    
    Tags: GeneralApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/general/usernotifications', tags=['GeneralApi'])
async def get_api_general_usernotifications(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of user notifications
    
    Tags: GeneralApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/general/usernotifications', tags=['GeneralApi'])
async def post_api_general_usernotifications() -> dict:
    """
    Marks all notifications as read for the current user
    
    Tags: GeneralApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/general/userorganization', tags=['GeneralApi'])
async def post_api_general_userorganization(body: MyProfileDto) -> str:
    """
    Saves organization Id for current user
    
    Tags: GeneralApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/general/userprofile', tags=['GeneralApi'])
async def post_api_general_userprofile(body: MyProfileDto) -> str:
    """
    Saves changes made on the myprofile page
    
    Tags: GeneralApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/general/userrolerequest', tags=['GeneralApi'])
async def post_api_general_userrolerequest(body: RoleDto) -> dict:
    """
    Request a role
    
    Tags: GeneralApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/Activities', tags=['LearningApi'])
async def get_api_Learning_Activities(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of Activities
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.delete('/api/Learning/Activities/activity/{id}', tags=['ActivityApi'])
async def delete_api_Learning_Activities_activity(id: str) -> str:
    """
    Deletes an activity
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/Learning/Activities/ActivityApprovalStatus/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_ActivityApprovalStatus(id: str, body: ActivityApprovalStatusDto) -> int:
    """
    Endpoint for saving Activity approval status
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/Activities/ActivityExistingLdEeas', tags=['ActivityApi'])
async def get_api_Learning_Activities_ActivityExistingLdEeas(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get the existing EEAs for an Activitys Learning Demands
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/Activities/ActivityLdEeaMapping/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_ActivityLdEeaMapping(id: str, learningdemandid: Optional[int] = None, eeaid: Optional[int] = None) -> dict:
    """
    Saves existing EEA to a Learning Demand mapping
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/Activities/ActivityLdEeaMappings', tags=['ActivityApi'])
async def get_api_Learning_Activities_ActivityLdEeaMappings(actid: Optional[int] = None, ldid: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get the linked Learning Demand and EEA mappings for an activity
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/Activities/ActivityLdMapping/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_ActivityLdMapping(id: str, learningdemandid: Optional[int] = None) -> dict:
    """
    Saves new mapped learning demand for an activity
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/Activities/ActivityLdMappings', tags=['ActivityApi'])
async def get_api_Learning_Activities_ActivityLdMappings(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get the linked Learning Demands for an Activity
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/Activities/ActivityLdNewEeaMapping/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_ActivityLdNewEeaMapping(id: str, body: LearningDemandEeaMappingDto) -> dict:
    """
    Saves newly created EEA to a Learning Demand mapping
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/Activities/DocumentSearch', tags=['ActivityApi'])
async def get_api_Learning_Activities_DocumentSearch(searchterm: Optional[str] = None, indexname: Optional[str] = None, sortorder: Optional[DocumentSearchSortOrder] = None, filters_activityname: Optional[str] = None, filters_eventtypeid: Optional[str] = None, filters_documentname: Optional[str] = None) -> dict:
    """
    Search the blob storage files for the search term
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/Activities/EeaEditSave/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_EeaEditSave(id: str, body: EeaDto) -> dict:
    """
    Saves updated EEA text
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/Activities/Equipment', tags=['ActivityApi'])
async def get_api_Learning_Activities_Equipment(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve data for Resource Equipment datagrid.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.delete('/api/Learning/Activities/Equipment/{id}', tags=['ActivityApi'])
async def delete_api_Learning_Activities_Equipment(id: str, equipmentid: Optional[str] = None) -> dict:
    """
    Deletes a row from Resource Equipment datagrid.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}

@app.post('/api/Learning/Activities/Equipment/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_Equipment(id: str, body: ResourcesNewViewDto) -> dict:
    """
    Calls a Services method to process the request.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Learning/Activities/EquipmentResourcesRequired/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_EquipmentResourcesRequired(id: str, value: Optional[bool] = None) -> dict:
    """
    Endpoint for saving equipment resources required.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/Activities/FileExists/{id}', tags=['ActivityApi'])
async def get_api_Learning_Activities_FileExists(id: str, relativepath: Optional[str] = None) -> dict:
    """
    Checks if a Learning Activity file exists
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/Activities/Files', tags=['ActivityApi'])
async def get_api_Learning_Activities_Files(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets the documents and their workflow state for an activity
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/Activities/Files/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_Files(id: str) -> dict:
    """
    Create a document for this activity.  File metadata should be in the format of Forge.Core.DTO.FileMetadataDto`1
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/Learning/Activities/Files/{id}', tags=['ActivityApi'])
async def delete_api_Learning_Activities_Files(id: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Delete activity files
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}

@app.put('/api/Learning/Activities/Files/{id}', tags=['ActivityApi'])
async def put_api_Learning_Activities_Files(id: str, body: List[Int32FileMetadataDto]) -> dict:
    """
    Bulk changes to existing documents
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Learning/Activities/GeneralInformation/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_GeneralInformation(id: str, body: LearningActivityGeneralInformationDto) -> int:
    """
    Create new learning activity or update general information
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Learning/Activities/InitialInsight/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_InitialInsight(id: str, body: ActivityInitialInsightsDto) -> int:
    """
    Endpoint for saving the initial insight for an activity.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.delete('/api/Learning/Activities/LdEeaMapping/{id}', tags=['ActivityApi'])
async def delete_api_Learning_Activities_LdEeaMapping(id: str, ldid: Optional[int] = None) -> dict:
    """
    Delete EEA learning demand mapping for an activity
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.delete('/api/Learning/Activities/LdMapping/{id}', tags=['ActivityApi'])
async def delete_api_Learning_Activities_LdMapping(id: str, ldid: Optional[int] = None) -> dict:
    """
    Delete a learning demand mapping and all associated EEA mappings for an Activity
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.delete('/api/Learning/Activities/LearningDemandLinkages/{id}', tags=['ActivityApi'])
async def delete_api_Learning_Activities_LearningDemandLinkages(id: str) -> dict:
    """
    Deletes all records linking the activity with learning demands
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/Learning/Activities/LearningDemandResponseMapping/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_LearningDemandResponseMapping(id: str, body: LdResponseMappingDto) -> dict:
    """
    Update results and responses mapping.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/Activities/LearningDemandResponseMappings', tags=['ActivityApi'])
async def get_api_Learning_Activities_LearningDemandResponseMappings(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get list of results and responses mappings.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/Activities/LearningDemandResponsesReview/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_LearningDemandResponsesReview(id: str, body: LdResponsesReviewDto) -> dict:
    """
    Save responses review data for the Activity's Learning Demands.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Learning/Activities/Notes/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_Notes(id: str, body: ActivityNotesDto) -> int:
    """
    Endpoint for saving the initial insight for an activity.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/Activities/Personnel', tags=['ActivityApi'])
async def get_api_Learning_Activities_Personnel(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve data for Resource Personnel datagrid.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.delete('/api/Learning/Activities/Personnel/{id}', tags=['ActivityApi'])
async def delete_api_Learning_Activities_Personnel(id: str, personnelid: Optional[str] = None) -> dict:
    """
    Deletes a row from Resource Personnel datagrid.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}

@app.post('/api/Learning/Activities/Personnel/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_Personnel(id: str, body: ResourcesNewViewDto) -> dict:
    """
    Determines type of the change action (Remove, Update or Insert) then calls method to process the request.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Learning/Activities/PersonnelResourcesRequired/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_PersonnelResourcesRequired(id: str, value: Optional[bool] = None) -> dict:
    """
    Endpoint for saving personnel resources required.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/Activities/PlanningTimelineMilestones', tags=['ActivityApi'])
async def get_api_Learning_Activities_PlanningTimelineMilestones(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get planning timeline milestones
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/Activities/PlanningTimelineMilestones/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_PlanningTimelineMilestones(id: str, body: ActivityPlanningTimelineDto) -> dict:
    """
    Save changes to planning timeline milestones
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Learning/Activities/PlanningTimelineMilestones/{id}', tags=['ActivityApi'])
async def delete_api_Learning_Activities_PlanningTimelineMilestones(id: str, milestoneid: Optional[int] = None) -> dict:
    """
    Delete a milestone
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.put('/api/Learning/Activities/QcData/{id}', tags=['ActivityApi'])
async def put_api_Learning_Activities_QcData(id: str, body: LearningActivityDocumentFileDto) -> dict:
    """
    Update/Save QC approval data for activity documents.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/Activities/RecentlyUpdatedActivities', tags=['ActivityApi'])
async def get_api_Learning_Activities_RecentlyUpdatedActivities(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Recently Updated Activities
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/Activities/RecentlyUploadedActivityDocs', tags=['ActivityApi'])
async def get_api_Learning_Activities_RecentlyUploadedActivityDocs(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Recently Uploaded Activity Documents
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/Activities/RecommendationMappings', tags=['ActivityApi'])
async def get_api_Learning_Activities_RecommendationMappings(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get list of recommendations for an activity.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/Activities/Recommendations/{id}', tags=['ActivityApi'])
async def post_api_Learning_Activities_Recommendations(id: str, body: ActivityRecommendationsDto) -> int:
    """
    Endpoint for saving the recommendation for an activity.
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/Activities/UpcomingActivities', tags=['ActivityApi'])
async def get_api_Learning_Activities_UpcomingActivities(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Upcoming Activities
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/Activities/Venues', tags=['ActivityApi'])
async def get_api_Learning_Activities_Venues(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Get venues for Activities
    
    Tags: ActivityApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/ActivitiesExport', tags=['LearningApi'])
async def get_api_Learning_ActivitiesExport() -> dict:
    """
    Retrieve all Activity Export Data
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/ActivityDocumentsExport', tags=['LearningApi'])
async def get_api_Learning_ActivityDocumentsExport() -> dict:
    """
    Export all Learning Activity Documents as a Zip File
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/CopyLiteratureLibraryDocument', tags=['LearningApi'])
async def post_api_Learning_CopyLiteratureLibraryDocument() -> dict:
    """
    Copy the Blob Document
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/CrcActivities', tags=['LearningApi'])
async def get_api_Learning_CrcActivities(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of Activities linked to a CRC
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/CreateLiteratureLibraryDirectory', tags=['LearningApi'])
async def post_api_Learning_CreateLiteratureLibraryDirectory() -> dict:
    """
    Create a new Directory in Blob Storage
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/DeleteLiteratureLibraryDocument', tags=['LearningApi'])
async def post_api_Learning_DeleteLiteratureLibraryDocument() -> dict:
    """
    Delete the Blob Document
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/LearningDemands', tags=['LearningApi'])
async def get_api_Learning_LearningDemands(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of learning demands
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/LearningDemands/CrcLinkages', tags=['LearningDemandApi'])
async def get_api_Learning_LearningDemands_CrcLinkages(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List CRC linkages for a learning demand
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/LearningDemands/CrcLinkages/{id}', tags=['LearningDemandApi'])
async def post_api_Learning_LearningDemands_CrcLinkages(id: str, body: List[dict]) -> dict:
    """
    Link CRCs to a learning demand
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Learning/LearningDemands/CrcLinkages/{id}', tags=['LearningDemandApi'])
async def delete_api_Learning_LearningDemands_CrcLinkages(id: str, crcids: Optional[List[dict]] = None) -> dict:
    """
    Unlink CRCs from a learning demand
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Learning/LearningDemands/EventLinkages', tags=['LearningDemandApi'])
async def get_api_Learning_LearningDemands_EventLinkages(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List event linkages for a learning demand
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/LearningDemands/EventLinkages/{id}', tags=['LearningDemandApi'])
async def post_api_Learning_LearningDemands_EventLinkages(id: str, body: List[LearningEventDto]) -> dict:
    """
    Link events to a learning demand
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Learning/LearningDemands/EventLinkages/{id}', tags=['LearningDemandApi'])
async def delete_api_Learning_LearningDemands_EventLinkages(id: str, learningeventids: Optional[List[dict]] = None) -> dict:
    """
    Unlink events from a learning demand
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/Learning/LearningDemands/GeneralInformation/{id}', tags=['LearningDemandApi'])
async def post_api_Learning_LearningDemands_GeneralInformation(id: str, body: LearningDemandGenInfoDto) -> int:
    """
    Save general information for an existing learning demand
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Learning/LearningDemands/LearningDemandClosure/{id}', tags=['LearningDemandApi'])
async def post_api_Learning_LearningDemands_LearningDemandClosure(id: str, body: LearningDemandDto) -> dict:
    """
    Saves the Learning Demand's Closure data.
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/LearningDemands/LearningDemandResponses', tags=['LearningDemandApi'])
async def get_api_Learning_LearningDemands_LearningDemandResponses(ldid: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of mapped Responses for the learning demand.
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/LearningDemands/LearningDemands', tags=['LearningDemandApi'])
async def post_api_Learning_LearningDemands_LearningDemands(body: LearningDemandDto) -> dict:
    """
    Creates a new learning demand
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/LearningDemands/LearningDemands/{id}', tags=['LearningDemandApi'])
async def get_api_Learning_LearningDemands_LearningDemands(id: str) -> LearningDemandDto:
    """
    Retrieves a learning demand using its ID
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/Learning/LearningDemands/LearningDemands/{id}', tags=['LearningDemandApi'])
async def delete_api_Learning_LearningDemands_LearningDemands(id: str) -> str:
    """
    Deletes a learning demand
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Learning/LearningDemands/LinkableCrcs', tags=['LearningDemandApi'])
async def get_api_Learning_LearningDemands_LinkableCrcs(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List the CRCs that aren't already linked
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/LearningDemands/LinkableEvents', tags=['LearningDemandApi'])
async def get_api_Learning_LearningDemands_LinkableEvents(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List the events that aren't already linked or marked as deleted
    
    Tags: LearningDemandApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/LearningDemandsExport', tags=['LearningApi'])
async def get_api_Learning_LearningDemandsExport() -> dict:
    """
    Retrieve all learning demands for export
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/MoveLiteratureLibraryDocument', tags=['LearningApi'])
async def post_api_Learning_MoveLiteratureLibraryDocument() -> dict:
    """
    Move the Blob Document
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/SaveLiteratureLibraryDocument', tags=['LearningApi'])
async def post_api_Learning_SaveLiteratureLibraryDocument() -> dict:
    """
    Save File for Literature Library.
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/TDD', tags=['LearningApi'])
async def get_api_Learning_TDD(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of TDDs
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/Learning/TDD', tags=['TddApi'])
async def post_api_Learning_TDD(body: TddCreateDto) -> dict:
    """
    CreateTdd
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return body
@app.delete('/api/Learning/TDD/{tddId}', tags=['TddApi'])
async def delete_api_Learning_TDD(tddId: str) -> dict:
    """
    Endpoint that serves as the delete action for TDD catalog.
Only module managers should be able to delete TDDs.
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/Learning/TDD/AdministrativeData', tags=['TddApi'])
async def post_api_Learning_TDD_AdministrativeData(body: TddAdministrativeFormDto) -> dict:
    """
    Save administrative data for the TDD
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Learning/TDD/ClosureData/{id}', tags=['TddApi'])
async def post_api_Learning_TDD_ClosureData(id: str, body: TddClosureDto) -> dict:
    """
    Saves the Learning Demand's Closure data.
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/Learning/TDD/ClosureLearningDemands', tags=['TddApi'])
async def get_api_Learning_TDD_ClosureLearningDemands(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of mapped Learning Demands
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/TDD/LearningDemandResponses', tags=['TddApi'])
async def get_api_Learning_TDD_LearningDemandResponses(ldid: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of mapped Responses
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/TDD/LearningDemands', tags=['TddApi'])
async def get_api_Learning_TDD_LearningDemands(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List mapped learning demands for a TDD
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/TDD/LearningDemands/{id}', tags=['TddApi'])
async def post_api_Learning_TDD_LearningDemands(id: str, body: TddLearningDemandMappingDto) -> dict:
    """
    Saves updates to TDD learning demand mappings
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/Learning/TDD/LearningDemands/{id}', tags=['TddApi'])
async def delete_api_Learning_TDD_LearningDemands(id: str, mappingid: Optional[int] = None) -> str:
    """
    Delete a TDD learning demand mapping
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Learning/TDD/LearningDemandsExport/{id}', tags=['TddApi'])
async def get_api_Learning_TDD_LearningDemandsExport(id: str) -> dict:
    """
    List mapped learning demands for a TDD formatted for exporting
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/Learning/TDD/ProblemDisposition', tags=['TddApi'])
async def post_api_Learning_TDD_ProblemDisposition(body: TddProblemDispositionFormDto) -> dict:
    """
    Saves all data on the TDD problem displsition tab
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Learning/TDD/ProblemSummary/{id}', tags=['TddApi'])
async def post_api_Learning_TDD_ProblemSummary(id: str, body: TddDto) -> dict:
    """
    Saves problem summary page
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/Learning/TDD/ProblemSummaryFiles/{id}', tags=['TddApi'])
async def post_api_Learning_TDD_ProblemSummaryFiles(id: str) -> dict:
    """
    Saves problem summary page
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/Learning/TDD/ProblemSummaryFiles/{id}', tags=['TddApi'])
async def delete_api_Learning_TDD_ProblemSummaryFiles(id: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Delete TDD problem summery source files
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/Learning/TDD/RecentlyClosedLearningDemands', tags=['TddApi'])
async def get_api_Learning_TDD_RecentlyClosedLearningDemands(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List recently closed learning demands
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/TDD/SourcesFiles', tags=['TddApi'])
async def get_api_Learning_TDD_SourcesFiles(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Gets a list of TDD problem summary source files
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/TDD/TddMappableLearningDemands', tags=['TddApi'])
async def get_api_Learning_TDD_TddMappableLearningDemands(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieves a list of learning demands that are not closed
    
    Tags: TddApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/TddByActivity', tags=['LearningApi'])
async def get_api_Learning_TddByActivity(id: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of TDDs
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/Learning/TddExport', tags=['LearningApi'])
async def get_api_Learning_TddExport() -> dict:
    """
    Retrieve all Tdd Export Data
    
    Tags: LearningApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/litlib/CopyDocument', tags=['LiteratureLibraryApi'])
async def post_api_litlib_CopyDocument() -> dict:
    """
    Copy the Blob Document
    
    Tags: LiteratureLibraryApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/litlib/CreateDirectory', tags=['LiteratureLibraryApi'])
async def post_api_litlib_CreateDirectory() -> dict:
    """
    Create a new Directory in Blob Storage
    
    Tags: LiteratureLibraryApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/litlib/DeleteDocument', tags=['LiteratureLibraryApi'])
async def post_api_litlib_DeleteDocument() -> dict:
    """
    Delete the Blob Document
    
    Tags: LiteratureLibraryApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/litlib/DownloadFile', tags=['LiteratureLibraryApi'])
async def get_api_litlib_DownloadFile() -> dict:
    """
    Download selected file(s), using a zip for multiple at once
    
    Tags: LiteratureLibraryApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/litlib/File', tags=['LiteratureLibraryApi'])
async def get_api_litlib_File(filepath: Optional[str] = None) -> dict:
    """
    Downloads a File using a path
    
    Tags: LiteratureLibraryApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/litlib/FileExists', tags=['LiteratureLibraryApi'])
async def get_api_litlib_FileExists(path: Optional[str] = None) -> dict:
    """
    Checks if a file exists at the specified path.
    
    Tags: LiteratureLibraryApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/litlib/GetBlobFileList', tags=['LiteratureLibraryApi'])
async def get_api_litlib_GetBlobFileList(folderpath: Optional[str] = None) -> dict:
    """
    Retrieve a List of all Blob Files
    
    Tags: LiteratureLibraryApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/litlib/MoveDocument', tags=['LiteratureLibraryApi'])
async def post_api_litlib_MoveDocument() -> dict:
    """
    Move the Blob Document
    
    Tags: LiteratureLibraryApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/litlib/SaveDocument', tags=['LiteratureLibraryApi'])
async def post_api_litlib_SaveDocument() -> dict:
    """
    Save File to Blob Storage.
    
    Tags: LiteratureLibraryApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/CommandPosts', tags=['PathfinderApi'])
async def get_api_pathfinder_CommandPosts(fcwconceptid: Optional[int] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Retrieve a list of command posts for a concept
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/DownloadFile/{solutionIdeaId}', tags=['PathfinderApi'])
async def get_api_pathfinder_DownloadFile(solutionIdeaId: str, fileid: Optional[int] = None) -> dict:
    """
    Download file associated with the solution idea.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/LinkableExperiments', tags=['PathfinderApi'])
async def get_api_pathfinder_LinkableExperiments(solutionideaid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of experiments available to map to solution idea.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/LinkableSolutionIdeas', tags=['PathfinderApi'])
async def get_api_pathfinder_LinkableSolutionIdeas(solutionideaid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of solution ideas available to map to solution idea.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/LinkableSolutionSetCrcs', tags=['PathfinderApi'])
async def get_api_pathfinder_LinkableSolutionSetCrcs(solutionsetid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of solution ideas available to map to solution set.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/LinkableSolutionSetSolutionIdeas', tags=['PathfinderApi'])
async def get_api_pathfinder_LinkableSolutionSetSolutionIdeas(solutionsetid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns a list of solution ideas available to map to solution set.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/LinkedSolutionIdeas', tags=['PathfinderApi'])
async def get_api_pathfinder_LinkedSolutionIdeas(solutionideaid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns all solution ideas linked to a parent solution idea.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/pathfinder/LinkedSolutionIdeas', tags=['PathfinderApi'])
async def delete_api_pathfinder_LinkedSolutionIdeas(mappingid: Optional[str] = None) -> dict:
    """
    Removes a linked solution idea that was mapped to a parent solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/pathfinder/LinkedSolutionIdeas/{solutionIdeaId}', tags=['PathfinderApi'])
async def post_api_pathfinder_LinkedSolutionIdeas(solutionIdeaId: str, linkedsolutionideaid: Optional[str] = None) -> dict:
    """
    Links a solution idea to a parent solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.post('/api/pathfinder/MergeSolutionIdeas', tags=['PathfinderApi'])
async def post_api_pathfinder_MergeSolutionIdeas(body: SolutionIdeaDto, currentsolutionideaid: Optional[str] = None, incomingsolutionideaid: Optional[str] = None) -> dict:
    """
    Merges two solution ideas into one
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return body
@app.get('/api/pathfinder/MilestoneCompletion', tags=['PathfinderApi'])
async def get_api_pathfinder_MilestoneCompletion(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns milestones grouped by solution idea for a user's organization.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/SolutionIdeaFileExists/{solutionIdeaId}', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionIdeaFileExists(solutionIdeaId: str, relativepath: Optional[str] = None) -> dict:
    """
    Checks if a Solution Idea file exists
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/SolutionIdeaFiles', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionIdeaFiles(solutionideaid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Endpoint for getting a list of file mappings for a solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/pathfinder/SolutionIdeaFiles', tags=['PathfinderApi'])
async def post_api_pathfinder_SolutionIdeaFiles(solutionideaid: Optional[str] = None) -> dict:
    """
    Saves posted files to storage and associated the files to a solution idea.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.delete('/api/pathfinder/SolutionIdeaFiles/{solutionIdeaId}', tags=['PathfinderApi'])
async def delete_api_pathfinder_SolutionIdeaFiles(solutionIdeaId: str, mappingids: Optional[List[dict]] = None) -> dict:
    """
    Deletes a set of file mappings for the solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/pathfinder/SolutionIdeaLinkedExperiments', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionIdeaLinkedExperiments(solutionideaid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns all experiments linked to a solution idea.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.delete('/api/pathfinder/SolutionIdeaLinkedExperiments/{solutionIdeaId}', tags=['PathfinderApi'])
async def delete_api_pathfinder_SolutionIdeaLinkedExperiments(solutionIdeaId: str, mappingid: Optional[str] = None) -> dict:
    """
    Removes a linked experiment that was mapped to a solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}

@app.post('/api/pathfinder/SolutionIdeaLinkedExperiments/{solutionIdeaId}', tags=['PathfinderApi'])
async def post_api_pathfinder_SolutionIdeaLinkedExperiments(solutionIdeaId: str, expguid: Optional[str] = None) -> dict:
    """
    Links and experiment to a solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.delete('/api/pathfinder/SolutionIdeaMapping/{solutionIdeaId}', tags=['PathfinderApi'])
async def delete_api_pathfinder_SolutionIdeaMapping(solutionIdeaId: str) -> dict:
    """
    Deletes a solution idea mapping
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/pathfinder/SolutionIdeaMilestones', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionIdeaMilestones(solutionideaid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns all experiments linked to a solution idea.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/pathfinder/SolutionIdeaMilestones', tags=['PathfinderApi'])
async def post_api_pathfinder_SolutionIdeaMilestones(body: MilestoneDto) -> dict:
    """
    Creates a new solution idea milestone
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return body

@app.delete('/api/pathfinder/SolutionIdeaMilestones', tags=['PathfinderApi'])
async def delete_api_pathfinder_SolutionIdeaMilestones(milestoneids: Optional[List[dict]] = None) -> dict:
    """
    Deletes milestones from a solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/pathfinder/SolutionIdeaMilestoneState', tags=['PathfinderApi'])
async def post_api_pathfinder_SolutionIdeaMilestoneState(body: List[MilestoneDto]) -> dict:
    """
    Contains a list of milestones and their workflow state changes.
Pages that use this method:
    Milestone Completion: users can update one milestone at a time
    Solution idea data card milestone grid: users can batch update milestone completion states
    Milestone details: user can update one milestone at a time
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return body
@app.post('/api/pathfinder/SolutionIdeaMilestoneTemplates/{solutionIdeaId}', tags=['PathfinderApi'])
async def post_api_pathfinder_SolutionIdeaMilestoneTemplates(solutionIdeaId: str) -> dict:
    """
    Creates milestones based on a template for a solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/SolutionIdeas', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionIdeas(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns all non-deleted Solution Ideas.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.get('/api/pathfinder/SolutionIdea', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionIdea() -> dict:
    """
    Returns all Solution Ideas creation content.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic

    response = '''
<p class="d-flex align-items-center workflow-section-heading workflow-section-heading--lg">
    Add a new solution idea
    <span class="flex-grow-1 flex-grow-1 d-flex align-items-center justify-content-end">
        <a href="#" class="d-flex text-decoration-none text-body" title="Close" onclick="FORGE.Pathfinder.SolutionIdeas.hideSolutionIdeaPopup()">
            <i class="fa-solid fa-xmark"></i>
        </a>
    </span>
</p>


<div id="solution-idea-form">
    <script>
DevExpress.config({"serverDecimalSeparator":"."});
DevExpress.aspnet.setTemplateEngine();
DevExpress.assertDevExtremeVersion('DevExtreme.AspNet.Core', '24.2.7');
DevExpress.config({ "licenseKey": window.atob("ZXdvZ0lDSm1iM0p0WVhRaU9pQXhMQW9nSUNKcGJuUmxjbTVoYkZWellXZGxTV1FpT2lBaVVUTmhiM0ZJYzFKRU0zWllaVlZOVUdSWVNEZHhOU0lLZlE9PS5rMTA4KzRjbVFYSU96S1F1bUlqUE5oQkw0ejc5N0VSNlByVkkxcTB3V1QwbnkwUTVNZnkzRkJONlV5Zk9PV2p1eUJwaDR1ZllMM0llb0g4UHhNUU5wQUhUb3VUTTFFOHZaM01CM0lac2c1L1ZoOXhUNkg4TFJQSGZoQk00Rk5HUE5zNkY0dz09") });
</script>
<div id="solution-idea-general-information-form"></div><script>
DevExpress.utils.readyCallbacks.add((function($){$("#solution-idea-general-information-form").dxForm({"readOnly":false,"colCount":5,"formData":{"SolutionIdeaId":null,"ShortName":null,"Description":null,"DomainId":null,"FcwConceptId":null,"CrcEchelonIds":[],"PossibleIocDate":null,"IsSnt":false,"CriticalPath":false,"GapCategoryIds":[],"OcrProponentIds":[],"OrgGuid":"e1ed176c-2116-424a-a79a-296842c56f5a","WorkflowStepId":61},"labelMode":"static","labelLocation":"left","items":[{"itemType":"group","colSpan":3,"colCount":3,"items":[{"itemType":"simple","dataField":"ShortName","editorOptions":{"maxLength":100,"_ignoreElementAttrDeprecation":true,"elementAttr":{"id":"short-name-textbox"}},"editorType":"dxTextBox","validationRules":[{"type":"required","message":"Please enter a short name."}],"isRequired":true,"colSpan":3,"label":{"text":"Short Name"}},{"itemType":"simple","dataField":"Description","editorOptions":{"height":108,"_ignoreElementAttrDeprecation":true,"elementAttr":{"id":"text-editor"}},"editorType":"dxTextArea","validationRules":[{"type":"required","message":"Please enter a description."}],"isRequired":true,"colSpan":3,"label":{"text":"Description / Summary","location":"top"}},{"itemType":"simple","dataField":"PossibleIocDate","editorOptions":{"_ignoreElementAttrDeprecation":true,"elementAttr":{"id":"possible-ioc-date-editor"}},"editorType":"dxDateBox","validationRules":[{"type":"required","message":"Please enter a possible IOC date."}],"isRequired":true,"colSpan":1,"label":{"text":"Possible IOC Date"}},{"itemType":"simple","template":$("#is-snt-radio-template")},{"itemType":"simple","template":$("#critical-path-radio-template")},{"itemType":"simple","dataField":"GapCategoryIds","visible":true,"colSpan":3,"name":"gap-category-critical-path","label":{"text":"Gap Category Critical Path"},"editorOptions":{"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"Key":"f154c5b7-cf0b-ef11-8075-0003ff1f473c","Value":"Undefined","Code":"00"},{"Key":"64e20793-0aab-4b79-aa0e-f7eb3c1df4e4","Value":"Network","Code":"01"},{"Key":"e5eef621-6cc5-4a03-9529-ced4542e6c64","Value":"CEMA","Code":"02"},{"Key":"13a371fd-2105-4dd3-84d2-837cba99f18a","Value":"Counter-C5ISRT","Code":"03"},{"Key":"7ff249ec-169c-4f64-bd3b-26d7d832fbec","Value":"Space Operations","Code":"04"},{"Key":"417c8ca2-b67c-40d8-9f6f-858e01473cda","Value":"Battlefield Visibility/Situational Understanding","Code":"05"},{"Key":"9bda6ca3-6de4-4634-a6a4-45bdc78aaf10","Value":"C2 Overmatch","Code":"06"},{"Key":"9ade68ff-4ebe-4905-9105-fcebc9c26007","Value":"Inter/Intra-Theater Lift","Code":"07"},{"Key":"6299b2a0-7ac8-4aa5-9bb0-b076a4293d19","Value":"Protect the Force","Code":"10"},{"Key":"626cf0de-2b9b-4fdc-9cc3-bb623857eca8","Value":"Defend Airspace","Code":"11"},{"Key":"adf40c6a-5998-4364-aec2-8c9208014df9","Value":"Maneuver/Lethality ","Code":"13"},{"Key":"d10f0aff-c989-4140-b1a8-4c1861f2e074","Value":"Aerial Operations","Code":"14"},{"Key":"5d391129-deb8-4331-bc83-cd0048645c30","Value":"Army Maritime Operations","Code":"15"},{"Key":"07bdec77-3ab5-4a2b-a6ca-3e501e91335f","Value":"Mass Casualty Evacuation and Treatment","Code":"16"},{"Key":"fc0dd63a-c434-4133-a2fa-4ab3c37dddde","Value":"Dynamic and Deliberate Targeting","Code":"21"}],"key":"Key"})},"valueExpr":"Key","displayExpr":"Value","value":[],"placeholder":"Select Gap Categories","showClearButton":true,"contentTemplate":$("#GapCategoryDataGridMultipleTemplate"),"_ignoreElementAttrDeprecation":true,"elementAttr":{"id":"gap-category-critical-path-dropdownbox"}},"editorType":"dxDropDownBox"}]},{"itemType":"group","name":"domain-group","colSpan":2,"colCount":2,"items":[{"itemType":"simple","dataField":"DomainId","validationRules":[{"type":"required","message":"Please select a DOTmLPF-P domain."}],"colSpan":1,"isRequired":true,"label":{"text":"Idea Type (Domain)"},"editorOptions":{"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"DomainId":"626235e6-d1cc-ee11-b8ae-0003ff0c7f2f","DomainCode":"D","DomainText":"Doctrine","OrdinalityQuantity":10},{"DomainId":"636235e6-d1cc-ee11-b8ae-0003ff0c7f2f","DomainCode":"O","DomainText":"Organization","OrdinalityQuantity":20},{"DomainId":"646235e6-d1cc-ee11-b8ae-0003ff0c7f2f","DomainCode":"T","DomainText":"Training","OrdinalityQuantity":30},{"DomainId":"656235e6-d1cc-ee11-b8ae-0003ff0c7f2f","DomainCode":"M","DomainText":"Materiel","OrdinalityQuantity":40},{"DomainId":"6c6235e6-d1cc-ee11-b8ae-0003ff0c7f2f","DomainCode":"S","DomainText":"Software","OrdinalityQuantity":45},{"DomainId":"666235e6-d1cc-ee11-b8ae-0003ff0c7f2f","DomainCode":"L","DomainText":"Leadership","OrdinalityQuantity":50},{"DomainId":"676235e6-d1cc-ee11-b8ae-0003ff0c7f2f","DomainCode":"P","DomainText":"Personnel","OrdinalityQuantity":60},{"DomainId":"686235e6-d1cc-ee11-b8ae-0003ff0c7f2f","DomainCode":"F","DomainText":"Facilities","OrdinalityQuantity":70},{"DomainId":"696235e6-d1cc-ee11-b8ae-0003ff0c7f2f","DomainCode":"X","DomainText":"Policy","OrdinalityQuantity":80}]})},"displayExpr":"DomainText","valueExpr":"DomainId","value":null,"onSelectionChanged":function (e) {
        FORGE.Pathfinder.SolutionIdeas.onDomainSelected(e, '636235e6-d1cc-ee11-b8ae-0003ff0c7f2f');
        },"_ignoreElementAttrDeprecation":true,"elementAttr":{"id":"domain-selectbox"}},"editorType":"dxSelectBox"},{"itemType":"simple","dataField":"OrgGuid","validationRules":[{"type":"required","message":"Please enter an Organization."}],"colSpan":1,"label":{"text":"OPR"},"isRequired":true,"editorOptions":{"readOnly":false,"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"OrganizationGuid":"9353f360-b56e-4837-a729-6f5b2feca0a3","OrganizationName":"2nd Multidomain Task Force (MDTF)","ShortName":"2 MDTF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"600fd729-86e6-4313-a59f-90d5689589b9"},{"OrganizationGuid":"69949f20-73d6-4dea-ad50-b9a07020c690","OrganizationName":"3rd Multidomain Task Force (MDTF)","ShortName":"3 MDTF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"80c9fb2f-d15a-4be9-9aad-9bf1dc7b038c"},{"OrganizationGuid":"45f2b8c5-ea5b-4128-b1fd-a2dc6e3b84ed","OrganizationName":"75th Innovation CMD","ShortName":"75th IC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"6ec532a5-eb94-4603-abeb-475e7bbcf93b","OrganizationName":"Air and Missile Defense CFT","ShortName":"A\u0026MD CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"33dcd4be-f3f9-41f8-935c-d44d263e59db","OrganizationName":"Applied Concepts Division","ShortName":"ACD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"ede09f65-93a8-4871-96af-dc6dbbb922c2"},{"OrganizationGuid":"e1ed176c-2116-424a-a79a-296842c56f5a","OrganizationName":"Architecture Integration and Management Division","ShortName":"AIMD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"80b6edda-db81-42ac-b871-8ccb4ace08a8"},{"OrganizationGuid":"adc4811e-e4cf-4a79-b254-daaef21fde7f","OrganizationName":"Armaments Center","ShortName":"AC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"b7a0d8b6-4ab3-4ae8-ab6b-491f1ca8fd6b","OrganizationName":"Army Applications Lab","ShortName":"AAL","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"66b5b714-8721-453e-bf60-874a815b5467","OrganizationName":"Army Artificial Intellegence Integration Center","ShortName":"AI2C","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"85c1733f-9df1-4c47-be3a-660894a6da36","OrganizationName":"Army Capability Manager- Cyber","ShortName":"ACM Cyber","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"c38cd089-4402-45f4-8664-efb067509b70","OrganizationName":"Army Capability Manager- Electronic Warfare (EW)","ShortName":"ACM Electronic Warfare (EW)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"7afbb964-16f9-4e0f-8b38-dbc4bc3f70ed","OrganizationName":"Army Capability Manager- Networks and Services (N\u0026S)","ShortName":"ACM Networks and Services (N\u0026S)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"597dfc7a-a287-48f7-a15f-07ae11bdc441","OrganizationName":"Army Capability Manager- Tactical Radio (TR)","ShortName":"ACM Tactical Radio (TR)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5","OrganizationName":"Army Futures Command","ShortName":"AFC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"3fc3ab1d-fad7-444a-994c-6d299b84c388","OrganizationName":"Army Futures Command G-3/5/7","ShortName":"AFC G-3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"94449402-3aa4-403e-bb5f-7fedefac432e","OrganizationName":"Army Research Institute","ShortName":"ARI","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"5b1151ba-bd21-4220-9f71-d792df685f48","OrganizationName":"Army Service Combatant Command  - US Army Central","ShortName":"ASCC - USARCENT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"a32fa529-8bab-4959-aed6-abb9de49cd5f","OrganizationName":"Army Service Combatant Command  - US Army Europe","ShortName":"ASCC - USAREUR","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"e176a0d8-fc3f-4185-82e4-57f2772fb914","OrganizationName":"Army Service Combatant Command  - US Army N America","ShortName":"ASCC - USARNORTH","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"1f98a656-8724-464b-8f26-59259b37f440","OrganizationName":"Army Service Combatant Command  - US Army Pacific","ShortName":"ASCC - USARPAC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"7a5af3a7-53b8-41ae-97ae-f6ba66e995c8","OrganizationName":"Army Service Combatant Command  - US Army S. America","ShortName":"ASCC - USARSO","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"21bce6a8-5eb4-46f9-a0cb-5cf69f415819","OrganizationName":"Army Service Combatant Command  US Army- Africa","ShortName":"ASCC - USARAF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"a963d32e-121b-40e4-9296-a47c344deb60","OrganizationName":"Army Service Combatant Command - US Army Cyber","ShortName":"ASCC - ARCYBER","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"41d1051f-15c6-47ee-820e-dba2fbfb704a","OrganizationName":"Army Test and Evaluation Command","ShortName":"ATEC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"15479e18-be41-4c51-aaa6-f608d82f4aa8","OrganizationName":"Army Training and Doctrine Command","ShortName":"TRADOC","IsOpr":true,"ProponentCode":"TRADOC HQ","GapCode":"99","ParentOrganizationGuid":null},{"OrganizationGuid":"3e6b0e8e-4eaf-4c35-81df-e1168b1e760e","OrganizationName":"Assistant Sec.Army- Acquisitions, Logistics, Technology","ShortName":"ASA(ALT)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"9ac0ee04-30e4-49d8-9c75-c6be301406cd","OrganizationName":"Assistant Sec.Army- Manpower, Reserves ","ShortName":"ASA(MRA)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"d82b5e4a-1777-4c1e-ae5c-b4a12a020cd0","OrganizationName":"Assured Positioning, Navigation, and Timing CFT","ShortName":"A-PNT CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"1a6813dd-2434-42bc-ac8b-103f4c6a0faa","OrganizationName":"Aviation CDID","ShortName":"A-CDID","IsOpr":true,"ProponentCode":"AV","GapCode":"02","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"fc6c71f0-0fc4-4b63-9ec7-cd60046730c0","OrganizationName":"Aviation Center of Excellence","ShortName":"AVCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"0014905e-c18e-4ff3-a185-dc2cc640458a","OrganizationName":"Chaplain CDID","ShortName":"Chaplain CDID","IsOpr":true,"ProponentCode":"CHAP","GapCode":"14","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"ac442dc4-7fd8-4388-b7f7-96684c078d3c","OrganizationName":"Chief of Engineers","ShortName":"Chief of Engineers","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4","OrganizationName":"Combined Arms Center","ShortName":"CAC","IsOpr":true,"ProponentCode":"CAC-T","GapCode":"99","ParentOrganizationGuid":"15479e18-be41-4c51-aaa6-f608d82f4aa8"},{"OrganizationGuid":"eaec5a7a-818e-4901-8094-be3e9947b4e5","OrganizationName":"Command and Control CFT","ShortName":"C2 CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"a524a75b-6164-458b-80ee-b86c28cadd82","OrganizationName":"Contested Logistics CFT ","ShortName":"CLFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687","OrganizationName":"Cyber CDID","ShortName":"C-CDID","IsOpr":true,"ProponentCode":"Cyber","GapCode":"03","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"f0a8068c-f61b-4269-b6bf-bb85d2a2ffba","OrganizationName":"Cyber Center of Excellence","ShortName":"CCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"53742f86-debd-4880-bc54-7348db9e40d6","OrganizationName":"Cyber Command","ShortName":"CYBERCOM","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"f4263fda-a85f-47fe-8c47-7da5a761b8cd","OrganizationName":"Cyber Theater Information Advantage Detachment","ShortName":"Cyber TIAD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"53742f86-debd-4880-bc54-7348db9e40d6"},{"OrganizationGuid":"6d110399-f359-487d-829d-2dd283a90914","OrganizationName":"Deputy Chief of Staff G-3/5/7","ShortName":"DCoS G-3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"9be557f4-4853-48f8-aa6c-0885cde155f4","OrganizationName":"Deputy Chief of Staff- G1","ShortName":"DCoS-G1","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"83d92df4-b9be-4780-b378-67c7ac1a75ae","OrganizationName":"Deputy Chief of Staff- G8","ShortName":"DCoS-G8","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"615d09e2-6091-46d7-8530-38677f3c8eb7","OrganizationName":"Deputy Chief of Staff-G6","ShortName":"DCoS-G6","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"8ccda746-5efb-407c-aef7-f9048d366d1b","OrganizationName":"DEVCOM Analysis Center","ShortName":"DAC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"4f8be144-d40f-4520-905d-fcf5e28a9c13","OrganizationName":"DEVCOM Army Research Labratory","ShortName":"ARL","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"ac4aabc2-ab2b-4778-ab50-de93bb4067e1","OrganizationName":"DEVCOM Aviation \u0026 Missile Center","ShortName":"AvMC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"099bf1c1-0ed4-4842-a6da-064490a717f4","OrganizationName":"DEVCOM Chemical Biological Center","ShortName":"CBC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"301ac328-d33f-434c-ba87-5b6800506ad6","OrganizationName":"DEVCOM Command, Control, Communications, Computers, Cyber, Intelligence, Surveillance and Reconnaissance Center","ShortName":"C5ISRC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"bea30b04-693e-4141-9518-178cf03a636e","OrganizationName":"DEVCOM Ground Vehicle Systems Center","ShortName":"GVSC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a","OrganizationName":"DEVCOM HQ","ShortName":"DEVCOM","IsOpr":true,"ProponentCode":"STRACD","GapCode":"99","ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"08d8a04d-3985-4872-80bf-0ea5dfe9c312","OrganizationName":"DEVCOM Soldier Center","ShortName":"SC","IsOpr":true,"ProponentCode":"PAO","GapCode":"99","ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"ede09f65-93a8-4871-96af-dc6dbbb922c2","OrganizationName":"Directorate Of Concepts","ShortName":"DoC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"80b6edda-db81-42ac-b871-8ccb4ace08a8"},{"OrganizationGuid":"e0ae1f08-98ad-473a-8bed-90ba1bfac4fc","OrganizationName":"Engineer Research and Development Center","ShortName":"ERDC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"7b66058e-3afd-4018-9b66-00af3c90e07a","OrganizationName":"FCC - Other","ShortName":"FCC - Other","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"edb7b359-780e-4683-889d-ac14f7f90c42","OrganizationName":"Fires CDID","ShortName":"F-CDID","IsOpr":true,"ProponentCode":"FIRES","GapCode":"04","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"654c6c12-ac3e-4eb9-970a-4db40a15370e","OrganizationName":"Fires Center of Excellence","ShortName":"FCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"3b99add5-20ba-4ade-8dd6-245c05a2b1c5","OrganizationName":"Future Vertical Lift CFT","ShortName":"FVL CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a","OrganizationName":"Futures and Concepts Center","ShortName":"FCC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"555b21e2-ab9d-446b-bc9c-1f6fc40cbc63","OrganizationName":"Futures and Concepts Center G-3/5/7","ShortName":"FCC G-3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"80b6edda-db81-42ac-b871-8ccb4ace08a8","OrganizationName":"Futures Integration Division","ShortName":"FID","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"c0076d6e-c606-4d9e-ba59-0f33ff509d12","OrganizationName":"G-1","ShortName":"G-1","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"302bddc4-91de-4ef9-82e3-d12f491b7b8a","OrganizationName":"G-4/8","ShortName":"G-4/8","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"732ce29c-7edc-420c-b011-76e32a476126","OrganizationName":"G2","ShortName":"G2","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"4fe068b7-d8bd-4f61-8ff6-2d7284e1b442","OrganizationName":"G3/5/7","ShortName":"G3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7","OrganizationName":"Headquarters, Department of the Army","ShortName":"HQDA","IsOpr":true,"ProponentCode":"HQDA","GapCode":"99","ParentOrganizationGuid":null},{"OrganizationGuid":"ee3f32e9-292e-4a35-9a1f-a84e6e770521","OrganizationName":"INDOPACOM Theater Information Advantage Detachment","ShortName":"INDOPACOM TIAD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"1f98a656-8724-464b-8f26-59259b37f440"},{"OrganizationGuid":"fd75206d-a105-4083-8314-697bb70636e0","OrganizationName":"Intelligence CDID","ShortName":"I-CDID","IsOpr":true,"ProponentCode":"MI","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"aed516e4-a952-411b-b5fd-35920ea47308","OrganizationName":"Intelligence Center of Excellence","ShortName":"ICoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"daa6d46f-1db9-4ecf-a3f5-b3975f70bbb6","OrganizationName":"JMC Forward","ShortName":"JMC - F","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25"},{"OrganizationGuid":"f1dd4686-435c-4910-85c5-d4b0b72a545d","OrganizationName":"Joint and Multiniational Interoperability","ShortName":null,"IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25"},{"OrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25","OrganizationName":"Joint Modernization Command","ShortName":"JMC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"cb2a109b-0cba-44cf-b18d-cc906c8eda47","OrganizationName":"Long Range Precision Fires CFT","ShortName":"LRPF CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"35be3ac6-78ab-4fc5-b053-bd64c6fe2c65","OrganizationName":"Maneuver CDID","ShortName":"M-CDID","IsOpr":true,"ProponentCode":"MCOE","GapCode":"06","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"b44fbe80-2a99-40d4-81f1-54879ffa2d53","OrganizationName":"Maneuver COE","ShortName":"MCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"17ae2a31-1a53-4031-a591-50698a97c250","OrganizationName":"Maneuver Support CDID","ShortName":"MS-CDID","IsOpr":true,"ProponentCode":"MSCoE","GapCode":"07","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"3f92ab0e-a1e8-44c3-9f21-5fd186ff1938","OrganizationName":"Maneuver Support COE","ShortName":"MSCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"af873155-cbb7-433c-b65f-054d3585ee4a","OrganizationName":"Medical CDID","ShortName":"MED-CDID","IsOpr":true,"ProponentCode":"AMEDD","GapCode":"08","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"34cc4e49-50fe-46a4-8936-867562924047","OrganizationName":"Medical COE","ShortName":"MEDCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"4d79c4f3-581e-499e-a5b3-8dac986fd45a","OrganizationName":"Medical Research and Development Command","ShortName":"MRDC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"40c030d7-e404-4dde-9e01-4fe65e04c0c3"},{"OrganizationGuid":"a5931914-afa1-4c74-aae0-1d3136ba2e9c","OrganizationName":"Mission Command CDID","ShortName":"MC-CDID","IsOpr":true,"ProponentCode":"MC CDID","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"78cfc0cb-883b-467e-b18e-b3e2ba0a4ef1","OrganizationName":"Mission Command COE","ShortName":"MCCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"112ea80d-2cad-4e1e-a052-673ea4e55188","OrganizationName":"Multi Domain Operations Simulation Center","ShortName":"MDOSC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"49671561-4ce7-4c52-9dfe-ccacafb995ce","OrganizationName":"Multi-Domain Operations Center","ShortName":"MDOC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25"},{"OrganizationGuid":"f32904a2-81b1-4478-839c-776272247bbf","OrganizationName":"NET CFT","ShortName":"N-CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"13ba87e2-7e10-4d91-9b1d-8b4461c5d220","OrganizationName":"Network Integration Division (NID)/G6","ShortName":null,"IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"462de215-ade7-4ffe-9386-03f14e1250af","OrganizationName":"Next Generation Combat VehicleCFT","ShortName":"NGCV CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"94df18c7-3f93-400e-9196-a2de00d79315","OrganizationName":"Other","ShortName":"Other","IsOpr":true,"ProponentCode":"","GapCode":"","ParentOrganizationGuid":null},{"OrganizationGuid":"938c021b-5c8b-40d0-8bf0-9c118483eba1","OrganizationName":"Rapid Capabilities and Critical Technologies Office","ShortName":"RCCTO","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"a65293e9-d254-484f-a3e7-c853702df228","OrganizationName":"Soldier Lethality CFT","ShortName":"SL CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"f6d0e947-96eb-4d8e-802b-58dd298d9f10","OrganizationName":"Space and Missile Defense Command CDID","ShortName":"SMDC CDID","IsOpr":true,"ProponentCode":"SMDC","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"2a5fd93d-fc50-f011-9fa5-a01881b906d0","OrganizationName":"Space and Missile Defense Command Technical Center","ShortName":"SMDC TC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f6d0e947-96eb-4d8e-802b-58dd298d9f10"},{"OrganizationGuid":"83fe81a4-d307-47d7-a368-2c5a634ff0d7","OrganizationName":"Special Operations CoE","ShortName":"SOCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"e7b1fdf7-acc9-47a5-a1d9-595e2cdfec5d","OrganizationName":"Sustainment CDID","ShortName":"S-CDID","IsOpr":true,"ProponentCode":"CASCOM/SUST","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"6ba69e20-5a45-432a-b33a-27f010e851e8","OrganizationName":"Sustainment COE","ShortName":"SCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"e8084a86-f7e0-4341-8c12-3d7a9449cb8c","OrganizationName":"Synthetic Training Environment CFT","ShortName":"STE CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245","OrganizationName":"The Research and Analysis Center","ShortName":"TRAC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"b9f375c4-35eb-4609-9697-7cafea51ead2","OrganizationName":"TRAC-Fort Leavenworth","ShortName":"TRAC-FLVN","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"980bee65-8ab7-4211-a816-09eeba185802","OrganizationName":"TRAC-Gregg-Addams","ShortName":"TRAC-GRAD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"e92fd86d-351c-4766-8198-c8ded4b061c8","OrganizationName":"TRAC-Monterey","ShortName":"TRAC-MTRY","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"c5a2be1e-b81f-419a-8935-8c6b4085f65c","OrganizationName":"TRAC-White Sands Missile Range","ShortName":"TRAC-WSMR","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"521e7722-87b9-4ec4-8818-f9a67dda0784","OrganizationName":"TRADOC Proponent Office- Echelons above Brigade","ShortName":"TPO-EAB","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"ba1dbc0d-f0ef-47bb-932a-bd677531f667","OrganizationName":"US Air Force","ShortName":"USAF","IsOpr":true,"ProponentCode":"JOINT","GapCode":"99","ParentOrganizationGuid":null},{"OrganizationGuid":"600fd729-86e6-4313-a59f-90d5689589b9","OrganizationName":"US Army Europe","ShortName":"USAREUR-AF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"80c9fb2f-d15a-4be9-9aad-9bf1dc7b038c","OrganizationName":"US Army Pacific","ShortName":"USARPAC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"f2ce22c9-0328-4822-90fd-8c8e98c05cde","OrganizationName":"US Army Special Operations Command CDID","ShortName":"USASOC CDID","IsOpr":true,"ProponentCode":"USASOC","GapCode":"12","ParentOrganizationGuid":null},{"OrganizationGuid":"c05f2986-177d-48a2-a91f-7653b07bef17","OrganizationName":"US Forces Command","ShortName":"FORSCOM","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"3b28f5c5-7175-4a2c-b34a-53ecb85b837e","OrganizationName":"US Marine Corps","ShortName":"USMC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"6a014307-b05e-4af6-a232-04d10ced80c4","OrganizationName":"US Navy","ShortName":"USN","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"aa901092-afcc-4aa0-95c4-ed890a034adb","OrganizationName":"US Space Force","ShortName":"USSF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null}]})},"displayExpr":function(e) { return e ? e.OrganizationName : ''; },"placeholder":"Select OPR","valueExpr":"OrganizationGuid"},"editorType":"dxSelectBox"},{"itemType":"simple","dataField":"OcrProponentIds","colSpan":2,"name":"ocr-proponents","isRequired":true,"label":{"text":"OCR(s)"},"editorOptions":{"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"OrganizationGuid":"9353f360-b56e-4837-a729-6f5b2feca0a3","OrganizationName":"2nd Multidomain Task Force (MDTF)","ShortName":"2 MDTF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"600fd729-86e6-4313-a59f-90d5689589b9"},{"OrganizationGuid":"69949f20-73d6-4dea-ad50-b9a07020c690","OrganizationName":"3rd Multidomain Task Force (MDTF)","ShortName":"3 MDTF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"80c9fb2f-d15a-4be9-9aad-9bf1dc7b038c"},{"OrganizationGuid":"45f2b8c5-ea5b-4128-b1fd-a2dc6e3b84ed","OrganizationName":"75th Innovation CMD","ShortName":"75th IC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"6ec532a5-eb94-4603-abeb-475e7bbcf93b","OrganizationName":"Air and Missile Defense CFT","ShortName":"A\u0026MD CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"33dcd4be-f3f9-41f8-935c-d44d263e59db","OrganizationName":"Applied Concepts Division","ShortName":"ACD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"ede09f65-93a8-4871-96af-dc6dbbb922c2"},{"OrganizationGuid":"e1ed176c-2116-424a-a79a-296842c56f5a","OrganizationName":"Architecture Integration and Management Division","ShortName":"AIMD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"80b6edda-db81-42ac-b871-8ccb4ace08a8"},{"OrganizationGuid":"adc4811e-e4cf-4a79-b254-daaef21fde7f","OrganizationName":"Armaments Center","ShortName":"AC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"b7a0d8b6-4ab3-4ae8-ab6b-491f1ca8fd6b","OrganizationName":"Army Applications Lab","ShortName":"AAL","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"66b5b714-8721-453e-bf60-874a815b5467","OrganizationName":"Army Artificial Intellegence Integration Center","ShortName":"AI2C","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"85c1733f-9df1-4c47-be3a-660894a6da36","OrganizationName":"Army Capability Manager- Cyber","ShortName":"ACM Cyber","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"c38cd089-4402-45f4-8664-efb067509b70","OrganizationName":"Army Capability Manager- Electronic Warfare (EW)","ShortName":"ACM Electronic Warfare (EW)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"7afbb964-16f9-4e0f-8b38-dbc4bc3f70ed","OrganizationName":"Army Capability Manager- Networks and Services (N\u0026S)","ShortName":"ACM Networks and Services (N\u0026S)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"597dfc7a-a287-48f7-a15f-07ae11bdc441","OrganizationName":"Army Capability Manager- Tactical Radio (TR)","ShortName":"ACM Tactical Radio (TR)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5","OrganizationName":"Army Futures Command","ShortName":"AFC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"3fc3ab1d-fad7-444a-994c-6d299b84c388","OrganizationName":"Army Futures Command G-3/5/7","ShortName":"AFC G-3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"94449402-3aa4-403e-bb5f-7fedefac432e","OrganizationName":"Army Research Institute","ShortName":"ARI","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"5b1151ba-bd21-4220-9f71-d792df685f48","OrganizationName":"Army Service Combatant Command  - US Army Central","ShortName":"ASCC - USARCENT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"a32fa529-8bab-4959-aed6-abb9de49cd5f","OrganizationName":"Army Service Combatant Command  - US Army Europe","ShortName":"ASCC - USAREUR","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"e176a0d8-fc3f-4185-82e4-57f2772fb914","OrganizationName":"Army Service Combatant Command  - US Army N America","ShortName":"ASCC - USARNORTH","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"1f98a656-8724-464b-8f26-59259b37f440","OrganizationName":"Army Service Combatant Command  - US Army Pacific","ShortName":"ASCC - USARPAC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"7a5af3a7-53b8-41ae-97ae-f6ba66e995c8","OrganizationName":"Army Service Combatant Command  - US Army S. America","ShortName":"ASCC - USARSO","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"21bce6a8-5eb4-46f9-a0cb-5cf69f415819","OrganizationName":"Army Service Combatant Command  US Army- Africa","ShortName":"ASCC - USARAF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"a963d32e-121b-40e4-9296-a47c344deb60","OrganizationName":"Army Service Combatant Command - US Army Cyber","ShortName":"ASCC - ARCYBER","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"41d1051f-15c6-47ee-820e-dba2fbfb704a","OrganizationName":"Army Test and Evaluation Command","ShortName":"ATEC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"15479e18-be41-4c51-aaa6-f608d82f4aa8","OrganizationName":"Army Training and Doctrine Command","ShortName":"TRADOC","IsOpr":true,"ProponentCode":"TRADOC HQ","GapCode":"99","ParentOrganizationGuid":null},{"OrganizationGuid":"3e6b0e8e-4eaf-4c35-81df-e1168b1e760e","OrganizationName":"Assistant Sec.Army- Acquisitions, Logistics, Technology","ShortName":"ASA(ALT)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"9ac0ee04-30e4-49d8-9c75-c6be301406cd","OrganizationName":"Assistant Sec.Army- Manpower, Reserves ","ShortName":"ASA(MRA)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"d82b5e4a-1777-4c1e-ae5c-b4a12a020cd0","OrganizationName":"Assured Positioning, Navigation, and Timing CFT","ShortName":"A-PNT CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"1a6813dd-2434-42bc-ac8b-103f4c6a0faa","OrganizationName":"Aviation CDID","ShortName":"A-CDID","IsOpr":true,"ProponentCode":"AV","GapCode":"02","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"fc6c71f0-0fc4-4b63-9ec7-cd60046730c0","OrganizationName":"Aviation Center of Excellence","ShortName":"AVCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"0014905e-c18e-4ff3-a185-dc2cc640458a","OrganizationName":"Chaplain CDID","ShortName":"Chaplain CDID","IsOpr":true,"ProponentCode":"CHAP","GapCode":"14","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"ac442dc4-7fd8-4388-b7f7-96684c078d3c","OrganizationName":"Chief of Engineers","ShortName":"Chief of Engineers","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4","OrganizationName":"Combined Arms Center","ShortName":"CAC","IsOpr":true,"ProponentCode":"CAC-T","GapCode":"99","ParentOrganizationGuid":"15479e18-be41-4c51-aaa6-f608d82f4aa8"},{"OrganizationGuid":"eaec5a7a-818e-4901-8094-be3e9947b4e5","OrganizationName":"Command and Control CFT","ShortName":"C2 CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"a524a75b-6164-458b-80ee-b86c28cadd82","OrganizationName":"Contested Logistics CFT ","ShortName":"CLFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687","OrganizationName":"Cyber CDID","ShortName":"C-CDID","IsOpr":true,"ProponentCode":"Cyber","GapCode":"03","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"f0a8068c-f61b-4269-b6bf-bb85d2a2ffba","OrganizationName":"Cyber Center of Excellence","ShortName":"CCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"53742f86-debd-4880-bc54-7348db9e40d6","OrganizationName":"Cyber Command","ShortName":"CYBERCOM","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"f4263fda-a85f-47fe-8c47-7da5a761b8cd","OrganizationName":"Cyber Theater Information Advantage Detachment","ShortName":"Cyber TIAD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"53742f86-debd-4880-bc54-7348db9e40d6"},{"OrganizationGuid":"6d110399-f359-487d-829d-2dd283a90914","OrganizationName":"Deputy Chief of Staff G-3/5/7","ShortName":"DCoS G-3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"9be557f4-4853-48f8-aa6c-0885cde155f4","OrganizationName":"Deputy Chief of Staff- G1","ShortName":"DCoS-G1","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"83d92df4-b9be-4780-b378-67c7ac1a75ae","OrganizationName":"Deputy Chief of Staff- G8","ShortName":"DCoS-G8","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"615d09e2-6091-46d7-8530-38677f3c8eb7","OrganizationName":"Deputy Chief of Staff-G6","ShortName":"DCoS-G6","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"8ccda746-5efb-407c-aef7-f9048d366d1b","OrganizationName":"DEVCOM Analysis Center","ShortName":"DAC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"4f8be144-d40f-4520-905d-fcf5e28a9c13","OrganizationName":"DEVCOM Army Research Labratory","ShortName":"ARL","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"ac4aabc2-ab2b-4778-ab50-de93bb4067e1","OrganizationName":"DEVCOM Aviation \u0026 Missile Center","ShortName":"AvMC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"099bf1c1-0ed4-4842-a6da-064490a717f4","OrganizationName":"DEVCOM Chemical Biological Center","ShortName":"CBC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"301ac328-d33f-434c-ba87-5b6800506ad6","OrganizationName":"DEVCOM Command, Control, Communications, Computers, Cyber, Intelligence, Surveillance and Reconnaissance Center","ShortName":"C5ISRC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"bea30b04-693e-4141-9518-178cf03a636e","OrganizationName":"DEVCOM Ground Vehicle Systems Center","ShortName":"GVSC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a","OrganizationName":"DEVCOM HQ","ShortName":"DEVCOM","IsOpr":true,"ProponentCode":"STRACD","GapCode":"99","ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"08d8a04d-3985-4872-80bf-0ea5dfe9c312","OrganizationName":"DEVCOM Soldier Center","ShortName":"SC","IsOpr":true,"ProponentCode":"PAO","GapCode":"99","ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"ede09f65-93a8-4871-96af-dc6dbbb922c2","OrganizationName":"Directorate Of Concepts","ShortName":"DoC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"80b6edda-db81-42ac-b871-8ccb4ace08a8"},{"OrganizationGuid":"e0ae1f08-98ad-473a-8bed-90ba1bfac4fc","OrganizationName":"Engineer Research and Development Center","ShortName":"ERDC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"7b66058e-3afd-4018-9b66-00af3c90e07a","OrganizationName":"FCC - Other","ShortName":"FCC - Other","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"edb7b359-780e-4683-889d-ac14f7f90c42","OrganizationName":"Fires CDID","ShortName":"F-CDID","IsOpr":true,"ProponentCode":"FIRES","GapCode":"04","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"654c6c12-ac3e-4eb9-970a-4db40a15370e","OrganizationName":"Fires Center of Excellence","ShortName":"FCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"3b99add5-20ba-4ade-8dd6-245c05a2b1c5","OrganizationName":"Future Vertical Lift CFT","ShortName":"FVL CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a","OrganizationName":"Futures and Concepts Center","ShortName":"FCC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"555b21e2-ab9d-446b-bc9c-1f6fc40cbc63","OrganizationName":"Futures and Concepts Center G-3/5/7","ShortName":"FCC G-3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"80b6edda-db81-42ac-b871-8ccb4ace08a8","OrganizationName":"Futures Integration Division","ShortName":"FID","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"c0076d6e-c606-4d9e-ba59-0f33ff509d12","OrganizationName":"G-1","ShortName":"G-1","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"302bddc4-91de-4ef9-82e3-d12f491b7b8a","OrganizationName":"G-4/8","ShortName":"G-4/8","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"732ce29c-7edc-420c-b011-76e32a476126","OrganizationName":"G2","ShortName":"G2","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"4fe068b7-d8bd-4f61-8ff6-2d7284e1b442","OrganizationName":"G3/5/7","ShortName":"G3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7","OrganizationName":"Headquarters, Department of the Army","ShortName":"HQDA","IsOpr":true,"ProponentCode":"HQDA","GapCode":"99","ParentOrganizationGuid":null},{"OrganizationGuid":"ee3f32e9-292e-4a35-9a1f-a84e6e770521","OrganizationName":"INDOPACOM Theater Information Advantage Detachment","ShortName":"INDOPACOM TIAD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"1f98a656-8724-464b-8f26-59259b37f440"},{"OrganizationGuid":"fd75206d-a105-4083-8314-697bb70636e0","OrganizationName":"Intelligence CDID","ShortName":"I-CDID","IsOpr":true,"ProponentCode":"MI","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"aed516e4-a952-411b-b5fd-35920ea47308","OrganizationName":"Intelligence Center of Excellence","ShortName":"ICoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"daa6d46f-1db9-4ecf-a3f5-b3975f70bbb6","OrganizationName":"JMC Forward","ShortName":"JMC - F","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25"},{"OrganizationGuid":"f1dd4686-435c-4910-85c5-d4b0b72a545d","OrganizationName":"Joint and Multiniational Interoperability","ShortName":null,"IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25"},{"OrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25","OrganizationName":"Joint Modernization Command","ShortName":"JMC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"cb2a109b-0cba-44cf-b18d-cc906c8eda47","OrganizationName":"Long Range Precision Fires CFT","ShortName":"LRPF CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"35be3ac6-78ab-4fc5-b053-bd64c6fe2c65","OrganizationName":"Maneuver CDID","ShortName":"M-CDID","IsOpr":true,"ProponentCode":"MCOE","GapCode":"06","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"b44fbe80-2a99-40d4-81f1-54879ffa2d53","OrganizationName":"Maneuver COE","ShortName":"MCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"17ae2a31-1a53-4031-a591-50698a97c250","OrganizationName":"Maneuver Support CDID","ShortName":"MS-CDID","IsOpr":true,"ProponentCode":"MSCoE","GapCode":"07","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"3f92ab0e-a1e8-44c3-9f21-5fd186ff1938","OrganizationName":"Maneuver Support COE","ShortName":"MSCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"af873155-cbb7-433c-b65f-054d3585ee4a","OrganizationName":"Medical CDID","ShortName":"MED-CDID","IsOpr":true,"ProponentCode":"AMEDD","GapCode":"08","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"34cc4e49-50fe-46a4-8936-867562924047","OrganizationName":"Medical COE","ShortName":"MEDCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"4d79c4f3-581e-499e-a5b3-8dac986fd45a","OrganizationName":"Medical Research and Development Command","ShortName":"MRDC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"40c030d7-e404-4dde-9e01-4fe65e04c0c3"},{"OrganizationGuid":"a5931914-afa1-4c74-aae0-1d3136ba2e9c","OrganizationName":"Mission Command CDID","ShortName":"MC-CDID","IsOpr":true,"ProponentCode":"MC CDID","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"78cfc0cb-883b-467e-b18e-b3e2ba0a4ef1","OrganizationName":"Mission Command COE","ShortName":"MCCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"112ea80d-2cad-4e1e-a052-673ea4e55188","OrganizationName":"Multi Domain Operations Simulation Center","ShortName":"MDOSC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"49671561-4ce7-4c52-9dfe-ccacafb995ce","OrganizationName":"Multi-Domain Operations Center","ShortName":"MDOC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25"},{"OrganizationGuid":"f32904a2-81b1-4478-839c-776272247bbf","OrganizationName":"NET CFT","ShortName":"N-CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"13ba87e2-7e10-4d91-9b1d-8b4461c5d220","OrganizationName":"Network Integration Division (NID)/G6","ShortName":null,"IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"462de215-ade7-4ffe-9386-03f14e1250af","OrganizationName":"Next Generation Combat VehicleCFT","ShortName":"NGCV CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"94df18c7-3f93-400e-9196-a2de00d79315","OrganizationName":"Other","ShortName":"Other","IsOpr":true,"ProponentCode":"","GapCode":"","ParentOrganizationGuid":null},{"OrganizationGuid":"938c021b-5c8b-40d0-8bf0-9c118483eba1","OrganizationName":"Rapid Capabilities and Critical Technologies Office","ShortName":"RCCTO","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"a65293e9-d254-484f-a3e7-c853702df228","OrganizationName":"Soldier Lethality CFT","ShortName":"SL CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"f6d0e947-96eb-4d8e-802b-58dd298d9f10","OrganizationName":"Space and Missile Defense Command CDID","ShortName":"SMDC CDID","IsOpr":true,"ProponentCode":"SMDC","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"2a5fd93d-fc50-f011-9fa5-a01881b906d0","OrganizationName":"Space and Missile Defense Command Technical Center","ShortName":"SMDC TC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f6d0e947-96eb-4d8e-802b-58dd298d9f10"},{"OrganizationGuid":"83fe81a4-d307-47d7-a368-2c5a634ff0d7","OrganizationName":"Special Operations CoE","ShortName":"SOCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"e7b1fdf7-acc9-47a5-a1d9-595e2cdfec5d","OrganizationName":"Sustainment CDID","ShortName":"S-CDID","IsOpr":true,"ProponentCode":"CASCOM/SUST","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"6ba69e20-5a45-432a-b33a-27f010e851e8","OrganizationName":"Sustainment COE","ShortName":"SCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"e8084a86-f7e0-4341-8c12-3d7a9449cb8c","OrganizationName":"Synthetic Training Environment CFT","ShortName":"STE CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245","OrganizationName":"The Research and Analysis Center","ShortName":"TRAC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"b9f375c4-35eb-4609-9697-7cafea51ead2","OrganizationName":"TRAC-Fort Leavenworth","ShortName":"TRAC-FLVN","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"980bee65-8ab7-4211-a816-09eeba185802","OrganizationName":"TRAC-Gregg-Addams","ShortName":"TRAC-GRAD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"e92fd86d-351c-4766-8198-c8ded4b061c8","OrganizationName":"TRAC-Monterey","ShortName":"TRAC-MTRY","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"c5a2be1e-b81f-419a-8935-8c6b4085f65c","OrganizationName":"TRAC-White Sands Missile Range","ShortName":"TRAC-WSMR","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"521e7722-87b9-4ec4-8818-f9a67dda0784","OrganizationName":"TRADOC Proponent Office- Echelons above Brigade","ShortName":"TPO-EAB","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"ba1dbc0d-f0ef-47bb-932a-bd677531f667","OrganizationName":"US Air Force","ShortName":"USAF","IsOpr":true,"ProponentCode":"JOINT","GapCode":"99","ParentOrganizationGuid":null},{"OrganizationGuid":"600fd729-86e6-4313-a59f-90d5689589b9","OrganizationName":"US Army Europe","ShortName":"USAREUR-AF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"80c9fb2f-d15a-4be9-9aad-9bf1dc7b038c","OrganizationName":"US Army Pacific","ShortName":"USARPAC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"f2ce22c9-0328-4822-90fd-8c8e98c05cde","OrganizationName":"US Army Special Operations Command CDID","ShortName":"USASOC CDID","IsOpr":true,"ProponentCode":"USASOC","GapCode":"12","ParentOrganizationGuid":null},{"OrganizationGuid":"c05f2986-177d-48a2-a91f-7653b07bef17","OrganizationName":"US Forces Command","ShortName":"FORSCOM","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"3b28f5c5-7175-4a2c-b34a-53ecb85b837e","OrganizationName":"US Marine Corps","ShortName":"USMC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"6a014307-b05e-4af6-a232-04d10ced80c4","OrganizationName":"US Navy","ShortName":"USN","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"aa901092-afcc-4aa0-95c4-ed890a034adb","OrganizationName":"US Space Force","ShortName":"USSF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null}],"key":"OrganizationGuid"})},"valueExpr":"OrganizationGuid","displayExpr":"OrganizationName","value":[],"placeholder":"Select OCRs","showClearButton":true,"contentTemplate":$("#OcrDataGridMultipleTemplate"),"_ignoreElementAttrDeprecation":true,"elementAttr":{"id":"ocr-proponents-dropdownbox"}},"editorType":"dxDropDownBox"},{"itemType":"simple","dataField":"FcwConceptId","editorOptions":{"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"Id":316,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"T3st","LeadOrganizationId":null,"LeadOrganization":"G3/5/7","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 7, 12, 18, 4, 38, 923),"LastModified":new Date(2025, 7, 13, 16, 34, 5, 413),"ImageId":null,"AwcYear":2030,"Authorization":2,"ShowFcw":true},{"Id":112,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test ","LeadOrganizationId":null,"LeadOrganization":"DEVCOM Command, Control, Communications, Computers, Cyber, Intelligence, Surveillance and Reconnaissance Center","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2024, 4, 14, 16, 18, 37, 360),"LastModified":new Date(2025, 6, 21, 11, 44, 4, 73),"ImageId":3806,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":119,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"test retest 624","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2024, 5, 24, 23, 53, 17, 997),"LastModified":new Date(2024, 5, 24, 23, 55, 57, 207),"ImageId":3477,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":117,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"pennys permission test","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Protected","Created":new Date(2024, 5, 20, 11, 49, 5, 0),"LastModified":new Date(2025, 2, 19, 20, 38, 48, 767),"ImageId":3474,"AwcYear":2040,"Authorization":0,"ShowFcw":true},{"Id":240,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"nancy test1","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 2, 12, 9, 32, 28, 903),"LastModified":new Date(2025, 2, 13, 21, 27, 50, 487),"ImageId":null,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":241,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"test redo","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 2, 14, 15, 15, 17, 353),"LastModified":new Date(2025, 2, 28, 14, 46, 52, 903),"ImageId":4042,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":238,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"penny is the best tester concept","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 2, 7, 16, 39, 14, 0),"LastModified":new Date(2025, 2, 18, 15, 42, 52, 940),"ImageId":4059,"AwcYear":2060,"Authorization":2,"ShowFcw":true},{"Id":229,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"jared test 4","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 0, 28, 13, 10, 22, 247),"LastModified":new Date(2025, 1, 12, 18, 7, 50, 860),"ImageId":null,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":87,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"penny concept","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2023, 11, 15, 13, 26, 45, 970),"LastModified":new Date(2025, 2, 11, 23, 25, 18, 847),"ImageId":null,"AwcYear":2030,"Authorization":2,"ShowFcw":true},{"Id":1,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"Carson Test FCW","LeadOrganizationId":null,"LeadOrganization":"Maneuver CDID","Status":"Published","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2020, 2, 2, 9, 20, 46, 350),"LastModified":new Date(2024, 8, 17, 12, 16, 33, 417),"ImageId":3499,"AwcYear":2030,"Authorization":2,"ShowFcw":true},{"Id":129,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"sdfasdfas","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Public","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2024, 7, 19, 16, 13, 29, 177),"LastModified":new Date(2024, 7, 20, 9, 12, 24, 763),"ImageId":3544,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":53,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"concept name ","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft_7","AccessLevelGuid":null,"AccessLevel":"Protected","Created":new Date(2023, 7, 21, 17, 51, 49, 433),"LastModified":new Date(2025, 2, 14, 10, 56, 57, 547),"ImageId":null,"AwcYear":2040,"Authorization":0,"ShowFcw":true}],"key":"Id"})},"displayExpr":function(e) { return e ? e.Id + ' - ' + e.Title : ''; },"valueExpr":"Id","value":null,"placeholder":"Select an FCW Link","showClearButton":true,"dropDownOptions":{"width":1000},"contentTemplate":$("#FcwConceptDataGrid")},"editorType":"dxDropDownBox","name":"fcw-link","cssClass":"gen-info-fcw-concept-id-editor d-none","colSpan":2,"label":{"text":"FCW Link"}},{"itemType":"simple","dataField":"CrcEchelonIds","name":"echelon","cssClass":"gen-info-crc-echelon-id-editor d-none","colSpan":2,"label":{"text":"Echelons"},"editorOptions":{"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"Key":"c69ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Battalion","Order":0,"Deleted":false},{"Key":"c79ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Brigade","Order":0,"Deleted":false},{"Key":"d09ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"CCF","Order":0,"Deleted":false},{"Key":"c59ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Company","Order":0,"Deleted":false},{"Key":"d29ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Corps","Order":0,"Deleted":false},{"Key":"d19ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Division","Order":0,"Deleted":false},{"Key":"cb9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Element","Order":0,"Deleted":false},{"Key":"c99ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Group","Order":0,"Deleted":false},{"Key":"c89ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Headquarters","Order":0,"Deleted":false},{"Key":"cc9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Main CP","Order":0,"Deleted":false},{"Key":"ce9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Mobile CP","Order":0,"Deleted":false},{"Key":"cf9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"OCG","Order":0,"Deleted":false},{"Key":"cd9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Tactical CP","Order":0,"Deleted":false},{"Key":"ca9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Theater","Order":0,"Deleted":false}],"key":"Key"})},"displayExpr":"Value","valueExpr":"Key","value":[],"placeholder":"Select Echelons","showClearButton":true,"contentTemplate":$("#EchelonDataGrid")},"editorType":"dxDropDownBox"}]}]});}).bind(this, jQuery));</script>
</div>

<script type="text/html" id="is-snt-radio-template">    <div class="form-check form-switch mt-3">
        <input id="is-snt-checkbox"
            class="form-check-input"
            type="checkbox"
            title="Indicates if the Solution Idea is in DEVCOM's area of responsibility"
            onchange="FORGE.Pathfinder.SolutionIdeas.toggleIsSnt();"
            
             
        >
        <label class="form-check-label" for="is-snt-checkbox">Is this S&T?</label>
        <abbr title="Indicates if the Solution Idea is in DEVCOM's area of responsibility?" class="data-column-hint ms-1"><i class="fa-solid fa-circle-info me-2 fs-6 forge-icon--instruction text-right px-2"></i></abbr>
     </div>
</script>
<script type="text/html" id="critical-path-radio-template">    <div class="form-check form-switch mt-3">
        <input
            id="critical-path-checkbox"
            class="form-check-input"
            type="checkbox"
            title="Is critical path?"
            onchange="FORGE.Pathfinder.SolutionIdeas.toggleCriticalPath();"    
            
            
        >
        <label class="form-check-label" for="critical-path-checkbox">Is Critical Path?</label>
        <abbr title="Is Critical Path?" class="data-column-hint ms-1"><i class="fa-solid fa-circle-info me-2 fs-6 forge-icon--instruction text-right px-2"></i></abbr>
    </div>
</script>

<script type="text/html" id="GapCategoryDataGridMultipleTemplate"><%!function(){%><div id="<%=arguments[0]%>"></div><%DevExpress.aspnet.createComponent("dxDataGrid",{"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"Key":"f154c5b7-cf0b-ef11-8075-0003ff1f473c","Value":"Undefined","Code":"00"},{"Key":"64e20793-0aab-4b79-aa0e-f7eb3c1df4e4","Value":"Network","Code":"01"},{"Key":"e5eef621-6cc5-4a03-9529-ced4542e6c64","Value":"CEMA","Code":"02"},{"Key":"13a371fd-2105-4dd3-84d2-837cba99f18a","Value":"Counter-C5ISRT","Code":"03"},{"Key":"7ff249ec-169c-4f64-bd3b-26d7d832fbec","Value":"Space Operations","Code":"04"},{"Key":"417c8ca2-b67c-40d8-9f6f-858e01473cda","Value":"Battlefield Visibility/Situational Understanding","Code":"05"},{"Key":"9bda6ca3-6de4-4634-a6a4-45bdc78aaf10","Value":"C2 Overmatch","Code":"06"},{"Key":"9ade68ff-4ebe-4905-9105-fcebc9c26007","Value":"Inter/Intra-Theater Lift","Code":"07"},{"Key":"6299b2a0-7ac8-4aa5-9bb0-b076a4293d19","Value":"Protect the Force","Code":"10"},{"Key":"626cf0de-2b9b-4fdc-9cc3-bb623857eca8","Value":"Defend Airspace","Code":"11"},{"Key":"adf40c6a-5998-4364-aec2-8c9208014df9","Value":"Maneuver/Lethality ","Code":"13"},{"Key":"d10f0aff-c989-4140-b1a8-4c1861f2e074","Value":"Aerial Operations","Code":"14"},{"Key":"5d391129-deb8-4331-bc83-cd0048645c30","Value":"Army Maritime Operations","Code":"15"},{"Key":"07bdec77-3ab5-4a2b-a6ca-3e501e91335f","Value":"Mass Casualty Evacuation and Treatment","Code":"16"},{"Key":"fc0dd63a-c434-4133-a2fa-4ab3c37dddde","Value":"Dynamic and Deliberate Targeting","Code":"21"}],"key":"Key"})},"columns":[{"dataField":"Key","validationRules":[{"type":"required","message":"The Key field is required."}],"visible":false},{"dataField":"Code","dataType":"string","width":100},{"dataField":"Value","dataType":"string"}],"headerFilter":{"visible":true},"showBorders":true,"rowAlternationEnabled":true,"hoverStateEnabled":true,"wordWrapEnabled":true,"paging":{"enabled":false},"filterRow":{"visible":true},"height":"345","selection":{"mode":"multiple","showCheckBoxesMode":"always"},"selectedRowKeys":component.option("value"),"onSelectionChanged":function(e) {  FORGE.devExtreme.onMultiSelectionGridChanged(e, component); }},arguments[0])%><%}("gap-category-datagrid")%></script>
<script type="text/html" id="FcwConceptDataGrid"><%!function(){%><div id="<%=arguments[0]%>"></div><%DevExpress.aspnet.createComponent("dxDataGrid",{"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"Id":316,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"T3st","LeadOrganizationId":null,"LeadOrganization":"G3/5/7","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 7, 12, 18, 4, 38, 923),"LastModified":new Date(2025, 7, 13, 16, 34, 5, 413),"ImageId":null,"AwcYear":2030,"Authorization":2,"ShowFcw":true},{"Id":112,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test nancy test ","LeadOrganizationId":null,"LeadOrganization":"DEVCOM Command, Control, Communications, Computers, Cyber, Intelligence, Surveillance and Reconnaissance Center","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2024, 4, 14, 16, 18, 37, 360),"LastModified":new Date(2025, 6, 21, 11, 44, 4, 73),"ImageId":3806,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":119,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"test retest 624","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2024, 5, 24, 23, 53, 17, 997),"LastModified":new Date(2024, 5, 24, 23, 55, 57, 207),"ImageId":3477,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":117,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"pennys permission test","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Protected","Created":new Date(2024, 5, 20, 11, 49, 5, 0),"LastModified":new Date(2025, 2, 19, 20, 38, 48, 767),"ImageId":3474,"AwcYear":2040,"Authorization":0,"ShowFcw":true},{"Id":240,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"nancy test1","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 2, 12, 9, 32, 28, 903),"LastModified":new Date(2025, 2, 13, 21, 27, 50, 487),"ImageId":null,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":241,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"test redo","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 2, 14, 15, 15, 17, 353),"LastModified":new Date(2025, 2, 28, 14, 46, 52, 903),"ImageId":4042,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":238,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"penny is the best tester concept","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 2, 7, 16, 39, 14, 0),"LastModified":new Date(2025, 2, 18, 15, 42, 52, 940),"ImageId":4059,"AwcYear":2060,"Authorization":2,"ShowFcw":true},{"Id":229,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"jared test 4","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2025, 0, 28, 13, 10, 22, 247),"LastModified":new Date(2025, 1, 12, 18, 7, 50, 860),"ImageId":null,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":87,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"penny concept","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2023, 11, 15, 13, 26, 45, 970),"LastModified":new Date(2025, 2, 11, 23, 25, 18, 847),"ImageId":null,"AwcYear":2030,"Authorization":2,"ShowFcw":true},{"Id":1,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"Carson Test FCW","LeadOrganizationId":null,"LeadOrganization":"Maneuver CDID","Status":"Published","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2020, 2, 2, 9, 20, 46, 350),"LastModified":new Date(2024, 8, 17, 12, 16, 33, 417),"ImageId":3499,"AwcYear":2030,"Authorization":2,"ShowFcw":true},{"Id":129,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"sdfasdfas","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Public","AccessLevelGuid":null,"AccessLevel":"Public","Created":new Date(2024, 7, 19, 16, 13, 29, 177),"LastModified":new Date(2024, 7, 20, 9, 12, 24, 763),"ImageId":3544,"AwcYear":2040,"Authorization":2,"ShowFcw":true},{"Id":53,"TypeGuid":"9e3cfea5-8517-ef11-8076-0003ff0c3117","Type":"Formation Capability Workbook","TypeCode":null,"Title":"concept name ","LeadOrganizationId":null,"LeadOrganization":"Other","Status":"Draft_7","AccessLevelGuid":null,"AccessLevel":"Protected","Created":new Date(2023, 7, 21, 17, 51, 49, 433),"LastModified":new Date(2025, 2, 14, 10, 56, 57, 547),"ImageId":null,"AwcYear":2040,"Authorization":0,"ShowFcw":true}],"key":"Id"})},"filterRow":{"visible":true},"headerFilter":{"visible":true},"showBorders":true,"rowAlternationEnabled":true,"hoverStateEnabled":true,"wordWrapEnabled":true,"paging":{"pageSize":5},"selection":{"mode":"single"},"columnAutoWidth":true,"columns":[{"dataField":"Id","dataType":"number","validationRules":[{"type":"required","message":"The Id field is required."}],"caption":"Concept ID","width":100},{"dataField":"Title","dataType":"string"},{"dataField":"AwcYear","dataType":"number","caption":"AWC Year","alignment":"left","width":100},{"dataField":"LeadOrganization","dataType":"string","caption":"Lead","width":"200"}],"selectedRowKeys":component.option("value"),"onSelectionChanged":function (selectionChangedArgs) {
    FORGE.devExtreme.onSingleDropDownSelected(selectionChangedArgs, component);
    }},arguments[0])%><%}("fcw-concept-data-grid")%></script>
<script type="text/html" id="EchelonDataGrid"><%!function(){%><div id="<%=arguments[0]%>"></div><%DevExpress.aspnet.createComponent("dxDataGrid",{"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"Key":"c69ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Battalion","Order":0,"Deleted":false},{"Key":"c79ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Brigade","Order":0,"Deleted":false},{"Key":"d09ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"CCF","Order":0,"Deleted":false},{"Key":"c59ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Company","Order":0,"Deleted":false},{"Key":"d29ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Corps","Order":0,"Deleted":false},{"Key":"d19ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Division","Order":0,"Deleted":false},{"Key":"cb9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Element","Order":0,"Deleted":false},{"Key":"c99ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Group","Order":0,"Deleted":false},{"Key":"c89ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Headquarters","Order":0,"Deleted":false},{"Key":"cc9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Main CP","Order":0,"Deleted":false},{"Key":"ce9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Mobile CP","Order":0,"Deleted":false},{"Key":"cf9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"OCG","Order":0,"Deleted":false},{"Key":"cd9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Tactical CP","Order":0,"Deleted":false},{"Key":"ca9ffd62-3ee2-ef11-a838-0003ff1f3770","Value":"Theater","Order":0,"Deleted":false}],"key":"Key"})},"filterRow":{"visible":true},"headerFilter":{"visible":true},"showBorders":true,"rowAlternationEnabled":true,"height":400,"hoverStateEnabled":true,"wordWrapEnabled":true,"paging":{"enabled":false},"selection":{"mode":"multiple","showCheckBoxesMode":"always"},"columnAutoWidth":true,"columns":[{"dataField":"Key","dataType":"number","validationRules":[{"type":"required","message":"The Key field is required."}],"visible":false},{"dataField":"Value","dataType":"string","caption":"Echelon"}],"selectedRowKeys":component.option("value"),"onSelectionChanged":function (selectionChangedArgs) {
    FORGE.devExtreme.onMultiSelectionGridChanged(selectionChangedArgs, component);
    }},arguments[0])%><%}("echelon-data-grid")%></script>
<script type="text/html" id="OcrDataGridMultipleTemplate"><%!function(){%><div id="<%=arguments[0]%>"></div><%DevExpress.aspnet.createComponent("dxDataGrid",{"dataSource":{"store":new DevExpress.data.ArrayStore({"data":[{"OrganizationGuid":"9353f360-b56e-4837-a729-6f5b2feca0a3","OrganizationName":"2nd Multidomain Task Force (MDTF)","ShortName":"2 MDTF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"600fd729-86e6-4313-a59f-90d5689589b9"},{"OrganizationGuid":"69949f20-73d6-4dea-ad50-b9a07020c690","OrganizationName":"3rd Multidomain Task Force (MDTF)","ShortName":"3 MDTF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"80c9fb2f-d15a-4be9-9aad-9bf1dc7b038c"},{"OrganizationGuid":"45f2b8c5-ea5b-4128-b1fd-a2dc6e3b84ed","OrganizationName":"75th Innovation CMD","ShortName":"75th IC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"6ec532a5-eb94-4603-abeb-475e7bbcf93b","OrganizationName":"Air and Missile Defense CFT","ShortName":"A\u0026MD CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"33dcd4be-f3f9-41f8-935c-d44d263e59db","OrganizationName":"Applied Concepts Division","ShortName":"ACD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"ede09f65-93a8-4871-96af-dc6dbbb922c2"},{"OrganizationGuid":"e1ed176c-2116-424a-a79a-296842c56f5a","OrganizationName":"Architecture Integration and Management Division","ShortName":"AIMD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"80b6edda-db81-42ac-b871-8ccb4ace08a8"},{"OrganizationGuid":"adc4811e-e4cf-4a79-b254-daaef21fde7f","OrganizationName":"Armaments Center","ShortName":"AC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"b7a0d8b6-4ab3-4ae8-ab6b-491f1ca8fd6b","OrganizationName":"Army Applications Lab","ShortName":"AAL","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"66b5b714-8721-453e-bf60-874a815b5467","OrganizationName":"Army Artificial Intellegence Integration Center","ShortName":"AI2C","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"85c1733f-9df1-4c47-be3a-660894a6da36","OrganizationName":"Army Capability Manager- Cyber","ShortName":"ACM Cyber","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"c38cd089-4402-45f4-8664-efb067509b70","OrganizationName":"Army Capability Manager- Electronic Warfare (EW)","ShortName":"ACM Electronic Warfare (EW)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"7afbb964-16f9-4e0f-8b38-dbc4bc3f70ed","OrganizationName":"Army Capability Manager- Networks and Services (N\u0026S)","ShortName":"ACM Networks and Services (N\u0026S)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"597dfc7a-a287-48f7-a15f-07ae11bdc441","OrganizationName":"Army Capability Manager- Tactical Radio (TR)","ShortName":"ACM Tactical Radio (TR)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687"},{"OrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5","OrganizationName":"Army Futures Command","ShortName":"AFC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"3fc3ab1d-fad7-444a-994c-6d299b84c388","OrganizationName":"Army Futures Command G-3/5/7","ShortName":"AFC G-3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"94449402-3aa4-403e-bb5f-7fedefac432e","OrganizationName":"Army Research Institute","ShortName":"ARI","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"5b1151ba-bd21-4220-9f71-d792df685f48","OrganizationName":"Army Service Combatant Command  - US Army Central","ShortName":"ASCC - USARCENT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"a32fa529-8bab-4959-aed6-abb9de49cd5f","OrganizationName":"Army Service Combatant Command  - US Army Europe","ShortName":"ASCC - USAREUR","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"e176a0d8-fc3f-4185-82e4-57f2772fb914","OrganizationName":"Army Service Combatant Command  - US Army N America","ShortName":"ASCC - USARNORTH","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"1f98a656-8724-464b-8f26-59259b37f440","OrganizationName":"Army Service Combatant Command  - US Army Pacific","ShortName":"ASCC - USARPAC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"7a5af3a7-53b8-41ae-97ae-f6ba66e995c8","OrganizationName":"Army Service Combatant Command  - US Army S. America","ShortName":"ASCC - USARSO","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"21bce6a8-5eb4-46f9-a0cb-5cf69f415819","OrganizationName":"Army Service Combatant Command  US Army- Africa","ShortName":"ASCC - USARAF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"a963d32e-121b-40e4-9296-a47c344deb60","OrganizationName":"Army Service Combatant Command - US Army Cyber","ShortName":"ASCC - ARCYBER","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f4dc9ed5-32c5-485a-adb8-c69a5bd265a2"},{"OrganizationGuid":"41d1051f-15c6-47ee-820e-dba2fbfb704a","OrganizationName":"Army Test and Evaluation Command","ShortName":"ATEC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"15479e18-be41-4c51-aaa6-f608d82f4aa8","OrganizationName":"Army Training and Doctrine Command","ShortName":"TRADOC","IsOpr":true,"ProponentCode":"TRADOC HQ","GapCode":"99","ParentOrganizationGuid":null},{"OrganizationGuid":"3e6b0e8e-4eaf-4c35-81df-e1168b1e760e","OrganizationName":"Assistant Sec.Army- Acquisitions, Logistics, Technology","ShortName":"ASA(ALT)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"9ac0ee04-30e4-49d8-9c75-c6be301406cd","OrganizationName":"Assistant Sec.Army- Manpower, Reserves ","ShortName":"ASA(MRA)","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"d82b5e4a-1777-4c1e-ae5c-b4a12a020cd0","OrganizationName":"Assured Positioning, Navigation, and Timing CFT","ShortName":"A-PNT CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"1a6813dd-2434-42bc-ac8b-103f4c6a0faa","OrganizationName":"Aviation CDID","ShortName":"A-CDID","IsOpr":true,"ProponentCode":"AV","GapCode":"02","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"fc6c71f0-0fc4-4b63-9ec7-cd60046730c0","OrganizationName":"Aviation Center of Excellence","ShortName":"AVCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"0014905e-c18e-4ff3-a185-dc2cc640458a","OrganizationName":"Chaplain CDID","ShortName":"Chaplain CDID","IsOpr":true,"ProponentCode":"CHAP","GapCode":"14","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"ac442dc4-7fd8-4388-b7f7-96684c078d3c","OrganizationName":"Chief of Engineers","ShortName":"Chief of Engineers","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4","OrganizationName":"Combined Arms Center","ShortName":"CAC","IsOpr":true,"ProponentCode":"CAC-T","GapCode":"99","ParentOrganizationGuid":"15479e18-be41-4c51-aaa6-f608d82f4aa8"},{"OrganizationGuid":"eaec5a7a-818e-4901-8094-be3e9947b4e5","OrganizationName":"Command and Control CFT","ShortName":"C2 CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"a524a75b-6164-458b-80ee-b86c28cadd82","OrganizationName":"Contested Logistics CFT ","ShortName":"CLFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"d2e77de5-2b4b-466e-aad1-b3f557b35687","OrganizationName":"Cyber CDID","ShortName":"C-CDID","IsOpr":true,"ProponentCode":"Cyber","GapCode":"03","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"f0a8068c-f61b-4269-b6bf-bb85d2a2ffba","OrganizationName":"Cyber Center of Excellence","ShortName":"CCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"53742f86-debd-4880-bc54-7348db9e40d6","OrganizationName":"Cyber Command","ShortName":"CYBERCOM","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"f4263fda-a85f-47fe-8c47-7da5a761b8cd","OrganizationName":"Cyber Theater Information Advantage Detachment","ShortName":"Cyber TIAD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"53742f86-debd-4880-bc54-7348db9e40d6"},{"OrganizationGuid":"6d110399-f359-487d-829d-2dd283a90914","OrganizationName":"Deputy Chief of Staff G-3/5/7","ShortName":"DCoS G-3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"9be557f4-4853-48f8-aa6c-0885cde155f4","OrganizationName":"Deputy Chief of Staff- G1","ShortName":"DCoS-G1","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"83d92df4-b9be-4780-b378-67c7ac1a75ae","OrganizationName":"Deputy Chief of Staff- G8","ShortName":"DCoS-G8","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"615d09e2-6091-46d7-8530-38677f3c8eb7","OrganizationName":"Deputy Chief of Staff-G6","ShortName":"DCoS-G6","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7"},{"OrganizationGuid":"8ccda746-5efb-407c-aef7-f9048d366d1b","OrganizationName":"DEVCOM Analysis Center","ShortName":"DAC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"4f8be144-d40f-4520-905d-fcf5e28a9c13","OrganizationName":"DEVCOM Army Research Labratory","ShortName":"ARL","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"ac4aabc2-ab2b-4778-ab50-de93bb4067e1","OrganizationName":"DEVCOM Aviation \u0026 Missile Center","ShortName":"AvMC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"099bf1c1-0ed4-4842-a6da-064490a717f4","OrganizationName":"DEVCOM Chemical Biological Center","ShortName":"CBC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"301ac328-d33f-434c-ba87-5b6800506ad6","OrganizationName":"DEVCOM Command, Control, Communications, Computers, Cyber, Intelligence, Surveillance and Reconnaissance Center","ShortName":"C5ISRC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"bea30b04-693e-4141-9518-178cf03a636e","OrganizationName":"DEVCOM Ground Vehicle Systems Center","ShortName":"GVSC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a","OrganizationName":"DEVCOM HQ","ShortName":"DEVCOM","IsOpr":true,"ProponentCode":"STRACD","GapCode":"99","ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"08d8a04d-3985-4872-80bf-0ea5dfe9c312","OrganizationName":"DEVCOM Soldier Center","ShortName":"SC","IsOpr":true,"ProponentCode":"PAO","GapCode":"99","ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"ede09f65-93a8-4871-96af-dc6dbbb922c2","OrganizationName":"Directorate Of Concepts","ShortName":"DoC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"80b6edda-db81-42ac-b871-8ccb4ace08a8"},{"OrganizationGuid":"e0ae1f08-98ad-473a-8bed-90ba1bfac4fc","OrganizationName":"Engineer Research and Development Center","ShortName":"ERDC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"7b66058e-3afd-4018-9b66-00af3c90e07a","OrganizationName":"FCC - Other","ShortName":"FCC - Other","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"edb7b359-780e-4683-889d-ac14f7f90c42","OrganizationName":"Fires CDID","ShortName":"F-CDID","IsOpr":true,"ProponentCode":"FIRES","GapCode":"04","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"654c6c12-ac3e-4eb9-970a-4db40a15370e","OrganizationName":"Fires Center of Excellence","ShortName":"FCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"3b99add5-20ba-4ade-8dd6-245c05a2b1c5","OrganizationName":"Future Vertical Lift CFT","ShortName":"FVL CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a","OrganizationName":"Futures and Concepts Center","ShortName":"FCC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"555b21e2-ab9d-446b-bc9c-1f6fc40cbc63","OrganizationName":"Futures and Concepts Center G-3/5/7","ShortName":"FCC G-3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"80b6edda-db81-42ac-b871-8ccb4ace08a8","OrganizationName":"Futures Integration Division","ShortName":"FID","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"c0076d6e-c606-4d9e-ba59-0f33ff509d12","OrganizationName":"G-1","ShortName":"G-1","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"302bddc4-91de-4ef9-82e3-d12f491b7b8a","OrganizationName":"G-4/8","ShortName":"G-4/8","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"732ce29c-7edc-420c-b011-76e32a476126","OrganizationName":"G2","ShortName":"G2","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"4fe068b7-d8bd-4f61-8ff6-2d7284e1b442","OrganizationName":"G3/5/7","ShortName":"G3/5/7","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"125c4be2-5a25-4adc-9aa6-cb3e43a0aca7","OrganizationName":"Headquarters, Department of the Army","ShortName":"HQDA","IsOpr":true,"ProponentCode":"HQDA","GapCode":"99","ParentOrganizationGuid":null},{"OrganizationGuid":"ee3f32e9-292e-4a35-9a1f-a84e6e770521","OrganizationName":"INDOPACOM Theater Information Advantage Detachment","ShortName":"INDOPACOM TIAD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"1f98a656-8724-464b-8f26-59259b37f440"},{"OrganizationGuid":"fd75206d-a105-4083-8314-697bb70636e0","OrganizationName":"Intelligence CDID","ShortName":"I-CDID","IsOpr":true,"ProponentCode":"MI","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"aed516e4-a952-411b-b5fd-35920ea47308","OrganizationName":"Intelligence Center of Excellence","ShortName":"ICoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"daa6d46f-1db9-4ecf-a3f5-b3975f70bbb6","OrganizationName":"JMC Forward","ShortName":"JMC - F","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25"},{"OrganizationGuid":"f1dd4686-435c-4910-85c5-d4b0b72a545d","OrganizationName":"Joint and Multiniational Interoperability","ShortName":null,"IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25"},{"OrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25","OrganizationName":"Joint Modernization Command","ShortName":"JMC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"cb2a109b-0cba-44cf-b18d-cc906c8eda47","OrganizationName":"Long Range Precision Fires CFT","ShortName":"LRPF CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"35be3ac6-78ab-4fc5-b053-bd64c6fe2c65","OrganizationName":"Maneuver CDID","ShortName":"M-CDID","IsOpr":true,"ProponentCode":"MCOE","GapCode":"06","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"b44fbe80-2a99-40d4-81f1-54879ffa2d53","OrganizationName":"Maneuver COE","ShortName":"MCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"17ae2a31-1a53-4031-a591-50698a97c250","OrganizationName":"Maneuver Support CDID","ShortName":"MS-CDID","IsOpr":true,"ProponentCode":"MSCoE","GapCode":"07","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"3f92ab0e-a1e8-44c3-9f21-5fd186ff1938","OrganizationName":"Maneuver Support COE","ShortName":"MSCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"af873155-cbb7-433c-b65f-054d3585ee4a","OrganizationName":"Medical CDID","ShortName":"MED-CDID","IsOpr":true,"ProponentCode":"AMEDD","GapCode":"08","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"34cc4e49-50fe-46a4-8936-867562924047","OrganizationName":"Medical COE","ShortName":"MEDCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"4d79c4f3-581e-499e-a5b3-8dac986fd45a","OrganizationName":"Medical Research and Development Command","ShortName":"MRDC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"40c030d7-e404-4dde-9e01-4fe65e04c0c3"},{"OrganizationGuid":"a5931914-afa1-4c74-aae0-1d3136ba2e9c","OrganizationName":"Mission Command CDID","ShortName":"MC-CDID","IsOpr":true,"ProponentCode":"MC CDID","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"78cfc0cb-883b-467e-b18e-b3e2ba0a4ef1","OrganizationName":"Mission Command COE","ShortName":"MCCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"112ea80d-2cad-4e1e-a052-673ea4e55188","OrganizationName":"Multi Domain Operations Simulation Center","ShortName":"MDOSC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"68aad018-3554-4373-aca7-7c0b51dc0e1a"},{"OrganizationGuid":"49671561-4ce7-4c52-9dfe-ccacafb995ce","OrganizationName":"Multi-Domain Operations Center","ShortName":"MDOC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"facd6c8d-cf51-4213-8533-95a7c09b1f25"},{"OrganizationGuid":"f32904a2-81b1-4478-839c-776272247bbf","OrganizationName":"NET CFT","ShortName":"N-CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"13ba87e2-7e10-4d91-9b1d-8b4461c5d220","OrganizationName":"Network Integration Division (NID)/G6","ShortName":null,"IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"462de215-ade7-4ffe-9386-03f14e1250af","OrganizationName":"Next Generation Combat VehicleCFT","ShortName":"NGCV CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"94df18c7-3f93-400e-9196-a2de00d79315","OrganizationName":"Other","ShortName":"Other","IsOpr":true,"ProponentCode":"","GapCode":"","ParentOrganizationGuid":null},{"OrganizationGuid":"938c021b-5c8b-40d0-8bf0-9c118483eba1","OrganizationName":"Rapid Capabilities and Critical Technologies Office","ShortName":"RCCTO","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"a65293e9-d254-484f-a3e7-c853702df228","OrganizationName":"Soldier Lethality CFT","ShortName":"SL CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"f6d0e947-96eb-4d8e-802b-58dd298d9f10","OrganizationName":"Space and Missile Defense Command CDID","ShortName":"SMDC CDID","IsOpr":true,"ProponentCode":"SMDC","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"2a5fd93d-fc50-f011-9fa5-a01881b906d0","OrganizationName":"Space and Missile Defense Command Technical Center","ShortName":"SMDC TC","IsOpr":true,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f6d0e947-96eb-4d8e-802b-58dd298d9f10"},{"OrganizationGuid":"83fe81a4-d307-47d7-a368-2c5a634ff0d7","OrganizationName":"Special Operations CoE","ShortName":"SOCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"e7b1fdf7-acc9-47a5-a1d9-595e2cdfec5d","OrganizationName":"Sustainment CDID","ShortName":"S-CDID","IsOpr":true,"ProponentCode":"CASCOM/SUST","GapCode":"99","ParentOrganizationGuid":"61110a8d-eb5d-4a16-8e83-f8d8a2c0df2a"},{"OrganizationGuid":"6ba69e20-5a45-432a-b33a-27f010e851e8","OrganizationName":"Sustainment COE","ShortName":"SCoE","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"e8084a86-f7e0-4341-8c12-3d7a9449cb8c","OrganizationName":"Synthetic Training Environment CFT","ShortName":"STE CFT","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245","OrganizationName":"The Research and Analysis Center","ShortName":"TRAC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"0aafc880-27a3-4068-86da-1d92bb7132c5"},{"OrganizationGuid":"b9f375c4-35eb-4609-9697-7cafea51ead2","OrganizationName":"TRAC-Fort Leavenworth","ShortName":"TRAC-FLVN","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"980bee65-8ab7-4211-a816-09eeba185802","OrganizationName":"TRAC-Gregg-Addams","ShortName":"TRAC-GRAD","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"e92fd86d-351c-4766-8198-c8ded4b061c8","OrganizationName":"TRAC-Monterey","ShortName":"TRAC-MTRY","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"c5a2be1e-b81f-419a-8935-8c6b4085f65c","OrganizationName":"TRAC-White Sands Missile Range","ShortName":"TRAC-WSMR","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"f600eb86-d639-4825-ad24-71b6a3200245"},{"OrganizationGuid":"521e7722-87b9-4ec4-8818-f9a67dda0784","OrganizationName":"TRADOC Proponent Office- Echelons above Brigade","ShortName":"TPO-EAB","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":"cae43ded-f3b4-4276-9254-6394d7724ee4"},{"OrganizationGuid":"ba1dbc0d-f0ef-47bb-932a-bd677531f667","OrganizationName":"US Air Force","ShortName":"USAF","IsOpr":true,"ProponentCode":"JOINT","GapCode":"99","ParentOrganizationGuid":null},{"OrganizationGuid":"600fd729-86e6-4313-a59f-90d5689589b9","OrganizationName":"US Army Europe","ShortName":"USAREUR-AF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"80c9fb2f-d15a-4be9-9aad-9bf1dc7b038c","OrganizationName":"US Army Pacific","ShortName":"USARPAC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"f2ce22c9-0328-4822-90fd-8c8e98c05cde","OrganizationName":"US Army Special Operations Command CDID","ShortName":"USASOC CDID","IsOpr":true,"ProponentCode":"USASOC","GapCode":"12","ParentOrganizationGuid":null},{"OrganizationGuid":"c05f2986-177d-48a2-a91f-7653b07bef17","OrganizationName":"US Forces Command","ShortName":"FORSCOM","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"3b28f5c5-7175-4a2c-b34a-53ecb85b837e","OrganizationName":"US Marine Corps","ShortName":"USMC","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"6a014307-b05e-4af6-a232-04d10ced80c4","OrganizationName":"US Navy","ShortName":"USN","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null},{"OrganizationGuid":"aa901092-afcc-4aa0-95c4-ed890a034adb","OrganizationName":"US Space Force","ShortName":"USSF","IsOpr":false,"ProponentCode":null,"GapCode":null,"ParentOrganizationGuid":null}],"key":"OrganizationGuid"})},"columns":[{"dataField":"OrganizationGuid","validationRules":[{"type":"required","message":"The OrganizationGuid field is required."}],"visible":false},{"dataField":"OrganizationName","dataType":"string"}],"headerFilter":{"visible":true},"showBorders":true,"rowAlternationEnabled":true,"hoverStateEnabled":true,"wordWrapEnabled":true,"paging":{"enabled":false},"filterRow":{"visible":true},"height":"345","selection":{"mode":"multiple","showCheckBoxesMode":"always"},"selectedRowKeys":component.option("value"),"onSelectionChanged":function(e) {  FORGE.devExtreme.onMultiSelectionGridChanged(e, component); }},arguments[0])%><%}("dgOcrProponents")%></script>
<div style="position: absolute; right: -900px">
  <div id="gap-category-critical-path-dropdownbox-tooltip">
      <div style="width: 400px; height: 70px; text-align: left" class="d-block text-wrap text-left">
          <span class="fw-bold">
              Gap Category Critical Paths:
          </span>
           Impactful solution ideas within an Army FOE Gap category that best mitigate the gap risk within a concept critical component.  Could include solutions that are quick-turn capabilities that were not included in out concept-driven solutions analysis.
      </div>
  </div>

  <div id="possible-ioc-date-editor-tooltip">
      <div style="width: 400px; height: 120px; text-align: left" class="d-block text-wrap text-left">
          <span class="fw-bold">
              Initial Operational Capability (IOC) is reached when a capability is available in its minimum, usefully deployable form.
          </span>
          This typically occurs when some designated <span class="fw-bold">BCT(s) and/or division enabler units(s)</span> have received the system
          and can operate and maintain it.  The system's Initial Capabilities Document (ICD) first specifies the IOC date while
          the system's Capability Development Document (CDD) and its updates specify IOC criteria
      </div>
  </div>
</div>


<div class="d-flex justify-content-end mt-3">
    <div class="me-3">
        <div id="save-btn"></div><script>
DevExpress.utils.readyCallbacks.add((function($){$("#save-btn").dxButton({"text":"Save","type":"default","stylingMode":"contained","width":120,"visible":true,"icon":"fa-duotone fa-pen","onClick":FORGE.Pathfinder.SolutionIdeas.saveNewSolutionIdea});}).bind(this, jQuery));</script>
    </div>
    <div class="me-0">
        <div id="cancel-btn"></div><script>
DevExpress.utils.readyCallbacks.add((function($){$("#cancel-btn").dxButton({"text":"Close/Cancel","type":"normal","stylingMode":"outlined","width":120,"onClick":FORGE.Pathfinder.SolutionIdeas.hideSolutionIdeaPopup});}).bind(this, jQuery));</script>
    </div>
</div>'''
    return JSONResponse(
        content=response,
        headers={"Content-Type": "text/html; charset=utf-8"}
    )

@app.post('/api/pathfinder/SolutionIdeas', tags=['PathfinderApi'])
async def post_api_pathfinder_SolutionIdeas(body: SolutionIdeaDto) -> dict:
    """
    Creates a new solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {"status": "created"}
@app.get('/api/pathfinder/SolutionIdeas/{solutionIdeaId}', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionIdeas(solutionIdeaId: str) -> dict:
    """
    Returns a Solution Idea by ID.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/pathfinder/SolutionIdeas/{solutionIdeaId}', tags=['PathfinderApi'])
async def delete_api_pathfinder_SolutionIdeas(solutionIdeaId: str) -> dict:
    """
    Deletes a solution idea
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/pathfinder/SolutionSetCrcs', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionSetCrcs(solutionsetid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    List mapped CRCs for a solution set
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/pathfinder/SolutionSets', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionSets(loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns all non-deleted Solution Sets.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.post('/api/pathfinder/SolutionSets', tags=['PathfinderApi'])
async def post_api_pathfinder_SolutionSets(body: SolutionSetDto) -> dict:
    """
    Creates a new solution set
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return body
@app.delete('/api/pathfinder/SolutionSets/{solutionSetId}', tags=['PathfinderApi'])
async def delete_api_pathfinder_SolutionSets(solutionSetId: str) -> dict:
    """
    Deletes a solution set
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.get('/api/pathfinder/SolutionSetSolutionIdeas', tags=['PathfinderApi'])
async def get_api_pathfinder_SolutionSetSolutionIdeas(solutionsetid: Optional[str] = None, loadoptions: Optional[DataSourceLoadOptions] = None) -> dict:
    """
    Returns all non-deleted solution ideas mapped to a solution set.
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}

@app.delete('/api/pathfinder/SolutionSetSolutionIdeas', tags=['PathfinderApi'])
async def delete_api_pathfinder_SolutionSetSolutionIdeas(mappingid: Optional[str] = None) -> dict:
    """
    Removes a solution idea that was mapped to a solution set
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {'status': 'deleted'}
@app.post('/api/pathfinder/SolutionSetSolutionIdeas/{solutionSetId}', tags=['PathfinderApi'])
async def post_api_pathfinder_SolutionSetSolutionIdeas(solutionSetId: str, solutionideaid: Optional[str] = None) -> dict:
    """
    Links a solution idea to a solution set
    
    Tags: PathfinderApi
    """
    # TODO: Implement endpoint logic
    return {}
@app.get('/api/requirements/documentsearch', tags=['RequirementsApi'])
async def get_api_requirements_documentsearch(searchterm: Optional[str] = None, indexname: Optional[str] = None, sortorder: Optional[DocumentSearchSortOrder] = None, filters: Optional[str] = None) -> dict:
    """
    Search the blob storage files for the search term in the requirements search index
    
    Tags: RequirementsApi
    """
    # TODO: Implement endpoint logic
    return {}


















if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8042)