import React, { useState, useEffect, useCallback, useMemo, useRef } from 'react';
import { supabase } from './supabase';
import { parseModuleTheme } from './moduleTheme';
import { BoardTheme, DEFAULT_BOARD_THEME, BoardThemeModal, createCustomTheme, loadTheme, saveTheme } from './ThemeModal';
import InteractiveLecturePlayer from './InteractiveLecturePlayer';

const LECTURE_MANIFEST_MAP: Record<string, string> = {
  '6286cb6f-b4ac-495b-b2ea-5a2bab09f764': '/audio/lectures/geography/1_1/manifest.json', // 1.1
  'bade96ee-497d-4d75-8d82-c691133eb9d6': '/audio/lectures/geography/1_2/manifest.json', // 1.2
  'fea9a6ec-9ff0-456a-9185-4076073b04c1': '/audio/lectures/geography/1_3/manifest.json', // 1.3
  'd38db7a8-e92e-450c-a034-b9d46dc10a7f': '/audio/lectures/geography/2_1/manifest.json', // 2.1
  'b0ca05f2-dab3-4223-9c25-c92d73df56c1': '/audio/lectures/geography/2_2/manifest.json', // 2.2
  '446dabf6-7c9d-4509-a3f9-78161a684e3e': '/audio/lectures/geography/2_3/manifest.json', // 2.3
  '1b4caf37-15e4-475a-939c-e6490b366fd0': '/audio/lectures/geography/3_1/manifest.json', // 3.1
  '93a28707-1b95-4ed2-a3ff-4789143118cd': '/audio/lectures/geography/3_2/manifest.json', // 3.2
  '7d543b73-837d-4129-afc6-7196df47b6f6': '/audio/lectures/geography/3_3/manifest.json', // 3.3
  'c5ce49f0-7b81-4843-a477-3ee46e41928e': '/audio/lectures/geography/3_4/manifest.json', // 3.4
  'e5fde4e7-a1e6-4b3c-aeb2-756155f06ff5': '/audio/lectures/geography/4_1/manifest.json', // 4.1
  'f45dd9b1-ef60-4521-a067-04bd896fc7e2': '/audio/lectures/geography/4_2/manifest.json', // 4.2
  '1f909afc-865f-46d0-bb20-2e6d474fa87b': '/audio/lectures/geography/4_3/manifest.json', // 4.3
  'c81dc416-7aa4-4e26-a2af-341d6c03fa52': '/audio/lectures/geography/4_4/manifest.json', // 4.4
  '7c30919a-5d22-425a-a167-21e5de07d203': '/audio/lectures/geography/5_1/manifest.json', // 5.1
  '23eee2fb-427c-4843-8d2d-ec296188730d': '/audio/lectures/geography/5_2/manifest.json', // 5.2
  '36e35bdb-986b-4cd5-b8df-6bb0f93282e5': '/audio/lectures/geography/5_3/manifest.json', // 5.3
  // Topic 6: Population and Migration
  'c6fccfc5-088b-4145-9a23-9cbb2df1cce9': '/audio/lectures/geography/6_1/manifest.json', // 6.1
  '5390b0d7-995c-4c18-a092-b5cdd4eda49a': '/audio/lectures/geography/6_2/manifest.json', // 6.2
  '33c91ae9-b13f-49d7-b29f-0c3b794d192d': '/audio/lectures/geography/6_3/manifest.json', // 6.3
  // Topic 7: Settlement & Urbanisation
  '556bc6b6-1555-49a9-a043-35f059b44559': '/audio/lectures/geography/7_1/manifest.json', // 7.1
  '30bae547-a9b0-4c09-8850-ce22b96cfea2': '/audio/lectures/geography/7_2/manifest.json', // 7.2
  '0b658b3f-bf70-4991-95d5-d65616b7ec1a': '/audio/lectures/geography/7_3/manifest.json', // 7.3
  // Topic 8: Economic Development
  '5ff5f837-df39-4488-bbd2-5138f4faed1e': '/audio/lectures/geography/8_1/manifest.json', // 8.1
  '9cf90212-43f4-4b28-8014-fd6c130db8ef': '/audio/lectures/geography/8_2/manifest.json', // 8.2
  '7da208d1-559d-4e60-a6a3-ebfb8c2d232f': '/audio/lectures/geography/8_3/manifest.json', // 8.3
  // Topic 9: Employment, Globalisation & Tourism
  '6c14f92b-774a-45d1-a68d-2e9fe5e0b85d': '/audio/lectures/geography/9_1/manifest.json', // 9.1
  '5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b': '/audio/lectures/geography/9_2/manifest.json', // 9.2
  '53517557-9eb4-450d-a8dd-18b73c71938a': '/audio/lectures/geography/9_3/manifest.json', // 9.3
  // Topic 10: Food & Energy Resources
  '362104be-aedc-4cbe-87b2-29034e93cc9c': '/audio/lectures/geography/10_1/manifest.json', // 10.1
  '76dcafbf-e6b8-47f1-8618-be1b14e975ed': '/audio/lectures/geography/10_2/manifest.json', // 10.2
  '96d7f427-3b6d-43e3-84dc-f8f052f20033': '/audio/lectures/geography/10_3/manifest.json', // 10.3
  '199a26cd-1226-4ff7-b063-f7df7fa7b5ba': '/audio/lectures/geography/10_4/manifest.json', // 10.4
  'a3a8d904-d277-4eef-b8ff-52a913ebc5f6': '/audio/lectures/geography/10_5/manifest.json', // 10.5
  'fb30c141-db3a-49e8-aa55-028c913640d4': '/audio/lectures/geography/10_6/manifest.json', // 10.6

  // ==========================================
  // Business Studies 0450 (Course ID: 564f9e56-b77c-43af-9299-23eb2e7dcb7e)
  // ==========================================
  // Topic 1: Understanding business activity
  '6049f916-3af9-428a-bcd0-ce0574f1d7f7': '/audio/lectures/business/1_1/manifest.json', // 1.1 Business activity
  '7027f2e2-0ac5-4ee6-8913-7d93c7857733': '/audio/lectures/business/1_2/manifest.json', // 1.2 Classification of businesses
  'a8ebc541-78ef-4202-96ad-161ed647a1b1': '/audio/lectures/business/1_3/manifest.json', // 1.3 Enterprise, business growth and size
  '71458f5f-ba54-4ac7-a4c2-8bc68f8f15a0': '/audio/lectures/business/1_4/manifest.json', // 1.4 Types of business organisation
  'a6bf8fbd-9c3d-45a3-8cd7-d63a3e79e7b3': '/audio/lectures/business/1_5/manifest.json', // 1.5 Business objectives and stakeholder objectives
  // Topic 2: People in business
  'cd1763a9-f030-4be1-b65b-c6dc6dde91c9': '/audio/lectures/business/2_1/manifest.json', // 2.1 Motivating employees
  'fe4967aa-7d4c-480c-af71-e0d867459044': '/audio/lectures/business/2_2/manifest.json', // 2.2 Organisation and people management
  'c2d359f6-1921-459e-a295-def7e891c352': '/audio/lectures/business/2_3/manifest.json', // 2.3 Recruitment, selection and training
  '47166a31-2a55-40ea-a86c-81569cfafa32': '/audio/lectures/business/2_4/manifest.json', // 2.4 Internal and external communication
  // Topic 3: Marketing
  '6cbe4a84-26ed-4a1d-933b-5843e9b9a501': '/audio/lectures/business/3_1/manifest.json', // 3.1 Marketing, competition and customer
  '356dede8-277a-441a-ad73-ef9384973eb7': '/audio/lectures/business/3_2/manifest.json', // 3.2 Market research
  '25fe41d9-780d-41a6-876d-fff3e0d854c5': '/audio/lectures/business/3_3/manifest.json', // 3.3 The marketing mix
  'c0d60bf9-ad33-456c-807e-9e29318113b8': '/audio/lectures/business/3_4/manifest.json', // 3.4 The marketing strategy
  // Topic 4: Operations management
  '1e280547-ce64-44c2-8fcf-997f7d61cacf': '/audio/lectures/business/4_1/manifest.json', // 4.1 Production of goods and services
  '66589390-767c-4aab-957b-a970fa1a976e': '/audio/lectures/business/4_2/manifest.json', // 4.2 Costs, scale and break-even
  '8f0fd09a-d6e6-438f-a2ab-ddc1447e0b00': '/audio/lectures/business/4_3/manifest.json', // 4.3 Quality management
  '95eb54ae-44d4-42f6-9d1d-c5c729a69954': '/audio/lectures/business/4_4/manifest.json', // 4.4 Location decisions
  // Topic 5: Financial information and decisions
  '7b510a8f-757c-4856-9c68-65f98bf96836': '/audio/lectures/business/5_1/manifest.json', // 5.1 Business Finance: Needs and Sources
  'dc0411df-d831-468a-9a7d-16fb4009290d': '/audio/lectures/business/5_2/manifest.json', // 5.2 Cash flow forecasting and working capital
  '71f25939-98d4-4fa3-8227-be8434f64581': '/audio/lectures/business/5_3/manifest.json', // 5.3 Income statements
  '5421db93-9d7b-4241-b362-171974092a30': '/audio/lectures/business/5_4/manifest.json', // 5.4 Statement of financial position
  'd7564fe9-d338-4abc-acf3-affd8cca23fa': '/audio/lectures/business/5_5/manifest.json', // 5.5 Analysis of accounts
  // Topic 6: External influences on business activity
  '0e8fbc94-5976-4c7f-8588-471ea93926f5': '/audio/lectures/business/6_1/manifest.json', // 6.1 Economic issues
  'a1d571ff-fa12-46c2-a49d-1df88df13214': '/audio/lectures/business/6_2/manifest.json', // 6.2 Environmental and ethical issues
  '1bc6f5c1-e71b-4d0d-8153-d2f74180a845': '/audio/lectures/business/6_3/manifest.json', // 6.3 Business and globalisation

  // =========================================================================
  // CAMBRIDGE IGCSE BIOLOGY (0610) BILINGUAL AUDIO LECTURES (TOPICS 1 - 21)
  // =========================================================================
  '11cfe97d-205e-418b-ae79-e39d7e57e0a8': '/audio/lectures/biology/1/manifest.json', // Topic 1: Characteristics and classification
  '2d2545c0-ccb9-4d04-a6fa-f2eec55cdecc': '/audio/lectures/biology/2/manifest.json', // Topic 2: Cells and organisms
  '0f5013fb-eaf1-4f79-8f41-c6102d2185a2': '/audio/lectures/biology/3/manifest.json', // Topic 3: Movement into and out of cells
  '821ff271-c9ae-493a-b14c-e3f4b074a9d9': '/audio/lectures/biology/4/manifest.json', // Topic 4: Biological molecules
  'a5d1775c-6ecb-4d6c-bc50-8aafbf641c1e': '/audio/lectures/biology/5/manifest.json', // Topic 5: Enzymes
  'e7d6e813-b7b9-4038-9911-8b886978cd07': '/audio/lectures/biology/6/manifest.json', // Topic 6: Plant Nutrition
  '85f36013-879b-49a8-a531-69c245a9630e': '/audio/lectures/biology/7/manifest.json', // Topic 7: Human nutrition
  '37f08657-58e8-4fad-8035-2d935e1259e8': '/audio/lectures/biology/8/manifest.json', // Topic 8: Transport in plants
  'b50dd00a-e2b4-4dba-8b1d-3f679dadae74': '/audio/lectures/biology/9/manifest.json', // Topic 9: Transport in animals
  '62278d87-97ea-4fa5-aa46-748bca28db68': '/audio/lectures/biology/10/manifest.json', // Topic 10: Diseases and immunity
  'da59c2b3-124f-4e25-8537-74059e74f9b0': '/audio/lectures/biology/11/manifest.json', // Topic 11: Gas exchange in humans
  'fb098b77-64fa-463a-9829-64f5c9055de5': '/audio/lectures/biology/12/manifest.json', // Topic 12: Respiration
  'b8f0539e-9361-4ba4-a96e-74c106494ebe': '/audio/lectures/biology/13/manifest.json', // Topic 13: Excretion in humans
  'c9abc870-7cbd-4c7e-b6c9-2d6237ff7670': '/audio/lectures/biology/14/manifest.json', // Topic 14: Coordination and response
  'f87b29a1-56a3-4668-a249-ed9f118d31d8': '/audio/lectures/biology/15/manifest.json', // Topic 15: Drugs
  '936affb8-f062-4e39-b415-cc3794fb341e': '/audio/lectures/biology/16/manifest.json', // Topic 16: Reproduction
  '77f1f7b8-f30e-4b0b-89e2-2e2482242791': '/audio/lectures/biology/17/manifest.json', // Topic 17: Inheritance
  '89750884-8439-4cda-916a-56bf5524741b': '/audio/lectures/biology/18/manifest.json', // Topic 18: Variation and selection
  '7b2384dd-b79d-47fe-b36b-7abf36784f06': '/audio/lectures/biology/19/manifest.json', // Topic 19: Organisms and their environment
  '7777b4df-68dd-4600-b4ba-a4ce56ecc6ac': '/audio/lectures/biology/20/manifest.json', // Topic 20: Human influences on ecosystems
  '55023dc0-7fdc-46ea-a3e9-9a049306d086': '/audio/lectures/biology/21/manifest.json', // Topic 21: Biotechnology and Genetic Engineering

  // =========================================================================
  // CAMBRIDGE IGCSE CO-ORDINATED SCIENCES (0654) BILINGUAL AUDIO LECTURES
  // =========================================================================
  // --- BIOLOGY ---
  '1231b474-8a99-4330-b45d-fdda19a802fe': '/audio/lectures/science/b1/manifest.json', // B1: Characteristics of living organisms
  '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c': '/audio/lectures/science/b2/manifest.json', // B2: Cells and organisms
  '9a23109e-ad73-4fcf-a599-9605cc4906eb': '/audio/lectures/science/b3/manifest.json', // B3: Movement into and out of cells
  '757409b3-5cec-4e1f-8877-18d81e440103': '/audio/lectures/science/b4/manifest.json', // B4: Biological molecules
  '8ab2afa2-59e3-4c56-8971-8d93dec5ad8e': '/audio/lectures/science/b5/manifest.json', // B5: Enzymes
  '1d6a6b7b-ae57-404f-9ad1-58b11219b4d1': '/audio/lectures/science/b6/manifest.json', // B6: Plant Nutrition
  'cbebf582-244c-48bf-a586-c6c1922d8e20': '/audio/lectures/science/b7/manifest.json', // B7: Human nutrition
  'e2819423-13ed-47a2-bd80-9a083989e8bd': '/audio/lectures/science/b8/manifest.json', // B8: Transport in plants
  'a79dd569-671f-4559-84a3-eee1e6018172': '/audio/lectures/science/b9/manifest.json', // B9: Transport in animals
  '04d34896-13fb-411b-9e13-2bc3f9725136': '/audio/lectures/science/b10/manifest.json', // B10: Diseases and immunity
  '39003a2f-708e-47fe-b8ad-7aae073273a3': '/audio/lectures/science/b11/manifest.json', // B11: Gas exchange and respiration
  '58e65add-a67a-4b90-8b84-52de1a2840be': '/audio/lectures/science/b12/manifest.json', // B12: Respiration
  '2637d6ee-fd5f-48fc-aa7a-fc794fb3e561': '/audio/lectures/science/b13/manifest.json', // B13: Coordination and response
  '7ed510d0-acd2-4d0a-9079-1f1e4e4fc463': '/audio/lectures/science/b14/manifest.json', // B14: Drugs
  'deb8222d-2b75-42a3-b454-9601fbfa1bd2': '/audio/lectures/science/b15/manifest.json', // B15: Reproduction
  'd48c8f84-ba93-49d4-bf61-c7890bd6d2ce': '/audio/lectures/science/b16/manifest.json', // B16: Inheritance
  '24f0deeb-3cd9-4b82-b253-5a070ca31275': '/audio/lectures/science/b17/manifest.json', // B17: Variation and selection
  'cbeb6b74-e9c2-4a91-b39f-decb63e72ec0': '/audio/lectures/science/b18/manifest.json', // B18: Organisms and their environment
  '298327a8-455a-44d5-9a4c-164e2653c456': '/audio/lectures/science/b19/manifest.json', // B19: Human influences on ecosystems
  // --- CHEMISTRY ---
  '3fc0ef74-3661-4f23-a8a8-9c33d11051f5': '/audio/lectures/science/c1/manifest.json', // C1: States of matter
  'ee4f94c2-382b-4dbb-aaf8-981e7b0d7223': '/audio/lectures/science/c2/manifest.json', // C2: Atoms elements and compounds
  'f0988036-6fd0-4768-993d-a5ea5fe4eb0b': '/audio/lectures/science/c3/manifest.json', // C3: Stoichiometry
  '4732621b-f827-4b12-934b-3b53e694cc2a': '/audio/lectures/science/c4/manifest.json', // C4: Electrochemistry
  '71545c83-4d45-4201-978c-aa58d01b57e5': '/audio/lectures/science/c5/manifest.json', // C5: Chemical energetics
  '7f2b44b2-ba70-4cfc-85b3-3a0709058b46': '/audio/lectures/science/c6/manifest.json', // C6: Chemical reactions
  '2c83104c-9413-4ee1-bdf3-2c0da8fd96a6': '/audio/lectures/science/c7/manifest.json', // C7: Acids bases and salts
  '856f20da-80e8-4c6a-9cd1-dbe8a1f40828': '/audio/lectures/science/c8/manifest.json', // C8: Periodic table
  'd34bbfa2-7449-4192-b471-3a6a8ba49257': '/audio/lectures/science/c9/manifest.json', // C9: Metals
  '9d61f516-a24c-4485-8490-8485604130ec': '/audio/lectures/science/c10/manifest.json', // C10: Chemistry of the environment
  '69b82c81-05a0-40a8-816f-c21a882cef54': '/audio/lectures/science/c11/manifest.json', // C11: Organic chemistry
  'd51b5192-ff57-48a0-bcd9-d4f8a7d10757': '/audio/lectures/science/c12/manifest.json', // C12: Experimental techniques and Chemical analysis
  // --- PHYSICS ---
  '690ff013-5d01-4c1e-8546-25b3cd056e64': '/audio/lectures/science/p1/manifest.json', // P1: Motion, forces & energy
  'dc33ed9d-e328-4f60-8c47-f0dbd103e8c1': '/audio/lectures/science/p2/manifest.json', // P2: Thermal physics
  'eb3ed0a0-bd5e-4c0f-961f-1b9af74bf4a8': '/audio/lectures/science/p3/manifest.json', // P3: Waves
  '2a155fd4-9bd1-4136-b7b7-3ce55d6fbb69': '/audio/lectures/science/p4/manifest.json', // P4: Electricity and magnetism
  'a6077865-db01-4785-9ec7-e8b0f531fcdc': '/audio/lectures/science/p5/manifest.json', // P5: Nuclear physics
  'd11f8920-fe86-4cd4-ad9a-e8b669bc687b': '/audio/lectures/science/p6/manifest.json', // P6: Space physics

  // =========================================================================
  // CAMBRIDGE IGCSE ECONOMICS (0455) BILINGUAL AUDIO LECTURES
  // =========================================================================
  // --- TOPIC 1: THE BASIC ECONOMIC PROBLEM ---
  '1fba7e8c-742f-4697-b93e-a0205fc7d825': '/audio/lectures/economics/1/manifest.json', // 1. The Basic Economic Problem
  '34bbcc7c-6b51-40fd-9585-9eb3c37da582': '/audio/lectures/economics/2/manifest.json', // 2. The Factors of Production
  '9b0e6a87-ed26-43bb-a20c-ffa636f9ef11': '/audio/lectures/economics/3/manifest.json', // 3. Opportunity Cost
  '9d5f779b-5254-48ed-8284-3918eaacd579': '/audio/lectures/economics/4/manifest.json', // 4. Production Possibility Curve

  // --- TOPIC 2: THE ALLOCATION OF RESOURCES ---
  'd6e6ad94-1106-43ae-b37c-1b36832f03e6': '/audio/lectures/economics/5/manifest.json', // 5. Microeconomics and Macroeconomics
  '71e51517-0174-49fc-9796-802abee0c5a5': '/audio/lectures/economics/6/manifest.json', // 6. The Role of Market in Allocating Resources
  '06450a33-0477-4bd2-9d1b-4e424f8e973d': '/audio/lectures/economics/7/manifest.json', // 7. Demand
  'd15b56e7-9b09-4120-829c-1955efd21602': '/audio/lectures/economics/8/manifest.json', // 8. Supply
  '763cd322-6b7d-43b0-a18d-15da34137d9d': '/audio/lectures/economics/9/manifest.json', // 9. Price Determination
  '16314014-7787-41dc-9ff5-47fd1d2c7409': '/audio/lectures/economics/10/manifest.json', // 10. Price Changes
  '4a5f97fd-91d2-41f4-8cbb-b928f5aea5e9': '/audio/lectures/economics/11/manifest.json', // 11. Price Elasticity of Demand (PED)
  '38954a57-c9bc-4714-b53e-e404e78379cd': '/audio/lectures/economics/12/manifest.json', // 12. Price Elasticity of Supply (PES)
  '6f3173be-e12a-4a93-8f76-8cb09fb026fe': '/audio/lectures/economics/13/manifest.json', // 13. Market Economic System
  '69df5ed2-ce91-4e2a-b818-0e2957483b12': '/audio/lectures/economics/14/manifest.json', // 14. Market Failure
  '1af33337-f02c-45ff-a8d0-040864272c98': '/audio/lectures/economics/15/manifest.json', // 15. Mixed Economic System

  // --- TOPIC 3: MICROECONOMIC DECISION MAKERS ---
  '3adca75c-b852-48be-9cbf-5074ae12e430': '/audio/lectures/economics/16/manifest.json', // 16. Money and Banking
  '123d8a13-d619-45cd-b363-702e9039627a': '/audio/lectures/economics/17/manifest.json', // 17. Households: Income, Saving, Borrowing & Spending
  '95fb66bf-66f0-4bbd-a7e4-418f191f487a': '/audio/lectures/economics/18/manifest.json', // 18. Workers: Wage Determination, Specialisation & Trade Unions
  '1943e7bc-cdee-45b1-93d5-830b704a4017': '/audio/lectures/economics/19/manifest.json', // 19. Trade Unions
  '07e42111-1e2c-4810-bce3-02d8df497c97': '/audio/lectures/economics/20/manifest.json', // 20. Firms: Size, Growth & Integration
  '604d1490-caed-47aa-a562-a6a902790a30': '/audio/lectures/economics/21/manifest.json', // 21. Firms and Production: Costs, Revenue & Objectives
  'd2019792-c956-44e2-98ed-c247617a9162': '/audio/lectures/economics/22/manifest.json', // 22. Market Structure: Competitive Markets
  '4a814791-86ae-4aab-b9e2-a94b2565c55c': '/audio/lectures/economics/23/manifest.json', // 23. Market Structure: Monopoly
};

type LectureVideoItem = { title: string; videoId: string };
type LectureVideoConfig = string | LectureVideoItem[];

