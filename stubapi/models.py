from typing import Optional
from pydantic import BaseModel, Field

from enum import IntEnum


class ActivityApprovalStatusDto(BaseModel):
    Id: Optional[int] = None
    WorkflowStepId: int


class ActivityInitialInsightsDto(BaseModel):
    ExpId: Optional[int] = None
    InitialInsight: Optional[str] = None


class ActivityNotesDto(BaseModel):
    ExpId: Optional[int] = None
    Notes: Optional[str] = None


class ActivityPlanningTimelineDto(BaseModel):
    MilestoneId: Optional[int] = None
    ActivityId: Optional[int] = None
    Name: Optional[str] = None
    PlannedStartDate: Optional[str] = None
    PlannedEndDate: Optional[str] = None
    ApprovalAuthority: Optional[str] = None
    Status: Optional[str] = None


class ActivityRecommendationsDto(BaseModel):
    RecommendationId: Optional[str] = None
    ExpId: Optional[int] = None
    Recommendations: Optional[str] = None
    RecommendationDomains: Optional[list] = None
    RecommendationDomainsGridStr: Optional[str] = None
    CreatedDate: Optional[str] = None
    CreatedBy: Optional[str] = None


class AssessmentAccessRequestDto(BaseModel):
    AccessRequestId: Optional[int] = None
    UserID: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[str] = None
    Id: Optional[int] = None
    AssessmentTitle: Optional[str] = None
    RoleName: Optional[str] = None
    RoleId: Optional[int] = None
    WorkflowStateId: Optional[int] = None
    WorkflowStepId: Optional[int] = None
    WorkflowStepName: Optional[str] = None
    CreatedDate: Optional[str] = None
    CreatedByName: Optional[str] = None
    CreatedById: Optional[str] = None


class AssessmentClaDto(BaseModel):
    ClaId: Optional[int] = None
    AssessmentId: Optional[int] = None
    Type: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreatedDate: Optional[str] = None
    ModifiedBy: Optional[str] = None
    ModifiedDate: Optional[str] = None


class AssessmentGapRsaDto(BaseModel):
    GapCodeId: Optional[str] = None
    GapCode: Optional[str] = None
    GapShortName: Optional[str] = None
    RsaId: Optional[int] = None
    RiskMitigationLevelId: Optional[str] = None
    RiskMitigationLevel: Optional[str] = None
    RiskMitigationLevelNbr: Optional[int] = None
    CreatedDate: Optional[str] = None
    ModifiedDate: Optional[str] = None
    WorkflowStepId: Optional[int] = None
    WorkflowStepName: Optional[str] = None
    ApprovedByAfc: Optional[bool] = None


class AssessmentGeneralInformationDto(BaseModel):
    Id: Optional[int] = None
    Title: Optional[str] = None
    Guidance: Optional[str] = None
    StudyObjective: Optional[str] = None
    ExecutiveSummary: Optional[str] = None
    Scope: Optional[str] = None
    Proponent: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None


class AssessmentTcbaProjectCreateDto(BaseModel):
    AssessmentTypeId: Optional[int] = None
    Title: Optional[str] = None
    Guidance: Optional[str] = None
    StudyObjective: Optional[str] = None
    ExecutiveSummary: Optional[str] = None
    Scope: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None


class ClaDto(BaseModel):
    ClaId: Optional[int] = None
    ConceptId: Optional[int] = None
    Type: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    isCritical: Optional[bool] = None


class CommentDto(BaseModel):
    Id: Optional[int] = None
    ConceptId: Optional[int] = None
    CreatedBy: Optional[str] = None
    CreatedDate: Optional[str] = None
    Text: Optional[str] = None
    IsCritical: Optional[bool] = None


class ConceptCommandPostDto(BaseModel):
    CommandPostId: Optional[int] = None
    CommandPostSizeId: Optional[str] = None
    CommandPostTypeId: Optional[str] = None
    Quantity: Optional[int] = None
    ConceptId: Optional[int] = None
    CreatedDate: Optional[str] = None


class ConceptEnablerDto(BaseModel):
    EnablerId: Optional[int] = None
    ConceptId: Optional[int] = None
    EnablerText: Optional[str] = None
    CreatedDate: Optional[str] = None


class ConceptEquipCapabilityChangesDto(BaseModel):
    EquipmentChangeId: Optional[int] = None
    ConceptId: Optional[int] = None
    EquipmentChangeDescription: Optional[str] = None
    CreatedDate: Optional[str] = None


class ConceptEquipmentMappingDto(BaseModel):
    MappingId: Optional[int] = None
    ConceptId: Optional[int] = None
    EquipmentId: Optional[int] = None
    Quantity: Optional[int] = None
    IsCritical: Optional[bool] = None


