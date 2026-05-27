/* index.js - Premium Interactive Presentation Controller for Batch 89 */

document.addEventListener("DOMContentLoaded", () => {
  // 1. Data Model representing the 13 groups of Batch 89
  const groupData =   {
    "1": {
      "groupNum": 1,
      "members": [
        {
          "name": "王慈惠",
          "talent": "支持者",
          "role": "家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "＃資深平面設計師",
            "＃加入Rich二年多還清百萬",
            "＃從負到富的樂天派女孩"
          ]
        },
        {
          "name": "蕭惠允",
          "talent": "積蓄者",
          "role": "副家長",
          "image": "reference/avatar_female_2.png",
          "tags": [
            "#精力充沛的小電池",
            "#轉職中的工程師",
            "#樂於助人"
          ]
        }
      ]
    },
    "2": {
      "groupNum": 2,
      "members": [
        {
          "name": "許蓓瑾",
          "talent": "積蓄者",
          "role": "家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "#一對一健身教練",
            "#天賦輔導員",
            "#暖心天賦指引師"
          ]
        },
        {
          "name": "楊家瑜",
          "talent": "積蓄者",
          "role": "副家長",
          "image": "reference/avatar_female_2.png",
          "tags": [
            "#孕育中的溫火媽咪",
            "#暖心陪跑天使",
            "#NAHA高階芳療師"
          ]
        }
      ]
    },
    "3": {
      "groupNum": 3,
      "members": [
        {
          "name": "劉錦芳",
          "talent": "媒合者",
          "role": "家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "#寺廟建築採購",
            "#夢想實現家",
            "#稚齡童軍團長"
          ]
        },
        {
          "name": "楊琬琳",
          "talent": "支持者",
          "role": "副家長",
          "image": "reference/avatar_female_2.png",
          "tags": [
            "#咖啡師斜槓房仲",
            "#崇尚自由的靈魂",
            "#自帶貴人幸運星"
          ]
        }
      ]
    },
    "4": {
      "groupNum": 4,
      "members": [
        {
          "name": "楊君慧",
          "talent": "創作者",
          "role": "家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "#學苑自媒體營運總監",
            "#遠距自由工作者",
            "#操練天賦年收入成長四倍"
          ]
        },
        {
          "name": "周詩容",
          "talent": "技師",
          "role": "副家長",
          "image": "reference/avatar_female_2.png",
          "tags": [
            "＃ 11年行銷人",
            "＃可愛又奇怪的自學達人",
            "＃人類圖系統化咨詢師"
          ]
        }
      ]
    },
    "5": {
      "groupNum": 5,
      "members": [
        {
          "name": "黃雲嵩",
          "talent": "創作者",
          "role": "家長",
          "image": "reference/avatar_male_1.png",
          "tags": [
            "＃徒走戈壁沙漠的挑戰者",
            "＃在Rich兩年內賺回10倍學費",
            "＃ 財富流教練"
          ]
        },
        {
          "name": "賴貞如",
          "talent": "商人",
          "role": "副家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "#暖心陪伴數十位小孩長高的管理師",
            "#超愛抽血的醫檢師",
            "#屏東雙寶媽"
          ]
        }
      ]
    },
    "6": {
      "groupNum": 6,
      "members": [
        {
          "name": "王雅琳",
          "talent": "地主",
          "role": "家長",
          "image": "reference/avatar_female_2.png",
          "tags": [
            "#生涯發展諮詢師找到你的光",
            "#連鎖集團人資閱歷超過上千人",
            "#天賦輔導員"
          ]
        },
        {
          "name": "林苡姗",
          "talent": "明星",
          "role": "副家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "#1313小星星",
            "#氣氛製造機",
            "#人稱RICH小Ella"
          ]
        }
      ]
    },
    "7": {
      "groupNum": 7,
      "members": [
        {
          "name": "陳瑩臻",
          "talent": "支持者",
          "role": "家長",
          "image": "reference/avatar_female_2.png",
          "tags": [
            "#國營鐵飯碗轉保險經紀人",
            "#轉職一年後出國7次",
            "#貴人磁鐵"
          ]
        },
        {
          "name": "許淳皓",
          "talent": "媒合者",
          "role": "副家長",
          "image": "reference/avatar_male_2.png",
          "tags": [
            "#北漂公務員",
            "#發現自己價值的陪跑員",
            "#擅長表格的媒合者"
          ]
        }
      ]
    },
    "8": {
      "groupNum": 8,
      "members": [
        {
          "name": "林胤呈",
          "talent": "創作者",
          "role": "家長",
          "image": "reference/avatar_male_1.png",
          "tags": [
            "#國家創業比賽優勝",
            "#NASDAQ Pre-IPO輔導",
            "#中山醫創新創業教育計畫輔導講師"
          ]
        },
        {
          "name": "張庭熒",
          "talent": "積蓄者",
          "role": "副家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "#天賦指引師",
            "#暖心鋼鐵業務",
            "#專治財務焦慮優雅生活"
          ]
        }
      ]
    },
    "9": {
      "groupNum": 9,
      "members": [
        {
          "name": "楊振達",
          "talent": "技師",
          "role": "家長",
          "image": "reference/avatar_male_2.png",
          "tags": [
            "#短影音操盤手",
            "#操盤影片流量破439萬",
            "#皮膚管理師"
          ]
        },
        {
          "name": "王佩婷",
          "talent": "支持者",
          "role": "副家長",
          "image": "reference/avatar_female_2.png",
          "tags": [
            "#溫慢熱情支持者",
            "#財務規劃教練",
            "#順流人生實踐者"
          ]
        }
      ]
    },
    "10": {
      "groupNum": 10,
      "members": [
        {
          "name": "吳家怡",
          "talent": "創作者",
          "role": "家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "＃ 10年日商品牌企劃經驗",
            "＃馬拉松跑者/專業配速員",
            "＃富而喜悅/輕易豐盛 文化的傳播者"
          ]
        },
        {
          "name": "徐瑩瑩",
          "talent": "地主",
          "role": "副家長",
          "image": "reference/avatar_female_2.png",
          "tags": [
            "#德國芳療協會芳療師",
            "#身心平衡療癒老師",
            "#細胞優化代言人"
          ]
        }
      ]
    },
    "11": {
      "groupNum": 11,
      "members": [
        {
          "name": "江勁霖",
          "talent": "支持者",
          "role": "家長",
          "image": "reference/avatar_male_1.png",
          "tags": [
            "#蝦皮百萬營業額賣家",
            "#天賦指引師",
            "#生命數字研究者"
          ]
        },
        {
          "name": "楊媛媛",
          "talent": "積蓄者",
          "role": "副家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "#細水長流積蓄者",
            "#天賦諮詢師",
            "#專業財務規劃師"
          ]
        }
      ]
    },
    "12": {
      "groupNum": 12,
      "members": [
        {
          "name": "王宥鈞",
          "talent": "支持者",
          "role": "家長",
          "image": "reference/avatar_male_2.png",
          "tags": [
            "#溫暖陪伴輔導員",
            "#天賦指引師",
            "#能量學實踐者"
          ]
        },
        {
          "name": "陳彥萍",
          "talent": "積蓄者",
          "role": "副家長",
          "image": "reference/avatar_female_2.png",
          "tags": [
            "#寵物美容師",
            "#豐盛自在寶媽",
            "#章魚燒小幫手"
          ]
        }
      ]
    },
    "13": {
      "groupNum": 13,
      "members": [
        {
          "name": "謝彥馨",
          "talent": "創作者",
          "role": "家長",
          "image": "reference/avatar_female_1.png",
          "tags": [
            "#能量學高階輔導長",
            "#天賦順流指引師",
            "#雙北地區財富流教練"
          ]
        },
        {
          "name": "張家榮",
          "talent": "地主",
          "role": "副家長",
          "image": "reference/avatar_male_1.png",
          "tags": [
            "#16年機構工程師",
            "#象棋密碼卜卦師",
            "#單身二寶爸"
          ]
        }
      ]
    }
  };



  // State Management
  const groupNums = Object.keys(groupData).map(Number).sort((a, b) => a - b);
  let currentGroupIdx = 0;

  // DOM Elements
  const groupTabsContainer = document.getElementById("groupTabs");
  const presentationStage = document.getElementById("presentationStage");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const bgParticles = document.getElementById("bgParticles");

  // Helper: Wealth Dynamics Profile Energy Category (kept for compatibility)
  function getEnergyClass(talent) {
    const dynamo = ["創作者", "明星"];
    const blaze = ["支持者", "媒合者"];
    const tempo = ["商人", "積蓄者"];
    const steel = ["地主", "技師"];
    
    if (dynamo.includes(talent)) return "energy-dynamo";
    if (blaze.includes(talent)) return "energy-blaze";
    if (tempo.includes(talent)) return "energy-tempo";
    if (steel.includes(talent)) return "energy-steel";
    return "energy-blaze"; // default
  }

  // Helper: Get Talent Key Name for CSS variables and classes mapping (from 天賦四能量八屬性.png)
  function getTalentName(talent) {
    const mapping = {
      "創作者": "creator",
      "明星": "star",
      "支持者": "supporter",
      "媒合者": "dealmaker",
      "商人": "trader",
      "積蓄者": "accumulator",
      "地主": "lord",
      "技師": "mechanic"
    };
    return mapping[talent] || "supporter";
  }

  // 2. Initialize Background Particles with all 8 Talent colors for a premium vibrant environment
  function initBackgroundParticles() {
    const colors = [
      "#8bc34a", // 創作者 (Lime Green)
      "#ffb300", // 明星 (Amber Gold)
      "#ff4e20", // 支持者 (Vermilion Orange-Red)
      "#d81b60", // 媒合者 (Deep Fuchsia Pink)
      "#9c27b0", // 商人 (Purple)
      "#3f51b5", // 積蓄者 (Indigo)
      "#03a9f4", // 地主 (Sky Blue)
      "#009688"  // 技師 (Deep Teal)
    ];
    for (let i = 0; i < 15; i++) {
      const particle = document.createElement("div");
      particle.classList.add("particle");
      
      // Randomize styles
      const size = Math.random() * 20 + 8;
      particle.style.width = `${size}px`;
      particle.style.height = `${size}px`;
      particle.style.left = `${Math.random() * 100}vw`;
      particle.style.bottom = `-${size}px`;
      particle.style.background = colors[Math.floor(Math.random() * colors.length)];
      particle.style.animationDuration = `${Math.random() * 15 + 10}s`;
      particle.style.animationDelay = `${Math.random() * 10}s`;
      particle.style.opacity = `${Math.random() * 0.05 + 0.02}`;
      
      bgParticles.appendChild(particle);
    }
  }

  // 3. Render Navigation Tabs
  function renderNavTabs() {
    groupTabsContainer.innerHTML = "";
    groupNums.forEach((num, index) => {
      const button = document.createElement("button");
      button.classList.add("nav-button");
      button.setAttribute("id", `tab-group-${num}`);
      button.setAttribute("role", "tab");
      button.setAttribute("aria-selected", index === currentGroupIdx ? "true" : "false");
      button.setAttribute("aria-controls", `slide-group-${num}`);
      button.innerHTML = num;
      
      button.addEventListener("click", () => {
        switchGroup(index);
      });
      groupTabsContainer.appendChild(button);
    });
  }

  // 4. Render Presentation Slides
  function renderSlides() {
    presentationStage.innerHTML = "";
    groupNums.forEach((num, index) => {
      const group = groupData[num];
      
      const slide = document.createElement("article");
      slide.classList.add("group-slide");
      slide.setAttribute("id", `slide-group-${num}`);
      slide.setAttribute("role", "tabpanel");
      slide.setAttribute("aria-labelledby", `tab-group-${num}`);
      
      if (index === currentGroupIdx) {
        slide.classList.add("active");
      }
      
      // Vertical Group badge strip layout from template
      const groupStrip = document.createElement("div");
      groupStrip.classList.add("vertical-group-badge");
      groupStrip.innerHTML = `<span>第 ${num} 組</span>`;
      
      // Dynamic double-color gradient representing the golden partnership of the two parents
      if (group.members && group.members.length >= 2) {
        const talent1 = getTalentName(group.members[0].talent);
        const talent2 = getTalentName(group.members[1].talent);
        groupStrip.style.background = `linear-gradient(180deg, var(--color-${talent1}) 0%, var(--color-${talent2}) 100%)`;
      } else if (group.members && group.members.length === 1) {
        const talent = getTalentName(group.members[0].talent);
        groupStrip.style.background = `var(--color-${talent})`;
      }
      
      const contentGrid = document.createElement("div");
      contentGrid.classList.add("slide-content-grid");
      
      // Add profile cards
      group.members.forEach(member => {
        const talentName = getTalentName(member.talent);
        const talentClass = `talent-${talentName}`;
        
        const card = document.createElement("div");
        card.classList.add("profile-card", talentClass);
        
        // Render tags list
        const tagsHtml = member.tags
          .map(tag => `<span class="identity-tag">${tag}</span>`)
          .join("");
          
        card.innerHTML = `
          <div class="role-badge">${member.role}</div>
          <div class="profile-image-container">
            <img class="profile-image" src="${member.image}" alt="${member.name} - ${member.talent}" loading="lazy">
            <div class="image-gradient-overlay"></div>
            <div class="profile-overlay-badge-container">
              <span class="talent-badge">${member.talent}</span>
              <h2 class="profile-name">${member.name}</h2>
            </div>
          </div>
          <div class="tags-container">
            ${tagsHtml}
          </div>
        `;
        
        contentGrid.appendChild(card);
      });
      
      slide.appendChild(groupStrip);
      slide.appendChild(contentGrid);
      presentationStage.appendChild(slide);
    });
  }

  // 5. Active Switch Logic
  function switchGroup(targetIdx) {
    if (targetIdx < 0 || targetIdx >= groupNums.length) return;
    
    // Deactivate current tab & slide
    const activeTab = document.querySelector(".nav-button.active");
    if (activeTab) {
      activeTab.classList.remove("active");
      activeTab.setAttribute("aria-selected", "false");
    }
    
    const activeSlide = document.querySelector(".group-slide.active");
    if (activeSlide) {
      activeSlide.classList.remove("active");
    }
    
    // Set new index
    currentGroupIdx = targetIdx;
    const nextGroupNum = groupNums[currentGroupIdx];
    
    // Activate new tab
    const nextTab = document.getElementById(`tab-group-${nextGroupNum}`);
    if (nextTab) {
      nextTab.classList.add("active");
      nextTab.setAttribute("aria-selected", "true");
      
      // Auto-scroll nav tab bar on small screens
      nextTab.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
    }
    
    // Activate new slide
    const nextSlide = document.getElementById(`slide-group-${nextGroupNum}`);
    if (nextSlide) {
      nextSlide.classList.add("active");
    }
    
    // Enable/Disable direction buttons visually if at boundaries
    updateDirectionButtons();
  }

  function updateDirectionButtons() {
    prevBtn.disabled = currentGroupIdx === 0;
    nextBtn.disabled = currentGroupIdx === groupNums.length - 1;
    
    // Style adjustments for disabled buttons
    prevBtn.style.opacity = currentGroupIdx === 0 ? "0.35" : "1";
    prevBtn.style.cursor = currentGroupIdx === 0 ? "not-allowed" : "pointer";
    
    nextBtn.style.opacity = currentGroupIdx === groupNums.length - 1 ? "0.35" : "1";
    nextBtn.style.cursor = currentGroupIdx === groupNums.length - 1 ? "not-allowed" : "pointer";
  }

  // 6. Controllers and Listeners
  prevBtn.addEventListener("click", () => {
    if (currentGroupIdx > 0) {
      switchGroup(currentGroupIdx - 1);
    }
  });

  nextBtn.addEventListener("click", () => {
    if (currentGroupIdx < groupNums.length - 1) {
      switchGroup(currentGroupIdx + 1);
    }
  });

  // Keyboard Navigation (Arrow keys Left / Right)
  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") {
      if (currentGroupIdx > 0) {
        switchGroup(currentGroupIdx - 1);
      }
    } else if (e.key === "ArrowRight") {
      if (currentGroupIdx < groupNums.length - 1) {
        switchGroup(currentGroupIdx + 1);
      }
    }
  });

  // Drag/Swipe Support for Mobile Devices
  let touchStartX = 0;
  let touchEndX = 0;

  presentationStage.addEventListener("touchstart", (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  presentationStage.addEventListener("touchend", (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }, { passive: true });

  function handleSwipe() {
    const swipeThreshold = 50; // pixels
    if (touchStartX - touchEndX > swipeThreshold) {
      // Swipe Left -> next group
      if (currentGroupIdx < groupNums.length - 1) {
        switchGroup(currentGroupIdx + 1);
      }
    } else if (touchEndX - touchStartX > swipeThreshold) {
      // Swipe Right -> prev group
      if (currentGroupIdx > 0) {
        switchGroup(currentGroupIdx - 1);
      }
    }
  }

  // 7. Fire Layout Initialization
  initBackgroundParticles();
  renderNavTabs();
  renderSlides();
  switchGroup(0); // Set default group to Group 1
});