const LECTURE_VIDEO_MAP: Record<string, LectureVideoConfig> = {
  // Topic 1: Rivers
  '6286cb6f-b4ac-495b-b2ea-5a2bab09f764': 'aIJplswoSok', // 1.1 The main hydrological characteristics and processes that operate in rivers and drainage basins
  'bade96ee-497d-4d75-8d82-c691133eb9d6': '3oBcd0vYKSk', // 1.2 The main landforms associated with these processes
  'fea9a6ec-9ff0-456a-9185-4076073b04c1': 'uNsZOo73pLE', // 1.3 Rivers present opportunities and hazards for people
  // Topic 2: Coasts
  'd38db7a8-e92e-450c-a034-b9d46dc10a7f': 'UW2yfjZ7zrM', // 2.1 The physical processes that shape the coast
  'b0ca05f2-dab3-4223-9c25-c92d73df56c1': 'Q4R59xr8VTc', // 2.2 The main landforms associated with these processes
  '446dabf6-7c9d-4509-a3f9-78161a684e3e': 'kZJCN0h9DLE', // 2.3 Coasts present opportunities and hazards for people
  // Topic 3: Ecosystems
  '1b4caf37-15e4-475a-939c-e6490b366fd0': '_QCvBSfF96M', // 3.1 The characteristics of the Antarctic ecosystem
  '93a28707-1b95-4ed2-a3ff-4789143118cd': 'yphbpRu_d2I', // 3.2 The threats to the Antarctic ecosystem and how they can be managed
  '7d543b73-837d-4129-afc6-7196df47b6f6': 'nZAcU_HrUAg', // 3.3 The characteristics of the tropical rainforest ecosystem
  'c5ce49f0-7b81-4843-a477-3ee46e41928e': 'liAZ7TmiQrA', // 3.4 The threats to the tropical rainforest ecosystem and how they can be managed
  // Topic 4: Tectonics
  'e5fde4e7-a1e6-4b3c-aeb2-756155f06ff5': 'VLYGrJ36_Yw', // 4.1 The structure of the Earth and the distribution of earthquakes and volcanoes
  'f45dd9b1-ef60-4521-a067-04bd896fc7e2': 'fRGhmfyTaK8', // 4.2 The processes and features associated with earthquakes and volcanoes
  '1f909afc-865f-46d0-bb20-2e6d474fa87b': 'isAwD7t1uiA', // 4.3 The impact of tectonic hazards
  'c81dc416-7aa4-4e26-a2af-341d6c03fa52': 'vXKcocIppaE', // 4.4 Managing the impacts of tectonic hazards
  // Topic 5: Weather & Climate
  '7c30919a-5d22-425a-a167-21e5de07d203': 'MUsve5SkUs4', // 5.1 The natural and human causes of climate change
  '23eee2fb-427c-4843-8d2d-ec296188730d': 'DZT3vKnDXF8', // 5.2 The impacts of climate change at a range of geographic scales
  '36e35bdb-986b-4cd5-b8df-6bb0f93282e5': 'xlpkGrJOBgk', // 5.3 The responses to climate change
  // Topic 6: Population and Migration
  'c6fccfc5-088b-4145-9a23-9cbb2df1cce9': 'lrvbeVH8-X4', // 6.1 Populations grow and decline
  '5390b0d7-995c-4c18-a092-b5cdd4eda49a': 'pojs-B-sBeY', // 6.2 Population structures change over time
  '33c91ae9-b13f-49d7-b29f-0c3b794d192d': 'NX-YJ36nLNs', // 6.3 The causes and impacts of international migration
  // Topic 7: Settlement & Urbanisation
  '556bc6b6-1555-49a9-a043-35f059b44559': 'VaVB_D-uQVA', // 7.1 Where people live
  '30bae547-a9b0-4c09-8850-ce22b96cfea2': '0JSmcb4Gq7c', // 7.2 The opportunities and challenges of urbanisation
  '0b658b3f-bf70-4991-95d5-d65616b7ec1a': '7ma8mQ1JMzo', // 7.3 The management of urban growth
  // Topic 8: Economic Development
  '5ff5f837-df39-4488-bbd2-5138f4faed1e': 'npHWl1MV2jk', // 8.1 Measuring development
  '9cf90212-43f4-4b28-8014-fd6c130db8ef': '95JKAkAj3Mg', // 8.2 The world is developing unevenly
  '7da208d1-559d-4e60-a6a3-ebfb8c2d232f': 'os1p-r_O7Fc', // 8.3 Achieving sustainable development
  // Topic 9: Employment, Globalisation & Tourism
  '6c14f92b-774a-45d1-a68d-2e9fe5e0b85d': '13WDqq7MSLQ', // 9.1 Changing employment structures
  '5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b': 'nbSj6yqgLik', // 9.2 The impact of globalisation and the role of transnational corporations
  '53517557-9eb4-450d-a8dd-18b73c71938a': 'bF2xyprA4x8', // 9.3 Tourism is a growing industry
  // Topic 10: Food & Energy Resources
  '362104be-aedc-4cbe-87b2-29034e93cc9c': '9ElDT579thw', // 10.1 How our food is produced
  '76dcafbf-e6b8-47f1-8618-be1b14e975ed': '3GK_Y32i_M8', // 10.2 The global patterns of food supply and demand
  '96d7f427-3b6d-43e3-84dc-f8f052f20033': 'yMTIsH6BJE0', // 10.3 The challenges of food supply
  '199a26cd-1226-4ff7-b063-f7df7fa7b5ba': 'PFnyXKbH4rc', // 10.4 How our energy is produced
  'a3a8d904-d277-4eef-b8ff-52a913ebc5f6': 'R9O7708GCbw', // 10.5 The global patterns of energy supply and demand
  'fb30c141-db3a-49e8-aa55-028c913640d4': 'YLWXoCv1UnY', // 10.6 The impacts of energy production

  // ==========================================
  // Cambridge IGCSE Business Studies 0450
  // ==========================================
  // Topic 1: Understanding business activity
  '6049f916-3af9-428a-bcd0-ce0574f1d7f7': 'BoYOa7pn6tY', // 1.1 Business activity
  '7027f2e2-0ac5-4ee6-8913-7d93c7857733': 'oqVG5AaiIyM', // 1.2 Classification of businesses
  'a8ebc541-78ef-4202-96ad-161ed647a1b1': 'fj4ji4q_6AM', // 1.3 Enterprise, business growth and size
  '71458f5f-ba54-4ac7-a4c2-8bc68f8f15a0': 'WXgH5p34-Hw', // 1.4 Types of business organisation
  'a6bf8fbd-9c3d-45a3-8cd7-d63a3e79e7b3': '-hE0o1I92Uw', // 1.5 Business objectives and stakeholder objectives
  // Topic 2: People in business
  'cd1763a9-f030-4be1-b65b-c6dc6dde91c9': 'RiKN7hyGQNo', // 2.1 Motivating employees
  'fe4967aa-7d4c-480c-af71-e0d867459044': '4NaB99RTJDY', // 2.2 Organisation and people management
  'c2d359f6-1921-459e-a295-def7e891c352': '36YjJR4vC98', // 2.3 Recruitment, selection and training of employees
  '47166a31-2a55-40ea-a86c-81569cfafa32': 'KMkqwS5GEmY', // 2.4 Internal and external communication
  // Topic 3: Marketing
  '6cbe4a84-26ed-4a1d-933b-5843e9b9a501': '4wcVhLjnGi0', // 3.1 Marketing, competition and the customer
  '356dede8-277a-441a-ad73-ef9384973eb7': 'XHzq4yUEI7w', // 3.2 Market research
  '25fe41d9-780d-41a6-876d-fff3e0d854c5': [
    { title: '1. Product', videoId: 'ALwDbKo1LZw' },
    { title: '2. Price', videoId: 'OPpGREn5pIg' },
    { title: '3. Place', videoId: 'aeZ4oBioUMY' },
    { title: '4. Promotion', videoId: 'Zbn6fqHmNT0' },
    { title: '5. Technology', videoId: 'PXbnxsks8OY' },
  ], // 3.3 The marketing mix
  'c0d60bf9-ad33-456c-807e-9e29318113b8': '0I-wVlFKHvY', // 3.4 The marketing strategy
  // Topic 4: Operations management
  '1e280547-ce64-44c2-8fcf-997f7d61cacf': 'WcdaAxxAUr4', // 4.1 Production of goods and services
  '66589390-767c-4aab-957b-a970fa1a976e': 'tVabJQ_XpQE', // 4.2 Costs, scale of production and break even analysis
  '8f0fd09a-d6e6-438f-a2ab-ddc1447e0b00': '7qNmP5MgOPM', // 4.3 Quality management
  '95eb54ae-44d4-42f6-9d1d-c5c729a69954': 'rypWwJ8tt9M', // 4.4 Location decisions
  // Topic 5: Financial information and decisions
  '7b510a8f-757c-4856-9c68-65f98bf96836': 'W5MT_j-pxxg', // 5.1 Business Finance Needs and Sources
  'dc0411df-d831-468a-9a7d-16fb4009290d': 'mvtMlk16v5M', // 5.2 Cash flow forecasting and working capital
  '71f25939-98d4-4fa3-8227-be8434f64581': 'V8tYSSQhNIQ', // 5.3 Income statements
  '5421db93-9d7b-4241-b362-171974092a30': '92ZVr6rC1u8', // 5.4 Statement of financial position
  'd7564fe9-d338-4abc-acf3-affd8cca23fa': 'Kbhkue0jM8M', // 5.5 Analysis of accounts
  // Topic 6: External influences on business activity
  '0e8fbc94-5976-4c7f-8588-471ea93926f5': 'eH8ZU0drvOQ', // 6.1 Economic issues
  'a1d571ff-fa12-46c2-a49d-1df88df13214': 'cjxhZmsOBAA', // 6.2 Environmental and ethical issues
  '1bc6f5c1-e71b-4d0d-8153-d2f74180a845': 'QCvbpmvbYLQ', // 6.3 Business and globalisation

  // ==========================================
  // Cambridge IGCSE Co-ordinated Sciences 0654
  // ==========================================
  // --- Biology ---
  '1231b474-8a99-4330-b45d-fdda19a802fe': 'FQX0C3emIJg', // B1: Characteristics of living organisms
  '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c': 'ojDhyUwS0AQ', // B2: Cells and organisms
  '9a23109e-ad73-4fcf-a599-9605cc4906eb': 'ThkdsJ4O02k', // B3: Movement into and out of cells
  '757409b3-5cec-4e1f-8877-18d81e440103': '8Ytt_jpCspg', // B4: Biological molecules
  '8ab2afa2-59e3-4c56-8971-8d93dec5ad8e': 'CKXmyzhongw', // B5: Enzymes
  '1d6a6b7b-ae57-404f-9ad1-58b11219b4d1': 'T0tkVxCRqF4', // B6: Plant Nutrition
  'cbebf582-244c-48bf-a586-c6c1922d8e20': 'il6Xv0sYOFE', // B7: Human nutrition
  'e2819423-13ed-47a2-bd80-9a083989e8bd': '3579l3NtlEs', // B8: Transport in plants
  'a79dd569-671f-4559-84a3-eee1e6018172': 'W3GVWAGetcw', // B9: Transport in animals
  '04d34896-13fb-411b-9e13-2bc3f9725136': 'QhmEtSF0RXg', // B10: Diseases and immunity
  '39003a2f-708e-47fe-b8ad-7aae073273a3': 'mhCPspWCP1E', // B11: Gas exchange and respiration
  '58e65add-a67a-4b90-8b84-52de1a2840be': '48gGdqCkZR8', // B12: Respiration
  '2637d6ee-fd5f-48fc-aa7a-fc794fb3e561': 'Y3LPEiVRs_E', // B13: Coordination and response
  '7ed510d0-acd2-4d0a-9079-1f1e4e4fc463': 'Ogbbwhy7us0', // B14: Drugs
  'deb8222d-2b75-42a3-b454-9601fbfa1bd2': 'RaxNh_8P_J4', // B15: Reproduction
  'd48c8f84-ba93-49d4-bf61-c7890bd6d2ce': 'tdFJ9HXK8Mw', // B16: Inheritance
  '24f0deeb-3cd9-4b82-b253-5a070ca31275': 'XYGpw4-MOZA', // B17: Variation and selection
  'cbeb6b74-e9c2-4a91-b39f-decb63e72ec0': 'rhb581LgbH0', // B18: Organisms and their environment
  '298327a8-455a-44d5-9a4c-164e2653c456': 'TZGhMqpEBOY', // B19: Human influences on ecosystems
  // --- Chemistry ---
  '3fc0ef74-3661-4f23-a8a8-9c33d11051f5': 'LxRkVccWZRA', // C1: States of matter
  'ee4f94c2-382b-4dbb-aaf8-981e7b0d7223': 'RIdAsC6D5mY', // C2: Atoms elements and compounds
  'f0988036-6fd0-4768-993d-a5ea5fe4eb0b': '3Mh95hVf0-Y', // C3: Stoichiometry
  '4732621b-f827-4b12-934b-3b53e694cc2a': 'd-RgbhQC6P8', // C4: Electrochemistry
  '71545c83-4d45-4201-978c-aa58d01b57e5': 'd23r_Hv8uBc', // C5: Chemical energetics
  '7f2b44b2-ba70-4cfc-85b3-3a0709058b46': 'ilGzTGcCth0', // C6: Chemical reactions
  '2c83104c-9413-4ee1-bdf3-2c0da8fd96a6': 'XBSyl4h8qC8', // C7: Acids bases and salts
  '856f20da-80e8-4c6a-9cd1-dbe8a1f40828': 'ixdo6J_GdVA', // C8: Periodic table
  'd34bbfa2-7449-4192-b471-3a6a8ba49257': 'sLJNWrawAjw', // C9: Metals
  '9d61f516-a24c-4485-8490-8485604130ec': 'zR-JPRQh2S0', // C10: Chemistry of the environment
  '69b82c81-05a0-40a8-816f-c21a882cef54': 'ev99Cdk19Ns', // C11: Organic chemistry
  'd51b5192-ff57-48a0-bcd9-d4f8a7d10757': 'FJd9E7AQ6yE', // C12: Experimental techniques and Chemical analysis
  // --- Physics ---
  '690ff013-5d01-4c1e-8546-25b3cd056e64': 'YwihvOJ1w7o', // P1: Motion, forces & energy
  'dc33ed9d-e328-4f60-8c47-f0dbd103e8c1': 'pY_TRZC1JRw', // P2: Thermal physics
  'eb3ed0a0-bd5e-4c0f-961f-1b9af74bf4a8': 'P_uH3pzbH7c', // P3: Waves
  '2a155fd4-9bd1-4136-b7b7-3ce55d6fbb69': 'llyYTGan-eQ', // P4: Electricity and magnetism
  'a6077865-db01-4785-9ec7-e8b0f531fcdc': 'DeZjM41nqmo', // P5: Nuclear physics
  'd11f8920-fe86-4cd4-ad9a-e8b669bc687b': 'Ec9yMahD5xA', // P6: Space physics

  // ==========================================
  // Cambridge IGCSE Biology 0610
  // ==========================================
  '11cfe97d-205e-418b-ae79-e39d7e57e0a8': [
    { title: '1. Characteristics of living organisms', videoId: 'bKcUMgzGvhg' },
    { title: '2. Classification systems', videoId: 'vlQvflBYS8A' },
    { title: '3. Features of organisms', videoId: '3n_h19qGOOk' },
  ], // Topic 1: Characteristics and classification of living organisms
  '2d2545c0-ccb9-4d04-a6fa-f2eec55cdecc': [
    { title: '1. Cell structure and organisation', videoId: 'x97BLnxK2Bg' },
    { title: '2. Size of specimens', videoId: '1svEJYR2acw' },
  ], // Topic 2: Cells and organisms
  '0f5013fb-eaf1-4f79-8f41-c6102d2185a2': [
    { title: '1. Diffusion', videoId: '6pjddhlErzE' },
    { title: '2. Osmosis', videoId: 'F8RlY9DF9iE' },
    { title: '3. Active transport', videoId: 'hbcqa8Ynw_0' },
  ], // Topic 3: Movement into and out of cells
  '821ff271-c9ae-493a-b14c-e3f4b074a9d9': [
    { title: '1. Biological molecules', videoId: 'PnmEomL_Qss' },
    { title: '2. Structure of DNA', videoId: 'tsKCHHW5D-s' },
  ], // Topic 4: Biological molecules
  'a5d1775c-6ecb-4d6c-bc50-8aafbf641c1e': 'T2TnsUCO0Jg', // Topic 5: Enzymes
  'e7d6e813-b7b9-4038-9911-8b886978cd07': [
    { title: '1. Photosynthesis', videoId: 'gJ2KE6YCHgo' },
    { title: '2. Leaf structure', videoId: 'BxV5LQafe3c' },
    { title: '3. Mineral requirements', videoId: 'pqj0tpnEd1w' },
  ], // Topic 6: Plant Nutrition
  '85f36013-879b-49a8-a531-69c245a9630e': [
    { title: '1. Diet', videoId: 'nC3Xlwixqlk' },
    { title: '2. Digestive system', videoId: 'Ei5X_eIOetA' },
    { title: '3. Physical digestion', videoId: 'GHxnzZkASnM' },
    { title: '4. Chemical digestion', videoId: '6rmiyTexRwU' },
    { title: '5. Absorption', videoId: 'huKS787qa7U' },
  ], // Topic 7: Human nutrition
  '37f08657-58e8-4fad-8035-2d935e1259e8': [
    { title: '1. Xylem and phloem', videoId: 'e7jH24b-hIA' },
    { title: '2. Water uptake', videoId: '5Bo6-FhYxYs' },
    { title: '3. Transpiration', videoId: 'upenwiIznos' },
    { title: '4. Translocation', videoId: 'i92Zk6vTJYU' },
    { title: '5. Leaf, stem and root structure', videoId: 'ncjR0BrhtkM' },
  ], // Topic 8: Transport in plants
  'b50dd00a-e2b4-4dba-8b1d-3f679dadae74': [
    { title: '1. Circulatory systems', videoId: '4vGZbh83GaM' },
    { title: '2. Heart', videoId: '5e2FOAB9yx0' },
    { title: '3. Blood vessels', videoId: 'GL6n-BBnaFs' },
    { title: '4. Blood', videoId: 'SmIoisDnQic' },
  ], // Topic 9: Transport in animals
  '62278d87-97ea-4fa5-aa46-748bca28db68': [
    { title: '1. Pathogens and transmission', videoId: 'LQytBpCY0pE' },
    { title: '2. Defences against disease', videoId: 'fSTjfq2LRow' },
  ], // Topic 10: Diseases and immunity
  'da59c2b3-124f-4e25-8537-74059e74f9b0': 'LWxDndUR8Dg', // Topic 11: Gas exchange in humans
  'fb098b77-64fa-463a-9829-64f5c9055de5': [
    { title: '1. Respiration', videoId: 'wznxFqx7Lqw' },
    { title: '2. Aerobic respiration', videoId: '_a2It6ZkkNo' },
    { title: '3. Anaerobic respiration', videoId: 'IWlMLuA6qUI' },
  ], // Topic 12: Respiration
  'b8f0539e-9361-4ba4-a96e-74c106494ebe': 'HpENNSFbeEM', // Topic 13: Excretion in humans
  'c9abc870-7cbd-4c7e-b6c9-2d6237ff7670': [
    { title: '1. Coordination and response', videoId: 'xf__OW4hDOU' },
    { title: '2. Nervous control in humans', videoId: 'Ar22UcjAG3c' },
    { title: '3. Hormones', videoId: '5i9xXjy1pZ8' },
    { title: '4. Homeostasis', videoId: '8Jm3GQ-fVJ0' },
    { title: '5. Tropic responses', videoId: '3yW6unFD7yI' },
  ], // Topic 14: Coordination and response
  'f87b29a1-56a3-4668-a249-ed9f118d31d8': 'NL_Iw7qqzmU', // Topic 15: Drugs
  '936affb8-f062-4e39-b415-cc3794fb341e': [
    { title: '1. Asexual reproduction', videoId: 'yV5p5amlE0A' },
    { title: '2. Sexual reproduction', videoId: 'aWEneELEhlw' },
    { title: '3. Sexual reproduction in plants', videoId: 'ECqbUp-XeFA' },
    { title: '4. Sexual reproduction in humans', videoId: 'lpCagvh8NJI' },
    { title: '5. Sexual hormones in humans', videoId: 'oeTpLvSK2AY' },
    { title: '6. Sexually transmitted infections', videoId: 'b1BthpJ91gM' },
  ], // Topic 16: Reproduction
  '77f1f7b8-f30e-4b0b-89e2-2e2482242791': [
    { title: '1. Chromosomes, genes and proteins', videoId: '_4Lyprt1s2M' },
    { title: '2. Mitosis', videoId: 'OsgwzH6i4n8' },
    { title: '3. Meiosis', videoId: 'hAgF_hoOhpk' },
    { title: '4. Monohybrid inheritance', videoId: 'ug8SGHUcqOM' },
  ], // Topic 17: Inheritance
  '89750884-8439-4cda-916a-56bf5524741b': [
    { title: '1. Variation', videoId: 'mhF09ZFCupc' },
    { title: '2. Adaptive features', videoId: 'pUdkmwKCdVA' },
    { title: '3. Selection', videoId: 'VF4nTOE1M9o' },
  ], // Topic 18: Variation and selection
  '7b2384dd-b79d-47fe-b36b-7abf36784f06': [
    { title: '1. Energy flow', videoId: 'E03idQ4Kyo8' },
    { title: '2. Food chains and food webs', videoId: 'a5K0BT4XbRE' },
    { title: '3. Nutrient cycles', videoId: 'nFPOXQ7e7UM' },
    { title: '4. Populations', videoId: 'XASTEPupjwA' },
  ], // Topic 19: Organisms and their environment
  '7777b4df-68dd-4600-b4ba-a4ce56ecc6ac': [
    { title: '1. Food supply', videoId: 'eMpMnePtVp4' },
    { title: '2. Habitat destruction', videoId: 'uqbePk2VEGw' },
    { title: '3. Pollution', videoId: 'szBcHO9JvOE' },
    { title: '4. Conservation', videoId: 'Jm6VySV-eDw' },
  ], // Topic 20: Human influences on ecosystems
  '55023dc0-7fdc-46ea-a3e9-9a049306d086': [
    { title: '1. Biotechnology', videoId: 'qCCTkxsc178' },
    { title: '2. Genetic modification', videoId: 'VkxbDdc2ye0' },
  ], // Topic 21: Biotechnology and Genetic Engineering

  // ==========================================
  // Cambridge IGCSE Economics 0455
  // ==========================================
  '1fba7e8c-742f-4697-b93e-a0205fc7d825': 'DpDH1NRz1OI', // Topic 1. The Basic Economic Problem
  '34bbcc7c-6b51-40fd-9585-9eb3c37da582': 'vvEuzdewqcY', // Topic 2. The Factors of Production
  '9b0e6a87-ed26-43bb-a20c-ffa636f9ef11': 'Spyi_N--_1w', // Topic 3. Opportunity Cost
  '9d5f779b-5254-48ed-8284-3918eaacd579': '6Y274N6zuCA', // Topic 4. Production Possibility Curve
  'd6e6ad94-1106-43ae-b37c-1b36832f03e6': 'wC_Vsn4xADk', // Topic 5. Microeconomics and Macroeconomics
  '71e51517-0174-49fc-9796-802abee0c5a5': 'hQjfhAcpd_Y', // Topic 6. The Role of Market in Allocating Resources
  '06450a33-0477-4bd2-9d1b-4e424f8e973d': 'ahfISem0ELU', // Topic 7. Demand
  'd15b56e7-9b09-4120-829c-1955efd21602': 'BbqtSaBurOs', // Topic 8. Supply
  '763cd322-6b7d-43b0-a18d-15da34137d9d': 'JOZ8qs8agGM', // Topic 9. Price Determination
  '16314014-7787-41dc-9ff5-47fd1d2c7409': '6Di_5n1koc8', // Topic 10 . Price Changes
  '4a5f97fd-91d2-41f4-8cbb-b928f5aea5e9': 'QkYye8agvgw', // Topic 11. Price Easticity of Demand
  '38954a57-c9bc-4714-b53e-e404e78379cd': '7psgdqgYIyg', // Topic 12. Price Elasticity of Supply
  '6f3173be-e12a-4a93-8f76-8cb09fb026fe': 'tIlu-KE-YLI', // Topic 13. Market Economic System
  '69df5ed2-ce91-4e2a-b818-0e2957483b12': 'OweegukHj9g', // Topic 14. Market Failure
  '1af33337-f02c-45ff-a8d0-040864272c98': 'xnG_0xJ8ylg', // Topic 15. Mixed Economic System
  '3adca75c-b852-48be-9cbf-5074ae12e430': 'xosIsOUWM6A', // Topic 16. Money and Banking
  '123d8a13-d619-45cd-b363-702e9039627a': 'DDV6No_yyWs', // Topic 17. Households
  '95fb66bf-66f0-4bbd-a7e4-418f191f487a': 'wfGF8GzcXCE', // Topic 18. Workers
  '1943e7bc-cdee-45b1-93d5-830b704a4017': 'D5QVEhTkc4Q', // Topic 19. Trade Union
  '07e42111-1e2c-4810-bce3-02d8df497c97': 'lX6RsLX95mU', // Topic 20. Firms
  '604d1490-caed-47aa-a562-a6a902790a30': 'J27glkTyCbY', // Topic 21. Firms and Production
  'd2019792-c956-44e2-98ed-c247617a9162': 'mKqsamdWKtk', // Topic 22. Firms' Cost, Revenue and Objectives
  '4a814791-86ae-4aab-b9e2-a94b2565c55c': 'BELfJH0hS-Y', // Topic 23. Market Structure
  '73ce7854-ee86-46f4-bef0-b144bdace1dd': 'PwNi4QQUOMA', // Topic 24. The Role of Government
  '729d78eb-2564-407c-8279-c76b18a8c961': '4bntoRDDMXQ', // Topic 25. The Macroeconomic Aims of Government
  '50251f48-b7ab-4e4e-90e6-15f1c6129591': 'NxS2TMvGLp0', // Topic 26. Fiscal Policy
  'cb97d9d6-6009-4a15-83fc-e74ec2e1a959': 'T8tqhl3BKF0', // Topic 27. Monetary Policy
  '01041fd4-6608-4689-a502-832921ed3865': 'vb_DeLAGo54', // Topic 28. Supply-side Policy
  'c089b0b4-0a41-4e2e-98a9-22c41e6c2b3c': 'FxYPvyWbLEk', // Topic 29. Economic Growth
  '33de93b1-9eaf-446f-aa27-ce108d2cae49': 'Ug8lDbO-rBs', // Topic 30. Employment and Unemployment
  '8c3e99df-51fb-4bdf-859d-c0cb85a01e93': 'mjglwKCI8KA', // Topic 31. Inflation and Deflation
  '747ea49f-ae93-437c-9612-2d64c960e71d': 'AGx5DI_8ry0', // Topic 32. Living Standard
  'd2c35d4a-7334-4331-98c6-1f04bb58c079': 'dbew4q8NwGA', // Topic 33. Poverty
  '5d8ebacc-127e-4229-976b-3c75db87b8d4': 'I7aUzzYMdA0', // Topic 34. Population
  'c5023a42-f9b6-4742-a333-82c47124ae3e': 'aI1gEkq5X-E', // Topic 35. Differences in Economic Development Between Countries
  'f8fdb43e-1162-4445-97d0-e8199debf0ab': 'S_FETYyXBFc', // Topic 36. International Specialisation
  '0497aa28-0b26-45b3-a233-74fb121c1824': 'lrbcT5nZ_Ew', // Topic 37. Globalisation, Free Trade and Protection
  'ecb53067-d586-4806-9702-e52ad5c659e1': 'kof_fh3_k3M', // Topic 38. Foreign Exchange Rates
  '2d85d85e-815b-44f3-b6dd-82585e41b669': 'T67ZxnqM0iI', // Topic 39. Current Account of Balance of Payments
};

const getYouTubeVideoId = (url: string): string | null => {
  if (!url) return null;
  const match = url.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([\w-]{11})/);
  return match ? match[1] : null;
};

const COURSE_PODCAST_COUNT: Record<string, number> = {
  'a68bae8c-a21c-4cb2-8cd7-6097de211060': 64, // Biology 0610
  'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7': 35, // Co-ordinated Science 0654
  '9331cc50-d76b-4247-860e-25b2096e93cb': 35, // Geography 0460
  '564f9e56-b77c-43af-9299-23eb2e7dcb7e': 29, // Business Studies 0450
};

// =========================================================================================
// THƯ VIỆN ĐỌC PDF - TÍCH HỢP JUMP TO PAGE & VISION AI
// =========================================================================================
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';

pdfjs.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;