class ConceptGeneralInformationDto(BaseModel):
    Id: Optional[int] = None
    Name: str = Field(min_length=1)
    DiscoverabilityGuid: str
    StatusId: str
    StatusDescription: Optional[str] = None
    AocYear: int
    AocYearString: Optional[str] = None
    LearningYear: Optional[int] = None
    LearningYearString: Optional[str] = None
    TypeGuid: str
    LeadOrganizationId: str
    AdditionalLeadOrganizations: Optional[list] = None
    SupportingOrganizationId: Optional[str] = None
    AdditionalSupportingOrganizations: Optional[list] = None
    FormationIds: Optional[list] = None
    OrganizationDescription: Optional[str] = None
    OperationalChanges: Optional[str] = None
    Mission: Optional[str] = None
    Hypothesis: Optional[str] = None
    Purpose: Optional[str] = None
    Scope: Optional[str] = None
    Image: Optional[str] = None
    ModifiedDate: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    CreatorName: Optional[str] = None
    CreatorEmail: Optional[str] = None
    CreatorPhone: Optional[str] = None
    PocId: str
    PocName: Optional[str] = None
    PocEmail: Optional[str] = None
    PocPhone: Optional[str] = None
    OrganizationSize: Optional[int] = None
    ConceptNotionTypeId: Optional[str] = None
    ShortTitle: Optional[str] = None
    IsFcw: Optional[bool] = None


class ConceptLearningEventMappingDto(BaseModel):
    MappingId: Optional[int] = None
    ConceptId: Optional[int] = None
    ExpGuid: Optional[str] = None
    ExpId: Optional[int] = None
    IsCritical: Optional[bool] = None


class ConceptLitLibraryDocumentsDto(BaseModel):
    MappingId: Optional[int] = None
    ConceptId: Optional[int] = None
    LitLibraryId: Optional[int] = None
    Title: Optional[str] = None
    SectionName: Optional[str] = None
    Relevance: Optional[str] = None
    IsCritical: Optional[bool] = None


class ConceptMeasurementDto(BaseModel):
    MappingId: Optional[int] = None
    ConceptId: Optional[int] = None
    MeasurementId: Optional[int] = None
    MeasureId: Optional[int] = None
    MeasureName: Optional[str] = None
    MeasureCategoryId: Optional[int] = None
    MeasureCategoryName: Optional[str] = None
    MeasurementTypeId: Optional[int] = None
    Value: Optional[str] = None
    IsCritical: Optional[bool] = None


class ConceptNotionDto(BaseModel):
    ConceptNotionId: Optional[int] = None
    ConceptNotionName: Optional[str] = None


class ConceptScenarioMappingDto(BaseModel):
    MappingId: Optional[int] = None
    ConceptId: Optional[int] = None
    ScenarioId: Optional[str] = None
    IsCritical: Optional[bool] = None


class ConceptScienceTechMappingDto(BaseModel):
    MappingId: Optional[int] = None
    SntId: Optional[int] = None
    Description: Optional[str] = None
    TechShortName: Optional[str] = None
    TechLongName: Optional[str] = None
    TechDescription: Optional[str] = None
    TechSource: Optional[str] = None
    TechImpact: Optional[str] = None
    CategoryId: Optional[int] = None
    CategoryName: Optional[str] = None
    IsCritical: Optional[bool] = None


class ConceptTaskMappingDto(BaseModel):
    MappingId: Optional[int] = None
    ConceptId: Optional[int] = None
    TaskId: Optional[int] = None
    TaskNumber: Optional[str] = None
    TaskName: Optional[str] = None
    TaskDescription: Optional[str] = None
    TaskType: Optional[str] = None
    IsOnFcw: Optional[bool] = None
    IsCritical: Optional[bool] = None


class CrcMappingDto(BaseModel):
    MappingId: Optional[int] = None
    MappedEntityId: Optional[int] = None
    ConceptId: Optional[int] = None
    ConceptName: Optional[str] = None
    RcId: Optional[int] = None
    RcShortName: Optional[str] = None
    ProponentId: Optional[str] = None
    ProponentName: Optional[str] = None
    WorkflowStepId: Optional[int] = None
    DateSubmitted: Optional[str] = None
    DateModified: Optional[str] = None
    FileId: Optional[int] = None
    DownloadLink: Optional[str] = None
    IsApproved: Optional[bool] = None


class CrcSolutionSetMappingDto(BaseModel):
    RcId: Optional[int] = None
    RcName: Optional[str] = None
    SolutionSetId: Optional[str] = None
    SolutionSetName: Optional[str] = None
    SolutionSetDescription: Optional[str] = None
    SolutionSetMappingId: Optional[str] = None
    MaxIocDate: Optional[str] = None
    NoLaterDate: Optional[str] = None
    ConceptNotionName: Optional[str] = None


