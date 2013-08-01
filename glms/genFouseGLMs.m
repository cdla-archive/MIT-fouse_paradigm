% ----- funcLoc
% -----------------------

% Rows are TRs, Col are the vectors
% 1 = Scene
% 2 = Face
% 3 = fouse1_50 (scene)
% 4 = fouse2_50 (face)
% 5 = Fx fixation
% 6 = I instruction
% 7 = Fb feedback

block_len = 18;

SceneBlock = 1.*ones(1,block_len);
FaceBlock = 2.*ones(1,block_len);
Fouse1Block = [6, 3.*ones(1,block_len)];
Fouse2Block = [6, 4.*ones(1,block_len)];
FixBlock = 5.*ones(1,block_len);

% FuncLoc 01 order
%   Fixation
%   Faces
%   Attend to House (fouse1)
%   Scenes
%   Attend to Face (fouse2)
%   Fixation
%   Scenes
%   Attend to Face (fouse2)
%   Face
%   Attend to House (fouse1)

funcLoc01 = [FixBlock, FaceBlock, Fouse1Block, SceneBlock, Fouse2Block, FixBlock, SceneBlock, Fouse2Block, FaceBlock, Fouse1Block];

funcLoc01_scene   = funcLoc01==1;
funcLoc01_face    = funcLoc01==2;
funcLoc01_scene50 = funcLoc01==3;
funcLoc01_face50  = funcLoc01==4;

save -text funcLoc01_scene.txt   funcLoc01_scene
save -text funcLoc01_face.txt    funcLoc01_face
save -text funcLoc01_scene50.txt funcLoc01_scene50
save -text funcLoc01_face50.txt  funcLoc01_face50

%funcLoc01_GLM = vertcat(funcLoc01==1,funcLoc01==2,funcLoc01==3,funcLoc01==4)
%save -text funcLoc01_GLM.txt funcLoc01_GLM

%After reading the comments (2013/07/08):
%	36 seconds blocks
%	6 block types: 
%a) faces 
%b) scenes 
%c) objects 
%d) 50/50 blend - attend to faces
%e) 50/50 blend - attend to house
%f) fixation
%	each block shown twice with 2 s instructions before each 50/50 blend blocks
%	36s * 6 * 2views/blocks + (2 s instructions * 4 ) = 440 seconds (7 min 20 s). 


% ----- rtFouse, nfFouse
% -----------------------

TR_starting = 15;
TR_instruction = 1;
TR_fouse = 18;
TR_delay = 2;
TR_feedback = 2;
TR_fix = 5;

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
%   Attend to Houses
%   Attend to Faces
%   Attend to Faces
%   Attend to Houses
rtFouse02 = [Starting, SceneRunFb, FaceRunFb, FaceRunFb, SceneRunFb];

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