const PdfVisionViewer = ({ url, onClose, onCallTutor }: { url: string, onClose: () => void, onCallTutor?: () => void }) => {
  const [numPages, setNumPages] = useState<number | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [pageInput, setPageInput] = useState<string>('1'); 
  const [isLoading, setIsLoading] = useState(true);
  const [isTwoPageMode, setIsTwoPageMode] = useState(false);
  const [zoomLevel, setZoomLevel] = useState<number>(1.2);
  const [isFullscreen, setIsFullscreen] = useState(false);
  
  const viewerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
      setPageInput(currentPage.toString());
  }, [currentPage]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement).tagName)) {
          return;
      }
      
      if (e.key === 'ArrowRight') {
          handleNext();
      } else if (e.key === 'ArrowLeft') {
          handlePrev();
      } else if (e.key === '=' || e.key === '+') {
          handleZoomIn();
      } else if (e.key === '-' || e.key === '_') {
          handleZoomOut();
      }
    };
    
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [numPages, currentPage, isTwoPageMode]);

  useEffect(() => {
    const onFullscreenChange = () => {
        setIsFullscreen(!!document.fullscreenElement);
    };
    document.addEventListener('fullscreenchange', onFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', onFullscreenChange);
  }, []);

  const toggleFullscreen = () => {
      if (!document.fullscreenElement) {
          viewerRef.current?.requestFullscreen().catch(err => console.log(err));
      } else {
          document.exitFullscreen();
      }
  };

  const handlePageRenderSuccess = () => {
    clearTimeout((window as any).pdfCaptureTimeout);
    (window as any).pdfCaptureTimeout = setTimeout(() => {
      setIsLoading(false);
      const canvases = document.querySelectorAll('.react-pdf__Page__canvas');
      
      if (canvases.length > 0) {
        const combinedCanvas = document.createElement('canvas');
        const ctx = combinedCanvas.getContext('2d');
        
        let totalW = 0;
        let maxH = 0;
        
        canvases.forEach(c => {
            totalW += (c as HTMLCanvasElement).width;
            maxH = Math.max(maxH, (c as HTMLCanvasElement).height);
        });

        const MAX_WIDTH = 800;
        const scaleFactor = totalW > MAX_WIDTH ? MAX_WIDTH / totalW : 1;

        combinedCanvas.width = totalW * scaleFactor;
        combinedCanvas.height = maxH * scaleFactor;
        
        let curX = 0;
        canvases.forEach(c => {
            if (ctx) {
                const drawWidth = (c as HTMLCanvasElement).width * scaleFactor;
                const drawHeight = (c as HTMLCanvasElement).height * scaleFactor;
                ctx.drawImage(c as HTMLCanvasElement, curX, 0, drawWidth, drawHeight);
                curX += drawWidth;
            }
        });

        const base64Image = combinedCanvas.toDataURL('image/jpeg', 0.45); 
        (window as any).tonyLatestPdfPageImage = base64Image;
        window.dispatchEvent(new CustomEvent('tony-send-page-image', { detail: base64Image }));
      }
    }, 500);
  };

  const handleNext = () => {
      if (numPages && currentPage < numPages) {
          setIsLoading(true);
          setCurrentPage(p => Math.min(p + (isTwoPageMode ? 2 : 1), numPages || 1));
      }
  };

  const handlePrev = () => {
      if (currentPage > 1) {
          setIsLoading(true);
          setCurrentPage(p => Math.max(p - (isTwoPageMode ? 2 : 1), 1));
      }
  };

  const handlePageInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      setPageInput(e.target.value);
  };

  const handlePageInputSubmit = (e: React.KeyboardEvent<HTMLInputElement>) => {
      if (e.key === 'Enter') {
          let p = parseInt(pageInput);
          if (!isNaN(p)) {
              p = Math.max(1, Math.min(p, numPages || 1));
              setIsLoading(true);
              setCurrentPage(p);
              setPageInput(p.toString());
          } else {
              setPageInput(currentPage.toString());
          }
      }
  };

  const handleZoomIn = () => {
      setZoomLevel(prev => Math.min(prev + 0.2, 3.0));
  };
  
  const handleZoomOut = () => {
      setZoomLevel(prev => Math.max(prev - 0.2, 0.5));
  };

  return (
    <div ref={viewerRef} className="w-full h-full flex flex-col bg-[#0f172a] relative z-20 font-sans">
      <div className="flex flex-wrap items-center justify-between bg-slate-900/90 backdrop-blur-md p-2 md:p-3 shrink-0 border-b border-slate-700/50 shadow-lg gap-2 z-10">
         <div className="flex items-center gap-2 md:gap-4">
             <div className="hidden sm:flex items-center gap-2 text-emerald-400 bg-emerald-950/40 px-3 py-1.5 rounded-full border border-emerald-800/50 shadow-[0_0_10px_rgba(16,185,129,0.1)]">
                <span className="text-sm">🤖</span>
                <span className="text-[11px] md:text-xs font-semibold animate-pulse tracking-wide">AI đang hỗ trợ</span>
             </div>
             <div className="flex items-center bg-slate-800/80 rounded-lg border border-slate-700/50 p-0.5">
                <button onClick={handleZoomOut} className="w-8 h-8 flex items-center justify-center text-slate-400 hover:bg-slate-700 hover:text-white rounded-md transition-all" title="Thu nhỏ (-)">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607zM13.5 10.5h-6" /></svg>
                </button>
                <span className="text-slate-300 text-xs font-semibold font-mono w-12 text-center select-none">
                    {Math.round(zoomLevel * 100)}%
                </span>
                <button onClick={handleZoomIn} className="w-8 h-8 flex items-center justify-center text-slate-400 hover:bg-slate-700 hover:text-white rounded-md transition-all" title="Phóng to (+)">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607zM10.5 7.5v6m3-3h-6" /></svg>
                </button>
             </div>
         </div>
         <div className="flex items-center gap-3 flex-1 justify-center min-w-[250px]">
             <button 
                 onClick={() => { 
                     setIsTwoPageMode(!isTwoPageMode);
                 }}
                 className={`hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all border ${isTwoPageMode ? 'bg-[#0ea5e9]/20 text-[#0ea5e9] border-[#0ea5e9]/30' : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-slate-200'}`}
             >
                 {isTwoPageMode ? (
                     <><span className="text-sm">📖</span> 2 Trang</>
                 ) : (
                     <><span className="text-sm">📄</span> 1 Trang</>
                 )}
             </button>
             <div className="flex items-center gap-1 bg-slate-800/80 rounded-lg p-1 border border-slate-700/50">
                <button 
                    onClick={handlePrev} 
                    disabled={currentPage === 1} 
                    className="text-white px-3 py-1.5 rounded bg-slate-700/50 hover:bg-[#0ea5e9] font-bold text-xs disabled:opacity-30 transition-all shadow-sm"
                >
                    ←
                </button>
                <div className="flex items-center text-slate-400 text-xs font-medium px-2">
                    <input 
                        type="text" 
                        value={pageInput}
                        onChange={handlePageInputChange}
                        onKeyDown={handlePageInputSubmit}
                        onBlur={() => setPageInput(currentPage.toString())}
                        className="w-10 text-center bg-slate-900 text-white font-semibold mx-1 py-1 rounded border border-slate-600 focus:outline-none focus:border-[#0ea5e9] focus:ring-1 focus:ring-[#0ea5e9] transition-all"
                    />
                    <span className="opacity-70 mx-1">/</span> {numPages || '--'}
                </div>
                <button 
                    onClick={handleNext} 
                    disabled={numPages !== null && currentPage >= numPages} 
                    className="text-white px-3 py-1.5 rounded bg-slate-700/50 hover:bg-[#0ea5e9] font-bold text-xs disabled:opacity-30 transition-all shadow-sm"
                >
                    →
                </button>
             </div>
         </div>
         <div className="flex items-center gap-2">
             {onCallTutor && (
                 <button 
                     onClick={onCallTutor}
                     className="flex items-center gap-1.5 px-3 h-9 rounded-lg text-xs font-bold bg-emerald-500/10 border border-emerald-500/30 hover:bg-emerald-500 text-emerald-400 hover:text-white transition-all shadow-sm active:scale-95 shrink-0"
                     title="Vào lớp Học trực tiếp với Gia Sư AI"
                 >
                     <span className="animate-pulse">👨‍🏫</span>
                     <span>Lên Bảng</span>
                 </button>
             )}
             <button 
                onClick={toggleFullscreen} 
                className="w-9 h-9 rounded-lg bg-slate-800 border border-slate-700 hover:bg-slate-700 flex items-center justify-center text-slate-300 hover:text-white transition-all" 
                title="Toàn màn hình"
             >
                 {isFullscreen ? (
                     <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg>
                 ) : (
                     <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>
                 )}
             </button>
             <button 
                onClick={onClose} 
                className="w-9 h-9 rounded-lg bg-red-500/10 border border-red-500/30 hover:bg-red-500 flex items-center justify-center text-red-400 hover:text-white transition-all" 
                title="Đóng tài liệu"
             >
                 <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
             </button>
         </div>
      </div>
      {/* 3D Book styles */}
      <style>{`
        .pdf-page-left { box-shadow: inset -20px 0 30px -15px rgba(0,0,0,0.25), -4px 4px 20px rgba(0,0,0,0.4); }
        .pdf-page-right { box-shadow: inset 20px 0 30px -15px rgba(0,0,0,0.25), 4px 4px 20px rgba(0,0,0,0.4); }
        .pdf-page-single { box-shadow: 0 8px 40px rgba(0,0,0,0.5), 0 2px 10px rgba(0,0,0,0.3); }
      `}</style>
      <div className="flex-1 overflow-auto flex justify-center items-start p-4 md:p-8 bg-[#020617] relative custom-scrollbar scroll-smooth">
         {isLoading && (
            <div className="absolute inset-0 flex flex-col items-center justify-center bg-[#020617]/80 backdrop-blur-sm z-10">
               <div className="w-10 h-10 border-4 border-[#0ea5e9]/20 border-t-[#0ea5e9] rounded-full animate-spin"></div>
               <span className="mt-3 text-slate-400 text-sm font-medium animate-pulse">Đang tải trang tài liệu...</span>
            </div>
         )}
         <Document 
            file={url} 
            onLoadSuccess={({ numPages }) => setNumPages(numPages)} 
            loading={null}
         >
            <div className={`flex justify-center items-start ${isTwoPageMode ? 'gap-0 flex-col lg:flex-row' : ''}`}>
               <Page 
                   pageNumber={currentPage} 
                   scale={zoomLevel} 
                   renderTextLayer={false} 
                   renderAnnotationLayer={false} 
                   onRenderSuccess={handlePageRenderSuccess} 
                   className={`overflow-hidden max-w-full bg-white ${isTwoPageMode ? 'pdf-page-left' : 'pdf-page-single'}`}
                   loading={null} 
               />
               {isTwoPageMode && numPages && currentPage + 1 <= numPages && (
                   <Page 
                       pageNumber={currentPage + 1} 
                       scale={zoomLevel} 
                       renderTextLayer={false} 
                       renderAnnotationLayer={false} 
                       onRenderSuccess={handlePageRenderSuccess} 
                       className="overflow-hidden max-w-full bg-white hidden lg:block pdf-page-right"
                       loading={null} 
                   />
               )}
           </div>
         </Document>
      </div>
    </div>
  );
};
const StaticLectureContent = React.memo(({ html, isIframeOnly, onOpenPopup, onOpenDict, onCloseDict, onSwitchPage }: any) => {
   const iframeRef = useRef<HTMLIFrameElement>(null);
   const [iframeHeight, setIframeHeight] = useState(600);

    // Bỏ các style padding inline cứng có chứa !important do Jodit sinh ra, 
    // và các height/width gán cứng vào table/td/th để tránh bị lỗi hiển thị
    // CHÚ Ý: Chỉ xóa width/height bên trong thẻ <table>, <td>, <th> — KHÔNG xóa tràn lan toàn bộ HTML
    const cleanedHtml = (html || '')
        .replace(/padding(?:-left|-right|-top|-bottom)?:\s*0(?:px)?\s*!important;?/gi, '')
        .replace(/(<(?:table|td|th)\b[^>]*style="[^"]*?)height:\s*\d+px;?\s*/gi, '$1')
        .replace(/(<(?:table|td|th)\b[^>]*style="[^"]*?)width:\s*\d+(?:\.\d+)?px;?\s*/gi, '$1')
        .replace(/<div\b[^>]*class=["']audi["'][^>]*>[\s\S]*?<\/div>/gi, '')
        .replace(/width:\s*(?:1086\.59|1771\.65)px;?/gi, 'max-width: 960px; width: 100%;');

    const currentAudioRef = useRef<HTMLAudioElement | null>(null);
    const mediaRecorderRef = useRef<MediaRecorder | null>(null);
    const audioChunksRef = useRef<Blob[]>([]);
    const activeRecordingCardIdRef = useRef<string | null>(null);
    const activeTargetSentenceRef = useRef<string | null>(null);
    const autoStopTimerRef = useRef<any>(null);
    const audioStreamRef = useRef<MediaStream | null>(null);
    const audioDurationCacheRef = useRef<Map<string, number>>(new Map());

    useEffect(() => {
      const handleHighlight = (e: any) => {
        iframeRef.current?.contentWindow?.postMessage({
          type: 'HIGHLIGHT_LECTURE_SECTION',
          selector: e.detail?.selector,
          autoScroll: e.detail?.autoScroll
        }, '*');
      };
      window.addEventListener('tony-lecture-highlight-section', handleHighlight);
      return () => window.removeEventListener('tony-lecture-highlight-section', handleHighlight);
    }, []);

    const stopAllCurrentAudio = useCallback((notifyIframe: boolean = false) => {
      if (currentAudioRef.current) {
        try {
          currentAudioRef.current.pause();
          currentAudioRef.current.currentTime = 0;
          currentAudioRef.current.onended = null;
          currentAudioRef.current.onerror = null;
          currentAudioRef.current.src = '';
        } catch (e) {
          // ignore
        }
        currentAudioRef.current = null;
      }
      if ('speechSynthesis' in window) {
        try {
          window.speechSynthesis.cancel();
        } catch (e) {
          // ignore
        }
      }
      if (notifyIframe) {
        try {
          iframeRef.current?.contentWindow?.postMessage({
            type: 'STOP_AUDIO_PLAYBACK'
          }, '*');
        } catch (e) {
          // ignore
        }
      }
    }, []);

    const abortRecordingIfActive = useCallback(() => {
      if (activeRecordingCardIdRef.current) {
        if (autoStopTimerRef.current) {
          clearTimeout(autoStopTimerRef.current);
          autoStopTimerRef.current = null;
        }
        if (mediaRecorderRef.current && mediaRecorderRef.current.state !== 'inactive') {
          try {
            mediaRecorderRef.current.onstop = null;
            mediaRecorderRef.current.stop();
          } catch (e) {}
        }
        if (audioStreamRef.current) {
          audioStreamRef.current.getTracks().forEach(t => t.stop());
          audioStreamRef.current = null;
        }
        try {
          iframeRef.current?.contentWindow?.postMessage({
            type: 'PRONUNCIATION_STATUS',
            cardId: activeRecordingCardIdRef.current,
            status: 'STOPPED'
          }, '*');
        } catch (e) {}
        activeRecordingCardIdRef.current = null;
        activeTargetSentenceRef.current = null;
        audioChunksRef.current = [];
      }
    }, []);

    const playBritishPronunciation = useCallback((word: string) => {
      stopAllCurrentAudio(false);
      abortRecordingIfActive();

      const cleanWord = word.trim().toLowerCase().replace(/[^a-z]/g, '');
      if (!cleanWord) return;

      const localUrl = `/audio/pronunciation/${cleanWord}.mp3`;
      const audio = new Audio(localUrl);
      currentAudioRef.current = audio;

      audio.onended = () => {
        if (currentAudioRef.current === audio) {
          currentAudioRef.current = null;
        }
      };

      const playFallbackCloud = () => {
         const cloudUrl = `https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets/audio/pronunciation/${cleanWord}.mp3`;
         const cloudAudio = new Audio(cloudUrl);
         currentAudioRef.current = cloudAudio;
         cloudAudio.onended = () => {
           if (currentAudioRef.current === cloudAudio) {
             currentAudioRef.current = null;
           }
         };
         cloudAudio.play().catch(() => {
            if (currentAudioRef.current === cloudAudio) {
              currentAudioRef.current = null;
            }
            if ('speechSynthesis' in window) {
               window.speechSynthesis.cancel();
               const utter = new SpeechSynthesisUtterance(cleanWord);
               utter.lang = 'en-GB';
               const voices = window.speechSynthesis.getVoices();
               const gbMaleVoice = voices.find(v => 
                  v.lang.toLowerCase().startsWith('en-gb') && 
                  (v.name.toLowerCase().includes('male') || 
                   v.name.toLowerCase().includes('george') || 
                   v.name.toLowerCase().includes('ryan') || 
                   v.name.toLowerCase().includes('thomas') ||
                   v.name.toLowerCase().includes('daniel') ||
                   v.name.toLowerCase().includes('oliver'))
               ) || voices.find(v => v.lang.toLowerCase().startsWith('en-gb'));
               if (gbMaleVoice) {
                  utter.voice = gbMaleVoice;
               }
               utter.rate = 0.85;
               window.speechSynthesis.speak(utter);
            }
         });
      };

      audio.play().catch(() => {
         if (currentAudioRef.current === audio) {
           currentAudioRef.current = null;
         }
         playFallbackCloud();
      });
    }, [stopAllCurrentAudio, abortRecordingIfActive]);

    const playBritishSentence = useCallback((sentence: string, audioKey: string) => {
      stopAllCurrentAudio(false);
      abortRecordingIfActive();

      if (!sentence && !audioKey) return;

      const notifyAudioEnded = () => {
        try {
          iframeRef.current?.contentWindow?.postMessage({
            type: 'STOP_AUDIO_PLAYBACK'
          }, '*');
        } catch (e) {}
      };

      const localUrl = `/audio/communication/sentences/${audioKey}.mp3`;
      const audio = new Audio(localUrl);
      currentAudioRef.current = audio;

      if (audioKey) {
        audio.onloadedmetadata = () => {
          if (audio.duration && !isNaN(audio.duration) && audio.duration > 0) {
            audioDurationCacheRef.current.set(audioKey, audio.duration);
          }
        };
      }

      audio.onended = () => {
        if (currentAudioRef.current === audio) {
          currentAudioRef.current = null;
        }
        notifyAudioEnded();
      };

      const playFallbackCloud = () => {
         const cloudUrl = `https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets/audio/communication/sentences/${audioKey}.mp3`;
         const cloudAudio = new Audio(cloudUrl);
         currentAudioRef.current = cloudAudio;
         if (audioKey) {
           cloudAudio.onloadedmetadata = () => {
             if (cloudAudio.duration && !isNaN(cloudAudio.duration) && cloudAudio.duration > 0) {
               audioDurationCacheRef.current.set(audioKey, cloudAudio.duration);
             }
           };
         }
         cloudAudio.onended = () => {
           if (currentAudioRef.current === cloudAudio) {
             currentAudioRef.current = null;
           }
           notifyAudioEnded();
         };
         cloudAudio.play().catch(() => {
            if (currentAudioRef.current === cloudAudio) {
              currentAudioRef.current = null;
            }
            if ('speechSynthesis' in window) {
               window.speechSynthesis.cancel();
               const utter = new SpeechSynthesisUtterance(sentence);
               utter.lang = 'en-GB';
               const voices = window.speechSynthesis.getVoices();
               const gbMaleVoice = voices.find(v => 
                  v.lang.toLowerCase().startsWith('en-gb') && 
                  (v.name.toLowerCase().includes('male') || 
                   v.name.toLowerCase().includes('george') || 
                   v.name.toLowerCase().includes('ryan') || 
                   v.name.toLowerCase().includes('thomas') ||
                   v.name.toLowerCase().includes('daniel') ||
                   v.name.toLowerCase().includes('oliver'))
               ) || voices.find(v => v.lang.toLowerCase().startsWith('en-gb'));
               if (gbMaleVoice) {
                  utter.voice = gbMaleVoice;
               }
               utter.rate = 0.88;
               utter.onend = () => {
                 notifyAudioEnded();
               };
               utter.onerror = () => {
                 notifyAudioEnded();
               };
               window.speechSynthesis.speak(utter);
            } else {
               notifyAudioEnded();
            }
         });
      };

      audio.play().catch(() => {
         if (currentAudioRef.current === audio) {
           currentAudioRef.current = null;
         }
         playFallbackCloud();
      });
    }, [stopAllCurrentAudio, abortRecordingIfActive]);

    const playChimeSound = useCallback((isSuccess: boolean) => {
      try {
        const AudioCtx = window.AudioContext || (window as any).webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        if (isSuccess) {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
          osc.frequency.setValueAtTime(659.25, ctx.currentTime + 0.12); // E5
          osc.frequency.setValueAtTime(783.99, ctx.currentTime + 0.24); // G5
          gain.gain.setValueAtTime(0.12, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.5);
          osc.start();
          osc.stop(ctx.currentTime + 0.5);
        } else {
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(329.63, ctx.currentTime); // E4
          osc.frequency.setValueAtTime(261.63, ctx.currentTime + 0.15); // C4
          gain.gain.setValueAtTime(0.1, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.4);
          osc.start();
          osc.stop(ctx.currentTime + 0.4);
        }
      } catch (e) {
        // Ignore audio context error
      }
    }, []);

    const stopRecordingAndEvaluate = useCallback(() => {
      stopAllCurrentAudio(true);
      if (autoStopTimerRef.current) {
        clearTimeout(autoStopTimerRef.current);
        autoStopTimerRef.current = null;
      }
      const cardId = activeRecordingCardIdRef.current;
      const targetSentence = activeTargetSentenceRef.current;
      
      if (!cardId || !mediaRecorderRef.current || mediaRecorderRef.current.state === 'inactive') {
        return;
      }

      iframeRef.current?.contentWindow?.postMessage({
        type: 'PRONUNCIATION_STATUS',
        cardId: cardId,
        status: 'EVALUATING'
      }, '*');

      mediaRecorderRef.current.onstop = async () => {
        if (audioStreamRef.current) {
          audioStreamRef.current.getTracks().forEach(t => t.stop());
          audioStreamRef.current = null;
        }

        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        audioChunksRef.current = [];

        try {
          const reader = new FileReader();
          reader.readAsDataURL(audioBlob);
          reader.onloadend = async () => {
            const base64Data = (reader.result as string)?.split(',')[1];
            if (!base64Data) {
              iframeRef.current?.contentWindow?.postMessage({
                type: 'PRONUNCIATION_ERROR',
                cardId: cardId,
                error: 'Không ghi nhận được âm thanh. Vui lòng thử lại!'
              }, '*');
              return;
            }

            const prompt = `You are a friendly and accurate English pronunciation checker for an English learner.
The student is trying to speak the following target sentence:
"${targetSentence}"

Please listen to the attached student audio recording:
1. Determine what words the student actually spoke.
2. Check if the pronunciation of each word is correct and understandable.
3. Compare against the target sentence.
4. Calculate an accuracy_score between 0 and 100.
5. Provide a list of mispronounced_words (words from the sentence that were pronounced incorrectly or skipped). If all correct, return empty array.
6. Provide a short, encouraging feedback in Vietnamese (max 1-2 sentences), pointing out which sound or word to improve.
7. Set is_correct to true if accuracy_score >= 70, else false.

CRITICAL: Return ONLY valid JSON in this exact structure without markdown or backticks:
{
  "recognized_text": "...",
  "accuracy_score": 85,
  "is_correct": true,
  "mispronounced_words": [],
  "feedback": "..."
}`;

            const { data, error } = await supabase.functions.invoke('ai-grader', {
              body: {
                prompt,
                base64Audio: base64Data,
                model: 'gemini-2.5-flash'
              }
            });

            if (error) {
              throw new Error(error.message);
            }

            let resultData: any = null;
            if (data?.result && typeof data.result === 'string') {
              try {
                const cleanedJson = data.result.replace(/```(?:json)?/gi, '').replace(/```/g, '').trim();
                resultData = JSON.parse(cleanedJson);
              } catch (parseErr) {
                resultData = {
                  is_correct: false,
                  accuracy_score: 50,
                  recognized_text: targetSentence || '',
                  mispronounced_words: [],
                  feedback: data.result || 'Hãy thử đọc lại rõ ràng hơn nhé!'
                };
              }
            } else if (data?.result && typeof data.result === 'object') {
              resultData = data.result;
            } else if (typeof data === 'object') {
              resultData = data;
            }

            if (resultData) {
              playChimeSound(resultData.is_correct);

              iframeRef.current?.contentWindow?.postMessage({
                type: 'PRONUNCIATION_RESULT',
                cardId: cardId,
                result: resultData
              }, '*');
            }
          };
        } catch (err: any) {
          console.error('Lỗi khi chấm phát âm:', err);
          iframeRef.current?.contentWindow?.postMessage({
            type: 'PRONUNCIATION_ERROR',
            cardId: cardId,
            error: 'Có lỗi khi kết nối với AI chấm phát âm. Vui lòng thử lại!'
          }, '*');
        } finally {
          activeRecordingCardIdRef.current = null;
          activeTargetSentenceRef.current = null;
        }
      };

      mediaRecorderRef.current.stop();
    }, [playChimeSound, stopAllCurrentAudio]);

    const startRecordingSentence = useCallback(async (cardId: string, targetSentence: string, audioKey?: string) => {
      stopAllCurrentAudio(true);

      if (activeRecordingCardIdRef.current && mediaRecorderRef.current?.state !== 'inactive') {
        stopRecordingAndEvaluate();
      }

      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        audioStreamRef.current = stream;
        activeRecordingCardIdRef.current = cardId;
        activeTargetSentenceRef.current = targetSentence;
        audioChunksRef.current = [];

        let mimeType = 'audio/webm';
        if (!MediaRecorder.isTypeSupported('audio/webm')) {
          mimeType = MediaRecorder.isTypeSupported('audio/mp4') ? 'audio/mp4' : '';
        }

        const mediaRecorder = mimeType ? new MediaRecorder(stream, { mimeType }) : new MediaRecorder(stream);
        mediaRecorderRef.current = mediaRecorder;

        mediaRecorder.ondataavailable = (event) => {
          if (event.data.size > 0) {
            audioChunksRef.current.push(event.data);
          }
        };

        mediaRecorder.start(250);

        iframeRef.current?.contentWindow?.postMessage({
          type: 'PRONUNCIATION_STATUS',
          cardId: cardId,
          status: 'RECORDING'
        }, '*');

        // Tính toán thời lượng thu âm thông minh:
        // So sánh với thời lượng của câu đọc mẫu bên cạnh và cộng thêm 2-3 giây đệm để học sinh đọc thoải mái
        const wordCount = (targetSentence || '').trim().split(/\s+/).filter(Boolean).length;
        // Cơ bản: người học cần ~850ms/từ + 3.5s đệm (chuẩn bị, lấy hơi, ngắt nghỉ), tối thiểu 7.5s
        const baseSpeakingMs = Math.max(7500, wordCount * 850 + 3500);

        let finalTimeoutMs = baseSpeakingMs;

        const applyTimeout = (durMs: number) => {
          if (autoStopTimerRef.current) {
            clearTimeout(autoStopTimerRef.current);
          }
          autoStopTimerRef.current = setTimeout(() => {
            stopRecordingAndEvaluate();
          }, durMs);
        };

        if (audioKey) {
          if (audioDurationCacheRef.current.has(audioKey)) {
            const sampleDur = audioDurationCacheRef.current.get(audioKey)!;
            // Thời lượng câu mẫu nhân hệ số tốc độ người học 1.35x + thêm 2.5s đệm (hoặc tối thiểu mẫu + 2.0s)
            const sampleBasedMs = Math.max(
              Math.round(sampleDur * 1000 * 1.35 + 2500),
              Math.round((sampleDur + 2.0) * 1000)
            );
            finalTimeoutMs = Math.max(baseSpeakingMs, sampleBasedMs);
            applyTimeout(finalTimeoutMs);
          } else {
            // Đặt timer cơ bản trước trong lúc load metadata câu đọc mẫu
            applyTimeout(finalTimeoutMs);

            const localUrl = `/audio/communication/sentences/${audioKey}.mp3`;
            const cloudUrl = `https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets/audio/communication/sentences/${audioKey}.mp3`;
            const probeAudio = new Audio(localUrl);

            const onProbeLoaded = (dur: number) => {
              if (dur && !isNaN(dur) && dur > 0) {
                audioDurationCacheRef.current.set(audioKey, dur);
                const sampleBasedMs = Math.max(
                  Math.round(dur * 1000 * 1.35 + 2500),
                  Math.round((dur + 2.0) * 1000)
                );
                const adjustedTimeout = Math.max(baseSpeakingMs, sampleBasedMs);
                if (adjustedTimeout > finalTimeoutMs && activeRecordingCardIdRef.current === cardId) {
                  finalTimeoutMs = adjustedTimeout;
                  applyTimeout(finalTimeoutMs);
                }
              }
            };

            probeAudio.onloadedmetadata = () => onProbeLoaded(probeAudio.duration);
            probeAudio.onerror = () => {
              const probeCloud = new Audio(cloudUrl);
              probeCloud.onloadedmetadata = () => onProbeLoaded(probeCloud.duration);
            };
          }
        } else {
          applyTimeout(finalTimeoutMs);
        }

      } catch (err: any) {
        console.error('Lỗi truy cập micro:', err);
        iframeRef.current?.contentWindow?.postMessage({
          type: 'PRONUNCIATION_ERROR',
          cardId: cardId,
          error: 'Không thể truy cập Micro. Vui lòng cấp quyền Micro cho trình duyệt để kiểm tra phát âm!'
        }, '*');
        activeRecordingCardIdRef.current = null;
        activeTargetSentenceRef.current = null;
      }
    }, [stopAllCurrentAudio, stopRecordingAndEvaluate]);

    useEffect(() => { 
        // Giữ chiều cao an toàn tối thiểu thay vì 10px để màn hình không bị giật hoặc trắng khi đổi bài
        setIframeHeight(prev => (prev > 500 ? prev : 600)); 
    }, [html]);

    useEffect(() => {
      return () => {
        stopAllCurrentAudio(true);
        if (autoStopTimerRef.current) clearTimeout(autoStopTimerRef.current);
        if (mediaRecorderRef.current && mediaRecorderRef.current.state !== 'inactive') {
          mediaRecorderRef.current.stop();
        }
        if (audioStreamRef.current) {
          audioStreamRef.current.getTracks().forEach(t => t.stop());
        }
      };
    }, [stopAllCurrentAudio]);

    useEffect(() => {
      const handleMessage = (e: MessageEvent) => {
        if (e.data?.type === 'LECTURE_LINK_CLICK') {
          let href = e.data.href;
          if (href.startsWith('/')) {
              href = window.location.origin + href;
          }

          if (href.includes('tonyenglish.vn/uploads') || 
              href.includes('youtube.com') || 
              href.includes('youtu.be') || 
              href.toLowerCase().includes('.pdf')) {
              onOpenPopup(href);
          } else { 
              window.open(href, '_blank', 'noopener,noreferrer');
          }
        } else if (e.data?.type === 'LECTURE_PLAY_WORD') {
          const rawWord = e.data.word || '';
          playBritishPronunciation(rawWord);
        } else if (e.data?.type === 'LECTURE_PLAY_SENTENCE') {
          playBritishSentence(e.data.sentence || '', e.data.audioKey || '');
        } else if (e.data?.type === 'LECTURE_START_RECORDING') {
          startRecordingSentence(e.data.cardId, e.data.targetSentence, e.data.audioKey);
        } else if (e.data?.type === 'LECTURE_STOP_RECORDING') {
          stopRecordingAndEvaluate();
        } else if (e.data?.type === 'LECTURE_STOP_AUDIO') {
          stopAllCurrentAudio(true);
        } else if (e.data?.type === 'LECTURE_RESIZE') {
          const h = e.data.height;
          if (h && h > 0) {
              const targetHeight = Math.max(400, Math.ceil(h) + 16);
              setIframeHeight((prev: number) => {
                if (Math.abs(prev - targetHeight) <= 6) return prev;
                return targetHeight;
              });
          }
        } else if (e.data?.type === 'LECTURE_OPEN_DICT') {
          if (iframeRef.current) {
             const rect = iframeRef.current.getBoundingClientRect();
             onOpenDict(e.data.word, rect.left + e.data.x, rect.top + e.data.y, rect.top + e.data.rectTop);
          }
        } else if (e.data?.type === 'LECTURE_CLOSE_DICT') {
          onCloseDict();
        } else if (e.data?.type === 'OPEN_IELTS_AI') {
          const fakeBtn = document.createElement('button');
          fakeBtn.className = 'btn-ai-trigger hidden'; 
          
          if (e.data.topic) {
              fakeBtn.setAttribute('data-topic', e.data.topic);
          }
          if (e.data.image) {
              fakeBtn.setAttribute('data-image', e.data.image);
          }
          if (e.data.task) {
              fakeBtn.setAttribute('data-task', e.data.task);
          }
          
          document.body.appendChild(fakeBtn);
          fakeBtn.click();
          setTimeout(() => { 
              fakeBtn.remove(); 
          }, 100);
        } 
        else if (e.data?.type === 'OPEN_LIVE_SPEAKING') {
          const fakeLiveBtn = document.createElement('button');
          fakeLiveBtn.className = 'btn-live-trigger hidden';
          
          if (e.data.topic) {
              fakeLiveBtn.setAttribute('data-topic', e.data.topic);
          }
          
          document.body.appendChild(fakeLiveBtn);
          fakeLiveBtn.click();
          setTimeout(() => { 
              fakeLiveBtn.remove(); 
          }, 100);
        }
        else if (e.data?.type === 'LECTURE_PLAY_SECTION') {
          window.dispatchEvent(new CustomEvent('tony-lecture-play-section', { detail: { sectionId: e.data.sectionId } }));
        }
        else if (e.data?.type === 'LECTURE_SWITCH_PAGE') {
          const targetP = parseInt(e.data.page, 10);
          if (onSwitchPage && !isNaN(targetP)) {
            onSwitchPage(targetP);
          }
        }
      };
      
      window.addEventListener('message', handleMessage);
      return () => window.removeEventListener('message', handleMessage);
    }, [onOpenPopup, onOpenDict, onCloseDict, onSwitchPage, playBritishPronunciation, playBritishSentence, startRecordingSentence, stopRecordingAndEvaluate, stopAllCurrentAudio]);

   const iframeContent = `
     <!DOCTYPE html>
     <html lang="vi">
     <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
       <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
       <style>
         :root {
            --brand-color: #0ea5e9;
            --text-main: #334155;
            --bg-light: #f8fafc;
         }
         .lang-switch-bar {
             display: none !important;
         }
         html, body { 
             height: max-content !important;
             min-height: 0 !important;
             margin: 0; padding: 0; 
             font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
             color: var(--text-main);
             background: transparent; overflow: hidden; 
             line-height: 1.75;
             font-size: 17px;
             -webkit-font-smoothing: antialiased;
         }
         * { 
             box-sizing: border-box; 
             word-wrap: break-word;
             overflow-wrap: break-word;
         }
         
         /* Typography Styling cho Học thuật */
         h1, h2, h3, h4 { 
             color: #0f172a;
             font-weight: 700; 
             margin-top: 1.5em; 
             margin-bottom: 0.5em; 
             line-height: 1.3; 
         }
         h1 { 
             font-size: 1.75rem;
             border-bottom: 2px solid #e2e8f0; 
             padding-bottom: 0.3em; 
         }
         h2 { font-size: 1.5rem; }
         h3 { font-size: 1.25rem; }
         p { margin-top: 0; margin-bottom: 1.25rem; }
         
         /* Media & Elements */
         img, video { 
              max-width: 100%;
              height: auto; 
              display: block; 
              margin: 1.5rem auto; 
          }
          iframe {
               width: 100% !important;
               aspect-ratio: 16 / 9;
               border: none !important;
               margin: 0 !important;
               border-radius: 8px;
               display: block;
          }
          .iframe-only-mode iframe {
              margin: 0 !important;
              border-radius: 0 !important;
              box-shadow: none !important;
              width: 100% !important;
              min-height: 85vh !important;
          }
         svg { max-width: 100%; height: auto; pointer-events: all !important; }
         
         /* Links */
         a { 
             cursor: pointer;
             color: var(--brand-color); 
             text-decoration: none; 
             font-weight: 600; 
             border-bottom: 1px transparent; 
             transition: all 0.2s;
         }
         a:hover { 
             color: #0284c7;
             text-decoration: underline; 
             text-underline-offset: 4px; 
         }
         ::selection { background: #bae6fd; color: #0369a1; }
         
         /* EdTech Specifics */
         blockquote { 
            border-left: 4px solid var(--brand-color);
            background: var(--bg-light); 
            margin: 1.5rem 0; 
            padding: 1rem 1.5rem; 
            border-radius: 0 8px 8px 0;
            font-style: italic; 
            color: #475569;
         }
          
          /* Vietnamese translation style */
          .vi { 
              color: #64748b; 
              font-style: italic; 
              font-size: 15px; 
              margin-top: 6px; 
              margin-bottom: 16px; 
              border-left: 3px solid #cbd5e1; 
              padding-left: 12px; 
          }
          ul.vi, ol.vi { 
              padding-left: 32px !important; 
              margin-top: 4px !important; 
          }
          .vi ul, .vi ol { 
              padding-left: 24px !important; 
              margin: 4px 0 4px 0; 
          }
          .vi li, ul.vi li, ol.vi li { 
              margin-bottom: 4px; 
          }
          
         table { 
             border-collapse: collapse;
             width: 100% !important; 
             margin-bottom: 1.5rem; 
             border-radius: 8px; 
             box-shadow: 0 1px 3px rgba(0,0,0,0.05);
         }
         table th, table td { 
             border: 1px solid #94a3b8 !important;
             padding: 1rem 1.5rem !important; 
             vertical-align: top; 
         }
         table th { 
             background-color: var(--bg-light) !important;
             font-weight: 600; 
             text-align: left; 
             color: #0f172a; 
         }
         table tr:nth-child(even) { background-color: #fcfcfc !important; }
         code { 
             font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
             font-size: 0.9em; 
             background: #f1f5f9; 
             padding: 0.2em 0.4em; 
             border-radius: 4px; 
             color: #db2777;
         }
         pre code { background: transparent; padding: 0; color: inherit; }
         pre { 
             background: #1e293b;
             color: #f8fafc; 
             padding: 1.25rem; 
             border-radius: 12px; 
             overflow-x: auto; 
             margin-bottom: 1.5rem; 
             font-size: 0.9rem;
         }
          @media (max-width: 640px) {
              body { font-size: 15px; }
              h1 { font-size: 1.4rem; }
              h2 { font-size: 1.25rem; }
              h3 { font-size: 1.1rem; }
              table th, table td { 
                  padding: 0.5rem 0.65rem !important; 
                  font-size: 13.5px; 
              }
              pre { padding: 0.75rem; font-size: 0.8rem; }
          }
          
          #content-wrapper { display: flow-root; width: 100%; padding: 24px 14px 2rem 14px; box-sizing: border-box; }
          .audi { display: none !important; width: 0 !important; height: 0 !important; overflow: hidden !important; }
          #lib_content { width: 100% !important; max-width: 960px !important; margin: 0 auto !important; box-sizing: border-box !important; }
          .audiolink a, [data-word] {
              cursor: pointer !important;
              transition: all 0.2s ease !important;
              display: inline-block;
          }
          .audiolink a:hover, [data-word]:hover {
              color: #0284c7 !important;
              text-decoration: underline !important;
          }

          /* Interactive Lecture Highlight */
          .active-lecture-highlight {
              outline: 3px solid #0284c7 !important;
              outline-offset: -2px !important;
              box-shadow: 0 0 25px rgba(2, 132, 199, 0.45) !important;
              border-radius: 12px !important;
              background-color: #f0f9ff !important;
              transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
              position: relative !important;
              box-sizing: border-box !important;
          }
          .active-lecture-highlight::before {
              content: "🎙️ Đang giảng...";
              position: absolute;
              top: -12px;
              right: 12px;
              background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
              color: #ffffff;
              font-size: 11px;
              font-weight: 800;
              padding: 3px 10px;
              border-radius: 20px;
              box-shadow: 0 2px 8px rgba(0,0,0,0.2);
              z-index: 50;
              letter-spacing: 0.5px;
              pointer-events: none;
          }
          /* SVG Element Active Highlight */
          g.active-lecture-highlight circle,
          g.active-lecture-highlight rect,
          g.active-lecture-highlight path {
              stroke: #0284c7 !important;
              stroke-width: 4px !important;
              filter: drop-shadow(0 0 10px rgba(2, 132, 199, 0.95)) !important;
              animation: pulse-svg-active 1.5s infinite alternate !important;
          }
          @keyframes pulse-svg-active {
              0% { filter: drop-shadow(0 0 4px rgba(2, 132, 199, 0.6)); }
              100% { filter: drop-shadow(0 0 14px rgba(2, 132, 199, 1)); }
          }
          .active-svg-parent-highlight {
              outline: 2px dashed #0284c7 !important;
              outline-offset: 4px !important;
              border-radius: 12px !important;
          }
          [data-lecture-section] {
              cursor: pointer !important;
              transition: all 0.2s ease !important;
          }
          [data-lecture-section]:hover {
              filter: brightness(0.97);
          }

          .sentence-audio-card {
              cursor: pointer !important;
              transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
              user-select: none;
          }
          .sentence-audio-card:hover {
              background-color: #f0f9ff !important;
              border-left-color: #0284c7 !important;
              transform: translateY(-1px);
              box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
          }
          .sentence-audio-card:hover .speaker-icon {
              transform: scale(1.18);
              opacity: 1 !important;
          }
          .sentence-audio-card:active {
              transform: translateY(0);
              background-color: #e0f2fe !important;
          }
          .sentence-audio-card.is-playing {
              background-color: #e0f2fe !important;
              border-left-color: #0284c7 !important;
          }
          .sentence-audio-card.is-playing .speaker-icon {
              transform: scale(1.18);
              opacity: 1 !important;
              color: #0284c7 !important;
          }
          .card-actions {
              display: inline-flex !important;
              align-items: center !important;
              gap: 8px !important;
              margin-left: 8px !important;
              flex-shrink: 0 !important;
          }
          .sentence-mic-btn {
              display: inline-flex !important;
              align-items: center !important;
              justify-content: center !important;
              width: 28px !important;
              height: 28px !important;
              border-radius: 50% !important;
              background: #ffffff !important;
              border: 1px solid #cbd5e1 !important;
              cursor: pointer !important;
              font-size: 13px !important;
              line-height: 1 !important;
              padding: 0 !important;
              transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
              position: relative !important;
              user-select: none !important;
              outline: none !important;
              box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
          }
          .sentence-mic-btn:hover {
              background: #f0f9ff !important;
              border-color: #38bdf8 !important;
              transform: scale(1.12) !important;
              box-shadow: 0 2px 5px rgba(2, 132, 199, 0.2) !important;
          }
          .sentence-mic-btn.is-recording {
              background: #ef4444 !important;
              border-color: #dc2626 !important;
              color: #ffffff !important;
              animation: pulse-mic 1.1s infinite ease-in-out !important;
          }
          .sentence-mic-btn.is-evaluating {
              background: #f59e0b !important;
              border-color: #d97706 !important;
              color: #ffffff !important;
              animation: spin-mic 1s infinite linear !important;
          }
          @keyframes pulse-mic {
              0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); transform: scale(1.05); }
              70% { box-shadow: 0 0 0 8px rgba(239, 68, 68, 0); transform: scale(1.15); }
              100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); transform: scale(1.05); }
          }
          @keyframes spin-mic {
              0% { transform: rotate(0deg); }
              100% { transform: rotate(360deg); }
          }
          .pronunciation-feedback {
              width: 100% !important;
              box-sizing: border-box !important;
              animation: feedback-slide-down 0.25s ease-out !important;
          }
          .retry-pronunciation-btn {
              font-size: 12px !important;
              font-weight: bold !important;
              color: #b91c1c !important;
              background: #ffffff !important;
              border: 1px solid #f87171 !important;
              padding: 4px 10px !important;
              border-radius: 6px !important;
              cursor: pointer !important;
              transition: all 0.15s ease !important;
              box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
          }
          .retry-pronunciation-btn:hover {
              background-color: #fee2e2 !important;
          }
          .retry-pronunciation-btn.is-warning {
              color: #92400e !important;
              border-color: #fbbf24 !important;
              padding: 3px 8px !important;
              border-radius: 4px !important;
          }
          .retry-pronunciation-btn.is-warning:hover {
              background-color: #fef3c7 !important;
          }
          @keyframes feedback-slide-down {
              from { opacity: 0; transform: translateY(-4px); }
              to { opacity: 1; transform: translateY(0); }
          }

           /* INTERACTIVE DIALOGUE PRACTICE */
           .dialogue-practice-box {
               background: #ffffff !important;
               border: 1.5px solid #cbd5e1 !important;
               border-radius: 14px !important;
               padding: 16px 18px !important;
               margin-bottom: 24px !important;
               box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04) !important;
               transition: all 0.2s ease !important;
           }
           .practice-toolbar {
               display: flex !important;
               align-items: center !important;
               flex-wrap: wrap !important;
               gap: 10px !important;
               padding-bottom: 12px !important;
               margin-bottom: 12px !important;
               border-bottom: 1px solid #e2e8f0 !important;
           }
           .practice-toolbar .toolbar-label {
               font-size: 13px !important;
               font-weight: 800 !important;
               color: #475569 !important;
               margin-right: 4px !important;
               text-transform: uppercase !important;
               letter-spacing: 0.5px !important;
           }
           .btn-dialogue-play {
               display: inline-flex !important;
               align-items: center !important;
               gap: 6px !important;
               padding: 7px 14px !important;
               font-size: 13px !important;
               font-weight: 700 !important;
               border-radius: 8px !important;
               border: 1px solid transparent !important;
               cursor: pointer !important;
               transition: all 0.15s ease !important;
               user-select: none !important;
           }
           .btn-dialogue-play.btn-mode-all {
               background: #eff6ff !important;
               color: #1d4ed8 !important;
               border-color: #bfdbfe !important;
           }
           .btn-dialogue-play.btn-mode-all:hover {
               background: #dbeafe !important;
           }
           .btn-dialogue-play.btn-mode-a {
               background: #f0fdf4 !important;
               color: #15803d !important;
               border-color: #bbf7d0 !important;
           }
           .btn-dialogue-play.btn-mode-a:hover {
               background: #dcfce7 !important;
           }
           .btn-dialogue-play.btn-mode-b {
               background: #fdf4ff !important;
               color: #a21caf !important;
               border-color: #f5d0fe !important;
           }
           .btn-dialogue-play.btn-mode-b:hover {
               background: #fae8ff !important;
           }
           .btn-dialogue-play.is-active-btn {
               background: #fee2e2 !important;
               color: #b91c1c !important;
               border-color: #fca5a5 !important;
               box-shadow: 0 0 0 2px rgba(239, 68, 68, 0.25) !important;
               animation: pulse-active-btn 1.2s infinite alternate !important;
           }
           @keyframes pulse-active-btn {
               from { transform: scale(1); }
               to { transform: scale(1.03); }
           }
            .dialogue-turn-row {
                display: flex !important;
                align-items: flex-start !important;
                justify-content: space-between !important;
                gap: 12px !important;
                transition: all 0.2s ease !important;
            }
            .dialogue-turn-row:not(.sentence-audio-card) {
                padding: 10px 14px !important;
                margin-bottom: 8px !important;
                border-radius: 10px !important;
                border-left: 4px solid transparent !important;
                background: #f8fafc !important;
            }
            .dialogue-turn-row:not(.sentence-audio-card):last-child {
                margin-bottom: 0 !important;
            }
            .dialogue-turn-row.speaker-role-a:not(.sentence-audio-card) {
                border-left-color: #3b82f6 !important;
            }
            .dialogue-turn-row.speaker-role-b:not(.sentence-audio-card) {
                border-left-color: #10b981 !important;
            }
            .dialogue-turn-row.is-active-turn {
                background: #eff6ff !important;
                border-left-color: #2563eb !important;
                border-left-width: 4px !important;
                border-left-style: solid !important;
                box-shadow: 0 2px 10px rgba(37, 99, 235, 0.15) !important;
                transform: translateX(4px) !important;
            }
            .dialogue-turn-row.is-muted-turn {
                background: #fefce8 !important;
                border-left-color: #eab308 !important;
                border-left-width: 4px !important;
                border-left-style: solid !important;
                box-shadow: 0 2px 10px rgba(234, 179, 8, 0.2) !important;
                transform: translateX(4px) !important;
            }
            .dialogue-turn-content {
                flex: 1 !important;
           }
           .dialogue-turn-content .speaker-label {
               font-weight: 800 !important;
               font-size: 15px !important;
               margin-right: 6px !important;
           }
           .dialogue-turn-content .speaker-label.speaker-a {
               color: #2563eb !important;
           }
           .dialogue-turn-content .speaker-label.speaker-b {
               color: #059669 !important;
           }
           .dialogue-turn-content .turn-text {
               font-size: 16px !important;
               line-height: 1.5 !important;
               color: #1e293b !important;
           }
            .user-prompt-tag {
                display: inline-flex !important;
                align-items: center !important;
                flex-wrap: wrap !important;
                gap: 6px !important;
                margin-left: 8px !important;
                padding: 3px 10px !important;
                border-radius: 6px !important;
                font-size: 12.5px !important;
                font-weight: 800 !important;
                background: #fef08a !important;
                color: #854d0e !important;
                border: 1px solid #fde047 !important;
                box-shadow: 0 1px 3px rgba(133, 77, 14, 0.12) !important;
            }
            .btn-skip-silence {
                display: inline-flex !important;
                align-items: center !important;
                gap: 4px !important;
                padding: 2px 8px !important;
                font-size: 11px !important;
                font-weight: 700 !important;
                color: #854d0e !important;
                background: #ffffff !important;
                border: 1px solid #eab308 !important;
                border-radius: 999px !important;
                cursor: pointer !important;
                transition: all 0.15s ease !important;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08) !important;
                user-select: none !important;
            }
            .btn-skip-silence:hover {
                background: #fef9c3 !important;
                border-color: #ca8a04 !important;
                color: #713f12 !important;
                transform: scale(1.04) !important;
            }
            .btn-skip-silence:active {
                transform: scale(0.97) !important;
            }
            @keyframes pulse-prompt {
                from { opacity: 0.85; transform: scale(0.97); }
                to { opacity: 1; transform: scale(1.03); }
            }
           .turn-action-buttons {
               display: flex !important;
               align-items: center !important;
               gap: 6px !important;
               flex-shrink: 0 !important;
           }
           .turn-spk-btn {
               background: #ffffff !important;
               border: 1px solid #cbd5e1 !important;
               border-radius: 50% !important;
               width: 32px !important;
               height: 32px !important;
               display: flex !important;
               align-items: center !important;
               justify-content: center !important;
               font-size: 14px !important;
               cursor: pointer !important;
               transition: all 0.15s ease !important;
               box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
           }
           .turn-spk-btn:hover {
               background: #eff6ff !important;
               border-color: #3b82f6 !important;
               transform: scale(1.08) !important;
           }
       </style>
     </head>
     <body class="${isIframeOnly ? 'iframe-only-mode' : ''}">
       <div style="width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch;">
           <div id="content-wrapper">${cleanedHtml ? cleanedHtml.replace(/viewbox=/gi, 'viewBox=') : ''}</div>
       </div>
       <script>
         window.playWord = function(w) {
           if (w) window.parent.postMessage({ type: 'LECTURE_PLAY_WORD', word: w }, '*');
         };
         window.playSentence = function(sentence, audioKey) {
           if (typeof stopActiveDialoguePlayer === 'function') {
             stopActiveDialoguePlayer();
           }
           if (sentence || audioKey) {
             window.parent.postMessage({ type: 'LECTURE_PLAY_SENTENCE', sentence: sentence, audioKey: audioKey }, '*');
           }
         };
         window.playaudio = function(w) {
           if (w) {
             var clean = w.replace(/.*[\/\\]([^\/\\]+)\.mp3$/i, '$1').replace(/[^a-zA-Z]/g, '');
             window.parent.postMessage({ type: 'LECTURE_PLAY_WORD', word: clean || w }, '*');
           }
         };

         function enhanceSentenceCards() {
           var cards = document.querySelectorAll('.sentence-audio-card');
           cards.forEach(function(card, idx) {
               var sentence = card.getAttribute('data-sentence');
               if (!sentence) return;

               var cardId = card.getAttribute('data-card-id');
               if (!cardId) {
                   cardId = 'card_sc_' + idx;
                   card.setAttribute('data-card-id', cardId);
               }

               var existingMic = card.querySelector('.sentence-mic-btn');
               if (!existingMic) {
                   var spkIcon = card.querySelector('.speaker-icon');
                    var micBtn = document.createElement('button');
                    micBtn.className = 'sentence-mic-btn';
                    micBtn.setAttribute('type', 'button');
                    micBtn.setAttribute('data-card-id', cardId);
                    micBtn.setAttribute('data-sentence', sentence);
                    var audioKey = card.getAttribute('data-audio-key') || '';
                    if (audioKey) {
                        micBtn.setAttribute('data-audio-key', audioKey);
                    }
                    micBtn.title = 'Kiểm tra phát âm bằng AI';
                    micBtn.innerHTML = '🎙️';

                   if (spkIcon && spkIcon.parentNode) {
                       var p = spkIcon.parentNode;
                       if (!p.classList.contains('card-actions')) {
                           var wrap = document.createElement('div');
                           wrap.className = 'card-actions';
                           p.insertBefore(wrap, spkIcon);
                           wrap.appendChild(spkIcon);
                           wrap.appendChild(micBtn);
                       } else {
                           p.appendChild(micBtn);
                       }
                   } else {
                       card.appendChild(micBtn);
                   }
               }

               var existingFb = card.querySelector('.pronunciation-feedback');
               if (!existingFb) {
                   var fb = document.createElement('div');
                   fb.className = 'pronunciation-feedback';
                   fb.setAttribute('id', 'fb_' + cardId);
                   fb.style.display = 'none';
                   card.appendChild(fb);
               }
           });
         }

         if (document.readyState === 'loading') {
             document.addEventListener('DOMContentLoaded', enhanceSentenceCards);
         } else {
             enhanceSentenceCards();
         }
         setTimeout(enhanceSentenceCards, 200);
         setTimeout(enhanceSentenceCards, 1000);

            var activeDialoguePlayer = null;

            function stopActiveDialoguePlayer() {
              if (activeDialoguePlayer) {
                if (activeDialoguePlayer.audio) {
                  try {
                    activeDialoguePlayer.audio.pause();
                    activeDialoguePlayer.audio.currentTime = 0;
                  } catch(e) {}
                  activeDialoguePlayer.audio = null;
                }
                if (activeDialoguePlayer.timer) {
                  clearTimeout(activeDialoguePlayer.timer);
                  activeDialoguePlayer.timer = null;
                }
                if (activeDialoguePlayer.safetyTimer) {
                  clearTimeout(activeDialoguePlayer.safetyTimer);
                  activeDialoguePlayer.safetyTimer = null;
                }
                var box = document.querySelector('[data-dialogue-id="' + activeDialoguePlayer.dialogueId + '"]');
                if (box) {
                  box.querySelectorAll('.btn-dialogue-play').forEach(function(b) {
                    b.classList.remove('is-active-btn');
                    var origText = b.getAttribute('data-orig-text');
                    if (origText) b.innerHTML = origText;
                  });
                  box.querySelectorAll('.dialogue-turn-row').forEach(function(r) {
                    r.classList.remove('is-active-turn', 'is-muted-turn');
                    var prompt = r.querySelector('.user-prompt-tag');
                    if (prompt) prompt.remove();
                  });
                }
                activeDialoguePlayer = null;
              }
            }

            function playDialogueTurn() {
              if (!activeDialoguePlayer) return;
              var p = activeDialoguePlayer;
              var box = document.querySelector('[data-dialogue-id="' + p.dialogueId + '"]');
              if (!box) { stopActiveDialoguePlayer(); return; }

              box.querySelectorAll('.dialogue-turn-row').forEach(function(r) {
                r.classList.remove('is-active-turn', 'is-muted-turn');
                var prompt = r.querySelector('.user-prompt-tag');
                if (prompt) prompt.remove();
              });

              if (p.currentIndex >= p.turns.length) {
                stopActiveDialoguePlayer();
                return;
              }

              var turnEl = p.turns[p.currentIndex];
              var role = (turnEl.getAttribute('data-role') || 'A').toUpperCase();
              var audioKey = turnEl.getAttribute('data-audio-key') || '';
              var sentence = turnEl.getAttribute('data-sentence') || '';
              var spkLabel = turnEl.querySelector('.speaker-label') ? turnEl.querySelector('.speaker-label').textContent.replace(':', '').trim() : role;

              // QUAN TRỌNG: Muting logic
              // - mode === 'all': KHÔNG mute bất kỳ ai (nghe cả 2 người đối thoại)
              // - mode === 'as_1' (Play as Người 1 / A): MUTE vai A, PHÁT vai B để người học tự nói vai A
              // - mode === 'as_2' (Play as Người 2 / B): MUTE vai B, PHÁT vai A để người học tự nói vai B
              var isMuted = false;
              if (p.targetMutedRole && role === p.targetMutedRole) {
                isMuted = true;
              } else if (p.mode === 'as_1' && role === 'A') {
                isMuted = true;
              } else if (p.mode === 'as_2' && role === 'B') {
                isMuted = true;
              }

              if (isMuted) {
                turnEl.classList.add('is-muted-turn');
                var contentEl = turnEl.querySelector('.dialogue-turn-content') || turnEl;
                if (contentEl && !contentEl.querySelector('.user-prompt-tag')) {
                  var tag = document.createElement('span');
                  tag.className = 'user-prompt-tag';
                  tag.innerHTML = '🗣️ Đến lượt bạn nói (' + spkLabel + ')... <button type="button" class="btn-skip-silence" title="Bấm nếu bạn đã nói xong để chuyển câu tiếp ngay">⏭️ Đã nói xong</button>';
                  contentEl.appendChild(tag);
                }
              } else {
                turnEl.classList.add('is-active-turn');
              }

              try {
                turnEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
              } catch(e) {}

              var localUrl = '/audio/communication/sentences/' + audioKey + '.mp3';
              var cloudUrl = 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets/audio/communication/sentences/' + audioKey + '.mp3';

              var words = (sentence || '').trim().split(/\s+/).filter(Boolean).length;
              // Tính thời lượng nói thoải mái cho học viên:
              // - Tốc độ đọc tự nhiên của học viên: ~900ms / từ
              // - 3.5s đệm cho quan sát, lấy hơi và khoảng lặng phản xạ
              // - Tối thiểu 6.5s kể cả câu ngắn nhất
              var baseSpeakingMs = Math.max(6500, words * 900 + 3500);

              var turnEnded = false;
              var onTurnEnd = function() {
                if (turnEnded) return;
                turnEnded = true;
                if (!activeDialoguePlayer || activeDialoguePlayer !== p) return;
                if (p.safetyTimer) {
                  clearTimeout(p.safetyTimer);
                  p.safetyTimer = null;
                }
                if (p.timer) {
                  clearTimeout(p.timer);
                  p.timer = null;
                }
                if (p.audio) {
                  try { p.audio.pause(); } catch(e) {}
                  p.audio = null;
                }
                p.skipTurn = null;
                p.timer = setTimeout(function() {
                  p.currentIndex++;
                  playDialogueTurn();
                }, 600);
              };

              p.skipTurn = onTurnEnd;

              if (isMuted) {
                // Vai này do học sinh nói:
                // Tải audio mẫu để lấy duration thực tế, luôn nhân 1.65x + 3.5s đệm
                // để đảm bảo thời gian cho phép luôn dài hơn đáng kể so với bản nói mẫu
                var applySpeakingTimer = function(durationMs) {
                  if (turnEnded || !activeDialoguePlayer || activeDialoguePlayer !== p) return;
                  if (p.timer) clearTimeout(p.timer);
                  p.timer = setTimeout(onTurnEnd, durationMs);
                };

                applySpeakingTimer(baseSpeakingMs);

                var sampleAudio = new Audio(localUrl);
                p.audio = sampleAudio;
                sampleAudio.onloadedmetadata = function() {
                  if (sampleAudio.duration && !isNaN(sampleAudio.duration) && sampleAudio.duration > 0) {
                    var sampleDurationMs = Math.round(sampleAudio.duration * 1000 * 1.65 + 3500);
                    var finalSpeakingMs = Math.max(sampleDurationMs, baseSpeakingMs);
                    applySpeakingTimer(finalSpeakingMs);
                  }
                };
                sampleAudio.onerror = function() {
                  var cloudSample = new Audio(cloudUrl);
                  cloudSample.onloadedmetadata = function() {
                    if (cloudSample.duration && !isNaN(cloudSample.duration) && cloudSample.duration > 0) {
                      var sampleDurationMs = Math.round(cloudSample.duration * 1000 * 1.65 + 3500);
                      var finalSpeakingMs = Math.max(sampleDurationMs, baseSpeakingMs);
                      applySpeakingTimer(finalSpeakingMs);
                    }
                  };
                };
              } else {
                // Vai này máy đọc: phát audio rõ ràng (nghe cả 2 hoặc nghe đối phương)
                var audio = new Audio(localUrl);
                p.audio = audio;
                audio.muted = false;
                audio.volume = 1;
                audio.onended = onTurnEnd;

                var fallbackStarted = false;
                var startFallback = function() {
                  if (fallbackStarted) return;
                  fallbackStarted = true;
                  var fallbackAudio = new Audio(cloudUrl);
                  p.audio = fallbackAudio;
                  fallbackAudio.muted = false;
                  fallbackAudio.volume = 1;
                  fallbackAudio.onended = onTurnEnd;
                  fallbackAudio.onerror = function() {
                    p.timer = setTimeout(onTurnEnd, baseSpeakingMs);
                  };
                  fallbackAudio.play().catch(function() {
                    p.timer = setTimeout(onTurnEnd, baseSpeakingMs);
                  });
                };

                audio.onerror = startFallback;
                audio.play().catch(function() {
                  startFallback();
                });

                // Safety timeout nếu mạng lag hoặc audio bị đơ
                p.safetyTimer = setTimeout(function() {
                  onTurnEnd();
                }, Math.max(16000, baseSpeakingMs * 2));
              }
            }

            function startDialoguePlay(dialogueId, mode, clickedBtn, targetMutedRole) {
              if (activeDialoguePlayer && activeDialoguePlayer.dialogueId === dialogueId && activeDialoguePlayer.mode === mode) {
                stopActiveDialoguePlayer();
                return;
              }

              stopActiveDialoguePlayer();
              clearAllPlayingCards();
              window.parent.postMessage({ type: 'LECTURE_STOP_AUDIO' }, '*');

              var box = document.querySelector('[data-dialogue-id="' + dialogueId + '"]');
              if (!box) return;

              box.querySelectorAll('.btn-dialogue-play').forEach(function(b) {
                b.classList.remove('is-active-btn');
                var origText = b.getAttribute('data-orig-text');
                if (origText) b.innerHTML = origText;
              });

              if (!clickedBtn.hasAttribute('data-orig-text')) {
                clickedBtn.setAttribute('data-orig-text', clickedBtn.innerHTML);
              }
              clickedBtn.classList.add('is-active-btn');
              clickedBtn.innerHTML = '⏹️ Dừng';

              var turns = Array.from(box.querySelectorAll('.dialogue-turn-row'));
              if (turns.length === 0) return;

              var resolvedMutedRole = targetMutedRole;
              if (!resolvedMutedRole) {
                if (mode === 'as_1' || mode === 'as_a') resolvedMutedRole = 'A';
                else if (mode === 'as_2' || mode === 'as_b') resolvedMutedRole = 'B';
              }

              activeDialoguePlayer = {
                dialogueId: dialogueId,
                mode: mode,
                targetMutedRole: resolvedMutedRole,
                turns: turns,
                currentIndex: 0,
                audio: null,
                timer: null,
                safetyTimer: null
              };

              playDialogueTurn();
            }

          function clearAllPlayingCards() {
            var playingCards = document.querySelectorAll('.sentence-audio-card.is-playing');
            for (var i = 0; i < playingCards.length; i++) {
                var c = playingCards[i];
                c.classList.remove('is-playing');
                var tid = c.getAttribute('data-play-timeout');
                if (tid) {
                    clearTimeout(parseInt(tid, 10));
                    c.removeAttribute('data-play-timeout');
                }
            }
          }

          window.handleMicClick = function(micBtn) {
            var cardId = micBtn.getAttribute('data-card-id');
            var sentence = micBtn.getAttribute('data-sentence');
            var card = micBtn.closest('.sentence-audio-card');
            var audioKey = micBtn.getAttribute('data-audio-key') || (card ? card.getAttribute('data-audio-key') : '') || '';
            var fb = card ? card.querySelector('.pronunciation-feedback') : null;

            // Dừng ngay lập tức bất kỳ âm thanh nào đang phát
            stopActiveDialoguePlayer();
            window.parent.postMessage({ type: 'LECTURE_STOP_AUDIO' }, '*');
            clearAllPlayingCards();

            if (micBtn.classList.contains('is-recording')) {
                micBtn.classList.remove('is-recording');
                micBtn.classList.add('is-evaluating');
                micBtn.innerHTML = '⏳';
                micBtn.title = 'AI đang chấm...';

                if (fb) {
                    fb.style.display = 'block';
                    fb.innerHTML = '<div style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: #0284c7; background: #f0f9ff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bae6fd; margin-top: 10px;"><span style="font-size: 16px;">⏳</span><span><strong>AI đang lắng nghe và chấm phát âm...</strong> Vui lòng đợi trong giây lát</span></div>';
                }

                window.parent.postMessage({ type: 'LECTURE_STOP_RECORDING', cardId: cardId }, '*');
            } else {
                document.querySelectorAll('.sentence-mic-btn.is-recording').forEach(function(m) {
                    m.classList.remove('is-recording');
                    m.innerHTML = '🎙️';
                });

                micBtn.classList.add('is-recording');
                micBtn.innerHTML = '⏹️';
                micBtn.title = 'Đang thu âm... Bấm vào đây để dừng và chấm điểm';

                if (fb) {
                    fb.style.display = 'block';
                    fb.innerHTML = '<div style="display: flex; align-items: center; justify-content: space-between; font-size: 13px; color: #b91c1c; background: #fef2f2; padding: 10px 14px; border-radius: 8px; border: 1px solid #fecaca; margin-top: 10px;">' +
                        '<div style="display: flex; align-items: center; gap: 8px;">' +
                            '<span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background-color: #ef4444; animation: pulse-mic 1s infinite;"></span>' +
                            '<span><strong>Đang nghe:</strong> Hãy đọc câu trên vào mic...</span>' +
                        '</div>' +
                        '<button type="button" class="btn-stop-recording-prompt" style="font-size: 12px; color: #991b1b; font-weight: bold; cursor: pointer; text-decoration: underline; background: none; border: none; padding: 0;">Bấm ⏹️ để chấm</button>' +
                    '</div>';
                }

                window.parent.postMessage({ type: 'LECTURE_START_RECORDING', cardId: cardId, targetSentence: sentence, audioKey: audioKey }, '*');
            }
          };

           window.addEventListener('message', function(e) {
            if (!e || !e.data) return;
            if (e.data.type === 'STOP_AUDIO_PLAYBACK') {
                clearAllPlayingCards();
            } else if (e.data.type === 'PRONUNCIATION_STATUS') {
                var cardId = e.data.cardId;
                var status = e.data.status;
                var mic = document.querySelector('.sentence-mic-btn[data-card-id="' + cardId + '"]');
                var card = mic ? mic.closest('.sentence-audio-card') : null;
                var fb = card ? card.querySelector('.pronunciation-feedback') : null;

                if (status === 'STOPPED') {
                    if (mic) {
                        mic.classList.remove('is-recording');
                        mic.classList.remove('is-evaluating');
                        mic.innerHTML = '🎙️';
                    }
                    if (fb) {
                        fb.style.display = 'none';
                    }
                } else if (status === 'EVALUATING') {
                    if (mic) {
                        mic.classList.remove('is-recording');
                        mic.classList.add('is-evaluating');
                        mic.innerHTML = '⏳';
                        mic.title = 'AI đang chấm...';
                    }
                    if (fb) {
                        fb.style.display = 'block';
                        fb.innerHTML = '<div style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: #0284c7; background: #f0f9ff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bae6fd; margin-top: 10px;"><span style="font-size: 16px;">⏳</span><span><strong>AI đang lắng nghe và chấm phát âm...</strong></span></div>';
                    }
                }
            } else if (e.data.type === 'PRONUNCIATION_RESULT') {
                var cardId = e.data.cardId;
                var res = e.data.result || {};
                var isCorrect = !!res.is_correct;
                var score = res.accuracy_score !== undefined ? res.accuracy_score : (isCorrect ? 100 : 50);
                var recognized = res.recognized_text || '';
                var feedback = res.feedback || (isCorrect ? 'Phát âm rất chuẩn xác!' : 'Hãy cố gắng luyện tập lại nhé!');
                var mispronounced = res.mispronounced_words || [];

                var mic = document.querySelector('.sentence-mic-btn[data-card-id="' + cardId + '"]');
                var card = mic ? mic.closest('.sentence-audio-card') : null;
                var fb = card ? card.querySelector('.pronunciation-feedback') : null;

                if (mic) {
                    mic.classList.remove('is-recording');
                    mic.classList.remove('is-evaluating');
                    mic.innerHTML = isCorrect ? '✅' : '🎙️';
                    mic.title = isCorrect ? 'Đã phát âm đúng!' : 'Kiểm tra lại phát âm';
                    setTimeout(function() {
                        if (mic && !mic.classList.contains('is-recording')) {
                            mic.innerHTML = '🎙️';
                        }
                    }, 3500);
                }

                if (card) {
                    if (isCorrect) {
                        card.style.borderLeftColor = '#22c55e';
                        card.style.backgroundColor = '#f0fdf4';
                    } else {
                        card.style.borderLeftColor = '#ef4444';
                        card.style.backgroundColor = '#fef2f2';
                    }
                }

                if (fb) {
                    fb.style.display = 'block';
                    var bg = isCorrect ? '#f0fdf4' : '#fef2f2';
                    var border = isCorrect ? '#86efac' : '#fca5a5';
                    var textColor = isCorrect ? '#15803d' : '#991b1b';
                    var badgeBg = isCorrect ? '#dcfce7' : '#fee2e2';
                    var badgeText = isCorrect ? '#166534' : '#b91c1c';
                    var statusTitle = isCorrect ? '✅ Phát âm rất chuẩn!' : '❌ Chưa chuẩn lắm';

                    var misHtml = '';
                    if (!isCorrect && mispronounced.length > 0) {
                        misHtml = '<div style="margin-top: 4px; font-size: 12px; color: #b91c1c;"><span>Từ cần chú ý: </span>' +
                            mispronounced.map(function(w) {
                                return '<span style="background: #fecaca; color: #991b1b; padding: 1px 6px; border-radius: 4px; font-weight: bold; margin-right: 4px;">' + w + '</span>';
                            }).join('') + '</div>';
                    }

                    var retryHtml = !isCorrect ? '<button type="button" class="retry-pronunciation-btn">🔄 Thử lại</button>' : '';

                    fb.innerHTML = '<div style="background: ' + bg + '; border: 1px solid ' + border + '; padding: 12px 14px; border-radius: 8px; margin-top: 10px;">' +
                        '<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">' +
                            '<div style="display: flex; align-items: center; gap: 6px;">' +
                                '<span style="font-weight: bold; font-size: 14px; color: ' + textColor + ';">' + statusTitle + '</span>' +
                                '<span style="background: ' + badgeBg + '; color: ' + badgeText + '; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: bold;">' + score + '%</span>' +
                            '</div>' +
                            retryHtml +
                        '</div>' +
                        (recognized ? '<div style="font-size: 13px; color: #334155; margin-bottom: 4px;"><span style="color: #64748b;">AI nghe được: </span><strong style="color: ' + textColor + ';">"' + recognized + '"</strong></div>' : '') +
                        misHtml +
                        (feedback ? '<div style="font-size: 13px; color: #475569; margin-top: 4px;">💡 ' + feedback + '</div>' : '') +
                    '</div>';
                }
            } else if (e.data.type === 'PRONUNCIATION_ERROR') {
                var cardId = e.data.cardId;
                var errMsg = e.data.error || 'Có lỗi xảy ra.';
                var mic = document.querySelector('.sentence-mic-btn[data-card-id="' + cardId + '"]');
                var card = mic ? mic.closest('.sentence-audio-card') : null;
                var fb = card ? card.querySelector('.pronunciation-feedback') : null;

                if (mic) {
                    mic.classList.remove('is-recording');
                    mic.classList.remove('is-evaluating');
                    mic.innerHTML = '🎙️';
                }
                if (fb) {
                    fb.style.display = 'block';
                    fb.innerHTML = '<div style="background: #fffbeb; border: 1px solid #fcd34d; padding: 10px 14px; border-radius: 8px; margin-top: 10px; font-size: 13px; color: #92400e; display: flex; justify-content: space-between; align-items: center;">' +
                        '<span>⚠️ ' + errMsg + '</span>' +
                        '<button type="button" class="retry-pronunciation-btn is-warning">Thử lại</button>' +
                    '</div>';
                }
            }
          });

         document.addEventListener('click', function(e) {
           var target = e.target;
           
            // -1. Intercept interactive dialogue toolbar play buttons
            var playBtn = target.closest('.btn-dialogue-play');
            if (playBtn) {
                e.preventDefault();
                e.stopPropagation();
                var dBox = playBtn.closest('[data-dialogue-id]');
                var dId = dBox ? dBox.getAttribute('data-dialogue-id') : null;
                var mode = playBtn.getAttribute('data-mode') || 'all';
                var targetRole = playBtn.getAttribute('data-target-role') || (mode === 'as_1' ? 'A' : (mode === 'as_2' ? 'B' : null));
                if (dId) {
                    startDialoguePlay(dId, mode, playBtn, targetRole);
                }
                return false;
            }

            // -0.8 Intercept skip silence button when user finished speaking in Play as mode
            var skipBtn = target.closest('.btn-skip-silence');
            if (skipBtn) {
                e.preventDefault();
                e.stopPropagation();
                if (activeDialoguePlayer && typeof activeDialoguePlayer.skipTurn === 'function') {
                    activeDialoguePlayer.skipTurn();
                }
                return false;
            }

            // -0.5 Intercept individual turn play button
            var turnSpk = target.closest('.turn-spk-btn');
            if (turnSpk) {
                e.preventDefault();
                e.stopPropagation();
                stopActiveDialoguePlayer();
                var turnRow = turnSpk.closest('.dialogue-turn-row');
                if (turnRow) {
                    var s = turnRow.getAttribute('data-sentence') || '';
                    var ak = turnRow.getAttribute('data-audio-key') || '';
                    clearAllPlayingCards();
                    turnRow.classList.add('is-playing');
                    var tid = setTimeout(function() {
                        turnRow.classList.remove('is-playing');
                    }, 12000);
                    turnRow.setAttribute('data-play-timeout', tid);
                    window.playSentence(s, ak);
                }
                return false;
            }

           // 0. Intercept mic button for pronunciation checking
           var micTarget = target.closest('.sentence-mic-btn');
           if (micTarget) {
               e.preventDefault();
               e.stopPropagation();
               window.handleMicClick && window.handleMicClick(micTarget);
               return false;
           }

           // 0.05 Intercept stop recording text prompt
           var stopPromptTarget = target.closest('.btn-stop-recording-prompt');
           if (stopPromptTarget) {
               e.preventDefault();
               e.stopPropagation();
               var card = stopPromptTarget.closest('.sentence-audio-card');
               if (card) {
                   var mic = card.querySelector('.sentence-mic-btn');
                   if (mic) {
                       window.handleMicClick && window.handleMicClick(mic);
                   }
               }
               return false;
           }

           // 0.1 Intercept retry button inside pronunciation feedback
           var retryTarget = target.closest('.retry-pronunciation-btn');
           if (retryTarget) {
               e.preventDefault();
               e.stopPropagation();
               var card = retryTarget.closest('.sentence-audio-card');
               if (card) {
                   var mic = card.querySelector('.sentence-mic-btn');
                   if (mic) {
                       window.handleMicClick && window.handleMicClick(mic);
                   }
               }
               return false;
           }

           // 1. Intercept sentence audio cards
           var cardTarget = target.closest('.sentence-audio-card, [data-audio-key]');
           if (cardTarget) {
               e.preventDefault();
               e.stopPropagation();

               // Tắt trạng thái đang thu âm nếu học sinh chuyển sang nghe audio
               document.querySelectorAll('.sentence-mic-btn.is-recording').forEach(function(m) {
                   m.classList.remove('is-recording');
                   m.innerHTML = '🎙️';
               });

               clearAllPlayingCards();
               stopActiveDialoguePlayer();
               cardTarget.classList.add('is-playing');
               var tid = setTimeout(function() {
                   cardTarget.classList.remove('is-playing');
               }, 12000);
               cardTarget.setAttribute('data-play-timeout', tid);

               var sentence = cardTarget.getAttribute('data-sentence') || '';
               var audioKey = cardTarget.getAttribute('data-audio-key') || '';
               window.playSentence(sentence, audioKey);
               return false;
           }

           // 2. Intercept pronunciation links
           var audioTarget = target.closest('.audiolink a, [data-word], a[onclick*="playaudio"], a[onclick*="playWord"]');
           if (audioTarget) {
               e.preventDefault();
               e.stopPropagation();
               clearAllPlayingCards();
               stopActiveDialoguePlayer();
               var word = audioTarget.getAttribute('data-word') || audioTarget.textContent.trim();
               word = word.replace(/[^a-zA-Z]/g, '');
               if (word) {
                   audioTarget.style.transition = 'all 0.2s ease';
                   var origBg = audioTarget.style.backgroundColor;
                   var origColor = audioTarget.style.color;
                   audioTarget.style.backgroundColor = '#dbeafe';
                   audioTarget.style.color = '#0284c7';
                   audioTarget.style.borderRadius = '4px';
                   audioTarget.style.padding = '1px 5px';
                   setTimeout(function() {
                       audioTarget.style.backgroundColor = origBg || 'transparent';
                       audioTarget.style.color = origColor || '';
                       audioTarget.style.padding = '';
                   }, 500);
                   window.parent.postMessage({ type: 'LECTURE_PLAY_WORD', word: word }, '*');
               }
               return false;
           }

           var anchor = target.closest('a');
           if (anchor && 
               anchor.hasAttribute('href') && 
               !anchor.getAttribute('href').startsWith('javascript:') &&
               anchor.getAttribute('href') !== '#' &&
               !anchor.outerHTML.includes('openIELTSAssessor') && 
               !anchor.classList.contains('btn-ielts-trigger') && 
               !anchor.classList.contains('btn-ai-trigger') && 
               !anchor.classList.contains('btn-live-trigger')) {
                   
               e.preventDefault(); 
               var rawHref = anchor.getAttribute('href');
               window.parent.postMessage({ type: 'LECTURE_LINK_CLICK', href: rawHref }, '*'); 
               return; 
           }

           var btn = target.closest('.btn-ai-trigger, .btn-ielts-trigger, .btn-live-trigger');
           if (btn) {
               e.preventDefault(); 
               e.stopPropagation();
               e.stopImmediatePropagation();
               
               var isLive = btn.classList.contains('btn-live-trigger');
               
               var originalText = btn.innerHTML;
               btn.innerHTML = isLive ? "📞 Đang kết nối..." : "✨ Đang mở AI...";
               btn.style.opacity = "0.7";
               setTimeout(function() { 
                   btn.innerHTML = originalText; 
                   btn.style.opacity = "1"; 
               }, 1500);
               if(isLive) {
                  window.parent.postMessage({ 
                      type: 'OPEN_LIVE_SPEAKING', 
                      topic: btn.getAttribute('data-topic') || '' 
                  }, '*');
               } else {
                  window.parent.postMessage({ 
                      type: 'OPEN_IELTS_AI', 
                      topic: btn.getAttribute('data-topic') || '', 
                      image: btn.getAttribute('data-image') || '', 
                      task: btn.getAttribute('data-task') || 'task2' 
                  }, '*');
               }
               return false;
           }

         }, true);
         
         var selectionTimer = null;
         document.addEventListener('mouseup', function(e) {
           clearTimeout(selectionTimer);
           
           selectionTimer = setTimeout(function() {
               var sel = window.getSelection();
               var text = sel.toString().trim();
               
               if (text && text.length > 0 && text.length < 40 && text.split(' ').length <= 4) {
                 var range = sel.getRangeAt(0);
                 var rect = range.getBoundingClientRect();
                 window.parent.postMessage({ 
                     type: 'LECTURE_OPEN_DICT', 
                     word: text, 
                     x: rect.left + (rect.width/2), 
                     y: rect.bottom, 
                     rectTop: rect.top 
                 }, '*');
               }
           }, 150);
         });
         document.addEventListener('mousedown', function(e) {
           var sel = window.getSelection();
           if (!sel.toString().trim()) { 
               window.parent.postMessage({ type: 'LECTURE_CLOSE_DICT' }, '*'); 
           }
         });
          function reportHeight() {
             var wrapper = document.getElementById('content-wrapper');
             if (wrapper) {
                 var h = Math.max(wrapper.scrollHeight || 0, wrapper.offsetHeight || 0, Math.ceil(wrapper.getBoundingClientRect().height || 0));
                 if (h > 0) {
                     window.parent.postMessage({ type: 'LECTURE_RESIZE', height: h }, '*');
                 }
             }
          }
          
          if (document.readyState === 'loading') {
             document.addEventListener('DOMContentLoaded', reportHeight);
          } else {
             reportHeight();
          }
          window.addEventListener('load', reportHeight);
          setTimeout(reportHeight, 50);
          setTimeout(reportHeight, 200);
          setTimeout(reportHeight, 600);
          setTimeout(reportHeight, 1500);
          if (window.ResizeObserver) {
             var ro = new ResizeObserver(reportHeight);
             ro.observe(document.body);
             var wrapEl = document.getElementById('content-wrapper');
             if (wrapEl) ro.observe(wrapEl);
          } else { 
             setInterval(reportHeight, 500);
          }

          // Lắng nghe lệnh Highlight phân đoạn từ Player
          window.addEventListener('message', function(e) {
             if (e.data?.type === 'HIGHLIGHT_LECTURE_SECTION') {
                var sel = e.data.selector;
                document.querySelectorAll('.active-lecture-highlight').forEach(function(el) {
                   el.classList.remove('active-lecture-highlight');
                });
                document.querySelectorAll('.active-svg-parent-highlight').forEach(function(el) {
                   el.classList.remove('active-svg-parent-highlight');
                });
                if (sel) {
                   var targets = document.querySelectorAll(sel);
                   targets.forEach(function(target) {
                      target.classList.add('active-lecture-highlight');
                   });
                   var target = targets[0];
                   if (target) {
                      var scrollTarget = target;
                      if (target instanceof SVGElement) {
                         var parentContainer = target.closest('div, section, article') || target.ownerSVGElement;
                         if (parentContainer) {
                            parentContainer.classList.add('active-svg-parent-highlight');
                            scrollTarget = parentContainer;
                         }
                      }
                      if (e.data.autoScroll && scrollTarget && typeof scrollTarget.scrollIntoView === 'function') {
                         scrollTarget.scrollIntoView({ behavior: 'smooth', block: 'center' });
                      }
                   }
                }
             }
          });

          // Click vào thẻ trên bài giảng để nghe giảng riêng thẻ đó
          document.addEventListener('click', function(e) {
             var sec = e.target.closest('[data-lecture-section]');
             if (sec) {
                var sid = sec.getAttribute('data-lecture-section');
                window.parent.postMessage({ type: 'LECTURE_PLAY_SECTION', sectionId: sid }, '*');
             }
          });
        </script>
     </body>
     </html>
   `;
   return (
     <div className={`w-full animate-in fade-in duration-700 relative ${isIframeOnly ? 'h-[85vh]' : ''}`}>
       <iframe
         key={cleanedHtml ? `${cleanedHtml.length}_${cleanedHtml.substring(0, 32)}` : 'empty'}
         ref={iframeRef}
         srcDoc={iframeContent}
         style={{ width: '100%', height: isIframeOnly ? '100%' : `${iframeHeight}px`, border: 'none', overflow: 'hidden' }}
         sandbox="allow-scripts allow-same-origin allow-popups"
         allow="microphone; camera; clipboard-read; clipboard-write;"
         scrolling="no"
         allowFullScreen
       />
     </div>
   );
}, (prevProps, nextProps) => prevProps.html === nextProps.html);