class DataGridChangeDto(BaseModel):
    Key: Optional[str] = None
    Type: Optional[str] = None
    Data: Optional[str] = None
    Values: Optional[list] = None


class DataSourceLoadOptions(BaseModel):
    RequireTotalCount: Optional[bool] = None
    RequireGroupCount: Optional[bool] = None
    IsCountQuery: Optional[bool] = None
    IsSummaryQuery: Optional[bool] = None
    Skip: Optional[int] = None
    Take: Optional[int] = None
    Sort: Optional[list] = None
    Group: Optional[list] = None
    Filter: Optional[list] = None
    TotalSummary: Optional[list] = None
    GroupSummary: Optional[list] = None
    Select: Optional[list] = None
    PreSelect: Optional[list] = None
    RemoteSelect: Optional[bool] = None
    RemoteGrouping: Optional[bool] = None
    ExpandLinqSumType: Optional[bool] = None
    PrimaryKey: Optional[list] = None
    DefaultSort: Optional[str] = None
    StringToLower: Optional[bool] = None
    PaginateViaPrimaryKey: Optional[bool] = None
    SortByPrimaryKey: Optional[bool] = None
    AllowAsyncOverSync: Optional[bool] = None


class DiscriminatorDto(BaseModel):
    Description: Optional[str] = None
    Scale: Optional[int] = None
    Weight: Optional[int] = None


class DocumentSearchSortOrder(IntEnum):
    Relevance = 0
    Newest = 1
    Oldest = 2


class DynamicTableColumnDto(BaseModel):
    dataField: Optional[str] = None
    caption: Optional[str] = None
    dataType: Optional[str] = None
    allowEditing: Optional[bool] = None
    width: Optional[str] = None
    format: Optional[str] = None
    alignment: Optional[str] = None
    visible: Optional[bool] = None
    encodeHtml: Optional[bool] = None
    lookup: Optional[str] = None
    filterValues: Optional[list] = None


class DynamicTableColumnLookupDto(BaseModel):
    dataSource: Optional[str] = None
    valueExpr: Optional[str] = None
    displayExpr: Optional[str] = None


class DynamicTableDto(BaseModel):
    tableName: Optional[str] = None
    dataSource: Optional[str] = None
    keyExpr: Optional[str] = None
    columns: Optional[list] = None
    editing: Optional[str] = None


class DynamicTableEditingOptionsDto(BaseModel):
    allowUpdating: Optional[bool] = None
    allowAdding: Optional[bool] = None
    allowDeleting: Optional[bool] = None


class EeaDto(BaseModel):
    LdParentId: Optional[int] = None
    LdParentGuid: Optional[str] = None
    EeaId: Optional[int] = None
    EeaText: Optional[str] = None


class ForgeFileDto(BaseModel):
    Id: Optional[int] = None
    FileName: Optional[str] = None
    Path: Optional[str] = None
    Type: Optional[str] = None


class GapDraftDto(BaseModel):
    AssessmentId: Optional[int] = None
    AssessmentName: Optional[str] = None
    GapId: Optional[str] = None
    GapNumber: Optional[int] = None
    GapCodeId: Optional[str] = None
    GapCode: Optional[str] = None
    FormationDescription: Optional[str] = None
    FailedTaskDescription: Optional[str] = None
    Conditions: Optional[str] = None
    Standards: Optional[str] = None
    GapAssessments: list
    GapAssessmentNames: Optional[list] = None
    GapAssessmentNamesFormatted: Optional[str] = None
    SourceName: Optional[str] = None
    OprProponentId: Optional[str] = None
    OprProponentName: Optional[str] = None
    ForceMgmtOrgTypeId: Optional[str] = None
    ForceMgmtOrgTypeName: Optional[str] = None
    Crcs: Optional[list] = None
    CrcIds: Optional[list] = None
    CrcNames: Optional[str] = None
    GeographicalAorId: Optional[str] = None
    GeographicalAorName: Optional[str] = None
    JcaId: Optional[str] = None
    JcaName: Optional[str] = None
    OriginalGapCodeId: Optional[str] = None
    OriginalGapCode: Optional[str] = None
    IsOriginalGap: Optional[bool] = None
    ConceptLookupId: Optional[str] = None
    SeriesId: Optional[str] = None
    IterationNbr: Optional[int] = None
    WorkflowStepId: Optional[int] = None


class GapWorkflowStep(IntEnum):
    Draft = 1
    Approved = 3
    GapArchived = 11
    DraftStaffing = 28
    CdidApproved = 30


