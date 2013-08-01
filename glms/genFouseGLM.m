TR_starting = 15;
TR_instruction = 1;
TR_fouse = 18;
TR_delay = 2;
TR_feedback = 2;
TR_fix = 10;

% Rows are TRs, Col are the vectors
% 1 = F1 fouse1 (scene)
% 2 = F2 fouse2 (face)
% 3 = Fx fixation
% 4 = I instruction
% 5 = Fb feedback

Starting = 3.*ones(1,TR_starting);
SceneRunFb = [4.*ones(1,TR_instruction),1.*ones(1,TR_fouse),3.*ones(1,TR_delay),5.*ones(1,TR_feedback),3.*ones(1,TR_fix)];
FaceRunFb = [4.*ones(1,TR_instruction),2.*ones(1,TR_fouse),3.*ones(1,TR_delay),5.*ones(1,TR_feedback),3.*ones(1,TR_fix)];

SceneRunNoFb = [4.*ones(1,TR_instruction),1.*ones(1,TR_fouse),3.*ones(1,TR_delay),3.*ones(1,TR_feedback),3.*ones(1,TR_fix)];
FaceRunNoFb = [4.*ones(1,TR_instruction),2.*ones(1,TR_fouse),3.*ones(1,TR_delay),3.*ones(1,TR_feedback),3.*ones(1,TR_fix)];


% 1st run no feedback (same as other no feedback run)
%     Attend to Houses
%     Attend to Faces
%     Attend to Houses
%     Attend to Faces
nfFouse01 = [Starting, SceneRunNoFb, FaceRunNoFb, SceneRunNoFb, FaceRunNoFb];
nfFouse02 = [Starting, SceneRunNoFb, FaceRunNoFb, SceneRunNoFb, FaceRunNoFb];

% 1st run feedback (same as last feedback run)
%  Attend to Faces
%  attend to Houses
%  Attend to Houses
%  Attend to Faces
rtFouse01 = [Starting, FaceRunFb, SceneRunFb, SceneRunFb, FaceRunFb];

% 2nd  run feedback
%   Attend to Faces
%   Attend to Houses
%   Attend to Houses
%   Attend to Faces
rtFouse02 = [Starting, FaceRunFb, SceneRunFb, SceneRunFb, FaceRunFb];

% 3rd run feedback
%   Attend to Faces
%   Attend to Houses
%   Attend to Faces
%   Attend to Houses
rtFouse03 = [Starting, FaceRunFb, SceneRunFb, FaceRunFb, SceneRunFb];

% 4th run feedback
%   Attend to Faces
%   attend to Houses
%   Attend to Houses
%   Attend to Faces
rtFouse04 = [Starting, FaceRunFb, SceneRunFb, SceneRunFb, FaceRunFb];


% Rows are TRs, Col are the vectors
% 1 = F1 fouse1 (scene)
% 2 = F2 fouse2 (face)
% 3 = Fx fixation
% 4 = I instruction
% 5 = Fb feedback

nfFouse01_GLM = vertcat(nfFouse01==1,nfFouse01==2,nfFouse01==3,nfFouse01==4,nfFouse01==5);
nfFouse02_GLM = nfFouse01_GLM;
rtFouse01_GLM = vertcat(rtFouse01==1,rtFouse01==2,rtFouse01==3,rtFouse01==4,rtFouse01==5);
rtFouse02_GLM = vertcat(rtFouse02==1,rtFouse02==2,rtFouse02==3,rtFouse02==4,rtFouse02==5);
rtFouse03_GLM = vertcat(rtFouse03==1,rtFouse03==2,rtFouse03==3,rtFouse03==4,rtFouse03==5);
rtFouse04_GLM = vertcat(rtFouse04==1,rtFouse04==2,rtFouse04==3,rtFouse04==4,rtFouse04==5);

save -text nfFouse01_GLM.txt nfFouse01_GLM
save -text nfFouse02_GLM.txt nfFouse02_GLM
save -text rtFouse01_GLM.txt rtFouse01_GLM
save -text rtFouse02_GLM.txt rtFouse02_GLM
save -text rtFouse03_GLM.txt rtFouse03_GLM
save -text rtFouse04_GLM.txt rtFouse04_GLM