// =========================================================================================
// MAIN COMPONENT: LECTURE VIEWER
// =========================================================================================
export default function LectureViewer({ 
    courseId, 
    onBack, 
    onStartTest, 
    onOpenAI,
    onCourseChange
}: { 
    courseId: string, 
    onBack: () => void, 
    onStartTest?: (type: string, data: any) => void, 
    onOpenAI?: (passedMode?: string, topic?: string, image?: string, task?: string) => void,
    onCourseChange?: (newCourseId: string) => void
}) {
  const [currentCourseId, setCurrentCourseId] = useState<string>(courseId);
  const [availableCourses, setAvailableCourses] = useState<any[]>([]);
  const [isCourseDropdownOpen, setIsCourseDropdownOpen] = useState<boolean>(false);
  const [courseFilterQuery, setCourseFilterQuery] = useState<string>('');
  const courseDropdownRef = useRef<HTMLDivElement>(null);

  const [course, setCourse] = useState<any>(null);
  const [modules, setModules] = useState<any[]>([]);
  const [lectures, setLectures] = useState<any[]>([]);
  const [currentUser, setCurrentUser] = useState<any>(null);
  
  const [pages, setPages] = useState<any[]>([]);
  const [activeLectureId, setActiveLectureId] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [completedTasks, setCompletedTasks] = useState<string[]>([]);
  const [testScoresMap, setTestScoresMap] = useState<Map<string, { score: number; total: number; percent: number; isPassed: boolean }>>(new Map());
  const [allLectureProgress, setAllLectureProgress] = useState<Record<string, string[]>>({});
  
  const [completedLectures, setCompletedLectures] = useState<Set<string>>(new Set());
  const [viewedPages, setViewedPages] = useState<Set<number>>(new Set());
  const [expandedModules, setExpandedModules] = useState<string[]>([]);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false); 
  const [isTaskMenuOpen, setIsTaskMenuOpen] = useState(false);
  const [currentLectureAssignments, setCurrentLectureAssignments] = useState<any[]>([]);
  const taskMenuRef = useRef<HTMLDivElement>(null);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [popupUrl, setPopupUrl] = useState<string | null>(null);
  
  // 🚀 MỚI: HỨNG ẢNH ĐƯỢC UP TỪ SIDEBAR ĐỂ HIỂN THỊ NỬA TRÁI MÀN HÌNH
  const [uploadedBoardImage, setUploadedBoardImage] = useState<string | null>(null);

  const [dictPopup, setDictPopup] = useState<{show: boolean, word: string, x: number, y: number, rectTop: number, data: any, isLoading: boolean} | null>(null);
  const [isTeacherBoardOpen, setIsTeacherBoardOpen] = useState(false);
  const [boardWidthVw, setBoardWidthVw] = useState(50);
  const containerRef = useRef<HTMLDivElement>(null);

  const [isLectureThemeModalOpen, setIsLectureThemeModalOpen] = useState(false);
  const [lectureTheme, setLectureTheme] = useState<BoardTheme>(() => loadTheme('tony_lecture_theme'));
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isVideoCollapsed, setIsVideoCollapsed] = useState(false);
  const [selectedVideoSubIndex, setSelectedVideoSubIndex] = useState<number>(0);

  useEffect(() => {
    setSelectedVideoSubIndex(0);
  }, [activeLectureId]);

  const handleSelectLectureTheme = (theme: BoardTheme) => {
    setLectureTheme(theme);
    saveTheme('tony_lecture_theme', theme);
  };
  const handleApplyCustomLectureColor = (hex: string) => {
    handleSelectLectureTheme(createCustomTheme(hex));
  };

  const courseProgress = useMemo(() => {
      if (lectures.length === 0) return 0;
      return Math.round((completedLectures.size / lectures.length) * 100);
  }, [lectures, completedLectures]);

  const activeLecture = useMemo(() => {
      return lectures.find(l => l.id === activeLectureId);
  }, [lectures, activeLectureId]);

  const lectureVideoConfig = useMemo(() => {
    if (activeLectureId && LECTURE_VIDEO_MAP[activeLectureId]) {
      return LECTURE_VIDEO_MAP[activeLectureId];
    }
    if (activeLecture?.video_id) {
      return activeLecture.video_id;
    }
    if (activeLecture?.video_url) {
      return getYouTubeVideoId(activeLecture.video_url);
    }
    return null;
  }, [activeLectureId, activeLecture]);

  const currentVideoList = useMemo((): LectureVideoItem[] => {
    if (!lectureVideoConfig) return [];
    if (Array.isArray(lectureVideoConfig)) return lectureVideoConfig;
    if (typeof lectureVideoConfig === 'string') {
      return [{ title: activeLecture?.title || 'Video bài giảng', videoId: lectureVideoConfig }];
    }
    return [];
  }, [lectureVideoConfig, activeLecture]);

  const activeLectureVideoId = useMemo(() => {
    if (currentVideoList.length === 0) return null;
    const item = currentVideoList[selectedVideoSubIndex] || currentVideoList[0];
    return item?.videoId || null;
  }, [currentVideoList, selectedVideoSubIndex]);

  const activeLectureVideoSubTitle = useMemo(() => {
    if (currentVideoList.length <= 1) return activeLecture?.title;
    return currentVideoList[selectedVideoSubIndex]?.title || activeLecture?.title;
  }, [currentVideoList, selectedVideoSubIndex, activeLecture]);

  const currentSafeTasks = useMemo(() => {
      const raw = Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [];
      return [...raw].sort((a: any, b: any) => {
        const isExA = a.type === 'exercise' ? 1 : 0;
        const isExB = b.type === 'exercise' ? 1 : 0;
        return isExA - isExB;
      });
  }, [activeLecture]);

  const currentLectureDoneCount = useMemo(() => {
      if (!activeLectureId) return 0;
      return allLectureProgress[activeLectureId]?.length || 0;
  }, [allLectureProgress, activeLectureId]);

  const totalPages = pages.length;

  const currentHtmlContent = useMemo(() => { 
      const page = pages.find(p => p.page_number === currentPage); 
      return page ? page.content_html : ''; 
  }, [pages, currentPage]);

  const isIframeOnly = useMemo(() => {
      if (!currentHtmlContent) return false;
      try {
          const doc = new DOMParser().parseFromString(currentHtmlContent, 'text/html');
          const text = doc.body.textContent?.replace(/[\W_]+/g, '').trim();
          const mediaNodes = doc.body.querySelectorAll('iframe, embed, object');
          return (text === '' && mediaNodes.length === 1);
      } catch(e) {
          return false;
      }
  }, [currentHtmlContent]);

  useEffect(() => {
    const handleToggleBoard = (e: any) => {
        setIsTeacherBoardOpen(e.detail === true || e.detail === 'open');
    };
    const handleBoardResize = (e: any) => {
        setBoardWidthVw(e.detail);
    };
    window.addEventListener('tony-teacher-board-state', handleToggleBoard);
    window.addEventListener('tony-board-resize', handleBoardResize);
    return () => {
        window.removeEventListener('tony-teacher-board-state', handleToggleBoard);
        window.removeEventListener('tony-board-resize', handleBoardResize);
    };
  }, []);

  // 🚀 LẮNG NGHE LỆNH MỞ ẢNH ĐỀ BÀI TỪ SIDEBAR BẮN QUA
  useEffect(() => {
      const handleOpenImageBoard = (e: any) => {
          setUploadedBoardImage(e.detail);
          setIsTeacherBoardOpen(true);
      };
      window.addEventListener('tony-open-image-board', handleOpenImageBoard);
      return () => window.removeEventListener('tony-open-image-board', handleOpenImageBoard);
  }, []);

  useEffect(() => {
    if (popupUrl && popupUrl.toLowerCase().includes('.pdf')) {
        sessionStorage.setItem('tony_pdf_mode', 'true');
        window.dispatchEvent(new CustomEvent('tony-pdf-mode-change', { detail: true }));
    } else {
        sessionStorage.removeItem('tony_pdf_mode');
        window.dispatchEvent(new CustomEvent('tony-pdf-mode-change', { detail: false }));
    }
  }, [popupUrl]);

  useEffect(() => {
      if (isTeacherBoardOpen) {
          const interval = setInterval(() => {
              const liveMode = sessionStorage.getItem('tony_live_mode');
              if (!liveMode && !uploadedBoardImage) {
                  setIsTeacherBoardOpen(false); 
              }
          }, 500);
          return () => clearInterval(interval);
      }
  }, [isTeacherBoardOpen, uploadedBoardImage]);

  useEffect(() => {
    const handleTargetLectureEvent = (e: any) => {
      const targetLecId = e.detail || sessionStorage.getItem('tony_target_lecture_id');
      if (targetLecId && lectures.length > 0) {
        sessionStorage.removeItem('tony_target_lecture_id');
        const found = lectures.find(l => l.id === targetLecId);
        if (found) {
          if (found.module_id) {
            setExpandedModules(prev => [...new Set([...prev, found.module_id])]);
          }
          handleSelectLecture(found.id, currentUser?.id);
        }
      }
    };
    window.addEventListener('tony-open-target-lecture', handleTargetLectureEvent);
    return () => window.removeEventListener('tony-open-target-lecture', handleTargetLectureEvent);
  }, [lectures, currentUser]);

  useEffect(() => {
      if (!currentUser || !activeLectureId || pages.length === 0) return;
      
      const safeLectureTasks = Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [];
      if (safeLectureTasks.length > 0) return; 

      // Chỉ hoàn thành khi ĐÃ XEM HẾT TẤT CẢ CÁC TRANG (cuộn xuống cuối mỗi trang)
      if (viewedPages.size >= pages.length && !completedLectures.has(activeLectureId)) {
          setCompletedLectures(prev => new Set(prev).add(activeLectureId));
          
          supabase.from('lecture_progress')
              .select('id')
              .eq('user_id', currentUser.id)
              .eq('lecture_id', activeLectureId)
              .then(({ data: existingArray }) => {
                  if (existingArray && existingArray.length > 0) {
                      supabase.from('lecture_progress')
                          .update({ completed_tasks: [], is_completed: true })
                          .eq('id', existingArray[0].id)
                          .then();
                  } else {
                      supabase.from('lecture_progress')
                          .insert({ user_id: currentUser.id, lecture_id: activeLectureId, completed_tasks: [], is_completed: true })
                          .then();
                  }
              });
          supabase.from('activity_logs').insert([{
              user_id: currentUser.id,
              action_type: 'finish_lecture',
              details: { lecture_title: activeLecture?.title || "Bài giảng" }
          }]).then();
      }
  }, [viewedPages, pages.length, activeLectureId, currentUser, activeLecture, completedLectures]);

  const fullHtmlContent = useMemo(() => {
      if (!pages || pages.length === 0) return '';
      return [...pages]
          .sort((a, b) => a.page_number - b.page_number)
          .map(p => p.content_html || '')
          .join('\n\n');
  }, [pages]);

  useEffect(() => {
    if (activeLecture && fullHtmlContent) {
      window.dispatchEvent(new CustomEvent('tony-update-lecture-context', {
        detail: {
          title: activeLecture.title, 
          html: fullHtmlContent 
        }
      }));
    }
  }, [activeLecture, fullHtmlContent]);

  useEffect(() => {
    if (containerRef.current) {
        containerRef.current.scrollTo({ top: 0, behavior: 'smooth' });
        // Nếu trang ngắn không cần cuộn → tự động đánh dấu đã xem
        setTimeout(() => {
            if (containerRef.current && containerRef.current.scrollHeight <= containerRef.current.clientHeight + 100) {
                setViewedPages(prev => {
                    if (prev.has(currentPage)) return prev;
                    const next = new Set(prev);
                    next.add(currentPage);
                    return next;
                });
            }
        }, 500);
    }
  }, [activeLectureId, currentPage]);

  // Helper: save page to localStorage (called from navigation handlers only)
  const persistPage = (page: number) => {
    if (activeLectureId && currentUser?.id) {
      localStorage.setItem(`tony_last_page_${currentUser.id}_${activeLectureId}`, page.toString());
    }
  };

  useEffect(() => {
    const handleSwitchPageMsg = (e: MessageEvent) => {
      if (e.data?.type === 'LECTURE_SWITCH_PAGE') {
        const targetP = parseInt(e.data.page, 10);
        if (!isNaN(targetP) && targetP >= 1) {
          setCurrentPage(targetP);
          persistPage(targetP);
          try {
            containerRef.current?.scrollTo({ top: 0, behavior: 'smooth' });
          } catch(err) {}
        }
      }
    };
    window.addEventListener('message', handleSwitchPageMsg);
    return () => window.removeEventListener('message', handleSwitchPageMsg);
  }, [activeLectureId, currentUser]);

  useEffect(() => {
    if (courseId && courseId !== currentCourseId) {
      setCurrentCourseId(courseId);
    }
  }, [courseId]);

  useEffect(() => {
    if (currentCourseId && currentCourseId !== '') {
        fetchCourseData(currentCourseId);
    } else { 
        setErrorMessage("Không tìm thấy mã Khóa học."); 
        setIsLoading(false); 
    }
  }, [currentCourseId]);

  useEffect(() => {
    const handleFullscreenChange = () => {
        setIsFullscreen(!!document.fullscreenElement);
    };
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    
    if (window.innerWidth >= 768) {
        setIsSidebarOpen(true);
    }
    
    return () => {
        document.removeEventListener('fullscreenchange', handleFullscreenChange);
    };
  }, []);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
       const dictPop = document.getElementById('dict-popup');
       if (dictPop && !dictPop.contains(e.target as Node)) {
           setDictPopup(null);
       }
       if (taskMenuRef.current && !taskMenuRef.current.contains(e.target as Node)) {
           setIsTaskMenuOpen(false);
       }
       if (courseDropdownRef.current && !courseDropdownRef.current.contains(e.target as Node)) {
           setIsCourseDropdownOpen(false);
       }
    };
    
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const fetchAvailableCourses = useCallback(async (userId?: string) => {
    try {
      let targetCourses: any[] = [];
      if (userId) {
        const { data: profile } = await supabase.from('profiles').select('role').eq('id', userId).single();
        if (profile?.role === 'admin') {
          const { data: allC } = await supabase.from('courses').select('id, title, order_index').order('order_index');
          targetCourses = allC || [];
        } else {
          const { data: enrolls } = await supabase.from('enrollments').select('course_id').eq('user_id', userId);
          const courseIds = enrolls?.map(e => e.course_id) || [];
          if (courseIds.length > 0) {
            const { data: userC } = await supabase.from('courses').select('id, title, order_index').in('id', courseIds).order('order_index');
            targetCourses = userC || [];
          } else {
            const { data: allC } = await supabase.from('courses').select('id, title, order_index').order('order_index');
            targetCourses = allC || [];
          }
        }
      } else {
        const { data: allC } = await supabase.from('courses').select('id, title, order_index').order('order_index');
        targetCourses = allC || [];
      }
      setAvailableCourses(targetCourses);
    } catch (err) {
      console.error('Error fetching available courses:', err);
    }
  }, []);

  const handleSelectCourse = (newCourseId: string) => {
    if (newCourseId === currentCourseId) {
      setIsCourseDropdownOpen(false);
      return;
    }
    setIsCourseDropdownOpen(false);
    setCourseFilterQuery('');
    setUploadedBoardImage(null);
    setCurrentCourseId(newCourseId);
    
    try {
      sessionStorage.setItem('lms_active_course_id', newCourseId);
      sessionStorage.setItem('portal_selected_course_id', newCourseId);
      sessionStorage.setItem('portal_filter_course', newCourseId);
      localStorage.setItem('portal_filter_course', newCourseId);
      window.dispatchEvent(new CustomEvent('tony-change-course', { detail: newCourseId }));
    } catch(e) {}
    
    if (onCourseChange) {
      onCourseChange(newCourseId);
    }
  };

  const filteredAvailableCourses = useMemo(() => {
    if (!courseFilterQuery.trim()) return availableCourses;
    const q = courseFilterQuery.toLowerCase().trim();
    return availableCourses.filter(c => (c.title || '').toLowerCase().includes(q));
  }, [availableCourses, courseFilterQuery]);

  const fetchCourseData = async (targetCourseIdOverride?: string) => {
    const activeId = targetCourseIdOverride || currentCourseId;
    if (!activeId) return;
    setIsLoading(true);
    setErrorMessage(null);
    try {
      const { data: { user } } = await supabase.auth.getUser();
      setCurrentUser(user);
      fetchAvailableCourses(user?.id);

      const [
          { data: courseData, error: courseErr },
          { data: modData },
          { data: lecData }
      ] = await Promise.all([
          supabase.from('courses').select('*').eq('id', activeId).single(),
          supabase.from('lecture_modules').select('*').eq('course_id', activeId).order('order_index'),
          supabase.from('lectures').select('*').eq('course_id', activeId).eq('is_published', true)
      ]);

      if (courseErr || !courseData) {
          throw new Error("Không tìm thấy dữ liệu Khóa học trên hệ thống.");
      }
      
      setCourse(courseData);
      setAvailableCourses(prev => {
        if (!prev.some(c => c.id === courseData.id)) {
          return [courseData, ...prev];
        }
        return prev;
      });
      
      const safeModData = modData || [];
      setModules(safeModData);

      let validLectures = (lecData || []).filter(lec => 
          lec.module_id && safeModData.some(mod => mod.id === lec.module_id)
      );

      validLectures.sort((a, b) => {
          const modA = safeModData.find(m => m.id === a.module_id);
          const modB = safeModData.find(m => m.id === b.module_id);
          const modOrderDiff = (modA?.order_index || 0) - (modB?.order_index || 0);
          
          if (modOrderDiff !== 0) {
              return modOrderDiff;
          }
          return (a.order_index || 0) - (b.order_index || 0);
      });

      setLectures(validLectures);

      if (user && validLectures.length > 0) {
         const lectureIds = validLectures.map(l => l.id);
         const [allProgRes, allAssignRes] = await Promise.all([
             supabase.from('lecture_progress')
                 .select('lecture_id, completed_tasks, is_completed')
                 .eq('user_id', user.id)
                 .in('lecture_id', lectureIds),
             supabase.from('assignments')
                 .select('title, card_title, student_completed, task_type')
                 .eq('user_id', user.id)
                 .eq('task_type', 'manual')
                 .eq('student_completed', true)
         ]);

         const allProg = allProgRes.data;
         const completedAssignments = allAssignRes.data || [];

         const pMap: Record<string, string[]> = {};
         const compSet = new Set<string>();

         if (allProg) { 
             allProg.forEach(p => { 
                 pMap[p.lecture_id] = p.completed_tasks || []; 
                 if (p.is_completed) {
                     compSet.add(p.lecture_id);
                 }
             });
         }

         // Reconcile manual assignments into pMap for each lecture
         validLectures.forEach(lec => {
             const taskList = Array.isArray(lec.task_list) ? lec.task_list : [];
             if (taskList.length > 0) {
                 const curTasks = new Set<string>(pMap[lec.id] || []);
                 taskList.forEach((t: any) => {
                     if (t.type === 'manual') {
                         const syncTitle = `${lec.title || ''} : ${t.text}`;
                         const isDone = completedAssignments.some((a: any) => 
                             a.card_title === lec.title && 
                             (a.title === syncTitle || a.title === t.text || a.title === `[Bài giảng] ${t.text}`)
                         );
                         if (isDone) curTasks.add(t.id);
                     }
                 });
                 pMap[lec.id] = Array.from(curTasks);
                 if (pMap[lec.id].length === taskList.length && taskList.length > 0) {
                     compSet.add(lec.id);
                 }
             }
         });
         
         setAllLectureProgress(pMap);
         setCompletedLectures(compSet);
      }

      if (validLectures && validLectures.length > 0) {
         const targetLecId = sessionStorage.getItem('tony_target_lecture_id');
         if (targetLecId) {
           sessionStorage.removeItem('tony_target_lecture_id');
         }
         const savedLectureId = localStorage.getItem(`tony_last_lec_${user?.id}_${activeId}`);
         const targetLecture = (targetLecId && validLectures.find(l => l.id === targetLecId)) || validLectures.find(l => l.id === savedLectureId) || validLectures[0];
         if (targetLecture.module_id) {
             setExpandedModules([targetLecture.module_id]);
         }
         handleSelectLecture(targetLecture.id, user?.id);
      } else {
         if (safeModData.length > 0) {
             setExpandedModules([safeModData[0].id]);
         }
      }
    } catch (error: any) { 
        setErrorMessage(error.message);
    } finally { 
        setIsLoading(false); 
    }
  };

  const handleSelectLecture = async (lectureId: string, userIdOverride?: string) => {
    const targetUserId = userIdOverride || currentUser?.id;
    // Read saved page BEFORE any state changes (persist effect would overwrite it)
    const savedPageStr = localStorage.getItem(`tony_last_page_${targetUserId || ''}_${lectureId}`);
    const savedPage = savedPageStr ? parseInt(savedPageStr) : 1;
    const targetPage = savedPage > 0 ? savedPage : 1;
    
    try {
        setActiveLectureId(lectureId);
        setCurrentPage(targetPage); 
        setPages([]); 
        setCompletedTasks([]);
        setViewedPages(new Set());
        
        if (window.innerWidth < 768) {
            setIsSidebarOpen(false);
        }
        
        if (targetUserId) {
            localStorage.setItem(`tony_last_lec_${targetUserId}_${currentCourseId}`, lectureId);
        }

        const [
            { data: pageData },
            progressRes,
            trRes
        ] = await Promise.all([
            supabase.from('lecture_pages').select('*').eq('lecture_id', lectureId).order('page_number'),
            targetUserId 
                ? supabase.from('lecture_progress').select('*').eq('lecture_id', lectureId).eq('user_id', targetUserId) 
                : Promise.resolve({ data: null }),
            targetUserId
                ? supabase.from('test_results').select('id, test_title, score, total_score, details, created_at').eq('user_id', targetUserId).order('created_at', { ascending: false }).limit(2000)
                : Promise.resolve({ data: null })
        ]);

        const scoreMap = new Map<string, { score: number; total: number; percent: number; isPassed: boolean }>();
        if (trRes && trRes.data) {
            trRes.data.forEach((r: any) => {
                let d = r.details;
                if (typeof d === 'string') {
                    try { d = JSON.parse(d); } catch (e) {}
                }
                const testId = d?.test_id ? String(d.test_id) : (r.test_id ? String(r.test_id) : null);
                const testTitle = r.test_title ? r.test_title.trim().toLowerCase() : null;

                const score = parseFloat(r.score != null ? r.score : 0);
                const total = parseFloat(r.total_score != null ? r.total_score : 0);
                const percent = total > 0 ? Math.round((score / total) * 100) : (score >= 5 ? 100 : Math.round(score * 10));

                let isPassed = false;
                if (d?.bandScore != null && !isNaN(parseFloat(d.bandScore))) {
                    isPassed = parseFloat(d.bandScore) >= 4.0;
                } else if (total > 0) {
                    isPassed = (score / total) >= 0.5; // Cần đạt từ 50% trở lên
                } else {
                    isPassed = score >= 5.0;
                }

                const item = { score, total, percent, isPassed };

                const registerKey = (key: string) => {
                    const existing = scoreMap.get(key);
                    if (!existing) {
                        scoreMap.set(key, item);
                    } else if (!existing.isPassed && isPassed) {
                        scoreMap.set(key, item);
                    } else if (item.percent > existing.percent) {
                        scoreMap.set(key, item);
                    }
                };

                if (testId) registerKey(testId);
                if (testTitle) registerKey(testTitle);
            });
        }
        setTestScoresMap(scoreMap);

        const visiblePages = (pageData || [])
            .filter((p: any) => !String(p.content_html || '').startsWith('<!-- hidden -->'))
            .map((p: any, idx: number) => ({
                ...p,
                page_number: idx + 1
            }));
        setPages(visiblePages);
        
        // Restore saved page (read before state changes above)
        const validTargetPage = (targetPage > 0 && targetPage <= visiblePages.length) ? targetPage : 1;
        setPages(visiblePages);
        setCurrentPage(validTargetPage);
        
        let initialCompletedTasks: string[] = [];
        let isLectureCompleted = false;

        if (targetUserId && progressRes.data && progressRes.data.length > 0) {
           const pData = progressRes.data[0];
           if (pData && Array.isArray(pData.completed_tasks)) {
               initialCompletedTasks = pData.completed_tasks;
               isLectureCompleted = !!pData.is_completed;
           }
        }
        
        // --- ASSIGNMENT & TEST RECONCILIATION ---
        if (targetUserId) {
            // Fetch lecture's task_list to reconcile
            const { data: currentLec } = await supabase.from('lectures').select('title, task_list').eq('id', lectureId).single();
            const taskList = currentLec?.task_list || [];
            
            if (taskList.length > 0) {
                const { data: assignments } = await supabase.from('assignments').select('id, title, test_id, is_completed, student_completed, task_type, card_title, admin_approved').eq('user_id', targetUserId);
                
                const matchedAssigns = assignments?.filter((a: any) => 
                    a.task_type === 'manual' && (!currentLec?.title || a.card_title === currentLec.title)
                ) || [];
                setCurrentLectureAssignments(matchedAssigns);

                let reconciledCompletedTasks: string[] = [];
                
                taskList.forEach((t: any) => {
                    if (t.type === 'manual') {
                        const syncTitle = `${currentLec?.title || ''} : ${t.text}`;
                        const assign = assignments?.find(a => 
                            a.task_type === 'manual' && 
                            (!currentLec?.title || a.card_title === currentLec.title) && (
                                a.title === syncTitle || 
                                a.title === t.text || 
                                a.title === `[Bài giảng] ${t.text}`
                            )
                        );
                        if (initialCompletedTasks.includes(t.id) || assign?.student_completed) {
                            reconciledCompletedTasks.push(t.id);
                        }
                    } else if (t.type === 'exercise') {
                        // 🎯 Bài tập trong kho: PHẢI nộp bài và ĐẠT TỪ 50% ĐIỂM mới được tính hoàn thành!
                        const testKey = t.test_id ? String(t.test_id) : null;
                        const titleKey = t.text ? t.text.trim().toLowerCase() : null;
                        
                        const scoreInfo = (testKey && scoreMap.get(testKey)) || 
                                          (titleKey && scoreMap.get(titleKey)) || 
                                          (titleKey && Array.from(scoreMap.entries()).find(([k]) => titleKey.includes(k) || k.includes(titleKey))?.[1]);
                        
                        if (scoreInfo?.isPassed) {
                            reconciledCompletedTasks.push(t.id);
                        }
                    }
                });
                
                initialCompletedTasks = reconciledCompletedTasks;
                isLectureCompleted = taskList.length > 0 && initialCompletedTasks.length === taskList.length;
                
                if (progressRes.data && progressRes.data.length > 0) {
                     supabase.from('lecture_progress').update({ completed_tasks: initialCompletedTasks, is_completed: isLectureCompleted }).eq('id', progressRes.data[0].id).then();
                } else if (initialCompletedTasks.length > 0) {
                     supabase.from('lecture_progress').insert({ user_id: targetUserId, lecture_id: lectureId, completed_tasks: initialCompletedTasks, is_completed: isLectureCompleted }).then();
                }
            } else {
                setCurrentLectureAssignments([]);
            }
        }
        
        if (targetUserId) {
            setCompletedTasks(initialCompletedTasks);
            setAllLectureProgress(prev => ({
                ...prev, 
                [lectureId]: initialCompletedTasks
            }));
            
            if (isLectureCompleted) {
                setCompletedLectures(prev => new Set(prev).add(lectureId));
            } else {
                setCompletedLectures(prev => {
                    const newSet = new Set(prev);
                    newSet.delete(lectureId);
                    return newSet;
                });
            }
        }
    } catch (err) {
        console.error(err);
    }
  };

  // 🔄 Tự động làm mới điểm và trạng thái hoàn thành khi học sinh nộp bài xong
  // CHỈ cập nhật scores + progress, KHÔNG clear trang/content (tránh reload toàn bộ bài giảng khi alt-tab)
  const refreshScoresOnly = useCallback(async () => {
    if (!activeLectureId || !currentUser?.id) return;
    try {
      const [trRes, progressRes] = await Promise.all([
        supabase.from('test_results').select('id, test_title, score, total_score, details, created_at').eq('user_id', currentUser.id).order('created_at', { ascending: false }).limit(2000),
        supabase.from('lecture_progress').select('*').eq('lecture_id', activeLectureId).eq('user_id', currentUser.id)
      ]);

      // Update score map
      const scoreMap = new Map<string, { score: number; total: number; percent: number; isPassed: boolean }>();
      if (trRes.data) {
        trRes.data.forEach((r: any) => {
          let d = r.details;
          if (typeof d === 'string') { try { d = JSON.parse(d); } catch (e) {} }
          const testId = d?.test_id ? String(d.test_id) : (r.test_id ? String(r.test_id) : null);
          const testTitle = r.test_title ? r.test_title.trim().toLowerCase() : null;
          const score = parseFloat(r.score != null ? r.score : 0);
          const total = parseFloat(r.total_score != null ? r.total_score : 0);
          const percent = total > 0 ? Math.round((score / total) * 100) : (score >= 5 ? 100 : Math.round(score * 10));
          let isPassed = false;
          if (d?.bandScore != null && !isNaN(parseFloat(d.bandScore))) { isPassed = parseFloat(d.bandScore) >= 4.0; }
          else if (total > 0) { isPassed = (score / total) >= 0.5; }
          else { isPassed = score >= 5.0; }
          const item = { score, total, percent, isPassed };
          const registerKey = (key: string) => {
            const existing = scoreMap.get(key);
            if (!existing) { scoreMap.set(key, item); }
            else if (!existing.isPassed && isPassed) { scoreMap.set(key, item); }
            else if (item.percent > existing.percent) { scoreMap.set(key, item); }
          };
          if (testId) registerKey(testId);
          if (testTitle) registerKey(testTitle);
        });
      }
      setTestScoresMap(scoreMap);

      // Update completed tasks from progress (reconcile with scores)
      const currentLec = lectures.find(l => l.id === activeLectureId);
      const taskList = currentLec?.task_list || [];
      if (taskList.length > 0) {
        const pData = (progressRes.data && progressRes.data.length > 0) ? progressRes.data[0] : null;
        let initialCompletedTasks = pData?.completed_tasks || [];
        
        const { data: assignments } = await supabase.from('assignments').select('id, title, test_id, is_completed, student_completed, task_type, card_title, admin_approved').eq('user_id', currentUser.id);
        
        const matchedAssigns = assignments?.filter((a: any) => 
          a.task_type === 'manual' && (!currentLec?.title || a.card_title === currentLec.title)
        ) || [];
        setCurrentLectureAssignments(matchedAssigns);

        let reconciledCompletedTasks: string[] = [];
        taskList.forEach((t: any) => {
          if (t.type === 'manual') {
            const syncTitle = `${currentLec?.title || ''} : ${t.text}`;
            const assign = assignments?.find((a: any) => 
              a.task_type === 'manual' && 
              (!currentLec?.title || a.card_title === currentLec.title) && (
                a.title === syncTitle || a.title === t.text || a.title === `[Bài giảng] ${t.text}`
              )
            );
            if (initialCompletedTasks.includes(t.id) || assign?.student_completed) {
              reconciledCompletedTasks.push(t.id);
            }
          } else if (t.type === 'exercise') {
            const testKey = t.test_id ? String(t.test_id) : null;
            const titleKey = t.text ? t.text.trim().toLowerCase() : null;
            const scoreInfo = (testKey && scoreMap.get(testKey)) || 
                              (titleKey && scoreMap.get(titleKey)) || 
                              (titleKey && Array.from(scoreMap.entries()).find(([k]) => titleKey.includes(k) || k.includes(titleKey))?.[1]);
            if (scoreInfo?.isPassed) { reconciledCompletedTasks.push(t.id); }
          }
        });

        const isLectureCompleted = taskList.length > 0 && reconciledCompletedTasks.length === taskList.length;
        setCompletedTasks(reconciledCompletedTasks);
        setAllLectureProgress(prev => ({ ...prev, [activeLectureId]: reconciledCompletedTasks }));
        if (isLectureCompleted) {
          setCompletedLectures(prev => new Set(prev).add(activeLectureId));
        } else {
          setCompletedLectures(prev => {
            const next = new Set(prev);
            next.delete(activeLectureId);
            return next;
          });
        }
        // Persist reconciled data
        if (pData) {
          supabase.from('lecture_progress').update({ completed_tasks: reconciledCompletedTasks, is_completed: isLectureCompleted }).eq('id', pData.id).then();
        } else if (reconciledCompletedTasks.length > 0) {
          supabase.from('lecture_progress').insert({ user_id: currentUser.id, lecture_id: activeLectureId, completed_tasks: reconciledCompletedTasks, is_completed: isLectureCompleted }).then();
        }
      }
    } catch (err) {
      console.error('[LectureViewer] Error refreshing scores:', err);
    }
  }, [activeLectureId, currentUser, lectures]);

  useEffect(() => {
    // Khi nộp bài xong → cập nhật scores (lightweight, không reload nội dung)
    window.addEventListener('tony-refresh-lecture-progress', refreshScoresOnly);
    return () => {
      window.removeEventListener('tony-refresh-lecture-progress', refreshScoresOnly);
    };
  }, [refreshScoresOnly]);

  const toggleModule = (modId: string) => {
      setExpandedModules(prev => 
          prev.includes(modId) ? prev.filter(id => id !== modId) : [...prev, modId]
      );
  };

  const handleToggleTask = useCallback(async (taskId: string) => {
      if (!currentUser || !activeLectureId) {
          return;
      }
      
      const safeLectureTasks = Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [];
      const taskObj = safeLectureTasks.find((t: any) => t.id === taskId);
      
      // 🔒 CẤM học sinh tick thủ công bài tập trong kho! Bài tập phải làm và đạt từ 50% mới tự động hoàn thành!
      if (taskObj?.type === 'exercise') {
          return;
      }
      
      setCompletedTasks(prev => {
         const isNowCompleted = !prev.includes(taskId);
         const newCompleted = isNowCompleted ? [...prev, taskId] : prev.filter(id => id !== taskId);
         const isCompleted = safeLectureTasks.length > 0 && newCompleted.length === safeLectureTasks.length;
         
         // Cập nhật currentLectureAssignments local state ngay lập tức
         setCurrentLectureAssignments(cur => {
             const syncTitle = `${activeLecture?.title || ''} : ${taskObj?.text || ''}`;
             return cur.map(a => {
                 if (a.title === syncTitle || a.title === taskObj?.text || a.title === `[Bài giảng] ${taskObj?.text}`) {
                     return {
                         ...a,
                         student_completed: isNowCompleted,
                         admin_approved: isNowCompleted ? a.admin_approved : false
                     };
                 }
                 return a;
             });
         });

         // Đồng bộ với Assignment
         if (taskObj && taskObj.type === 'manual') {
             const syncTitle = `${activeLecture?.title || ''} : ${taskObj.text}`;
             const payload: any = { student_completed: isNowCompleted, updated_at: new Date().toISOString() };
             if (!isNowCompleted) payload.admin_approved = false;
             
             let query = supabase.from('assignments')
                 .update(payload)
                 .eq('user_id', currentUser.id)
                 .eq('task_type', 'manual');
             if (activeLecture?.title) {
                 query = query.eq('card_title', activeLecture.title);
             }
             query.in('title', [syncTitle, `[Bài giảng] ${taskObj.text}`, taskObj.text]).then(() => {
                 window.dispatchEvent(new CustomEvent('tony-refresh-lecture-progress'));
             });
         }
         
         supabase.from('lecture_progress')
             .select('id')
             .eq('user_id', currentUser.id)
             .eq('lecture_id', activeLectureId)
             .then(({ data: existingArray }) => {
                 if (existingArray && existingArray.length > 0) {
                     supabase.from('lecture_progress')
                         .update({ completed_tasks: newCompleted, is_completed: isCompleted })
                         .eq('id', existingArray[0].id)
                         .then();
                 } else {
                     supabase.from('lecture_progress')
                         .insert({ user_id: currentUser.id, lecture_id: activeLectureId, completed_tasks: newCompleted, is_completed: isCompleted })
                         .then();
                 }
             }).catch();

         setAllLectureProgress(allPrev => ({ 
             ...allPrev, 
             [activeLectureId]: newCompleted 
         }));

         if (isCompleted) {
             setCompletedLectures(prevSet => new Set(prevSet).add(activeLectureId));
             supabase.from('activity_logs').insert([{
                 user_id: currentUser.id,
                 action_type: 'finish_lecture',
                 details: { lecture_title: activeLecture?.title || "Bài giảng" }
             }]).then();
         } else {
             setCompletedLectures(prevSet => {
                 const newSet = new Set(prevSet);
                 newSet.delete(activeLectureId);
                 return newSet;
             });
         }
         
         return newCompleted;
      });
  }, [currentUser, activeLectureId, lectures, activeLecture]);

  const handleStartTaskExercise = async (task: any) => {
      if (!onStartTest || !task.test_id) {
          return;
      }
      
      try {
         const { data: testData, error } = await supabase.from('tests').select('*').eq('id', task.test_id).single();

         if (error || !testData) { 
             alert("Bài tập này hiện không khả dụng. Vui lòng liên hệ Admin.");
             return; 
         }
         
         const type = String(testData.test_type || '').toLowerCase();

          if (type === 'igcse-direct') {
              onStartTest('igcse-direct', testData);
          } else if (type.includes('igcse')) {
              onStartTest('igcse', testData);
          } else if (type.includes('split-standard')) {
              onStartTest('split-standard', testData);
          } else if (type.includes('standard-reading')) {
              onStartTest('standard-reading', testData);
          } else if (type.includes('splitscreen') && type.includes('standard')) {
              onStartTest('standard-splitscreen', testData);
          } else if (type.includes('standard')) {
              onStartTest('standard', testData);
         } else if (type.includes('case-study') || type.includes('business')) {
             onStartTest('case-study', testData);
         } else if (type === 'ielts-writing') {
             onStartTest('ielts-writing', testData);
         } else if (type === 'ielts-speaking') {
             onStartTest('ielts-speaking', testData);
         } else if (type.includes('ielts')) {
             onStartTest('computer', testData);
         } else {
             onStartTest('standard', testData);
         }
      } catch (err) {
          console.error(err);
      }
  };

  const handleNextPage = () => {
    if (currentPage < pages.length) {
        const nextP = currentPage + 1;
        setCurrentPage(nextP);
        persistPage(nextP);
    } else {
      const currentIndex = lectures.findIndex(l => l.id === activeLectureId);

      if (currentIndex !== -1 && currentIndex < lectures.length - 1) {
         const nextLecture = lectures[currentIndex + 1];

         if (nextLecture.module_id && !expandedModules.includes(nextLecture.module_id)) {
             setExpandedModules(prev => [...prev, nextLecture.module_id]);
         }
         
         handleSelectLecture(nextLecture.id);
      }
    }
  };

  const handlePrevPage = () => {
    if (currentPage > 1) {
        const prevP = currentPage - 1;
        setCurrentPage(prevP);
        persistPage(prevP);
    } else {
       const currentIndex = lectures.findIndex(l => l.id === activeLectureId);

       if (currentIndex > 0) {
          const prevLecture = lectures[currentIndex - 1];

          if (prevLecture.module_id && !expandedModules.includes(prevLecture.module_id)) {
              setExpandedModules(prev => [...prev, prevLecture.module_id]);
          }
          
          handleSelectLecture(prevLecture.id);
       }
    }
  };

  const fetchWithTimeout = async (url: string, ms = 4000) => {
    const controller = new AbortController();
    const id = setTimeout(() => controller.abort(), ms);
    try {
      const response = await fetch(url, { signal: controller.signal });
      clearTimeout(id);
      return response;
    } catch (err) {
      clearTimeout(id);
      throw err;
    }
  };

  const triggerDictionary = useCallback((word: string, x: number, y: number, rectTop: number) => {
    const cleanWord = word.trim();
    if (!cleanWord) return;
    setDictPopup({ show: true, word: cleanWord, x, y, rectTop, data: null, isLoading: true });
    
    Promise.allSettled([
        fetchWithTimeout(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(cleanWord.toLowerCase())}`)
            .then(r => r.ok ? r.json() : Promise.reject()),
        fetchWithTimeout(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=vi&dt=t&dt=rm&dj=1&q=${encodeURIComponent(cleanWord)}`)
            .then(r => r.ok ? r.json() : Promise.reject()),
        fetchWithTimeout(`https://en.wiktionary.org/api/rest_v1/page/html/${encodeURIComponent(cleanWord.toLowerCase())}`)
            .then(r => r.ok ? r.text() : Promise.reject())
    ]).then(([enRes, viRes, wikRes]) => {
         let phonetics = '';
         let audio = '';
         let translation = 'Không tìm thấy bản dịch (Hệ thống bận).';
        
         if (enRes.status === 'fulfilled' && enRes.value && enRes.value[0]) {
             const phs = enRes.value[0].phonetics || [];
             const ukPh = phs.find((p:any) => p.audio && p.audio.includes('-uk.mp3')) || phs.find((p:any) => p.text && p.text.includes('uk'));
             const usPh = phs.find((p:any) => p.audio && p.audio.includes('-us.mp3'));
             const anyPh = phs.find((p:any) => p.text);
             phonetics = ukPh?.text || anyPh?.text || enRes.value[0].phonetic || '';
             audio = ukPh?.audio || usPh?.audio || phs.find((p:any) => p.audio)?.audio || '';
             if (phonetics && !phonetics.includes('UK') && phonetics.includes('/')) {
                  phonetics = 'UK ' + phonetics;
             }
         }
         
         // Fallback to Wiktionary for true UK IPA
         if (!phonetics && wikRes.status === 'fulfilled' && wikRes.value) {
             const ipaMatches = [...wikRes.value.matchAll(/"wt":"(\/[^/]+\/)"/g)];
             if (ipaMatches.length > 0) {
                 phonetics = 'UK ' + ipaMatches[0][1];
             }
         }
      
         // Fallback to Google phonetics and audio
         if (viRes.status === 'fulfilled' && viRes.value) {
             const data = viRes.value;
             if (!phonetics) {
                 const ggPh = data.sentences?.find((s: any) => s.src_translit)?.src_translit;
                 if (ggPh) phonetics = '/' + ggPh + '/';
             }
             if (!audio) {
                 audio = `https://translate.google.com/translate_tts?ie=UTF-8&q=${encodeURIComponent(cleanWord)}&tl=en&client=tw-ob`;
             }
             const transStr = data.sentences?.find((s: any) => s.trans)?.trans;
             if (transStr) {
                 translation = transStr;
             }
         }
        
         setDictPopup(prev => prev ? { 
            ...prev, 
            data: { phonetics, audio, translation }, 
            isLoading: false 
         } : null);
    });
  }, []);

  const handleTextSelection = useCallback(() => {
     setTimeout(() => {
        const selection = window.getSelection();
        if (!selection || selection.rangeCount === 0) return;
        
        const text = selection.toString().trim();
        if (!text) return;
        
        if (text.length > 0 && text.length < 40 && text.split(' ').length <= 4) {
           const range = selection.getRangeAt(0);
           const rect = range.getBoundingClientRect();
           triggerDictionary(text, rect.left + (rect.width/2), rect.bottom, rect.top);
        }
     }, 100);
  }, [triggerDictionary]);

  const toggleFullScreen = () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(e => console.log(e));
    } else if (document.exitFullscreen) {
        document.exitFullscreen();
    }
  };

  const getEmbedUrl = (url: string) => {
    if (url.includes('youtube.com/playlist?list=')) {
        return url.replace('playlist?list=', 'embed/videoseries?list=');
    }
    if (url.includes('youtube.com/watch?v=')) {
        return url.replace('watch?v=', 'embed/');
    }
    if (url.includes('youtu.be/')) {
        return url.replace('youtu.be/', 'youtube.com/embed/');
    }
    return url;
  };

  const handleCallTutor = () => {
      const safeHtml = currentHtmlContent ? currentHtmlContent.replace(/<[^>]+>/g, '').slice(0, 2000) : 'Không có dữ liệu văn bản';
      const safeTitle = activeLecture?.title || 'Bài giảng English';
      
      const tutorContext = {
          overall: "N/A",
          transcript: `Học sinh đang học bài: "${safeTitle}". \nNội dung bài học: "${safeHtml}".`,
          feedback: "Bạn là gia sư đang dạy bài giảng này. Hãy chủ động chào học sinh, nhắc tên bài học và hỏi xem học sinh không hiểu phần nào trong nội dung trên để bạn giải thích bằng giọng nói ân cần."
      };
      
      sessionStorage.setItem('tony_live_mode', 'TUTOR');
      sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
      
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
  };

  const safeLectureTasks = useMemo(() => {
    const raw = Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [];
    return [...raw].sort((a: any, b: any) => {
      const isExA = a.type === 'exercise' ? 1 : 0;
      const isExB = b.type === 'exercise' ? 1 : 0;
      return isExA - isExB;
    });
  }, [activeLecture]);
  const safeCompletedTasks = Array.isArray(completedTasks) ? completedTasks : [];
  const isLastLectureAndPage = (totalPages === 0 || currentPage === totalPages) && lectures.findIndex(l => l.id === activeLectureId) === lectures.length - 1;

  const isAllTasksDone = safeLectureTasks.length > 0 && safeCompletedTasks.length === safeLectureTasks.length;

  // 📖 TRA TỪ ĐIỂN - State & Logic
  const [dictQuery, setDictQuery] = useState('');
  const [dictResults, setDictResults] = useState<any>(null);
  const [isDictLoading, setIsDictLoading] = useState(false);
  const [isDictOpen, setIsDictOpen] = useState(false);
  const dictRef = useRef<HTMLDivElement>(null);
  const dictTimerRef = useRef<any>(null);

  // Phát hiện ngôn ngữ: có ký tự tiếng Việt có dấu → Vietnamese
  const isVietnamese = (text: string) => /[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ]/i.test(text);

  const lookupDictionary = useCallback(async (word: string) => {
    const trimmed = word.trim();
    if (!trimmed || trimmed.length < 2) { setDictResults(null); return; }
    setIsDictLoading(true);
    setIsDictOpen(true);

    try {
      const isVi = isVietnamese(trimmed);

      if (isVi) {
        // VIETNAMESE → ENGLISH
        const res = await fetchWithTimeout(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=vi&tl=en&dt=t&dj=1&q=${encodeURIComponent(trimmed)}`);
        const data = await res.json();
        const translation = data?.sentences?.find((s: any) => s.trans)?.trans || data?.[0]?.[0]?.[0] || '';

        setDictResults({
          type: 'vi-en',
          word: trimmed,
          translation,
          alternatives: [],
        });
      } else {
        // ENGLISH → VIETNAMESE
        const [dictRes, transRes, wikRes] = await Promise.allSettled([
          fetchWithTimeout(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(trimmed.toLowerCase())}`),
          fetchWithTimeout(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=vi&dt=t&dt=rm&dj=1&q=${encodeURIComponent(trimmed)}`),
          fetchWithTimeout(`https://en.wiktionary.org/api/rest_v1/page/html/${encodeURIComponent(trimmed.toLowerCase())}`)
        ]);

        let definitions: any[] = [];
        let phonetic = '';
        let audioUrl = '';

        if (dictRes.status === 'fulfilled' && dictRes.value.ok) {
          const dictData = await dictRes.value.json();
          if (Array.isArray(dictData) && dictData.length > 0) {
            const entry = dictData[0];
            const phs = entry.phonetics || [];
            const ukPh = phs.find((p: any) => p.audio && p.audio.includes('-uk.mp3')) || phs.find((p:any) => p.text && p.text.includes('uk'));
            const usPh = phs.find((p: any) => p.audio && p.audio.includes('-us.mp3'));
            const anyPh = phs.find((p: any) => p.text);
            phonetic = ukPh?.text || anyPh?.text || entry.phonetic || '';
            audioUrl = ukPh?.audio || usPh?.audio || phs.find((p: any) => p.audio)?.audio || '';
            if (phonetic && !phonetic.includes('UK') && phonetic.includes('/')) {
                phonetic = 'UK ' + phonetic;
            }
            definitions = (entry.meanings || []).slice(0, 3).map((m: any) => ({
              partOfSpeech: m.partOfSpeech,
              defs: (m.definitions || []).slice(0, 2).map((d: any) => ({
                definition: d.definition,
                example: d.example || '',
              })),
            }));
          }
        }
        
        // Wiktionary Fallback for true UK IPA
        if (!phonetic && wikRes.status === 'fulfilled' && wikRes.value) {
             const ipaMatches = [...wikRes.value.matchAll(/"wt":"(\/[^/]+\/)"/g)];
             if (ipaMatches.length > 0) {
                 phonetic = 'UK ' + ipaMatches[0][1];
             }
        }

        let viTranslation = '';
        if (transRes.status === 'fulfilled' && transRes.value.ok) {
          const data = await transRes.value.json();
          viTranslation = data.sentences?.find((s: any) => s.trans)?.trans || data?.[0]?.[0]?.[0] || '';
          if (!phonetic) {
              const ggPh = data.sentences?.find((s: any) => s.src_translit)?.src_translit || data?.[0]?.[1]?.[3];
              if (ggPh) phonetic = '/' + ggPh + '/';
          }
          if (!audioUrl) {
              audioUrl = `https://translate.google.com/translate_tts?ie=UTF-8&q=${encodeURIComponent(trimmed)}&tl=en&client=tw-ob`;
          }
        }

        setDictResults({
          type: 'en-vi',
          word: trimmed,
          phonetic,
          audioUrl,
          viTranslation,
          definitions,
        });
      }
    } catch (error) {
      setDictResults({
        type: 'error',
        word: trimmed,
        message: 'Lỗi kết nối từ điển',
      });
    }
    setIsDictLoading(false);
  }, []);

  const handleDictInput = (value: string) => {
    setDictQuery(value);
    if (dictTimerRef.current) clearTimeout(dictTimerRef.current);
    if (!value.trim()) { setDictResults(null); setIsDictOpen(false); return; }
    dictTimerRef.current = setTimeout(() => lookupDictionary(value), 500);
  };

  // Đóng dropdown khi click ra ngoài
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (dictRef.current && !dictRef.current.contains(e.target as Node)) {
        setIsDictOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  if (isLoading) {
      return (
          <div className="min-h-[100dvh] flex flex-col items-center justify-center bg-slate-50">
              <div className="w-12 h-12 border-4 border-[#0ea5e9]/30 border-t-[#0ea5e9] rounded-full animate-spin"></div>
              <p className="mt-4 text-slate-500 font-medium">Đang tải không gian học...</p>
          </div>
      );
  }
  
  if (errorMessage) {
      return (
          <div className="min-h-[100dvh] flex flex-col items-center justify-center bg-slate-50">
              <div className="text-5xl mb-4 text-red-400">⚠️</div>
              <h2 className="text-xl font-bold text-slate-800 mb-2">Lỗi tải bài giảng</h2>
              <p className="text-slate-500 mb-6">{errorMessage}</p>
              <button 
                  onClick={onBack} 
                  className="bg-[#0ea5e9] text-white px-6 py-2.5 rounded-xl font-semibold shadow-md hover:bg-[#0284c7] transition-all"
              >
                  Quay lại trang chủ
              </button>
          </div>
      );
  }

  return (
    <div className="flex flex-col h-[100dvh] w-full bg-[#f8fafc] font-sans text-slate-800 overflow-hidden relative overscroll-none">
      
      <header 
         className="h-[64px] backdrop-blur-md text-white flex items-center px-4 md:px-6 shrink-0 z-30 shadow-md justify-between border-b border-white/20 transition-all duration-300"
         style={{
             background: lectureTheme?.titleBg || 'linear-gradient(135deg, #005a9c 0%, #004377 100%)',
            color: lectureTheme?.titleText || '#ffffff'
         }}
      >
         <div className="flex items-center gap-2 md:gap-4 min-w-0 flex-1">
            <button 
                onClick={onBack} 
                className="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/20 transition-all shrink-0" 
                title="Quay lại"
            >
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" /></svg>
            </button>
            <button 
                onClick={() => setIsSidebarOpen(!isSidebarOpen)} 
                className="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/20 transition-all shrink-0" 
                title="Danh mục"
            >
               <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M4 6h16M4 12h16M4 18h7" /></svg>
            </button>
            
            {/* 🎓 THANH LỌC / CHUYỂN KHÓA HỌC */}
            <div className="relative shrink-0" ref={courseDropdownRef}>
               <button 
                  type="button"
                  onClick={() => setIsCourseDropdownOpen(!isCourseDropdownOpen)}
                  className="flex items-center gap-1.5 sm:gap-2 px-2 sm:px-3 py-1 sm:py-1.5 rounded-xl bg-white/15 hover:bg-white/25 border border-white/20 transition-all text-left shadow-sm hover:shadow-md hover:border-white/40 group max-w-[110px] xs:max-w-[150px] sm:max-w-[260px] md:max-w-[320px]"
                  title="Bấm để lọc / chuyển khóa học khác"
               >
                  <div className="flex flex-col min-w-0 flex-1">
                     <div className="flex items-center gap-1.5">
                        <span className="text-[13px] sm:text-[15px] font-bold text-white truncate leading-tight tracking-tight">
                           {course?.title || 'Đang tải khóa học...'}
                        </span>
                        <span className={`text-[10px] text-white/80 transition-transform duration-200 shrink-0 ${isCourseDropdownOpen ? 'rotate-180' : ''}`}>
                           ▼
                        </span>
                     </div>
                     <div className="hidden sm:flex items-center gap-2 mt-0.5">
                        <div className="w-20 sm:w-24 h-1.5 bg-black/20 rounded-full overflow-hidden">
                           <div className="h-full bg-emerald-400 rounded-full transition-all duration-300" style={{ width: `${courseProgress}%` }}></div>
                        </div>
                        <span className="text-[10px] font-medium opacity-80">{courseProgress}%</span>
                     </div>
                  </div>
               </button>

               {/* DROPDOWN DANH SÁCH KHÓA HỌC */}
               {isCourseDropdownOpen && (
                  <div className="fixed top-[68px] left-3 right-3 sm:left-auto sm:right-auto sm:absolute sm:top-full sm:left-0 sm:mt-2 w-auto sm:w-[320px] max-h-[420px] bg-white rounded-2xl shadow-[0_20px_60px_rgba(0,0,0,0.25)] border border-slate-100 overflow-hidden z-[110] animate-in fade-in slide-in-from-top-2 duration-200 text-slate-800 flex flex-col">
                     <div className="p-3 bg-slate-50 border-b border-slate-100">
                        <div className="flex items-center justify-between mb-2">
                           <span className="text-[11px] font-bold uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
                              <span>📚</span> Chọn khóa học
                           </span>
                           <span className="text-[11px] font-semibold text-[#0ea5e9] bg-[#0ea5e9]/10 px-2 py-0.5 rounded-full">
                              {availableCourses.length} khóa
                           </span>
                        </div>
                        {availableCourses.length > 3 && (
                           <div className="relative">
                              <input
                                 type="text"
                                 placeholder="Tìm khóa học..."
                                 value={courseFilterQuery}
                                 onChange={(e) => setCourseFilterQuery(e.target.value)}
                                 className="w-full px-3 py-1.5 pl-8 text-[13px] bg-white border border-slate-200 rounded-xl focus:outline-none focus:border-[#0ea5e9] focus:ring-2 focus:ring-[#0ea5e9]/20 text-slate-800 placeholder-slate-400"
                                 onClick={(e) => e.stopPropagation()}
                                 autoFocus
                              />
                              <svg className="w-4 h-4 absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                              </svg>
                              {courseFilterQuery && (
                                 <button 
                                    onClick={() => setCourseFilterQuery('')}
                                    className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 text-xs"
                                 >
                                    ✕
                                 </button>
                              )}
                           </div>
                        )}
                     </div>

                     <div className="overflow-y-auto p-1.5 custom-scrollbar flex-1 space-y-1 max-h-[300px]">
                        {filteredAvailableCourses.length === 0 ? (
                           <div className="p-6 text-center text-slate-400 text-[13px]">
                              Không tìm thấy khóa học nào
                           </div>
                        ) : (
                           filteredAvailableCourses.map((c: any) => {
                              const isSelected = c.id === currentCourseId;
                              return (
                                 <button
                                    key={c.id}
                                    onClick={() => handleSelectCourse(c.id)}
                                    className={`w-full text-left px-3.5 py-2.5 rounded-xl text-[13px] font-medium transition-all flex items-center justify-between gap-3 group ${
                                       isSelected 
                                          ? 'bg-[#0ea5e9]/10 text-[#0ea5e9] font-bold border border-[#0ea5e9]/20' 
                                          : 'text-slate-700 hover:bg-slate-100 hover:text-slate-900 border border-transparent'
                                    }`}
                                 >
                                    <div className="flex items-center gap-2.5 min-w-0 flex-1">
                                       <span className="text-base shrink-0">{isSelected ? '📖' : '📘'}</span>
                                       <span className="truncate">{c.title}</span>
                                    </div>
                                    {isSelected ? (
                                       <span className="text-[11px] font-bold bg-[#0ea5e9] text-white px-2 py-0.5 rounded-full shrink-0 shadow-sm">
                                          Đang học
                                       </span>
                                    ) : (
                                       <span className="opacity-0 group-hover:opacity-100 text-[11px] text-[#0ea5e9] font-semibold shrink-0 transition-opacity">
                                          Chọn ➜
                                       </span>
                                    )}
                                 </button>
                              );
                           })
                        )}
                     </div>
                  </div>
               )}
            </div>
             
            {/* 🎨 NÚT ĐỔI MÀU NỀN BÊN PHẢI NÚT CHUYỂN KHÓA HỌC */}
            <button
              type="button"
              onClick={() => setIsLectureThemeModalOpen(true)}
              className="flex items-center justify-center w-8 h-8 sm:w-9 sm:h-9 rounded-xl transition-all bg-white/15 hover:bg-white/25 text-white border border-white/20 shadow-sm hover:scale-105 active:scale-95 shrink-0"
              title="Đổi màu nền bài giảng"
            >
              <span className="text-sm sm:text-base">🎨</span>
            </button>
          </div>



         {/* 📖 THANH TRA TỪ ĐIỂN - CHÍNH GIỮA */}
         <div className="hidden md:flex flex-1 justify-center mx-4 max-w-md relative" ref={dictRef}>
           <div className="relative w-full max-w-[340px]">
             <div className="flex items-center bg-white/15 hover:bg-white/25 focus-within:bg-white/30 rounded-full border border-white/20 transition-all px-3 h-9">
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4 text-white/70 shrink-0">
                 <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
               </svg>
               <input
                 type="text"
                 value={dictQuery}
                 onChange={(e) => handleDictInput(e.target.value)}
                 onFocus={() => { if (dictResults) setIsDictOpen(true); }}
                 onKeyDown={(e) => { if (e.key === 'Enter') { e.preventDefault(); lookupDictionary(dictQuery); } }}
                 placeholder="Tra từ điển EN ↔ VI..."
                 className="flex-1 bg-transparent text-white placeholder-white/50 text-[13px] font-medium px-2 py-1 outline-none border-none min-w-0"
               />
               {isDictLoading && (
                 <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin shrink-0"></div>
               )}
               {dictQuery && !isDictLoading && (
                 <button onClick={() => { setDictQuery(''); setDictResults(null); setIsDictOpen(false); }} className="text-white/50 hover:text-white shrink-0">
                   <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.28 7.22a.75.75 0 00-1.06 1.06L8.94 10l-1.72 1.72a.75.75 0 101.06 1.06L10 11.06l1.72 1.72a.75.75 0 101.06-1.06L11.06 10l1.72-1.72a.75.75 0 00-1.06-1.06L10 8.94 8.28 7.22z" clipRule="evenodd" /></svg>
                 </button>
               )}
             </div>

             {/* DROPDOWN KẾT QUẢ */}
             {isDictOpen && dictResults && (
               <div className="absolute top-full left-1/2 -translate-x-1/2 mt-2 w-[380px] max-h-[420px] overflow-y-auto bg-white rounded-2xl shadow-[0_20px_60px_rgba(0,0,0,0.2)] border border-slate-100 z-[100] animate-in slide-in-from-top-2 duration-200 custom-scrollbar">
                 
                 {dictResults.type === 'error' && (
                   <div className="p-5 text-center text-slate-400 text-[14px]">
                     <span className="text-2xl block mb-2">🔍</span>
                     {dictResults.message}
                   </div>
                 )}

                 {dictResults.type === 'en-vi' && (
                   <div className="p-5">
                     {/* TỪ + PHIÊN ÂM */}
                     <div className="flex items-center gap-3 mb-4">
                       <h3 className="text-[20px] font-black text-slate-800">{dictResults.word}</h3>
                       {dictResults.phonetic && (
                         <span className="text-[13px] text-slate-400 font-medium">{dictResults.phonetic}</span>
                       )}
                       {dictResults.audioUrl && (
                         <button
                           onClick={() => { const a = new Audio(dictResults.audioUrl); a.play(); }}
                           className="w-7 h-7 rounded-full bg-[#0ea5e9]/10 hover:bg-[#0ea5e9]/20 flex items-center justify-center text-[#0ea5e9] transition-colors"
                         >
                           🔊
                         </button>
                       )}
                     </div>

                     {/* NGHĨA TIẾNG VIỆT */}
                     {dictResults.viTranslation && (
                       <div className="bg-[#0ea5e9]/5 rounded-xl px-4 py-3 mb-4 border border-[#0ea5e9]/10">
                         <span className="text-[10px] font-bold uppercase tracking-widest text-[#0ea5e9] block mb-1">Nghĩa tiếng Việt</span>
                         <span className="text-[16px] font-bold text-slate-800">{dictResults.viTranslation}</span>
                       </div>
                     )}

                     {/* ĐỊNH NGHĨA TIẾNG ANH + VÍ DỤ */}
                     {dictResults.definitions?.length > 0 && (
                       <div className="space-y-3">
                         {dictResults.definitions.map((m: any, i: number) => (
                           <div key={i}>
                             <span className="inline-block bg-slate-100 text-slate-500 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md mb-1.5">{m.partOfSpeech}</span>
                             {m.defs.map((d: any, j: number) => (
                               <div key={j} className="ml-1 mb-2">
                                 <p className="text-[13px] text-slate-700 leading-relaxed">• {d.definition}</p>
                                 {d.example && (
                                   <p className="text-[12px] text-slate-400 italic ml-3 mt-0.5">"{d.example}"</p>
                                 )}
                               </div>
                             ))}
                           </div>
                         ))}
                       </div>
                     )}

                     {!dictResults.viTranslation && dictResults.definitions?.length === 0 && (
                       <div className="text-center text-slate-400 text-[14px] py-4">
                         <span className="text-2xl block mb-2">📚</span>
                         Không tìm thấy từ "<strong>{dictResults.word}</strong>"
                       </div>
                     )}
                   </div>
                 )}

                 {dictResults.type === 'vi-en' && (
                   <div className="p-5">
                     <h3 className="text-[20px] font-black text-slate-800 mb-3">{dictResults.word}</h3>
                     {dictResults.translation && (
                       <div className="bg-emerald-50 rounded-xl px-4 py-3 mb-4 border border-emerald-100">
                         <span className="text-[10px] font-bold uppercase tracking-widest text-emerald-600 block mb-1">English Translation</span>
                         <span className="text-[16px] font-bold text-slate-800">{dictResults.translation}</span>
                       </div>
                     )}
                     {dictResults.alternatives?.length > 0 && (
                       <div>
                         <span className="text-[10px] font-bold uppercase tracking-widest text-slate-400 block mb-2">Gợi ý khác</span>
                         <div className="flex flex-wrap gap-2">
                           {dictResults.alternatives.map((alt: string, i: number) => (
                             <span key={i} className="bg-slate-50 border border-slate-200 text-slate-600 text-[12px] font-medium px-3 py-1.5 rounded-lg">{alt}</span>
                           ))}
                         </div>
                       </div>
                     )}
                     {!dictResults.translation && (
                       <div className="text-center text-slate-400 text-[14px] py-4">
                         <span className="text-2xl block mb-2">📚</span>
                         Không tìm thấy nghĩa cho "<strong>{dictResults.word}</strong>"
                       </div>
                     )}
                   </div>
                 )}
               </div>
             )}
           </div>
         </div>

          <div className="flex items-center gap-1.5 sm:gap-3 shrink-0 ml-2">
              {/* 📱 NÚT MENU THAO TÁC NHANH CHO DI ĐỘNG (< sm) */}
              <div className="relative sm:hidden">
                <button
                  type="button"
                  onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                  className="w-9 h-9 rounded-full flex items-center justify-center bg-white/15 hover:bg-white/25 text-white font-black text-base transition-all active:scale-95 border border-white/20 shadow-xs"
                  title="Menu chức năng"
                >
                  ⋯
                </button>

                {isMobileMenuOpen && (
                  <>
                    <div className="fixed inset-0 z-40" onClick={() => setIsMobileMenuOpen(false)} />
                    <div className="absolute right-0 top-full mt-2 w-52 bg-white rounded-2xl shadow-2xl border border-slate-100 py-1.5 z-50 text-slate-800 animate-in fade-in slide-in-from-top-2 duration-150">
                      <button
                        onClick={() => {
                          setIsMobileMenuOpen(false);
                          localStorage.setItem('portal_filter_course', currentCourseId);
                          sessionStorage.setItem('portal_filter_course', currentCourseId);
                          sessionStorage.setItem('lms_portal_tab', 'calendar');
                          onBack();
                        }}
                        className="w-full text-left px-4 py-2.5 text-[13px] font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0ea5e9] flex items-center gap-2.5 transition-colors"
                      >
                        <span>📅</span> Lịch báo bài
                      </button>
                      <button
                        onClick={() => {
                          setIsMobileMenuOpen(false);
                          localStorage.setItem('portal_filter_course', currentCourseId);
                          sessionStorage.setItem('portal_filter_course', currentCourseId);
                          sessionStorage.setItem('lms_portal_tab', 'board');
                          onBack();
                        }}
                        className="w-full text-left px-4 py-2.5 text-[13px] font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0ea5e9] flex items-center gap-2.5 transition-colors"
                      >
                        <span>📋</span> Bảng công việc
                      </button>
                      <button
                        onClick={() => {
                          setIsMobileMenuOpen(false);
                          sessionStorage.setItem('portal_selected_course_id', currentCourseId);
                          sessionStorage.setItem('portal_active_view', 'course');
                          sessionStorage.setItem('portal_current_folder_id', '');
                          sessionStorage.setItem('lms_portal_tab', 'library');
                          onBack();
                        }}
                        className="w-full text-left px-4 py-2.5 text-[13px] font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0ea5e9] flex items-center gap-2.5 transition-colors"
                      >
                        <span>📚</span> Kho đề bài tập
                      </button>
                      <div className="h-px bg-slate-100 my-1" />
                      <button
                        onClick={() => {
                          setIsMobileMenuOpen(false);
                          setIsLectureThemeModalOpen(true);
                        }}
                        className="w-full text-left px-4 py-2.5 text-[13px] font-semibold text-slate-700 hover:bg-purple-50 hover:text-purple-600 flex items-center gap-2.5 transition-colors"
                      >
                        <span>🎨</span> Đổi màu nền bài giảng
                      </button>
                    </div>
                  </>
                )}
              </div>

              {/* 🖥️ CÁC NÚT ĐIỀU HƯỚNG TRÊN MÀN HÌNH LỚN (>= sm) */}
              <button
                  onClick={() => {
                      localStorage.setItem('portal_filter_course', currentCourseId);
                      sessionStorage.setItem('portal_filter_course', currentCourseId);
                      sessionStorage.setItem('lms_portal_tab', 'calendar');
                      onBack();
                  }}
                  className="hidden sm:flex items-center gap-2 px-3 py-2 md:px-4 md:h-10 rounded-full text-[13px] md:text-[14px] font-semibold transition-all bg-white/15 hover:bg-white/25 text-white border border-white/20 shadow-sm hover:shadow-md hover:-translate-y-0.5"
                  title="Đi đến Lịch báo bài của khóa học"
              >
                 <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5" /></svg>
                 <span className="hidden sm:inline">Lịch báo bài</span>
              </button>
              <button
                  onClick={() => {
                      localStorage.setItem('portal_filter_course', currentCourseId);
                      sessionStorage.setItem('portal_filter_course', currentCourseId);
                      sessionStorage.setItem('lms_portal_tab', 'board');
                      onBack();
                  }}
                  className="hidden sm:flex items-center gap-2 px-3 py-2 md:px-4 md:h-10 rounded-full text-[13px] md:text-[14px] font-semibold transition-all bg-white/15 hover:bg-white/25 text-white border border-white/20 shadow-sm hover:shadow-md hover:-translate-y-0.5"
                  title="Đi đến Bảng công việc của khóa học"
              >
                 <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25zM6.75 12h.008v.008H6.75V12zm0 3h.008v.008H6.75V15zm0 3h.008v.008H6.75V18z" /></svg>
                 <span className="hidden sm:inline">Bảng công việc</span>
              </button>
              <button
                  onClick={() => {
                      sessionStorage.setItem('portal_selected_course_id', currentCourseId);
                      sessionStorage.setItem('portal_active_view', 'course');
                      sessionStorage.setItem('portal_current_folder_id', '');
                      sessionStorage.setItem('lms_portal_tab', 'library');
                      onBack();
                  }}
                  className="hidden sm:flex items-center gap-2 px-3 py-2 md:px-4 md:h-10 rounded-full text-[13px] md:text-[14px] font-semibold transition-all bg-white/15 hover:bg-white/25 text-white border border-white/20 shadow-sm hover:shadow-md hover:-translate-y-0.5"
                  title="Đi đến kho đề của khóa học"
              >
                 <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" /></svg>
                 <span className="hidden sm:inline">Kho đề</span>
              </button>
              {!(course?.title || '').toLowerCase().includes('ielts') && (
                  <button 
                      onClick={() => { 
                          if(onOpenAI) {
                              onOpenAI('tutor'); 
                          }
                      }} 
                      className="flex items-center gap-1.5 sm:gap-2 px-2.5 sm:px-3 py-1.5 sm:py-2 md:px-4 md:h-10 rounded-full text-xs sm:text-[13px] md:text-[14px] font-semibold transition-all bg-gradient-to-r from-amber-400 to-orange-400 hover:from-amber-500 hover:to-orange-500 text-amber-950 shadow-md border border-amber-300/50 hover:shadow-lg hover:-translate-y-0.5"
                  >
                     <span className="animate-bounce">✨</span> <span className="hidden xs:inline">Hỏi AI Tutor</span>
                  </button>
              )}
             {(course?.title || '').toLowerCase().includes('ielts') && (
                 <>
                 <button 
                     onClick={() => onOpenAI?.('ielts', activeLecture?.title, undefined, 'speaking')} 
                     className="w-9 h-9 md:w-10 md:h-10 rounded-full flex items-center justify-center transition-all bg-gradient-to-br from-pink-400 to-rose-500 text-white shadow-md border border-white/20 hover:shadow-lg hover:scale-105 shrink-0"
                     title="Tutor Speaking"
                 >
                     <span className="text-[10px] md:text-[11px] font-bold leading-tight">Spk</span>
                 </button>
                 <button 
                     onClick={() => onOpenAI?.('ielts', activeLecture?.title, undefined, 'task1')} 
                     className="w-9 h-9 md:w-10 md:h-10 rounded-full flex items-center justify-center transition-all bg-gradient-to-br from-emerald-400 to-teal-500 text-white shadow-md border border-white/20 hover:shadow-lg hover:scale-105 shrink-0"
                     title="Tutor Writing Task 1"
                 >
                     <span className="text-[10px] md:text-[11px] font-bold leading-tight">WT1</span>
                 </button>
                 <button 
                     onClick={() => onOpenAI?.('ielts', activeLecture?.title, undefined, 'task2')} 
                     className="w-9 h-9 md:w-10 md:h-10 rounded-full flex items-center justify-center transition-all bg-gradient-to-br from-violet-400 to-purple-500 text-white shadow-md border border-white/20 hover:shadow-lg hover:scale-105 shrink-0"
                     title="Tutor Writing Task 2"
                 >
                     <span className="text-[10px] md:text-[11px] font-bold leading-tight">WT2</span>
                 </button>
                 </>
             )}
             <button 
                 onClick={toggleFullScreen} 
                 className="hidden md:flex w-10 h-10 rounded-full items-center justify-center bg-white/10 hover:bg-white/20 text-white transition-all"
             >
                {isFullscreen ? (
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg>
                ) : (
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>
                )}
             </button>
          </div>
      </header>

      <div className="flex flex-1 overflow-hidden relative w-full">
         
         {isSidebarOpen && (
             <div 
                 className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-40 md:hidden transition-opacity" 
                 onClick={() => setIsSidebarOpen(false)} 
             />
         )}

         <aside className={`fixed md:relative inset-y-0 left-0 z-50 md:z-20 h-[100dvh] md:h-full bg-white border-r border-slate-200 flex flex-col shrink-0 transition-transform duration-300 ease-in-out shadow-[4px_0_24px_rgba(0,0,0,0.05)] md:shadow-none
            ${isSidebarOpen && !isTeacherBoardOpen ? 'translate-x-0 w-[300px] md:w-[340px]' : '-translate-x-full w-[300px] md:w-0 md:opacity-0 md:border-r-0 md:translate-x-0'}`}>
           
           <div className="p-5 border-b border-slate-100 shrink-0 bg-slate-50/50">
              <div className="flex items-center justify-between mb-3">
                  <h3 className="font-bold text-slate-800 text-[16px]">Nội dung khóa học</h3>
                  <button 
                      onClick={() => setIsSidebarOpen(false)} 
                      className="md:hidden w-8 h-8 rounded-full bg-slate-200/60 hover:bg-slate-200 flex items-center justify-center font-bold text-slate-500 hover:text-slate-700 text-sm transition-colors"
                      title="Đóng danh sách"
                  >
                      ✕
                  </button>
              </div>
              <div className="flex flex-col gap-1.5">
                  <div className="flex justify-between text-[12px] font-medium text-slate-500">
                      <span>Tiến độ</span>
                      <span className="text-[#0ea5e9]">{completedLectures.size} / {lectures.length} bài</span>
                  </div>
                  <div className="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden">
                      <div className="h-full bg-[#0ea5e9] rounded-full transition-all duration-500" style={{ width: `${courseProgress}%` }}></div>
                  </div>
              </div>
           </div>
           
           
           <div className="flex-1 overflow-y-auto custom-scrollbar bg-white pb-24" style={{ WebkitOverflowScrolling: 'touch' }}>
             {modules.length === 0 ? (
                <div className="p-8 text-center text-slate-400 text-sm">Chưa có nội dung.</div>
             ) : (
                modules.map((mod, index) => {
                  const moduleLectures = lectures.filter(l => l.module_id === mod.id);
                  const isExpanded = expandedModules.includes(mod.id);
                  const theme = parseModuleTheme(mod.title, mod);
                  
                  return (
                    <div key={mod.id} id={`module-container-${mod.id}`} className="border-b border-slate-100 last:border-0">
                      <button 
                          onClick={(e) => { 
                              e.preventDefault(); 
                              toggleModule(mod.id); 
                              if (!expandedModules.includes(mod.id)) {
                                  setTimeout(() => {
                                      const el = document.getElementById(`module-container-${mod.id}`);
                                      if (el) {
                                          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                                      }
                                  }, 310);
                              }
                          }} 
                          style={theme.hasColor ? {
                              backgroundColor: theme.bg,
                              borderColor: theme.border,
                          } : {}}
                          className={`w-full text-left px-5 py-3.5 transition-all flex justify-between items-center ${
                              theme.hasColor 
                                ? 'hover:brightness-95' 
                                : isExpanded ? 'bg-slate-50/70' : 'hover:bg-slate-50'
                          }`}
                      >
                        <div className="flex items-center gap-3 min-w-0 pr-2">
                            <span 
                                className="font-bold text-xs px-2 py-0.5 rounded-md shrink-0 shadow-sm"
                                style={theme.hasColor ? { 
                                    backgroundColor: 'rgba(255,255,255,0.7)', 
                                    color: theme.text,
                                    border: `1px solid ${theme.border}`
                                } : { 
                                    backgroundColor: '#f1f5f9',
                                    color: '#64748b' 
                                }}
                            >
                                {(index+1).toString().padStart(2, '0')}
                            </span>
                            <h4 
                                className="text-[13.5px] md:text-[14px] font-bold leading-snug truncate"
                                style={theme.hasColor ? { color: theme.text } : { color: '#1e293b' }}
                            >
                                {theme.cleanTitle}
                            </h4>
                        </div>
                        <span 
                            className={`text-[10px] transition-transform duration-200 shrink-0 ml-2 ${isExpanded ? 'rotate-180' : ''}`}
                            style={theme.hasColor ? { color: theme.text, opacity: 0.8 } : { color: '#94a3b8' }}
                        >
                            ▼
                        </span>
                      </button>
                      
                      <div className={`overflow-hidden transition-all duration-300 ease-in-out ${isExpanded ? 'max-h-[2000px] opacity-100' : 'max-h-0 opacity-0'}`}>
                        <div 
                            className="py-2 bg-white flex flex-col gap-0.5 px-2"
                            style={theme.hasColor ? { borderLeft: `3px solid ${theme.border}`, marginLeft: '8px', marginRight: '4px' } : {}}
                        >
                          {moduleLectures.map((lec) => {
                             const isActive = activeLectureId === lec.id;
                             const totalTasks = Array.isArray(lec.task_list) ? lec.task_list.length : 0;
                             const completedCount = allLectureProgress[lec.id]?.length || 0;
                             const isLecCompleted = completedLectures.has(lec.id);

                             return (
                               <button 
                                   key={lec.id} 
                                   onClick={() => handleSelectLecture(lec.id)} 
                                   className={`w-full text-left px-3 py-2.5 rounded-lg text-[13px] transition-all flex items-start gap-3 relative group ${isActive ? 'bg-[#0ea5e9]/10 text-[#0ea5e9]' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'}`}
                               >
                                 <div className="mt-0.5 shrink-0">
                                     {isLecCompleted ? (
                                        <div className="w-5 h-5 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center">
                                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-3.5 h-3.5"><path fillRule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clipRule="evenodd" /></svg>
                                        </div>
                                     ) : isActive ? (
                                        <div className="w-5 h-5 rounded-full border-2 border-[#0ea5e9] text-[#0ea5e9] flex items-center justify-center">
                                            <div className="w-2 h-2 rounded-full bg-[#0ea5e9]"></div>
                                        </div>
                                     ) : (
                                        <div className="w-5 h-5 rounded-full border-2 border-slate-300 group-hover:border-[#0ea5e9] transition-colors"></div>
                                     )}
                                 </div>
                                 <div className="flex-1 min-w-0 flex flex-col gap-1">
                                    <span className={`leading-snug ${isActive ? 'font-semibold' : 'font-medium'}`}>
                                        {lec.title}
                                    </span>
                                    <div className="flex items-center gap-1.5 flex-wrap">
                                      {(LECTURE_VIDEO_MAP[lec.id] || (lec as any).video_url) && (
                                        <span 
                                          className="text-[10px] px-1.5 py-0.5 rounded font-medium bg-red-50 text-red-600 border border-red-100 flex items-center gap-1 shrink-0" 
                                          title="Có video bài giảng"
                                        >
                                          <svg className="w-2.5 h-2.5 fill-current" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                                          {Array.isArray(LECTURE_VIDEO_MAP[lec.id]) ? `Video (${(LECTURE_VIDEO_MAP[lec.id] as any[]).length})` : 'Video'}
                                        </span>
                                      )}
                                      {lec.title.toLowerCase().includes('podcast') && (
                                        <span 
                                          className="text-[10px] px-1.5 py-0.5 rounded font-medium bg-emerald-50 text-emerald-700 border border-emerald-200 flex items-center gap-1 shrink-0" 
                                          title="Bài giảng Audio Podcast"
                                        >
                                          <svg className="w-2.5 h-2.5 stroke-current" fill="none" strokeWidth="2.5" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 100-6 3 3 0 000 6z" /></svg>
                                          Podcast ({COURSE_PODCAST_COUNT[currentCourseId] || 64})
                                        </span>
                                      )}
                                      {totalTasks > 0 && (
                                         <span 
                                           onClick={(e) => { e.stopPropagation(); if (isActive) { setIsTaskMenuOpen(!isTaskMenuOpen); } else { handleSelectLecture(lec.id); setTimeout(() => setIsTaskMenuOpen(true), 300); } }}
                                           className={`text-[10px] w-fit px-1.5 py-0.5 rounded font-medium cursor-pointer transition-all ${isLecCompleted ? 'bg-emerald-50 text-emerald-600 hover:bg-emerald-100' : isActive ? 'bg-[#0ea5e9]/10 text-[#0ea5e9] hover:bg-[#0ea5e9]/20' : 'bg-slate-100 text-slate-500 hover:bg-slate-200'}`}
                                           title="Bấm để xem nhiệm vụ bài học"
                                         >
                                             🎯 {completedCount}/{totalTasks} bài tập
                                         </span>
                                      )}
                                    </div>
                                 </div>
                               </button>
                             )
                          })}
                        </div>
                      </div>
                    </div>
                  )
                })
             )}
           </div>
         </aside>

         <main 
             className={`flex-1 overflow-y-auto custom-scrollbar relative lecture-content transition-all duration-500 ease-in-out`} 
             style={{
                 ...(isTeacherBoardOpen ? { paddingRight: `${boardWidthVw}vw` } : {}),
                 backgroundColor: lectureTheme.boardBg
             }}
             ref={containerRef} 
             onMouseUp={handleTextSelection}
             onScroll={(e) => {
                 const el = e.currentTarget;
                 // Kiểm tra cuộn đến gần đáy (còn 100px)
                 if (el.scrollHeight - el.scrollTop - el.clientHeight < 100) {
                     setViewedPages(prev => {
                         if (prev.has(currentPage)) return prev;
                         const next = new Set(prev);
                         next.add(currentPage);
                         return next;
                     });
                 }
             }}
         >
             <div className={`min-h-full flex flex-col items-center ${isIframeOnly ? '' : 'py-6 md:py-12 px-0 sm:px-6 lg:px-8'}`}>
                <div className={`w-full flex-none transition-all ${
                    isIframeOnly 
                    ? 'p-0 mb-0 max-w-none' 
                    : `bg-white shadow-sm border border-slate-200 rounded-none sm:rounded-2xl p-5 sm:p-8 md:p-10 mb-8 min-h-[60vh] max-w-[1050px] ${isTeacherBoardOpen ? 'max-w-none' : ''}`
                }`}>
                  {!activeLectureId ? (
                    <div className="flex flex-col items-center justify-center h-full py-20 text-slate-400">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1} stroke="currentColor" className="w-16 h-16 mb-4 opacity-50"><path strokeLinecap="round" strokeLinejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25" /></svg>
                        <span className="font-medium text-lg">Chọn bài học ở danh sách bên trái để bắt đầu</span>
                    </div>
                  ) : pages.length === 0 ? (
                    <div className="flex flex-col items-center justify-center h-full py-20 text-slate-400 text-center">
                       <span className="text-4xl mb-3 opacity-50">📖</span>
                       <span className="font-bold text-slate-600">Nội dung bài học hiện đang được cập nhật.</span>
                       <span className="text-sm mt-1">Vui lòng quay lại sau nhé!</span>
                    </div>
                  ) : !currentHtmlContent ? (
                    <div className="flex flex-col items-center justify-center h-full py-20 text-slate-400">
                       <span className="w-8 h-8 border-4 border-[#0ea5e9]/30 border-t-[#0ea5e9] rounded-full animate-spin mb-4"></span>
                       <span className="font-medium">Đang tải nội dung...</span>
                    </div>
                  ) : (
                    <div className="animate-in fade-in duration-500">
                       <h2 className="text-[26px] md:text-[36px] text-slate-900 font-extrabold mb-8 md:mb-12 pb-6 border-b border-slate-100 leading-tight tracking-tight">
                           {activeLecture?.title}
                       </h2>
                       {activeLecture?.title?.toLowerCase().includes('podcast') && totalPages > 1 && (
                         <div className="flex items-center gap-2.5 mb-8 flex-wrap">
                           <button
                             type="button"
                             onClick={() => { setCurrentPage(1); persistPage(1); }}
                             className={`inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all border ${
                               currentPage === 1 
                                 ? 'bg-emerald-600 text-white border-emerald-600 shadow-md shadow-emerald-600/20' 
                                 : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50 hover:border-slate-300'
                             }`}
                           >
                             <span>🇻🇳</span>
                             <span>Bản Tiếng Việt (Trang 1)</span>
                           </button>
                           <button
                             type="button"
                             onClick={() => { setCurrentPage(2); persistPage(2); }}
                             className={`inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all border ${
                               currentPage === 2 
                                 ? 'bg-emerald-600 text-white border-emerald-600 shadow-md shadow-emerald-600/20' 
                                 : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50 hover:border-slate-300'
                             }`}
                           >
                             <span>🇬🇧</span>
                             <span>Bản Tiếng Anh (Trang 2)</span>
                           </button>
                         </div>
                       )}
                       {activeLectureVideoId && currentPage === 1 && (
                         <div className="mb-8 rounded-2xl overflow-hidden shadow-md border border-slate-200 bg-slate-900">
                           <div className="flex items-center justify-between px-4 py-3 bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border-b border-slate-700/60">
                             <div className="flex items-center gap-2.5 min-w-0">
                               <span className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-red-600 text-white text-xs font-bold shadow-sm tracking-wide shrink-0">
                                 <svg className="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
                                   <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                                 </svg>
                                 Video Bài Giảng
                               </span>
                               <span className="text-xs text-slate-300 font-medium hidden sm:inline truncate">
                                 {activeLectureVideoSubTitle}
                               </span>
                             </div>
                             <button 
                               onClick={() => setIsVideoCollapsed(!isVideoCollapsed)}
                               className="text-xs font-semibold text-slate-300 hover:text-white flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 transition-colors border border-slate-700/50 shrink-0 ml-2"
                             >
                               <span>{isVideoCollapsed ? 'Mở video' : 'Thu gọn'}</span>
                               <span className="text-[10px]">{isVideoCollapsed ? '▼' : '▲'}</span>
                             </button>
                           </div>
                           {currentVideoList.length > 1 && (
                             <div className="flex items-center gap-2 px-4 py-2 bg-slate-800/95 border-b border-slate-700/60 overflow-x-auto custom-scrollbar">
                               <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider shrink-0 mr-1">Các phần:</span>
                               {currentVideoList.map((item, idx) => (
                                 <button
                                   key={idx}
                                   onClick={() => setSelectedVideoSubIndex(idx)}
                                   className={`px-3 py-1 rounded-lg text-xs font-bold transition-all shrink-0 flex items-center gap-1.5 ${
                                     selectedVideoSubIndex === idx
                                       ? 'bg-red-600 text-white shadow-sm'
                                       : 'bg-slate-700/60 text-slate-300 hover:bg-slate-700 hover:text-white'
                                   }`}
                                 >
                                   <span>{item.title}</span>
                                 </button>
                               ))}
                             </div>
                           )}
                           {!isVideoCollapsed && (
                             <div className="w-full aspect-video bg-black relative">
                               <iframe
                                 key={activeLectureVideoId}
                                 src={`https://www.youtube.com/embed/${activeLectureVideoId}?rel=0`}
                                 title={activeLectureVideoSubTitle || "Video bài giảng"}
                                 className="w-full h-full border-0"
                                 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                 allowFullScreen
                               />
                             </div>
                           )}
                         </div>
                       )}
                       {activeLectureId && currentPage === 1 && LECTURE_MANIFEST_MAP[activeLectureId] && (
                         <InteractiveLecturePlayer 
                           key={activeLectureId}
                           manifestUrl={LECTURE_MANIFEST_MAP[activeLectureId]} 
                         />
                       )}
                       <StaticLectureContent 
                           key={`${activeLectureId}_page_${currentPage}`}
                           html={currentHtmlContent} 
                           isIframeOnly={isIframeOnly}
                           onOpenPopup={setPopupUrl} 
                           onOpenDict={triggerDictionary} 
                           onCloseDict={() => setDictPopup(null)} 
                           onSwitchPage={(page: number) => { setCurrentPage(page); persistPage(page); }}
                       />
                    </div>
                  )}
               </div>
               
                {activeLectureId && (
                    <div className={`max-w-[1050px] w-full flex justify-between items-center px-2 sm:px-0 pb-20 sm:pb-16 transition-all ${isTeacherBoardOpen ? 'max-w-none flex-col gap-6 md:flex-row' : ''}`}>
                       <button 
                           onClick={handlePrevPage} 
                           disabled={currentPage === 1 && lectures.findIndex(l => l.id === activeLectureId) === 0} 
                           className="flex items-center gap-1.5 sm:gap-2 text-slate-500 font-semibold text-xs sm:text-[14px] hover:text-[#0ea5e9] hover:bg-white disabled:opacity-30 transition-all bg-transparent px-3 sm:px-5 py-2.5 sm:py-3 rounded-xl disabled:hover:bg-transparent shrink-0"
                       >
                          <span>←</span> <span className="hidden xs:inline">Bài trước</span><span className="xs:hidden">Trước</span>
                       </button>
                       
                       {totalPages > 1 && (
                          <div className="flex gap-1.5 sm:gap-2 bg-white px-2 py-1.5 sm:py-2 rounded-xl shadow-sm border border-slate-200 overflow-x-auto max-w-[140px] xs:max-w-[200px] sm:max-w-none custom-scrollbar shrink">
                              {Array.from({ length: totalPages }).map((_, i) => (
                                  <button 
                                      key={i+1} 
                                      onClick={() => { setCurrentPage(i+1); persistPage(i+1); }} 
                                      className={`w-8 h-8 sm:w-10 sm:h-10 shrink-0 rounded-lg flex items-center justify-center text-xs sm:text-[14px] font-bold transition-all ${currentPage === i+1 ? 'bg-[#0ea5e9] text-white shadow-md' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'}`}
                                  >
                                      {i+1}
                                  </button>
                            ))}
                          </div>
                       )}

                       <button 
                           onClick={handleNextPage} 
                           disabled={isLastLectureAndPage} 
                           className="flex items-center gap-1.5 sm:gap-2 text-white font-semibold text-xs sm:text-[14px] transition-all bg-[#0ea5e9] hover:bg-[#0284c7] disabled:bg-slate-300 disabled:text-slate-500 disabled:cursor-not-allowed shadow-md shadow-blue-500/20 px-3.5 sm:px-6 py-2.5 sm:py-3 rounded-xl shrink-0"
                       >
                          <span>{currentPage < pages.length ? 'Trang sau' : 'Bài tiếp'}</span> <span>→</span>
                       </button>
                   </div>
                )}
             </div>
         </main>
      </div>

      {dictPopup && dictPopup.show && (
         <div id="dict-popup" className="fixed bg-white rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.15)] ring-1 ring-slate-900/5 w-[90vw] max-w-[340px] flex flex-col overflow-hidden animate-in fade-in zoom-in-95 duration-200"
           style={{ 
             zIndex: 99999, 
             left: Math.max(10, Math.min(dictPopup.x - 170, window.innerWidth - 350)), 
             ...(window.innerHeight - dictPopup.y < 300 ? { bottom: window.innerHeight - dictPopup.rectTop + 15 } : { top: dictPopup.y + 15 }), 
             maxHeight: '400px' 
           }}>
            
            <div className="bg-slate-50/80 backdrop-blur border-b border-slate-100 py-2.5 px-5 flex items-center justify-between shrink-0">
               <div className="flex items-center">
                   <img src="/logo-shield.png" alt="Logo" className="h-4 w-auto object-contain mr-2 opacity-80" />
                   <span className="font-bold text-[11px] text-slate-500 tracking-widest uppercase">Từ điển AI</span>
               </div>
               <button onClick={() => setDictPopup(null)} className="text-slate-400 hover:text-slate-700">✕</button>
            </div>

            <div className="bg-white border-b border-slate-100 p-5 shrink-0 relative">
               <h4 className="text-[20px] font-black text-slate-900 pr-10 leading-tight mb-1">
                   {dictPopup.word}
               </h4>
               {dictPopup.data?.phonetics && (
                   <span className="text-[14px] text-emerald-600 font-mono bg-emerald-50 px-2 py-0.5 rounded">
                       {dictPopup.data.phonetics}
                   </span>
               )}
               {dictPopup.data?.audio && (
                   <button 
                       onClick={() => {
                           if(dictPopup.data.audio) {
                               new Audio(dictPopup.data.audio).play();
                           }
                       }} 
                       className="absolute top-5 right-5 w-10 h-10 rounded-full bg-blue-50 text-[#0ea5e9] flex items-center justify-center hover:bg-[#0ea5e9] hover:text-white transition-colors shadow-sm"
                   >
                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path d="M13.5 4.06c0-1.336-1.616-2.005-2.56-1.06l-4.5 4.5H4.508c-1.141 0-2.318.664-2.66 1.905A9.76 9.76 0 001.5 12c0 .898.121 1.768.35 2.595.341 1.24 1.518 1.905 2.659 1.905h1.93l4.5 4.5c.945.945 2.561.276 2.561-1.06V4.06zM18.584 5.106a.75.75 0 011.06 0c3.808 3.807 3.808 9.98 0 13.788a.75.75 0 11-1.06-1.06 8.25 8.25 0 000-11.668.75.75 0 010-1.06z" /><path d="M15.932 7.757a.75.75 0 011.061 0 4.5 4.5 0 010 6.364.75.75 0 01-1.06-1.06 3 3 0 000-4.244.75.75 0 010-1.06z" /></svg>
                   </button>
               )}
            </div>
            
            <div className="p-5 bg-slate-50 overflow-y-auto custom-scrollbar flex-1 text-[15px]" style={{ WebkitOverflowScrolling: 'touch' }}>
              {dictPopup.isLoading ? (
                 <div className="flex flex-col items-center justify-center py-4 opacity-50">
                     <span className="w-6 h-6 border-2 border-[#0ea5e9] border-t-transparent rounded-full animate-spin mb-2"></span>
                     <span className="text-[13px] font-medium">Đang dịch...</span>
                 </div>
               ) : (
                 <div className="text-slate-700 leading-relaxed font-medium">
                     {dictPopup.data?.translation}
                 </div>
              )}
            </div>
          </div>
      )}

      {/* LỚP PHỦ MEDIA (PDF/YOUTUBE) VÀ ẢNH UPLOAD */}
      {(popupUrl || uploadedBoardImage) && (
        <div className="fixed inset-0 flex flex-col animate-in fade-in duration-200 pointer-events-none" style={{ zIndex: 99998 }}>
          <div 
              className="absolute inset-0 bg-slate-900/95 backdrop-blur-sm pointer-events-auto" 
              onClick={() => {
                  setPopupUrl(null);
                  setUploadedBoardImage(null);
                  window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: false }));
                  window.dispatchEvent(new CustomEvent('tony-force-close'));
              }}
          ></div>

          <div 
            className={`w-full h-full relative pointer-events-auto transition-all duration-500 ease-in-out ${isTeacherBoardOpen ? '' : 'w-full'}`}
            style={isTeacherBoardOpen ? { width: `${100 - boardWidthVw}vw` } : undefined}
          >
             
             {/* Render PDF */}
             {popupUrl && popupUrl.toLowerCase().includes('.pdf') && (
                 <PdfVisionViewer 
                    url={popupUrl} 
                    onClose={() => {
                        setPopupUrl(null);
                        window.dispatchEvent(new CustomEvent('tony-force-close'));
                    }} 
                    onCallTutor={handleCallTutor}
                 />
             )}
             
             {/* Render Youtube Video */}
             {popupUrl && !popupUrl.toLowerCase().includes('.pdf') && (
                 <>
                   <div className="absolute top-4 right-4 z-[100000]">
                       <button 
                           onClick={() => {
                               setPopupUrl(null);
                               window.dispatchEvent(new CustomEvent('tony-force-close'));
                           }} 
                           className="w-12 h-12 rounded-full bg-white/10 hover:bg-red-500 flex items-center justify-center text-white transition-colors backdrop-blur-md"
                       >
                           <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
                       </button>
                   </div>
                   <div className="absolute inset-0 flex items-center justify-center z-0">
                      <div className="w-8 h-8 border-4 border-white/20 border-t-white rounded-full animate-spin"></div>
                   </div>
                   <iframe 
                       src={getEmbedUrl(popupUrl)} 
                       className="absolute inset-0 w-full h-full border-0 z-10 shadow-2xl" 
                       allowFullScreen
                   ></iframe>
                 </>
             )}

             {/* 🚀 CLASS react-pdf__Document ĐỂ ĐÁNH LỪA BẢNG ĐEN MỞ CÙNG LÚC VỚI ẢNH ĐỀ BÀI MỚI UPLOAD */}
             {uploadedBoardImage && (
                 <div className="react-pdf__Document absolute top-0 left-0 w-full h-full flex flex-col items-center justify-center p-4 md:p-8 z-10 pointer-events-none">
                     <div className="bg-slate-800/80 p-3 rounded-2xl shadow-2xl relative max-h-[90%] max-w-full flex flex-col pointer-events-auto border border-slate-700/50 overflow-hidden">
                         <div className="flex justify-between items-center mb-3 px-2">
                             <span className="text-emerald-400 font-bold text-xs tracking-widest uppercase flex items-center gap-2">
                                 <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shadow-[0_0_8px_#34d399]"></span>
                                 ĐỀ BÀI ĐÍNH KÈM TỪ HỌC SINH
                             </span>
                             <button 
                                 onClick={() => {
                                     setUploadedBoardImage(null);
                                     window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: false }));
                                     window.dispatchEvent(new CustomEvent('tony-force-close'));
                                 }} 
                                 className="text-slate-400 hover:text-white bg-slate-700/50 hover:bg-red-500 rounded-full w-8 h-8 flex items-center justify-center transition-all"
                             >
                                 ✕
                             </button>
                         </div>
                         <img src={uploadedBoardImage} className="max-w-full max-h-full object-contain rounded-xl bg-white/5 min-h-0" />
                     </div>
                 </div>
             )}
              
           </div>
         </div>
       )}

      {/* 🎯 POPUP NHIỆM VỤ - KHI BẤM VÀO BADGE BÀI TẬP TRONG SIDEBAR */}
      {isTaskMenuOpen && safeLectureTasks.length > 0 && (
        <>
          {/* Backdrop */}
          <div 
            className="fixed inset-0 bg-black/30 backdrop-blur-[2px] z-[80] animate-in fade-in duration-200" 
            onClick={() => setIsTaskMenuOpen(false)} 
          />

          {/* Popup task list - centered */}
          <div ref={taskMenuRef} className="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[92vw] max-w-[420px] max-h-[75vh] bg-white rounded-2xl shadow-[0_20px_60px_rgba(0,0,0,0.2)] border border-slate-100 overflow-hidden z-[90] animate-in zoom-in-95 fade-in duration-200 flex flex-col">
            {/* Header */}
            {(() => {
              const displayCompletedCount = safeLectureTasks.filter((t: any) => {
                if (t.type === 'exercise') return safeCompletedTasks.includes(t.id);
                const a = currentLectureAssignments.find((assign: any) => 
                  assign.task_type === 'manual' && (
                    assign.title === t.text || 
                    assign.title === `${activeLecture?.title || ''} : ${t.text}` || 
                    assign.title === `[Bài giảng] ${t.text}`
                  )
                );
                return safeCompletedTasks.includes(t.id) || !!a?.student_completed;
              }).length;
              const isModalAllDone = safeLectureTasks.length > 0 && displayCompletedCount === safeLectureTasks.length;
              const displayPct = safeLectureTasks.length > 0 ? Math.round((displayCompletedCount / safeLectureTasks.length) * 100) : 0;

              return (
                <div className="bg-gradient-to-r from-slate-50 to-white px-5 py-4 border-b border-slate-100 shrink-0">
                   <div className="flex justify-between items-center mb-2.5">
                     <h4 className="font-bold text-slate-800 text-[15px] flex items-center gap-2">
                       <span>{isModalAllDone ? '🏆' : '🎯'}</span>
                       Nhiệm vụ bài học
                     </h4>
                     <div className="flex items-center gap-2">
                       <span className={`font-bold text-[13px] px-2.5 py-1 rounded-full ${isModalAllDone ? 'bg-emerald-100 text-emerald-700' : 'bg-[#0ea5e9]/10 text-[#0ea5e9]'}`}>
                         {displayPct}%
                       </span>
                       <button 
                         onClick={() => setIsTaskMenuOpen(false)} 
                         className="w-7 h-7 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-400 hover:text-slate-600 transition-colors text-xs"
                       >✕</button>
                     </div>
                   </div>
                   <div className="w-full h-2 bg-slate-200 rounded-full overflow-hidden">
                     <div className={`h-full rounded-full transition-all duration-500 ${isModalAllDone ? 'bg-gradient-to-r from-emerald-400 to-teal-500' : 'bg-gradient-to-r from-[#0ea5e9] to-[#38bdf8]'}`} style={{ width: `${displayPct}%` }}></div>
                   </div>
                </div>
              );
            })()}

            {/* Task list */}
            <div className="flex-1 overflow-y-auto p-3 custom-scrollbar flex flex-col gap-2">
               {safeLectureTasks.map((task: any) => {
                  const isExercise = task.type === 'exercise';
                  const assign = currentLectureAssignments.find((a: any) => 
                    a.task_type === 'manual' && (
                      a.title === task.text || 
                      a.title === `${activeLecture?.title || ''} : ${task.text}` || 
                      a.title === `[Bài giảng] ${task.text}`
                    )
                  );
                  const isTaskChecked = isExercise 
                    ? safeCompletedTasks.includes(task.id) 
                    : (safeCompletedTasks.includes(task.id) || !!assign?.student_completed);
                  
                  const testKey = task.test_id ? String(task.test_id) : null;
                  const titleKey = task.text ? task.text.trim().toLowerCase() : null;
                  const scoreInfo = isExercise ? (
                    (testKey && testScoresMap.get(testKey)) || 
                    (titleKey && testScoresMap.get(titleKey)) || 
                    (titleKey && Array.from(testScoresMap.entries()).find(([k]) => titleKey.includes(k) || k.includes(titleKey))?.[1])
                  ) : null;

                  return (
                     <div key={task.id} className={`flex items-start gap-3 p-3.5 rounded-xl transition-all border ${isTaskChecked ? 'bg-emerald-50/50 border-emerald-200 shadow-sm' : 'bg-white border-slate-200 hover:border-[#0ea5e9]/50 hover:shadow-md'}`}>
                        {!isExercise ? (
                           <button 
                               onClick={() => handleToggleTask(task.id)} 
                               className={`relative flex items-center justify-center shrink-0 w-6 h-6 mt-0.5 rounded-full border-2 transition-all cursor-pointer ${isTaskChecked ? 'bg-emerald-500 border-emerald-500 text-white shadow-xs' : 'bg-slate-50 border-slate-300 hover:border-[#0ea5e9]'}`}
                               title={isTaskChecked ? "Bấm để bỏ đánh dấu hoàn thành" : "Bấm để đánh dấu đã hoàn thành"}
                           >
                               {isTaskChecked && (
                                   <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-3.5 h-3.5"><path fillRule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clipRule="evenodd" /></svg>
                               )}
                           </button>
                        ) : (
                           <div 
                               className={`relative flex items-center justify-center shrink-0 w-6 h-6 mt-0.5 rounded-full border-2 select-none ${isTaskChecked ? 'bg-emerald-500 border-emerald-500 text-white shadow-xs' : 'bg-slate-50 border-slate-300 text-slate-400'}`}
                               title={isTaskChecked ? "Đã đạt ≥ 50%" : "Cần nộp bài đạt từ 50%"}
                           >
                               {isTaskChecked ? (
                                   <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-3.5 h-3.5"><path fillRule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clipRule="evenodd" /></svg>
                               ) : (
                                   <span className="text-[10px]">📝</span>
                               )}
                           </div>
                        )}

                        <div className="flex-1 min-w-0 flex flex-col items-start gap-1">
                           <span className={`text-[13.5px] leading-snug transition-colors ${isTaskChecked ? 'text-slate-500 line-through' : 'text-slate-800 font-medium'}`}>
                               {task.text}
                           </span>

                           {!isExercise && isTaskChecked && (
                             <div className="flex flex-wrap gap-1.5 mt-0.5">
                               {assign?.admin_approved ? (
                                 <span className="text-[10px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-bold flex items-center gap-1">
                                   <span>✅</span> Đã hoàn thành
                                 </span>
                               ) : (
                                 <span className="text-[10px] px-2 py-0.5 rounded-full bg-amber-100 text-amber-700 font-bold flex items-center gap-1">
                                   <span>⏳</span> Chờ giáo viên phê duyệt
                                 </span>
                               )}
                             </div>
                           )}

                           {isExercise && (
                              <div className="flex items-center gap-2 flex-wrap">
                                {scoreInfo ? (
                                  scoreInfo.isPassed ? (
                                    <span className="text-[11px] font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-lg flex items-center gap-1">
                                      <span>✓</span> Đã đạt: {scoreInfo.score}/{scoreInfo.total > 0 ? scoreInfo.total : 10} ({scoreInfo.percent}%)
                                    </span>
                                  ) : (
                                    <span className="text-[11px] font-bold text-rose-700 bg-rose-50 border border-rose-200 px-2.5 py-0.5 rounded-lg flex items-center gap-1">
                                      <span>⚠️</span> Chưa đạt: {scoreInfo.score}/{scoreInfo.total > 0 ? scoreInfo.total : 10} ({scoreInfo.percent}%) • Cần ≥ 50%
                                    </span>
                                  )
                                ) : (
                                  <span className="text-[10.5px] font-medium text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md">
                                    Cần nộp bài đạt từ 50% điểm
                                  </span>
                                )}
                              </div>
                           )}

                           {isExercise && (
                              <button 
                                onClick={() => handleStartTaskExercise(task)} 
                                className={`text-[12px] font-semibold px-4 py-1.5 rounded-lg transition-all cursor-pointer ${
                                  isTaskChecked 
                                    ? 'bg-slate-100 text-slate-600 hover:bg-slate-200' 
                                    : scoreInfo && !scoreInfo.isPassed 
                                      ? 'bg-amber-500 hover:bg-amber-600 text-white shadow-sm shadow-amber-500/30' 
                                      : 'bg-[#0ea5e9] text-white shadow-sm shadow-blue-500/30 hover:bg-[#0284c7] active:scale-95'
                                }`}
                              >
                                {isTaskChecked ? 'Làm lại bài' : scoreInfo && !scoreInfo.isPassed ? 'Làm lại để đạt điểm ➜' : 'Bắt đầu làm bài ➜'}
                              </button>
                           )}
                        </div>
                     </div>
                  )
               })}
            </div>
          </div>
        </>
      )}

      {activeLectureId && currentSafeTasks.length > 0 && !isSidebarOpen && !isTaskMenuOpen && !isTeacherBoardOpen && (
        <button 
          onClick={() => setIsTaskMenuOpen(true)} 
          className="md:hidden fixed bottom-5 right-4 z-30 bg-white/95 backdrop-blur-md border border-slate-200/90 shadow-2xl rounded-full px-3.5 py-2 flex items-center gap-2 text-slate-800 text-xs font-bold hover:scale-105 active:scale-95 transition-all"
        >
          <span>🎯</span>
          <span className={`px-2 py-0.5 rounded-full text-[11px] font-black ${currentLectureDoneCount === currentSafeTasks.length ? 'bg-emerald-100 text-emerald-700' : 'bg-[#0ea5e9]/10 text-[#0ea5e9]'}`}>
            {currentLectureDoneCount}/{currentSafeTasks.length} việc
          </span>
        </button>
      )}

      <BoardThemeModal
        isOpen={isLectureThemeModalOpen}
        currentTheme={lectureTheme}
        onSelectTheme={handleSelectLectureTheme}
        onApplyCustomColor={handleApplyCustomLectureColor}
        onClose={() => setIsLectureThemeModalOpen(false)}
      />
    </div>
  );
}