class GapWorksheetDto(BaseModel):
    AssessmentId: Optional[int] = None
    AssessmentName: Optional[str] = None
    GapId: Optional[str] = None
    GapNumber: Optional[int] = None
    GapCodeId: Optional[str] = None
    GapCode: Optional[str] = None
    FailedTaskDescription: str = Field(min_length=1)
    ForceMgmtOrgTypeId: str
    ForceMgmtOrgTypeName: Optional[str] = None
    CrcIds: Optional[list] = None
    CrcNames: Optional[str] = None
    JcaId: str
    JcaName: Optional[str] = None
    OprProponentId: str
    OprProponentGapCode: Optional[str] = None
    OcrProponentIds: Optional[list] = None
    HasOcrProponents: Optional[bool] = None
    ConceptLookupId: str
    ConceptLookupCode: Optional[str] = None
    ConceptNotion: Optional[str] = None
    ClassificationId: str
    GeographicalAorId: str
    GeographicalAorCode: Optional[str] = None
    GeographicalAorName: Optional[str] = None
    FormationDescription: str = Field(min_length=1)
    Conditions: str = Field(min_length=1)
    Standards: str = Field(min_length=1)
    SeriesId: str
    SeriesCode: Optional[str] = None
    GapAssessments: list
    SourceName: Optional[str] = None
    TypeId: str
    TypeName: Optional[str] = None
    Tier1CategoryId: str
    Tier1CategoryPriorityNumber: Optional[str] = None
    ImpactStatement: str = Field(min_length=1)
    ShortTitle: str = Field(min_length=1)
    Ov1File: Optional[str] = None
    OriginalGapCodeId: Optional[str] = None
    OriginalGapCode: Optional[str] = None
    IsOriginalGap: Optional[bool] = None
    IterationNbr: Optional[int] = None
    JtfRiskMatrixId: Optional[str] = None
    JtfLikelihoodNumber: int
    JtfConsequenceNumber: int
    JtfRiskLevelJustification: str = Field(min_length=1)
    ProponentRiskMatrixId: Optional[str] = None
    ProponentLikelihoodNumber: int
    ProponentConsequenceNumber: int
    ProponentRiskLevelJustification: str = Field(min_length=1)
    GapNarrative: str = Field(min_length=1)
    GapStatement: str = Field(min_length=1)
    GapBinNarrative: str = Field(min_length=1)
    ModifiedByUser: Optional[str] = None
    ModifiedDate: Optional[str] = None
    WorkflowStepId: Optional[int] = None
    WorkflowStep: Optional[str] = None


class GroupingInfo(BaseModel):
    Selector: Optional[str] = None
    Desc: Optional[bool] = None
    GroupInterval: Optional[str] = None
    IsExpanded: Optional[bool] = None


