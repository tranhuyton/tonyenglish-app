require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY);

const questions = [
  {
    id: "1",
    content: "<p>Which characteristic of living things requires carbon dioxide to diffuse into a leaf?</p>",
    options: ["A. excretion", "B. movement", "C. nutrition", "D. respiration"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Ở thực vật, quá trình quang hợp là phương thức dinh dưỡng (nutrition), trong đó thực vật hấp thụ khí cacbonic (CO2) từ không khí để tổng hợp chất hữu cơ."
  },
  {
    id: "2",
    content: "<p>Which set of features is characteristic only of birds?</p>",
    options: ["A. hair and wings", "B. hard-shelled eggs and feathers", "C. scales and soft-shelled eggs", "D. wings and soft-shelled eggs"],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Chim là lớp động vật duy nhất có lông vũ (feathers) và đẻ trứng có vỏ cứng (hard-shelled eggs). Lông mao (hair) là đặc trưng của thú, còn vảy (scales) và trứng vỏ mềm phổ biến ở bò sát."
  },
  {
    id: "3",
    content: "<p>Which structures are found in both plant and animal cells?</p>",
    options: ["A. cell walls and cell membranes", "B. nuclei and cell walls", "C. cytoplasm and chloroplasts", "D. cell membranes and nuclei"],
    correctAnswer: "D",
    explanation: "Đáp án đúng là D. Màng tế bào (cell membranes) và nhân (nuclei) đều có ở cả tế bào thực vật và động vật. Thành tế bào (cell walls) và lục lạp (chloroplasts) chỉ có ở tế bào thực vật."
  },
  {
    id: "4",
    content: "<p>A student made the following statements about the movement of ions by active transport.</p><br>1 It is the net movement of particles from a low concentration to a high concentration.<br>2 It is the net movement of particles from a high concentration to a low concentration.<br>3 It requires the use of energy from respiration.<br>4 It can only take place in living cells.<br><br><p>Which statements are correct?</p>",
    options: ["A. 1, 3 and 4", "B. 1 and 4 only", "C. 2 and 4", "D. 2 only"],
    correctAnswer: "A",
    explanation: "Đáp án đúng là A. Vận chuyển chủ động (active transport) đưa các chất đi ngược chiều gradient nồng độ (từ thấp đến cao), do đó cần tiêu tốn năng lượng (ATP) từ quá trình hô hấp và chỉ có thể xảy ra ở các tế bào sống."
  },
  {
    id: "5",
    content: "<p>A DNA molecule contains pairs of bases.</p><p>What is a correct combination of a pair of bases?</p>",
    options: ["A. A and G", "B. C and A", "C. G and T", "D. T and A"],
    correctAnswer: "D",
    explanation: "Đáp án đúng là D. Trong phân tử DNA, theo nguyên tắc bổ sung, Adenine (A) luôn liên kết với Thymine (T), và Cytosine (C) luôn liên kết với Guanine (G)."
  },
  {
    id: "6",
    content: "<p>What is the test for protein?</p><table><tr><th>name of the test</th><th>heat</th><th>colour change</th></tr><tr><td>A</td><td>Benedict’s</td><td>yes</td><td>blue to purple</td></tr><tr><td>B</td><td>biuret</td><td>yes</td><td>blue to red</td></tr><tr><td>C</td><td>biuret</td><td>no</td><td>blue to purple</td></tr><tr><td>D</td><td>Benedict’s</td><td>no</td><td>blue to red</td></tr></table>",
    options: ["A. Benedict’s / yes / blue to purple", "B. biuret / yes / blue to red", "C. biuret / no / blue to purple", "D. Benedict’s / no / blue to red"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Thuốc thử Biuret được dùng để nhận biết protein. Phản ứng không cần đun nóng (no heat) và dung dịch sẽ chuyển từ màu xanh lam (blue) sang màu tím (purple) nếu có sự hiện diện của protein."
  },
  {
    id: "7",
    content: "<p>The graph shows how enzyme activity is affected by temperature.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>Why is enzyme activity lower at 55 °C than it is at 40 °C?</p>",
    options: ["A. Heat has killed the enzyme.", "B. The enzyme has been used up.", "C. The reactants are moving faster.", "D. The substrate is less likely to fit into the active site."],
    correctAnswer: "D",
    explanation: "Đáp án đúng là D. Ở 55°C (vượt quá nhiệt độ tối ưu), cấu trúc protein của enzyme bị biến tính (denatured), làm thay đổi hình dạng của trung tâm hoạt động. Do đó, cơ chất khó hoặc không thể khớp vào trung tâm hoạt động nữa."
  },
  {
    id: "8",
    content: "<p>Which descriptions of adaptations for photosynthesis are correct for spongy mesophyll tissue?</p><table><tr><th></th><th>air spaces for efficient gas exchange</th><th>long, rectangular cells to absorb light</th></tr><tr><td>A</td><td>yes</td><td>yes</td></tr><tr><td>B</td><td>yes</td><td>no</td></tr><tr><td>C</td><td>no</td><td>yes</td></tr><tr><td>D</td><td>no</td><td>no</td></tr></table>",
    options: ["A. yes / yes", "B. yes / no", "C. no / yes", "D. no / no"],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Mô khuyết (spongy mesophyll) có nhiều khoảng gian bào (air spaces) giúp trao đổi khí hiệu quả. Tuy nhiên, các tế bào hình chữ nhật dài là đặc điểm của mô giậu (palisade mesophyll) nằm ở lớp trên, không phải mô khuyết."
  },
  {
    id: "9",
    content: "<p>The table shows the recommended daily allowance (RDA) of some nutrients for young children.</p><p>The table also shows the masses of these nutrients eaten by a child in one day.</p><table><tr><th></th><th>mass of vitamin C / mg</th><th>mass of vitamin D / µg</th><th>mass of iron / mg</th><th>mass of calcium / mg</th></tr><tr><td>RDA</td><td>50</td><td>10</td><td>11</td><td>260</td></tr><tr><td>mass eaten in one day</td><td>54</td><td>5</td><td>11</td><td>150</td></tr></table><p>Which conditions will the child be at risk of developing if they consume the same diet for a long period of time?</p><br>1 anaemia (not having enough red blood cells)<br>2 rickets<br>3 scurvy",
    options: ["A. 1, 2 and 3", "B. 1 and 2 only", "C. 1 and 3 only", "D. 2 only"],
    correctAnswer: "D",
    explanation: "Đáp án đúng là D. Đứa trẻ ăn đủ lượng Vitamin C (54mg) và Sắt (11mg), nhưng bị thiếu hụt Vitamin D (chỉ 5µg so với 10µg) và Canxi. Việc thiếu Vitamin D và Canxi lâu ngày sẽ dẫn đến bệnh còi xương (rickets)."
  },
  {
    id: "10",
    content: "<p>Which term is used for the uptake and use of nutrients by cells?</p>",
    options: ["A. absorption", "B. assimilation", "C. egestion", "D. ingestion"],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Đồng hóa (assimilation) là quá trình các tế bào hấp thụ và sử dụng các chất dinh dưỡng để tổng hợp nên các cấu trúc sống hoặc tham gia vào quá trình trao đổi chất trong tế bào."
  },
  {
    id: "11",
    content: "<p>What is the function of trypsin in digestion?</p>",
    options: ["A. It catalyses the breakdown of maltose in the mouth.", "B. It catalyses the breakdown of maltose in the small intestine.", "C. It catalyses the breakdown of protein in the small intestine.", "D. It catalyses the breakdown of protein in the stomach."],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Trypsin là một enzyme protease do tuyến tụy tiết ra, hoạt động trong ruột non (small intestine) để phân giải protein thành các đoạn peptide ngắn hơn."
  },
  {
    id: "12",
    content: "<p>The diagram shows the structure of a villus.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>Which label shows a lacteal?</p>",
    options: ["A", "B", "C", "D"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Mạch bạch huyết (lacteal) là ống nằm ở trung tâm của lông ruột (villus), có chức năng hấp thụ các sản phẩm tiêu hóa của lipid (acid béo và glycerol)."
  },
  {
    id: "13",
    content: "<p>Which graph shows the effect of humidity in the air on the rate of transpiration in a plant?</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p>",
    options: ["A", "B", "C", "D"],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Độ ẩm (humidity) không khí càng cao thì sự chênh lệch nồng độ hơi nước giữa không gian bên trong lá và môi trường bên ngoài càng thấp. Điều này làm giảm tốc độ khuếch tán của hơi nước, kéo theo sự giảm tốc độ thoát hơi nước (đồ thị đường đi xuống)."
  },
  {
    id: "14",
    content: "<p>In some countries, spring is the time of year when daffodil plants have green leaves and produce flowers.</p><p>Which parts of the daffodil plants act as sources and sinks in spring?</p><table><tr><th></th><th>flowers</th><th>leaves</th></tr><tr><td>A</td><td>sink</td><td>sink</td></tr><tr><td>B</td><td>source</td><td>source</td></tr><tr><td>C</td><td>sink</td><td>source</td></tr><tr><td>D</td><td>source</td><td>sink</td></tr></table>",
    options: ["A. sink / sink", "B. source / source", "C. sink / source", "D. source / sink"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Vào mùa xuân, lá cây có màu xanh quang hợp mạnh để tạo chất hữu cơ, đóng vai trò là nguồn (source). Hoa đang trong quá trình phát triển cần tiêu thụ nhiều dưỡng chất, nên đóng vai trò là nơi tiêu thụ (sink)."
  },
  {
    id: "15",
    content: "<p>In a fish, what is the sequence of structures that blood passes through after it leaves the heart?</p>",
    options: ["A. gills &rarr; muscles &rarr; heart", "B. gills &rarr; heart &rarr; muscles &rarr; heart", "C. muscles &rarr; gills &rarr; heart", "D. muscles &rarr; heart"],
    correctAnswer: "A",
    explanation: "Đáp án đúng là A. Cá có hệ tuần hoàn đơn. Máu nghèo oxy từ tim được bơm lên mang (gills) để trao đổi khí, sau đó máu giàu oxy tiếp tục chảy thẳng đến các mao mạch ở cơ (muscles) và cơ quan, rồi mới quay trở về tim."
  },
  {
    id: "16",
    content: "<p>The diagram shows what happens in the body during active immunity.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>Which structures or cells represent W, X, Y and Z?</p>",
    options: ["A. W=antibodies, X=antigens, Y=memory cells, Z=phagocytes", "B. W=antibodies, X=antigens, Y=phagocytes, Z=memory cells", "C. W=antigens, X=antibodies, Y=memory cells, Z=phagocytes", "D. W=antigens, X=phagocytes, Y=antibodies, Z=memory cells"],
    correctAnswer: "D",
    explanation: "Đáp án đúng là D. Trong miễn dịch chủ động, kháng nguyên (antigens - W) bị nhận diện. Tế bào thực bào (phagocytes - X) trực tiếp tiêu diệt mầm bệnh. Kháng thể (antibodies - Y) được tiết ra để đánh dấu mầm bệnh. Các tế bào nhớ (memory cells - Z) được tạo ra giúp duy trì khả năng miễn dịch lâu dài."
  },
  {
    id: "17",
    content: "<p>Cholera is a disease caused by a bacterium called Vibrio cholerae which produces a toxin in the infected person’s gut.</p><p>What is the effect of this toxin?</p>",
    options: ["A. The toxin causes loss of water from the gut into the blood.", "B. The toxin causes loss of water from the gall bladder into the blood.", "C. The toxin causes water to enter the gut from the blood.", "D. The toxin causes water to enter the gall bladder from the blood."],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Độc tố của vi khuẩn tả kích thích các tế bào biểu mô ruột tiết các ion chloride vào lòng ruột. Điều này làm giảm thế nước trong ruột, kéo theo sự di chuyển của nước từ máu vào lòng ruột thông qua quá trình thẩm thấu, dẫn đến tiêu chảy nghiêm trọng."
  },
  {
    id: "18",
    content: "<p>The graph shows how the volume of air in lungs changes when a person is breathing at rest.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>Which processes are occurring to change the volume at the point marked X?</p>",
    options: ["A. The diaphragm is relaxing and the external intercostal muscles are relaxing.", "B. The diaphragm is contracting and the internal intercostal muscles are contracting.", "C. The diaphragm is contracting and the internal intercostal muscles are relaxing.", "D. The diaphragm is relaxing and the external intercostal muscles are contracting."],
    correctAnswer: "A",
    explanation: "Đáp án đúng là A. Tại điểm X trên đồ thị, thể tích không khí trong phổi đang bắt đầu giảm, tương ứng với quá trình thở ra. Khi thở ra bình thường ở trạng thái nghỉ, cả cơ hoành (diaphragm) và cơ liên sườn ngoài (external intercostal muscles) đều dãn ra (relax)."
  },
  {
    id: "19",
    content: "<p>The processes listed occur in living organisms.</p><br>1 cell division<br>2 diffusion<br>3 muscle contraction<br>4 osmosis<br><p>Which processes require energy from respiration?</p>",
    options: ["A. 1, 2, 3 and 4", "B. 1 and 3 only", "C. 2 and 3 only", "D. 3 and 4 only"],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Phân bào (cell division) và co cơ (muscle contraction) là các hoạt động sinh lý chủ động, cần tiêu tốn năng lượng ATP cung cấp từ hô hấp tế bào. Khuếch tán và thẩm thấu là những quá trình thụ động."
  },
  {
    id: "20",
    content: "<p>What is a role of the glomerulus?</p>",
    options: ["A. assembling amino acids into proteins", "B. filtration of water, glucose, urea and ions from the blood", "C. reabsorption of glucose, ions and water back into the blood", "D. removal of the nitrogen-containing part of amino acids to form urea"],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Cuộn mao mạch (glomerulus) trong thận đảm nhận quá trình siêu lọc (ultrafiltration). Dưới áp suất huyết áp cao, nước, glucose, urea và các ion bị đẩy từ máu ra khỏi cuộn mao mạch để vào nang Bowman."
  },
  {
    id: "21",
    content: "<p>The diagram shows a synapse.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>What are the labelled parts?</p>",
    options: ["A. P=synaptic gap, Q=neurotransmitter, R=vesicle, S=receptor", "B. P=synaptic gap, Q=receptor, R=vesicle, S=neurotransmitter", "C. P=vesicle, Q=neurotransmitter, R=synaptic gap, S=receptor", "D. P=vesicle, Q=receptor, R=synaptic gap, S=neurotransmitter"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Tại synapse, tín hiệu được truyền đi qua việc bóng chứa (vesicle - P) giải phóng chất dẫn truyền thần kinh (neurotransmitter - Q). Các phân tử này khuếch tán qua khe báp (synaptic gap - R) và gắn vào các thụ thể (receptor - S) trên màng tế bào sau synapse."
  },
  {
    id: "22",
    content: "<p>Which row shows the function of rod cells?</p><table><tr><th></th><th>night vision</th><th>colour vision</th></tr><tr><td>A</td><td>yes</td><td>yes</td></tr><tr><td>B</td><td>yes</td><td>no</td></tr><tr><td>C</td><td>no</td><td>yes</td></tr><tr><td>D</td><td>no</td><td>no</td></tr></table>",
    options: ["A. yes / yes", "B. yes / no", "C. no / yes", "D. no / no"],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Tế bào hình que (rod cells) ở võng mạc rất nhạy cảm với ánh sáng cường độ yếu, giúp chúng ta nhìn được trong môi trường tối (night vision), nhưng không phân biệt được màu sắc (colour vision)."
  },
  {
    id: "23",
    content: "<p>The diagram shows the positions of two endocrine glands in the human body.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>What is a response of the body to the hormone released from these glands?</p>",
    options: ["A. a decrease in heart rate", "B. a decrease in blood glucose concentration", "C. an increase in pupil diameter", "D. the development of secondary sexual characteristics"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Tuyến nội tiết nằm trên thận là tuyến thượng thận, tiết ra hormone adrenaline. Adrenaline gây ra các phản ứng chuẩn bị cho cơ thể đối mặt với nguy hiểm, bao gồm việc làm giãn đồng tử (increase in pupil diameter) để thu nhận nhiều ánh sáng hơn."
  },
  {
    id: "24",
    content: "<p>What is a response of the human body to overheating?</p>",
    options: ["A. vasoconstriction of arterioles", "B. vasoconstriction of veins", "C. vasodilation of arterioles", "D. vasodilation of veins"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Khi cơ thể quá nóng, các tiểu động mạch (arterioles) nằm dưới bề mặt da sẽ giãn ra (vasodilation). Quá trình này giúp đưa lượng máu lớn hơn đến sát bề mặt da, làm tăng tốc độ tỏa nhiệt ra môi trường."
  },
  {
    id: "25",
    content: "<p>What is an example of phototropism?</p>",
    options: ["A. the growth of a root in the direction of gravity", "B. the growth of a shoot towards light", "C. the release of energy from glucose using light", "D. the synthesis of glucose using light"],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Hướng sáng (phototropism) là phản ứng sinh trưởng định hướng của thực vật đối với ánh sáng. Sự sinh trưởng của chồi cây uốn cong về phía nguồn sáng là ví dụ điển hình nhất."
  },
  {
    id: "26",
    content: "<p>Which statement describes the effect of antibiotics?</p>",
    options: ["A. Antibiotics do not affect bacteria or viruses.", "B. Antibiotics kill bacteria but do not affect viruses.", "C. Antibiotics kill both bacteria and viruses.", "D. Antibiotics kill viruses but do not affect bacteria."],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Kháng sinh (antibiotics) là các chất phá vỡ hoặc cản trở các quá trình sống của vi khuẩn (như tổng hợp thành tế bào). Chúng không có tác dụng đối với virus vì virus không có cấu trúc tế bào độc lập."
  },
  {
    id: "27",
    content: "<p>The diagram shows one parent Hydra growing and releasing an offspring from the side of its body.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>Which row is correct?</p>",
    options: ["A. parent and offspring are genetically identical: yes, involves asexual reproduction: yes", "B. parent and offspring are genetically identical: yes, involves asexual reproduction: no", "C. parent and offspring are genetically identical: no, involves asexual reproduction: yes", "D. parent and offspring are genetically identical: no, involves asexual reproduction: no"],
    correctAnswer: "A",
    explanation: "Đáp án đúng là A. Sự nảy chồi ở thủy tức (Hydra) là một hình thức sinh sản vô tính (asexual reproduction). Quá trình này chỉ thông qua phân bào nguyên phân, do đó thế hệ con giống hệt cá thể mẹ về mặt di truyền."
  },
  {
    id: "28",
    content: "<p>The diagram shows the changing concentrations of some hormones involved in the menstrual cycle.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>Which letters identify two of the hormones?</p>",
    options: ["A. W is FSH and Y is oestrogen.", "B. W is LH and Y is oestrogen.", "C. W is progesterone and Y is FSH.", "D. W is progesterone and Y is LH."],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Đỉnh cao nhất của hormone W xuất hiện vào giữa chu kỳ (ngày 14) là nguyên nhân gây rụng trứng, tương ứng với hormone LH. Hormone Y có nồng độ tăng trong nửa đầu chu kỳ, chịu trách nhiệm phát triển niêm mạc tử cung, là oestrogen."
  },
  {
    id: "29",
    content: "<p>The diagram shows the chromosomes in the nucleus of a cell that divides by mitosis.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>Which diagram shows the chromosomes in the nucleus of one of the daughter cells produced?</p>",
    options: ["A", "B", "C", "D"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Quá trình nguyên phân (mitosis) luôn tạo ra các tế bào con có bộ nhiễm sắc thể giống hệt tế bào mẹ. Nếu tế bào mẹ ban đầu có 4 nhiễm sắc thể (2 cặp tương đồng lớn và nhỏ), thì tế bào con cũng giữ nguyên hình thái và số lượng y hệt như vậy."
  },
  {
    id: "30",
    content: "<p>A farmer bred together male cattle with white hair and female cattle with red hair. All the offspring produced had roan hair (a mixture of red and white).</p><p>He then repeatedly bred together two roan cattle, and the offspring were in the ratio of 1 red : 2 roan : 1 white.</p><p>What explains why the farmer obtained this ratio?</p>",
    options: ["A. The red phenotype is dominant to the white phenotype.", "B. The roan phenotype is an example of codominance.", "C. The roan phenotype is dominant to the red phenotype and the white phenotype.", "D. The white phenotype is dominant to the red phenotype."],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Kết quả lai giữa màu trắng và màu đỏ tạo ra kiểu hình trung gian dạng pha trộn (roan), và khi lai roan x roan cho tỉ lệ 1:2:1. Điều này chứng tỏ cả hai alen quy định màu đỏ và trắng đều biểu hiện đồng thời, gọi là hiện tượng đồng trội (codominance)."
  },
  {
    id: "31",
    content: "<p>Phagocytes and neurones are two types of specialised cell.</p><p>Which statements are correct?</p><br>1 Phagocytes and neurones express the same genes.<br>2 Both types of cell have the same genes.<br>3 Both types of cell only express the genes that make the proteins needed for the cell to function.",
    options: ["A. 1 and 2", "B. 1 and 3", "C. 2 and 3", "D. 2 only"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Tất cả các tế bào có nhân trong cùng một cơ thể đều mang bộ gen giống hệt nhau (mệnh đề 2 đúng). Tuy nhiên, mỗi loại tế bào chuyên hóa chỉ kích hoạt (biểu hiện) các gen cần thiết cho chức năng riêng biệt của chúng (mệnh đề 3 đúng)."
  },
  {
    id: "32",
    content: "<p>The table shows some features of leaves.</p><p>Which leaf is adapted to survive in hot, dry habitats?</p><table><tr><th></th><th>number of stomata</th><th>thickness of waxy cuticle</th><th>surface area of leaf</th></tr><tr><td>A</td><td>many</td><td>thick</td><td>small</td></tr><tr><td>B</td><td>many</td><td>thin</td><td>large</td></tr><tr><td>C</td><td>few</td><td>thick</td><td>small</td></tr><tr><td>D</td><td>few</td><td>thin</td><td>large</td></tr></table>",
    options: ["A. many / thick / small", "B. many / thin / large", "C. few / thick / small", "D. few / thin / large"],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Ở môi trường khô và nóng, thực vật phải tối đa hóa việc giữ nước. Chúng thích nghi bằng cách có ít khí khổng (few stomata) để giảm bốc hơi, lớp cutin sáp dày (thick waxy cuticle) để ngăn hơi nước thoát qua bề mặt, và diện tích lá nhỏ (small surface area)."
  },
  {
    id: "33",
    content: "<p>Which row correctly describes a type of selection?</p><table><tr><th></th><th>type of selection</th><th>humans involved</th><th>example</th></tr><tr><td>A</td><td>artificial</td><td>no</td><td>production of farmed animals that produce lots of milk</td></tr><tr><td>B</td><td>artificial</td><td>yes</td><td>production of bacteria that are resistant to antibiotics</td></tr><tr><td>C</td><td>natural</td><td>yes</td><td>production of insulin through genetic modification of bacteria</td></tr><tr><td>D</td><td>natural</td><td>no</td><td>production of wild animals with long necks to reach tree leaves as a food source</td></tr></table>",
    options: ["A", "B", "C", "D"],
    correctAnswer: "D",
    explanation: "Đáp án đúng là D. Sự tiến hóa của các loài động vật hoang dã có cổ dài (như hươu cao cổ) để thích nghi với việc ăn lá trên cao là ví dụ tiêu biểu cho chọn lọc tự nhiên (natural selection), không có sự can thiệp của con người."
  },
  {
    id: "34",
    content: "<p>Which statement about a pyramid of energy for a food chain is correct?</p>",
    options: ["A. It shows how energy is lost at each trophic level.", "B. It shows the energy stored at each trophic level.", "C. It shows the input of energy from the principal source.", "D. It shows the total energy stored within an ecosystem."],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Tháp năng lượng (pyramid of energy) được sử dụng để thể hiện tổng lượng năng lượng được tích lũy và chuyển hóa vào sinh khối ở mỗi bậc dinh dưỡng trong một hệ sinh thái."
  },
  {
    id: "35",
    content: "<p>The food web shows part of an ocean ecosystem.</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p><p>Which row shows the number of secondary consumers and the number of tertiary consumers in the food web?</p>",
    options: ["A. three / one", "B. four / one", "C. three / two", "D. four / two"],
    correctAnswer: "B",
    explanation: "Đáp án đúng là B. Dựa trên chuỗi thức ăn, sinh vật tiêu thụ bậc 1 (ăn tảo/sinh vật sản xuất) là sea urchin, clam, prawn. Các sinh vật tiêu thụ bậc 2 (ăn sinh vật bậc 1) bao gồm 4 loài. Sinh vật tiêu thụ bậc 3 (ăn bậc 2) chỉ có 1 loài."
  },
  {
    id: "36",
    content: "<p>A student investigated the effect of high temperature on the production of nitrate ions in soil.</p><p>Two samples of soil were taken. One sample was heated to 100 °C.</p><p>All the nitrate ions were completely removed from both soil samples.</p><p>Ammonium ions were then added to both soil samples.</p><p>After two weeks, both soil samples were tested for the presence of nitrate ions. The results are shown.</p><table><tr><th>soil sample</th><th>nitrate ions present or absent</th></tr><tr><td>not heated to 100 °C</td><td>present</td></tr><tr><td>heated to 100 °C</td><td>absent</td></tr></table><p>Which statement explains the results?</p>",
    options: ["A. Heating the soil broke down the nitrate ions.", "B. Heating the soil increased the activity of denitrifying bacteria.", "C. Heating the soil killed nitrifying bacteria.", "D. Heating the soil killed nitrogen-fixing bacteria."],
    correctAnswer: "C",
    explanation: "Đáp án đúng là C. Quá trình chuyển hóa ammonium thành nitrate được thực hiện bởi vi khuẩn nitrat hóa (nitrifying bacteria). Việc đun nóng đất lên 100°C đã tiêu diệt các vi khuẩn này, do đó quá trình tạo nitrate bị đình trệ ở mẫu đất bị đun nóng."
  },
  {
    id: "37",
    content: "<p>Which letter represents the lag phase in the population graph shown?</p><p class='text-amber-600 italic'>⚠️ Câu hỏi này có hình minh họa trong đề thi gốc. Xem PDF đề thi để xem hình.</p>",
    options: ["A", "B", "C", "D"],
    correctAnswer: "A",
    explanation: "Đáp án đúng là A. Trong đồ thị hình chữ S về sự tăng trưởng quần thể, giai đoạn đầu tiên khi quần thể mới bắt đầu phát triển và kích thước tăng lên rất chậm được gọi là pha tiềm phát (lag phase), tương ứng với vị trí A."
  },
  {
    id: "38",
    content: "<p>Which term describes the number of different species living in an area?</p>",
    options: ["A. biodiversity", "B. conservation", "C. ecosystem", "D. population"],
    correctAnswer: "A",
    explanation: "Đáp án đúng là A. Đa dạng sinh học (biodiversity) được định nghĩa là mức độ phong phú và số lượng các loài khác nhau cùng chung sống trong một khu vực môi trường nhất định."
  },
  {
    id: "39",
    content: "<p>Which source of pollution can cause eutrophication?</p>",
    options: ["A. carbon dioxide", "B. methane", "C. non-biodegradable plastic", "D. sewage"],
    correctAnswer: "D",
    explanation: "Đáp án đúng là D. Nước thải sinh hoạt (sewage) và phân bón thường chứa nhiều hợp chất nitrate và phosphate. Khi bị rửa trôi vào sông hồ, chúng trở thành nguồn dinh dưỡng quá mức, gây bùng phát tảo và dẫn đến hiện tượng phú dưỡng (eutrophication)."
  },
  {
    id: "40",
    content: "<p>Some of the processes involved in the production of insulin by genetic modification are listed.</p><br>1 cutting of bacterial plasmid DNA with restriction enzymes<br>2 expression in bacteria of the human gene to make insulin<br>3 insertion of recombinant plasmids into bacteria<br>4 multiplication of bacteria containing recombinant plasmids<br><p>In which order do these processes occur?</p>",
    options: ["A. 1 &rarr; 3 &rarr; 4 &rarr; 2", "B. 2 &rarr; 1 &rarr; 3 &rarr; 4", "C. 3 &rarr; 1 &rarr; 2 &rarr; 4", "D. 4 &rarr; 1 &rarr; 3 &rarr; 2"],
    correctAnswer: "A",
    explanation: "Đáp án đúng là A. Trình tự đúng của kỹ thuật gen: Đầu tiên cắt plasmid bằng enzyme giới hạn (1), sau đó đưa plasmid tái tổ hợp chứa gen insulin vào vi khuẩn (3), tiếp tục nuôi cấy nhân lên quần thể vi khuẩn (4) và cuối cùng vi khuẩn biểu hiện gen để sản xuất insulin (2)."
  }
];

const contentJson = {
  basicInfo: { title: "0610 June 2025 - Paper 21 (Multiple Choice)", timeLimit: "45", category: "test" },
  parts: [{
    content: "",
    sections: [{
      questionType: "Trắc nghiệm",
      content: "<p class='font-bold text-lg text-slate-800 mb-2'>Multiple Choice</p><p class='text-slate-600 mb-4'>Chọn đáp án đúng A, B, C hoặc D cho mỗi câu hỏi.</p>",
      questions: questions
    }]
  }]
};

async function updateDb() {
  const { data, error } = await supabase
    .from('tests')
    .update({ content_json: contentJson })
    .eq('title', '0610 June 2025 - Paper 21 (Multiple Choice)')
    .eq('course_id', 'a68bae8c-a21c-4cb2-8cd7-6097de211060');
    
  if (error) {
    console.error('Error updating:', error);
  } else {
    console.log('Update successful');
  }
}

updateDb();
