const fs = require('fs');

const basicInfo = {
  skill: "Standard-Reading",
  title: "Unit 18",
  category: "exercise",
  timeLimit: 0
};

const wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit18_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit18_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">` +
[
  ['armor', '[d:rmar]', 'n.', 'Armor is metal worn by soldiers to protect the body.', 'The soldier wore armor to protect his body.'],
  ['blaze', '[bleiz]', 'v.', 'To blaze means to burn brightly or powerfully.', 'The small fire soon blazed into a large dangerous one.'],
  ['boom', '[bu:m]', 'v.', 'To boom means to make a loud, deep sound.', 'The firecrackers made a loud boom when they exploded.'],
  ['cliff', '[klif]', 'n.', 'A cliff is a high and often flat wall of rock.', 'The wolf stood at the cliff and howled.'],
  ['flame', '[fleim]', 'n.', 'A flame is part of fire.', 'The torch was filled with yellow and orange flames.'],
  ['independence', '[indipendsns]', 'n.', 'Independence is the state of being free from the control of others.', 'After leaving home, Sophia had a great feeling of independence.'],
  ['invasion', '[invei3an]', 'n.', 'An invasion is an attack by a group from another country.', 'In Korea, walls were built around cities to protect them from invasions.'],
  ['knight', '[nait]', 'n.', 'A knight is a soldier of high rank and skill who usually serves a king.', 'He was the best soldier, so the king made him a knight.'],
  ['lightning', '[laitnirj]', 'n.', 'Lightning is the bright light seen during a storm.', 'The lightning flashed above the water.'],
  ['rebel', '[rebal]', 'n.', 'A rebel is a person who fights the government in order to change it.', 'The rebel had enough of the government\'s unfair polices.'],
  ['retreat', '[ritn:t]', 'v.', 'To retreat means to run away because you have been beaten in a fight.', 'The army retreated because they were losing the battle.'],
  ['revolution', '[revalu:Jan]', 'n.', 'A revolution is a change to the political system by a group of people.', 'The revolution in Russia led to the creation of the Soviet Union.'],
  ['spear', '[spiax]', 'n.', 'A spear is a long stick with a blade on one end that is used as a weapon.', 'The soldier was holding a spear in his hand.'],
  ['steep', '[sti-.p]', 'adj.', 'If something is steep, then its slope or angle rises or falls sharply.', 'He rode his bike up the steep hill to reach the top.'],
  ['summit', '[sAmit]', 'n.', 'A summit is the highest part of a hill or mountain.', 'Snow covered the summit of the mountain even during the summer.'],
  ['thunder', '[eAnda:r]', 'n.', 'Thunder is the loud noise heard during a storm.', 'The sound of the thunder startled me.'],
  ['troops', '[tru:ps]', 'n.', 'Troops are soldiers that fight in groups in a battle.', 'The troops were all prepared to go into battle.'],
  ['warrior', '[w 5(:)ria:r]', 'n.', 'A warrior is a brave soldier or fighter.', 'The samurai were some of the most skilled warriors in the ancient world.'],
  ['withdraw', '[widdro:]', 'v.', 'To withdraw means to leave a place, usually during war.', 'After losing the battle, the enemy withdrew back to its own country.'],
  ['yield', '[jhid]', 'v.', 'To yield something means to give up control of it or to give it away.', 'He had to yield his turn because he was in checkmate.']
].map((w, i) => `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${i+1}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w[0]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w[1]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w[2]}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w[3]}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w[4]}</div></div></div>`).join('') + `</div></div></div>`;

const readingHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Knight’s Plan</h1><p style="margin-bottom: 1rem;">A town was fighting for their <b>independence</b> from another country. Several <b>rebels</b> started a <b>revolution</b>. However, they were afraid of an <b>invasion</b> from a lot of <b>troops</b>. They didn’t have enough <b>warriors</b> to stop them, so they asked a <b>knight</b> for help.</p><p style="margin-bottom: 1rem;">The knight made a plan. A tall mountain was outside the town. The road near the top was very narrow. <b>Cliffs</b> rose on both sides of it.</p><p style="margin-bottom: 1rem;">“We must trick the enemy. They have to follow us up the mountain,” the knight explained. “On the narrow path, only a few can attack us at one time.”</p><p style="margin-bottom: 1rem;">The people agreed with the knight’s plan.</p><p style="margin-bottom: 1rem;">The knight put on his <b>armor</b>, and the warriors got their <b>spears</b>. When the enemy attacked, the knight and warriors acted as if they were afraid. They quickly <b>withdrew</b> toward the mountain.</p><p style="margin-bottom: 1rem;">The enemy troops followed them up the <b>steep</b> path. Soon, the enemy became tired.</p><p style="margin-bottom: 1rem;">At the <b>summit</b>, the knight and his troops stopped. The enemy was close behind them. But now they were tired. Also, only a few could attack because the path was narrow. The knight and the warriors fought the enemy.</p><p style="margin-bottom: 1rem;">But there were too many troops.</p><p style="margin-bottom: 1rem;">The knight was afraid. If the warriors <b>yielded</b> the path to the enemy, the town would be lost.</p><p style="margin-bottom: 1rem;">A storm suddenly came over the mountain. There was strong wind and rain. <b>Thunder</b> <b>boomed</b>. <b>Lightning</b> struck some trees near the enemy. The trees <b>blazed</b>. The <b>flames</b> scared the enemy and they <b>retreated</b>. They ran down the mountain, out of the town, and never returned.</p><p style="margin-bottom: 1rem;">The knight explained, “With a little luck, a good plan beats even a big army.”</p></div>`;

const data = {
  basicInfo,
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: wordListHtml.replace(/\n/g, ''),
      sections: [
        {
          id: "u18_ex1",
          title: "Exercise 1: Circle two words that are related in each group.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "u18_ex1_1",
              content: "1.\na. withdraw\nb. armor\nc. steep\nd. retreat",
              options: ["a, b", "b, c", "c, d", "a, d"],
              correctAnswer: "a, d",
              explanation: "withdraw và retreat đều có nghĩa là rút lui (to leave a place / run away)."
            },
            {
              id: "u18_ex1_2",
              content: "2.\na. blaze\nb. flame\nc. summit\nd. independence",
              options: ["a, b", "b, c", "c, d", "a, d"],
              correctAnswer: "a, b",
              explanation: "blaze và flame đều liên quan đến ngọn lửa, cháy."
            },
            {
              id: "u18_ex1_3",
              content: "3.\na. cliff\nb. spear\nc. rebel\nd. revolution",
              options: ["a, b", "b, c", "c, d", "a, d"],
              correctAnswer: "c, d",
              explanation: "rebel (người nổi loạn) và revolution (cuộc cách mạng) đều liên quan đến sự chống đối, đổi mới."
            },
            {
              id: "u18_ex1_4",
              content: "4.\na. yield\nb. knight\nc. warrior\nd. boom",
              options: ["a, b", "b, c", "c, d", "a, d"],
              correctAnswer: "b, c",
              explanation: "knight (hiệp sĩ) và warrior (chiến binh) đều là những người lính tham gia chiến đấu."
            },
            {
              id: "u18_ex1_5",
              content: "5.\na. thunder\nb. troop\nc. lightning\nd. steep",
              options: ["a, b", "b, c", "c, d", "a, c"],
              correctAnswer: "a, c",
              explanation: "thunder (sấm) và lightning (chớp) đều là hiện tượng thời tiết trong cơn bão."
            }
          ]
        },
        {
          id: "u18_ex2_a",
          title: "Exercise 2 Part A: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "u18_ex2_a_1",
              content: "1. to give up control",
              options: ["revolution", "flame", "yield", "independence"],
              correctAnswer: "yield",
              explanation: "yield: to give up control of it or to give it away."
            },
            {
              id: "u18_ex2_a_2",
              content: "2. to make a loud, deep sound",
              options: ["boom", "spear", "cliff", "blaze"],
              correctAnswer: "boom",
              explanation: "boom: to make a loud, deep sound."
            },
            {
              id: "u18_ex2_a_3",
              content: "3. the highest point",
              options: ["knight", "retreat", "steep", "summit"],
              correctAnswer: "summit",
              explanation: "summit: the highest part of a hill or mountain."
            },
            {
              id: "u18_ex2_a_4",
              content: "4. a flat wall of rock",
              options: ["lightning", "cliff", "armor", "withdraw"],
              correctAnswer: "cliff",
              explanation: "cliff: a high and often flat wall of rock."
            },
            {
              id: "u18_ex2_a_5",
              content: "5. someone who disagrees with those in charge",
              options: ["thunder", "invasion", "rebel", "troop"],
              correctAnswer: "rebel",
              explanation: "rebel: a person who fights the government in order to change it."
            }
          ]
        },
        {
          id: "u18_ex2_b",
          title: "Exercise 2 Part B: Choose the right definition for the given word.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "u18_ex2_b_1",
              content: "1. flame",
              options: ["a small piece of fire", "the total amount", "a long stick", "a loud sound"],
              correctAnswer: "a small piece of fire",
              explanation: "flame: part of fire."
            },
            {
              id: "u18_ex2_b_2",
              content: "2. spear",
              options: ["metal worn to protect", "a brave soldier", "a sharp weapon", "to give up control"],
              correctAnswer: "a sharp weapon",
              explanation: "spear: a long stick with a blade on one end that is used as a weapon."
            },
            {
              id: "u18_ex2_b_3",
              content: "3. withdraw",
              options: ["to leave a place", "a group of soldiers", "to burn brightly", "to stab with a point"],
              correctAnswer: "to leave a place",
              explanation: "withdraw: to leave a place, usually during war."
            },
            {
              id: "u18_ex2_b_4",
              content: "4. lightning",
              options: ["a mountain", "to run away", "a high flat rock", "what you see during a storm"],
              correctAnswer: "what you see during a storm",
              explanation: "lightning: the bright light seen during a storm."
            },
            {
              id: "u18_ex2_b_5",
              content: "5. knight",
              options: ["a king", "a skilled soldier", "a strange event", "a group attack"],
              correctAnswer: "a skilled soldier",
              explanation: "knight: a soldier of high rank and skill who usually serves a king."
            }
          ]
        },
        {
          id: "u18_ex3",
          title: "Exercise 3: Write a word that is similar in meaning to the underlined part.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "u18_ex3_1",
              content: "1. Miguel did not want to [give up control of] his managerial powers.",
              options: ["yield", "withdraw", "retreat", "boom"],
              correctAnswer: "yield",
              explanation: "yield: to give up control of it."
            },
            {
              id: "u18_ex3_2",
              content: "2. With his [long pointed stick with a blade at the end], he was able to defend himself.",
              options: ["armor", "spear", "knight", "cliff"],
              correctAnswer: "spear",
              explanation: "spear: a long stick with a blade on one end."
            },
            {
              id: "u18_ex3_3",
              content: "3. During the storm we heard [loud noises].",
              options: ["lightning", "flames", "thunder", "blazes"],
              correctAnswer: "thunder",
              explanation: "thunder: the loud noise heard during a storm."
            },
            {
              id: "u18_ex3_4",
              content: "4. The army was beaten, so it [ran away] to a safe place.",
              options: ["invaded", "retreated", "yielded", "rebelled"],
              correctAnswer: "retreated",
              explanation: "retreat: to run away because you have been beaten in a fight."
            },
            {
              id: "u18_ex3_5",
              content: "5. The [soldiers who fought in groups] during the battle were exhausted after the conflict.",
              options: ["troops", "knights", "rebels", "summit"],
              correctAnswer: "troops",
              explanation: "troops: soldiers that fight in groups in a battle."
            },
            {
              id: "u18_ex3_6",
              content: "6. The [metal we wore to protect our body] was heavy and hot during the summer.",
              options: ["armor", "spear", "flame", "troops"],
              correctAnswer: "armor",
              explanation: "armor: metal worn by soldiers to protect the body."
            },
            {
              id: "u18_ex3_7",
              content: "7. We walked carefully down the [sharp angle] of the mountain.",
              options: ["steep", "summit", "cliff", "retreat"],
              correctAnswer: "steep",
              explanation: "steep: its slope or angle rises or falls sharply."
            },
            {
              id: "u18_ex3_8",
              content: "8. A feeling of [being free] came over all the people after the election of a new prime minister.",
              options: ["invasion", "revolution", "independence", "rebel"],
              correctAnswer: "independence",
              explanation: "independence: the state of being free from the control of others."
            },
            {
              id: "u18_ex3_9",
              content: "9. The soldiers managed to hold off the [attack from another group].",
              options: ["revolution", "invasion", "summit", "lightning"],
              correctAnswer: "invasion",
              explanation: "invasion: an attack by a group from another country."
            },
            {
              id: "u18_ex3_10",
              content: "10. We heard a [loud sound] when the hammer hit the brick wall.",
              options: ["blaze", "boom", "yield", "thunder"],
              correctAnswer: "boom",
              explanation: "boom: to make a loud, deep sound."
            }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: readingHtml.replace(/\n/g, ''),
      imageUrl: "/unit18_v3_story.png",
      sections: [
        {
          id: "u18_rc_a",
          title: "Reading Comprehension Part A: Mark each statement T for true or F for false.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "u18_rc_a_1",
              content: "1. The town was afraid of an invasion.",
              options: ["T", "F"],
              correctAnswer: "T",
              explanation: "Theo bài đọc: 'they were afraid of an invasion from a lot of troops.'"
            },
            {
              id: "u18_rc_a_2",
              content: "2. The town agreed with the knight’s plan.",
              options: ["T", "F"],
              correctAnswer: "T",
              explanation: "Theo bài đọc: 'The people agreed with the knight’s plan.'"
            },
            {
              id: "u18_rc_a_3",
              content: "3. The warriors wore armor, and the knight used a spear.",
              options: ["T", "F"],
              correctAnswer: "F",
              explanation: "Sự thật: The knight wore armor, and the warriors used spears."
            },
            {
              id: "u18_rc_a_4",
              content: "4. The path to the summit was steep.",
              options: ["T", "F"],
              correctAnswer: "T",
              explanation: "Theo bài đọc: 'The enemy troops followed them up the steep path.'"
            },
            {
              id: "u18_rc_a_5",
              content: "5. Some rebels started a revolution for their independence.",
              options: ["T", "F"],
              correctAnswer: "T",
              explanation: "Theo bài đọc: 'A town was fighting for their independence... Several rebels started a revolution.'"
            },
            {
              id: "u18_rc_a_6",
              content: "6. Sounds from the trees scared the enemy.",
              options: ["T", "F"],
              correctAnswer: "F",
              explanation: "Sự thật: The flames scared the enemy."
            }
          ]
        },
        {
          id: "u18_rc_b",
          title: "Reading Comprehension Part B: Answer the questions.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "u18_rc_b_1",
              content: "1. Why was the narrow path important to the knight’s plan?\na. Few soldiers could attack from it.\nb. It led to a high cliff.\nc. It was a safe place to hide.\nd. The enemy troops were afraid of it.",
              options: ["a. Few soldiers could attack from it.", "b. It led to a high cliff.", "c. It was a safe place to hide.", "d. The enemy troops were afraid of it."],
              correctAnswer: "a. Few soldiers could attack from it.",
              explanation: "Theo bài đọc: 'On the narrow path, only a few can attack us at one time.'"
            },
            {
              id: "u18_rc_b_2",
              content: "2. After they withdrew to the mountain, where did the knight and warriors stop?\na. Between two cliffs\nb. At the summit\nc. Near the bottom\nd. Out of the town",
              options: ["a. Between two cliffs", "b. At the summit", "c. Near the bottom", "d. Out of the town"],
              correctAnswer: "b. At the summit",
              explanation: "Theo bài đọc: 'At the summit, the knight and his troops stopped.'"
            },
            {
              id: "u18_rc_b_3",
              content: "3. Why didn’t the enemy think there was a trap?\na. They had more troops.\nb. They thought the soldiers were scared.\nc. They were tired.\nd. They were scared.",
              options: ["a. They had more troops.", "b. They thought the soldiers were scared.", "c. They were tired.", "d. They were scared."],
              correctAnswer: "b. They thought the soldiers were scared.",
              explanation: "Hiệp sĩ và các chiến binh vờ như đang sợ hãi và rút lui nhanh chóng, khiến quân địch tin rằng họ bỏ chạy vì sợ chứ không phải là một cái bẫy."
            },
            {
              id: "u18_rc_b_4",
              content: "4. All of the following happened after the storm came EXCEPT______.\na. thunder boomed\nb. the trees blazed\nc. the knight retreated\nd. lightning struck",
              options: ["a. thunder boomed", "b. the trees blazed", "c. the knight retreated", "d. lightning struck"],
              correctAnswer: "c. the knight retreated",
              explanation: "Người rút lui là kẻ thù (the enemy retreated), không phải hiệp sĩ."
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('unit18_raw.json', JSON.stringify(data, null, 2), 'utf-8');
console.log('Successfully wrote unit18_raw.json');