class GuidLookupDto(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Order: Optional[int] = None
    Deleted: Optional[bool] = None


class Int32FileMetadataDto(BaseModel):
    FileId: Optional[int] = None
    ModuleId: Optional[int] = None
    MappingId: Optional[int] = None
    FileName: Optional[str] = None
    FilePath: Optional[str] = None
    Type: Optional[str] = None
    Status: Optional[str] = None
    SourceType: Optional[str] = None
    Version: Optional[str] = None
    ForgeFileTypeId: Optional[int] = None


class InterdependenciesDto(BaseModel):
    InterdependencyId: Optional[int] = None
    ConceptId: Optional[int] = None
    Type: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    IsCritical: Optional[bool] = None
    SubTypeId: Optional[int] = None


class LdResponseMappingDto(BaseModel):
    MappingGuid: Optional[str] = None
    ActivityId: Optional[int] = None
    LdTitle: Optional[str] = None
    Response: Optional[str] = None
    ResponseId: Optional[int] = None
    ResponseGuid: Optional[str] = None
    LearningDemandId: Optional[int] = None
    CreatedBy: Optional[str] = None
    CreatedDate: Optional[str] = None
    DeleteCode: Optional[bool] = None
    IsPriority: Optional[bool] = None


class LdResponsesReviewDto(BaseModel):
    ActivityHasPriorityLdResponse: Optional[bool] = None
    ActivityId: Optional[int] = None
    ReviewedLdResponses: Optional[bool] = None
    LdResponsesReviewComments: Optional[str] = None
    ReviewerName: Optional[str] = None


class LearningActivityDocumentFileDto(BaseModel):
    id: Optional[int] = None
    execSum: Optional[bool] = None
    finalReport: Optional[bool] = None
    execSumComments: Optional[str] = None
    finalReportComments: Optional[str] = None


class LearningActivityDto(BaseModel):
    Id: Optional[int] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    LastModified: Optional[str] = None
    ActivityType: Optional[str] = None
    LeadOrganization: Optional[str] = None
    LeadOrganizationGuid: Optional[str] = None
    QaqcFollowing: Optional[bool] = None
    PocName: Optional[str] = None
    PocEmail: Optional[str] = None
    PocPhone: Optional[str] = None
    FyId: Optional[int] = None
    ClassificationId: Optional[str] = None
    EventTypeId: Optional[str] = None
    Timeframe: Optional[str] = None
    WorkflowStepId: Optional[int] = None
    ActivityGuid: Optional[str] = None
    LearningDemands: Optional[list] = None
    CanEdit: Optional[bool] = None


class LearningActivityGeneralInformationDto(BaseModel):
    Id: Optional[int] = None
    Title: str = Field(min_length=1)
    Description: str = Field(min_length=1)
    ConceptRequiredCapabilities: Optional[list] = None
    VenueId: Optional[str] = None
    VenueName: Optional[str] = None
    LeadOrganizationId: str
    LeadOrganizationName: Optional[str] = None
    SupportingOrganizations: Optional[str] = None
    InitialInsights: Optional[str] = None
    Notes: Optional[str] = None
    PocId: Optional[str] = None
    PocName: Optional[str] = None
    PocEmail: Optional[str] = None
    PocPhone: Optional[str] = None
    FyId: Optional[str] = None
    EstStartDate: str
    EstStartDateFormatted: Optional[str] = None
    EstEndDate: str
    EstEndDateFormatted: Optional[str] = None
    ClassificationId: Optional[str] = None
    EventTypeId: str
    EventTypeName: Optional[str] = None
    Timeframe: str = Field(min_length=1)
    ExpectedOutcomes: Optional[str] = None
    Status: Optional[str] = None
    WorkflowStepId: Optional[int] = None
    EquipmentResourcesNeeded: Optional[bool] = None
    PersonnelResourcesNeeded: Optional[bool] = None
    RomCosts: Optional[float] = None


class LearningDemandDto(BaseModel):
    Id: Optional[int] = None
    Title: Optional[str] = None
    Tdds: Optional[list] = None
    TddLinks: Optional[str] = None
    Crcs: Optional[list] = None
    CrcLinks: Optional[str] = None
    Events: Optional[list] = None
    EventLinks: Optional[str] = None
    OrganizationGuid: Optional[str] = None
    OrganizationName: Optional[str] = None
    IsEditable: Optional[bool] = None
    WorkflowCurrentStepId: Optional[int] = None
    LearningDemandCatalogStatus: Optional[str] = None
    ShortName: Optional[str] = None
    CreationDate: Optional[str] = None
    WorkFlowModifiedDate: Optional[str] = None
    LdClosureDate: Optional[str] = None
    FinalAnswer: Optional[str] = None
    PocId: Optional[str] = None
    PocName: Optional[str] = None
    PocEmail: Optional[str] = None
    PocPhone: Optional[str] = None
    IsInUse: Optional[bool] = None
    IsFccG357: Optional[bool] = None
    IsPriority: Optional[bool] = None


class LearningDemandEeaMappingDto(BaseModel):
    MappingId: Optional[int] = None
    LdId: Optional[int] = None
    EeaId: Optional[int] = None
    EeaText: Optional[str] = None


class LearningDemandGenInfoDto(BaseModel):
    Id: Optional[int] = None
    Title: Optional[str] = None
    ShortTitle: Optional[str] = None
    OrgGuid: Optional[str] = None
    LdClosureWorkflowStepName: Optional[str] = None
    IsLdStatusArchived: Optional[bool] = None
    IsPriority: Optional[bool] = None
    IsLdInUse: Optional[bool] = None
    ModifiedDate: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    CreatorName: Optional[str] = None
    CreatorEmail: Optional[str] = None
    CreatorPhone: Optional[str] = None
    PocId: Optional[str] = None
    PocName: Optional[str] = None
    PocEmail: Optional[str] = None
    PocPhone: Optional[str] = None


class LearningDemandRequiredCapabilityDto(BaseModel):
    RcId: Optional[int] = None
    ConceptId: Optional[int] = None
    RcShortName: Optional[str] = None
    Statement: Optional[str] = None
    Comment: Optional[str] = None
    Who: Optional[str] = None
    CreatedDate: Optional[str] = None
    ModifiedDate: Optional[str] = None
    ProponentId: Optional[str] = None
    ProponentName: Optional[str] = None
    WorkflowStepId: Optional[int] = None


class LearningDemandTddDto(BaseModel):
    Id: Optional[int] = None
    ModifiedDate: Optional[str] = None
    ModifiedDateFormatted: Optional[str] = None
    TddType: Optional[str] = None
    TddText: Optional[str] = None
    TddDueDate: Optional[str] = None
    TddDueDateFormatted: Optional[str] = None
    ActionPoc: Optional[str] = None
    DeleteCode: Optional[bool] = None


class LearningEventDto(BaseModel):
    ExpGuid: Optional[str] = None
    ExpId: Optional[int] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[str] = None


class LearningTddType(IntEnum):
    Task = 1
    Deliverable = 2
    Decision = 3


class MeasureCategoryDto(BaseModel):
    CategoryId: Optional[int] = None
    Name: Optional[str] = None


class MeasureDto(BaseModel):
    MeasureId: Optional[int] = None
    MeasureName: str = Field(min_length=1)
    MeasureCategoryId: int
    MeasureCategoryName: Optional[str] = None


class MilestoneDto(BaseModel):
    MilestoneId: Optional[str] = None
    SolutionIdeaId: Optional[str] = None
    SolutionIdeaDomainId: Optional[str] = None
    SolutionIdeaOprOrgId: Optional[str] = None
    Title: Optional[str] = None
    Notes: Optional[str] = None
    TypeId: Optional[str] = None
    TypeName: Optional[str] = None
    ParentMilestoneId: Optional[str] = None
    WffIds: Optional[list] = None
    TargetDateId: Optional[str] = None
    TargetDateQuarter: Optional[int] = None
    TargetDateYear: Optional[int] = None
    TargetDateName: Optional[str] = None
    Poms: Optional[list] = None
    TimelineId: Optional[str] = None
    CurrentStepId: Optional[int] = None
    IsCompleted: Optional[bool] = None


class MilestoneTemplateDto(BaseModel):
    Id: Optional[str] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    MilestoneName: Optional[str] = None
    YearCount: Optional[int] = None


class ModernizationImpactDto(BaseModel):
    Id: Optional[int] = None
    ConceptId: Optional[int] = None
    DomainId: Optional[str] = None
    DomainText: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    IsCritical: Optional[bool] = None


class MyProfileDto(BaseModel):
    Id: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    RankId: Optional[str] = None
    GradeCode: Optional[str] = None
    OrganizationGuid: Optional[str] = None
    OrganizationName: Optional[str] = None
    NiprEmail: Optional[str] = None
    SiprEmail: Optional[str] = None
    CommercialPhone: Optional[str] = None
    AddressOne: Optional[str] = None
    AddressCity: Optional[str] = None
    AddressState: Optional[str] = None
    AddressZip: Optional[str] = Field(min_length=0, max_length=10)


class ReferenceTable(IntEnum):
    Invalid = 0
    FeasibilityMatrix = 1
    IntegrationReadinessLevel = 2
    ManufacturingReadinessLevel = 3
    MitigationExtent = 4
    TechnologyReadinessLevel = 5
    Tier1GapCategories = 6


class RequiredCapabilitiesDto(BaseModel):
    RcId: Optional[int] = None
    ConceptId: Optional[int] = None
    ConceptName: Optional[str] = None
    ConceptUrl: Optional[str] = None
    RcShortName: Optional[str] = None
    Statement: Optional[str] = None
    Comment: Optional[str] = None
    CreatedDate: Optional[str] = None
    ModifiedDate: Optional[str] = None
    OrganizationId: Optional[str] = None
    OrganizationName: Optional[str] = None
    AssociatedFileId: Optional[int] = None
    AssociatedFileName: Optional[str] = None
    WorkflowStepId: Optional[int] = None
    WorkflowStepName: Optional[str] = None
    IsApproved: Optional[bool] = None
    OtherDependencies: Optional[str] = None
    CrcWorkflowLink: Optional[str] = None
    ConceptNotions: Optional[list] = None


class ResourcesNewViewDto(BaseModel):
    Id: Optional[str] = None
    ExpId: Optional[int] = None
    SourceCategory: Optional[str] = None
    EquipmentNomenclature: Optional[str] = None
    EquipModel: Optional[str] = None
    Position: Optional[str] = None
    Rank: Optional[str] = None
    Mos: Optional[str] = None
    DutyDescription: Optional[str] = None
    Source: Optional[str] = None
    RequestedNumber: Optional[int] = None
    Rom: Optional[int] = None
    Location: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    Comments: Optional[str] = None


class RoleDto(BaseModel):
    Id: Optional[int] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    AuthorizationSystemId: Optional[int] = None
    AuthorizationSystemName: Optional[str] = None
    LinkedRightIds: Optional[list] = None


class RsaSolutionIdeaDto(BaseModel):
    MappingId: Optional[str] = None
    RsaId: Optional[int] = None
    SolutionIdeaId: Optional[str] = None
    GapCodeId: Optional[str] = None
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Domain: Optional[str] = None
    OprProponent: Optional[str] = None
    Comments: Optional[str] = None
    TechnicalRisk: Optional[str] = None
    Supportability: Optional[str] = None
    Affordability: Optional[str] = None
    Availability: Optional[str] = None
    ApprovedToRsa: Optional[bool] = None
    StudyLead: Optional[str] = None
    StudyLeadComment: Optional[str] = None
    MitigationExtentId: Optional[str] = None
    MitigationExtent: Optional[str] = None
    MitigationExtentOrderNbr: Optional[int] = None
    CdidSolutionPriority: Optional[int] = None
    TechnicalReadinessLevel: Optional[str] = None
    FeasibilityDegree: Optional[str] = None
    MappedGaps: Optional[list] = None
    MappedGapNames: Optional[str] = None


class ScienceTechnologyDto(BaseModel):
    SntId: Optional[int] = None
    ShortName: str = Field(min_length=1)
    LongName: str = Field(min_length=1)
    TechDescription: Optional[str] = None
    TechImpact: Optional[str] = None
    TechSource: Optional[str] = None
    TechnicalReadinessLevelId: Optional[str] = None
    TechnicalReadinessLevelName: Optional[str] = None
    ProponentId: Optional[str] = None
    CategoryId: Optional[int] = None
    CategoryName: Optional[str] = None
    RelatedFiles: Optional[list] = None


class SecureNetwork(IntEnum):
    NIPR = 0
    SIPR = 1


class SolutionIdeaAcquisitionDto(BaseModel):
    SolutionIdeaId: Optional[str] = None
    CardsNumber: Optional[str] = None
    AcquisitionOprProponentId: Optional[str] = None
    ExportabilityPlanningId: Optional[str] = None
    AcatLevelId: Optional[str] = None
    CompletedEntryGate: Optional[bool] = None
    FdwNumber: Optional[str] = None


class SolutionIdeaDto(BaseModel):
    SolutionIdeaId: Optional[str] = None
    GeneralInformation: Optional[str] = None
    ReadinessLevels: Optional[str] = None
    Feasibility: Optional[str] = None
    AcquisitionInformation: Optional[str] = None
    Poc: Optional[str] = None
    ModifiedByUser: Optional[str] = None
    Comments: Optional[str] = None
    SeniorLeaderOverrideNbr: Optional[int] = None
    SeniorLeaderOverrideJustification: Optional[str] = None
    SourceSystem: Optional[str] = None
    ModifiedDate: Optional[str] = None
    MilestoneTemplates: Optional[list] = None


class SolutionIdeaFeasibilityDto(BaseModel):
    SolutionIdeaId: Optional[str] = None
    TechnicalRiskId: Optional[str] = None
    SupportabilityId: Optional[str] = None
    AffordabilityId: Optional[str] = None
    AvailabilityTimeFrameId: Optional[str] = None
    FeasibilityId: Optional[str] = None


class SolutionIdeaGeneralInformationDto(BaseModel):
    SolutionIdeaId: Optional[str] = None
    ShortName: str = Field(min_length=1)
    Description: str = Field(min_length=1)
    DomainId: str
    FcwConceptId: Optional[int] = None
    CrcEchelonIds: Optional[list] = None
    PossibleIocDate: str
    IsSnt: Optional[bool] = None
    CriticalPath: Optional[bool] = None
    GapCategoryIds: Optional[list] = None
    OcrProponentIds: Optional[list] = None
    OrgGuid: str
    WorkflowStepId: Optional[int] = None


class SolutionIdeaPocDto(BaseModel):
    SolutionIdeaId: Optional[str] = None
    PocId: Optional[str] = None
    PocName: Optional[str] = None
    PocEmail: Optional[str] = None
    PocPhone: Optional[str] = None


class SolutionIdeaPriorityDto(BaseModel):
    GapRisk: Optional[str] = None
    SolutionIdeaFeasibility: Optional[str] = None
    GapTier1Category: Optional[str] = None
    RsaAvailability: Optional[str] = None
    GapRiskMitigation: Optional[str] = None
    GapBonus: Optional[str] = None
    SeniorLeaderOverride: Optional[str] = None


class SolutionIdeaReadinessDto(BaseModel):
    SolutionIdeaId: Optional[str] = None
    TechnologyReadinessLevelId: Optional[str] = None
    IntegrationReadinessLevelId: Optional[str] = None
    ManufacturingReadinessLevelId: Optional[str] = None


class SolutionPriorityAlgorithm(IntEnum):
    MostRecentApprovedRsas = 0
    MostRecentPendingRsas = 1


class SolutionReviewGridDto(BaseModel):
    RsaId: Optional[int] = None
    IsApproved: Optional[bool] = None
    GapCodeId: Optional[str] = None
    GapCode: Optional[str] = None
    TrackNum: Optional[int] = None
    GapRisk: Optional[int] = None
    GapShortName: Optional[str] = None
    GapPriorityLevel: Optional[int] = None
    Tier1GapCategoryName: Optional[str] = None
    ConceptNotion: Optional[str] = None
    ProponentId: Optional[str] = None
    FailedTask: Optional[str] = None
    CollectiveRsaRrlId: Optional[str] = None
    CollectiveRsaRrlNbr: Optional[int] = None
    CreatedDate: Optional[str] = None


class SolutionSetDto(BaseModel):
    SolutionSetId: Optional[str] = None
    SolutionSetName: Optional[str] = None
    SolutionSetDescription: Optional[str] = None
    Crcs: Optional[list] = None
    CrcNames: Optional[str] = None
    ModifiedDate: Optional[str] = None
    SolutionIdeaCount: Optional[int] = None
    ConceptNotionId: Optional[str] = None


class SortingInfo(BaseModel):
    Selector: Optional[str] = None
    Desc: Optional[bool] = None


class SummaryInfo(BaseModel):
    Selector: Optional[str] = None
    SummaryType: Optional[str] = None


class TaskMappingCreateUserDefinedDto(BaseModel):
    TaskId: Optional[int] = None
    TaskNumber: Optional[str] = None
    TaskName: Optional[str] = None
    TaskDescription: Optional[str] = None
    ConceptId: Optional[int] = None


class TcbaLookupTable(IntEnum):
    Invalid = 0
    GapSource = 1
    GeographicalAor = 2
    JointCapabilityArea = 3
    Series = 4
    Tier1GapCategory = 5
    Wff = 6


class TddAdministrativeFormDto(BaseModel):
    Id: Optional[int] = None
    OrganizationGuid: Optional[str] = None
    SourceOrgGuid: Optional[str] = None
    PocId: Optional[str] = None
    PocFirstName: Optional[str] = None
    PocLastName: Optional[str] = None
    PocFullName: Optional[str] = None
    PocEmail: Optional[str] = None
    PocPhoneNumber: Optional[str] = None


class TddClosureDto(BaseModel):
    LearningDemandId: Optional[int] = None
    FinalAnswer: Optional[str] = None
    WorkflowStepId: Optional[int] = None


class TddCreateDto(BaseModel):
    TypeId: str
    ShortName: str = Field(min_length=1)
    SourceOrgGuid: Optional[str] = None
    DueDate: Optional[str] = None
    DecisionEchelonId: Optional[int] = None
    SourcePoc: Optional[str] = None
    ActionPoc: Optional[str] = None
    ActionOrgGuid: Optional[str] = None
    ProblemStatement: Optional[str] = None


class TddDto(BaseModel):
    Id: Optional[int] = None
    ModifiedDate: Optional[str] = None
    ModifiedDateFormatted: Optional[str] = None
    TddType: Optional[str] = None
    TddText: Optional[str] = None
    TddDueDate: Optional[str] = None
    TddDueDateFormatted: Optional[str] = None
    ActionPoc: Optional[str] = None
    DirectedActivity: Optional[str] = None
    SubIssue: Optional[str] = None
    ProblemStatement: Optional[str] = None
    ProblemState: Optional[str] = None
    SourceOrgGuid: Optional[str] = None
    MappedLds: Optional[list] = None
    MappedLdIds: Optional[str] = None
    MappedLdTitles: Optional[str] = None
    MappedLdDateStrings: Optional[list] = None


class TddLearningDemandMappingDto(BaseModel):
    MappingId: Optional[int] = None
    Id: Optional[int] = None
    LdId: Optional[int] = None
    Title: Optional[str] = None
    Ltoiv: Optional[str] = None
    LtiovDriver: Optional[str] = None
    Importance: Optional[str] = None
    LastModified: Optional[str] = None
    MappedEventIds: Optional[list] = None
    MappedEvents: Optional[str] = None
    IsPriority: Optional[bool] = None
    IsEditable: Optional[bool] = None
    IsMappingDeletable: Optional[bool] = None
    OrganizationGuid: Optional[str] = None


class TddProblemDispositionFormDto(BaseModel):
    Id: Optional[int] = None
    TypeId: Optional[str] = None
    TypeName: Optional[str] = None
    TddType: Optional[str] = None
    TaskType: Optional[str] = None
    ShortName: str = Field(min_length=1)
    AmgTasks: Optional[list] = None
    SourceOrgGuid: Optional[str] = None
    DueDate: Optional[str] = None
    DecisionEchelonId: Optional[int] = None
    SourcePoc: Optional[str] = None


class UserInfoDto(BaseModel):
    Id: Optional[str] = None
    LastName: Optional[str] = None
    FirstName: Optional[str] = None
    RankCode: Optional[str] = None
    GradeCode: Optional[str] = None
    Email: Optional[str] = None
    PhoneNumber: Optional[str] = None
    FullName: Optional[str] = None
