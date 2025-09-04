#!/usr/bin/env python3
"""
TruthRise Case Directory Creation Tool
Creates organized directory structure for case evidence collection
"""

import os
import json
import datetime
from pathlib import Path

def create_case_directory(case_id=None, user_initials="USER"):
    """
    Creates a standardized directory structure for organizing case evidence
    
    Args:
        case_id (str): Unique case identifier (defaults to timestamp-based ID)
        user_initials (str): User's initials for folder naming
    
    Returns:
        str: Path to created case directory
    """
    
    # Generate case ID if not provided
    if not case_id:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        case_id = f"CASE_{timestamp}"
    
    # Create main case directory
    main_dir = f"Case_{case_id}_{user_initials}"
    Path(main_dir).mkdir(exist_ok=True)
    
    # Define directory structure
    subdirectories = {
        "01_Communications": {
            "description": "All messages, emails, calls, and social media interactions",
            "subdirs": ["WhatsApp", "Email", "Phone_Calls", "Social_Media", "Other"]
        },
        "02_Financial_Evidence": {
            "description": "Bank statements, transaction records, crypto exchange data",
            "subdirs": ["Bank_Statements", "Crypto_Exchanges", "Transfer_Services", "Receipts"]
        },
        "03_Documents": {
            "description": "Contracts, agreements, fake IDs, official papers",
            "subdirs": ["Contracts", "Identity_Documents", "Websites", "Screenshots"]
        },
        "04_Technical_Evidence": {
            "description": "Remote access logs, software installations, system evidence",
            "subdirs": ["Remote_Access_Logs", "System_Logs", "Installed_Software", "Network_Activity"]
        },
        "05_Timeline": {
            "description": "Chronological organization of events",
            "files": ["timeline.md", "key_dates.txt", "sequence_of_events.md"]
        },
        "06_Analysis": {
            "description": "Case summary, modus operandi analysis, impact assessment",
            "files": ["case_summary.md", "modus_operandi.md", "financial_impact.md", "evidence_checklist.md"]
        }
    }
    
    # Create all subdirectories
    for main_folder, config in subdirectories.items():
        main_path = Path(main_dir) / main_folder
        main_path.mkdir(exist_ok=True)
        
        # Create README for each main folder
        readme_path = main_path / "README.md"
        with open(readme_path, 'w') as f:
            f.write(f"# {main_folder}\n\n")
            f.write(f"{config['description']}\n\n")
            
            if 'subdirs' in config:
                f.write("## Subfolders:\n")
                for subdir in config['subdirs']:
                    subdir_path = main_path / subdir
                    subdir_path.mkdir(exist_ok=True)
                    f.write(f"- `{subdir}/`\n")
            
            if 'files' in config:
                f.write("## Standard Files:\n")
                for filename in config['files']:
                    file_path = main_path / filename
                    # Create template files
                    create_template_file(file_path, filename)
                    f.write(f"- `{filename}`\n")
    
    # Create main case information file
    case_info = {
        "case_id": case_id,
        "created_date": datetime.datetime.now().isoformat(),
        "user_initials": user_initials,
        "status": "Evidence Collection",
        "last_updated": datetime.datetime.now().isoformat(),
        "evidence_count": 0,
        "priority_level": "Standard",
        "case_type": "Online Fraud/Scam"
    }
    
    with open(Path(main_dir) / "case_info.json", 'w') as f:
        json.dump(case_info, f, indent=2)
    
    # Create evidence tracking spreadsheet template
    create_evidence_log(Path(main_dir) / "evidence_log.csv")
    
    # Create file naming guide
    create_naming_guide(Path(main_dir) / "FILE_NAMING_GUIDE.txt")
    
    print(f"✅ Case directory created: {main_dir}")
    print(f"📁 Directory structure ready for evidence collection")
    
    return main_dir

def create_template_file(file_path, filename):
    """Create template content for standard files"""
    
    templates = {
        "timeline.md": """# Case Timeline

## Key Events

| Date | Time | Event | Evidence | Notes |
|------|------|-------|----------|-------|
| YYYY-MM-DD | HH:MM | First contact | | |
| YYYY-MM-DD | HH:MM | Initial payment request | | |
| YYYY-MM-DD | HH:MM | Realized it was a scam | | |

## Detailed Timeline

### [Date] - Initial Contact
- **What happened:** 
- **Evidence:** 
- **Red flags:** 

### [Date] - Trust Building Phase
- **What happened:** 
- **Evidence:** 
- **Tactics used:** 

### [Date] - Financial Request
- **What happened:** 
- **Evidence:** 
- **Pressure tactics:** 

### [Date] - Realization
- **What happened:** 
- **Evidence:** 
- **Trigger event:** 
""",

        "case_summary.md": """# Case Summary

## Victim Information
- **Case ID:** 
- **Date Range:** 
- **Total Financial Loss:** 

## Scammer Information
- **Names Used:** 
- **Phone Numbers:** 
- **Email Addresses:** 
- **Websites/Platforms:** 

## Scam Overview
**Type of Scam:** 

**Initial Contact Method:** 

**Primary Promise/Hook:** 

**Method of Payment Requested:** 

## Modus Operandi
1. **Initial Contact:** 
2. **Trust Building:** 
3. **The Hook:** 
4. **Payment Request:** 
5. **Pressure Tactics:** 
6. **Red Flags Ignored:** 

## Impact Assessment
- **Financial Loss:** 
- **Emotional Impact:** 
- **Time Investment:** 
- **Additional Risks:** 

## Evidence Summary
- **Communications:** 
- **Financial Records:** 
- **Documentation:** 
- **Technical Evidence:** 

## Recommendations
- **Immediate Actions:** 
- **Preventive Measures:** 
- **Legal Considerations:** 
""",

        "key_dates.txt": """KEY DATES FOR CASE

Format: YYYY-MM-DD - Event Description

Example:
2024-01-15 - First contact via WhatsApp
2024-01-18 - Received fake investment proposal
2024-01-22 - Made first payment of $500
2024-01-25 - Requested additional payment
2024-01-28 - Realized it was a scam
2024-01-30 - Contacted bank/authorities

Add your dates here:
""",

        "sequence_of_events.md": """# Sequence of Events

## Phase 1: Initial Contact
**Duration:** 
**Summary:** 

### Key Events:
- [ ] First contact
- [ ] Initial conversation
- [ ] Basic information exchange

## Phase 2: Trust Building
**Duration:** 
**Summary:** 

### Key Events:
- [ ] Credentials/proof provided
- [ ] Success stories shared
- [ ] Initial small requests

## Phase 3: The Setup
**Duration:** 
**Summary:** 

### Key Events:
- [ ] Opportunity presented
- [ ] Urgency created
- [ ] Specific instructions given

## Phase 4: Financial Commitment
**Duration:** 
**Summary:** 

### Key Events:
- [ ] Payment requested
- [ ] Instructions provided
- [ ] Transaction completed

## Phase 5: Escalation
**Duration:** 
**Summary:** 

### Key Events:
- [ ] Additional requests
- [ ] Pressure applied
- [ ] Excuses given

## Phase 6: Realization
**Duration:** 
**Summary:** 

### Key Events:
- [ ] Suspicious behavior noted
- [ ] Research conducted
- [ ] Scam confirmed
""",

        "modus_operandi.md": """# Modus Operandi Analysis

## Scammer Profile
- **Sophistication Level:** (Low/Medium/High)
- **Organization:** (Individual/Small Group/Large Operation)
- **Geographic Indicators:** 
- **Language/Communication Style:** 

## Tactics Used

### 1. Initial Approach
- **Platform:** 
- **Method:** 
- **Hook:** 

### 2. Trust Building
- **Credentials Provided:** 
- **Social Proof:** 
- **Time Investment:** 

### 3. Psychological Manipulation
- **Authority:** 
- **Urgency:** 
- **Scarcity:** 
- **Social Proof:** 
- **Reciprocity:** 

### 4. Technical Methods
- **Platforms Used:** 
- **Payment Methods:** 
- **Communication Security:** 
- **Remote Access:** 

### 5. Pressure Tactics
- **Time Pressure:** 
- **Financial Pressure:** 
- **Emotional Pressure:** 
- **Threat/Intimidation:** 

## Red Flags Present
- [ ] Unsolicited contact
- [ ] Too good to be true promises
- [ ] Pressure for quick decisions
- [ ] Unusual payment methods
- [ ] Poor grammar/spelling
- [ ] Reluctance to meet in person
- [ ] Requests for personal information
- [ ] Remote access requests

## Pattern Analysis
**Similar to known scams:** 
**Unique aspects:** 
**Effectiveness factors:** 

## Prevention Recommendations
Based on this analysis, future victims could be protected by:
1. 
2. 
3. 
""",

        "financial_impact.md": """# Financial Impact Assessment

## Direct Financial Losses

### Payments Made
| Date | Amount | Method | Recipient | Purpose | Recoverable? |
|------|--------|--------|-----------|---------|--------------|
| | | | | | |

**Total Direct Loss:** $

### Transaction Fees and Costs
| Description | Amount | Notes |
|-------------|--------|-------|
| Wire transfer fees | | |
| Crypto exchange fees | | |
| Currency conversion | | |
| Other fees | | |

**Total Additional Costs:** $

## Indirect Costs

### Time Investment
- **Hours spent communicating:** 
- **Hours spent on transactions:** 
- **Hours spent on recovery:** 
- **Lost work time:** 

### Opportunity Costs
- **Missed investment opportunities:** 
- **Lost interest on funds:** 
- **Credit impact:** 

### Recovery Efforts
- **Legal consultation fees:** 
- **Credit monitoring services:** 
- **Identity protection services:** 
- **New accounts/cards:** 

## Total Impact
- **Direct Financial Loss:** $
- **Additional Costs:** $
- **Estimated Recovery Costs:** $
- **Total Financial Impact:** $

## Recovery Prospects
- **Funds potentially recoverable:** 
- **Insurance coverage:** 
- **Bank dispute potential:** 
- **Law enforcement recovery:** 

## Future Financial Protection
- **Account monitoring:** 
- **Credit freezes:** 
- **Fraud alerts:** 
- **Changed passwords/PINs:** 
""",

        "evidence_checklist.md": """# Evidence Collection Checklist

## Communications Evidence
- [ ] WhatsApp conversations exported
- [ ] Email threads saved (with headers)
- [ ] Phone call logs/recordings
- [ ] Social media interactions
- [ ] SMS/text messages
- [ ] Other messaging apps

### Details:
- **Number of conversations:** 
- **Date range:** 
- **File formats:** 
- **Total size:** 

## Financial Evidence
- [ ] Bank statements (all affected accounts)
- [ ] Credit card statements
- [ ] Crypto exchange transaction history
- [ ] Wire transfer receipts
- [ ] Money transfer service records
- [ ] ATM receipts
- [ ] Payment confirmations

### Details:
- **Number of transactions:** 
- **Total amount involved:** 
- **Date range:** 
- **Institutions involved:** 

## Document Evidence
- [ ] Contracts or agreements
- [ ] Identity documents provided by scammer
- [ ] Website screenshots
- [ ] Account statements (real or fake)
- [ ] Investment proposals
- [ ] Certificates or licenses shown
- [ ] Business registration documents

### Details:
- **Number of documents:** 
- **Types of documents:** 
- **Quality of evidence:** 

## Technical Evidence
- [ ] Remote access logs
- [ ] Software installation records
- [ ] System activity logs
- [ ] Browser history
- [ ] Downloaded files
- [ ] Network activity logs
- [ ] IP address information

### Details:
- **Remote access occurred:** Yes/No
- **Software installed:** 
- **Date range of activity:** 
- **Devices affected:** 

## Verification Evidence
- [ ] Reverse image searches of photos
- [ ] Company/license verification attempts
- [ ] Website registration information
- [ ] Social media profile analysis
- [ ] Phone number verification
- [ ] Address verification

### Details:
- **Verification methods used:** 
- **Results found:** 
- **Fake elements identified:** 

## Witness Information
- [ ] Family/friends who saw communications
- [ ] Bank representatives contacted
- [ ] Others who received similar contacts
- [ ] Professional advisors consulted

### Details:
- **Number of witnesses:** 
- **Types of witness:** 
- **Statements available:** 

## Quality Assessment
**Evidence Strength:** (Strong/Moderate/Weak)
**Gaps Identified:** 
**Additional Evidence Needed:** 
**Ready for Legal Review:** Yes/No

## Chain of Custody
**Evidence Collected By:** 
**Date Collected:** 
**Storage Method:** 
**Access Log:** 
**Backup Status:** 
"""
    }
    
    content = templates.get(filename, f"# {filename}\n\nTemplate content for {filename}")
    
    with open(file_path, 'w') as f:
        f.write(content)

def create_evidence_log(file_path):
    """Create CSV template for evidence tracking"""
    
    csv_header = "Date_Collected,Evidence_Type,File_Name,Description,Source,Importance_Level,File_Size,Notes\n"
    csv_example = "2024-01-15,WhatsApp,2024-01-15_WhatsApp_Initial_Contact.txt,First conversation with scammer,WhatsApp Export,Critical,156KB,Contains first promises and hook\n"
    
    with open(file_path, 'w') as f:
        f.write(csv_header)
        f.write(csv_example)

def create_naming_guide(file_path):
    """Create file naming convention guide"""
    
    guide_content = """FILE NAMING CONVENTION GUIDE

Format: [YYYY-MM-DD]_[TYPE]_[DESCRIPTION].[extension]

TYPES:
- WhatsApp
- Email
- BankStatement
- Screenshot
- Document
- PhoneLog
- CryptoRecord
- SystemLog
- WebsiteCapture

EXAMPLES:
- 2024-01-15_WhatsApp_Initial_Contact.txt
- 2024-01-20_BankStatement_Suspicious_Transfer.pdf
- 2024-01-25_Screenshot_Fake_Website.png
- 2024-01-18_Email_Investment_Proposal.pdf
- 2024-01-22_CryptoRecord_Binance_Transfer.csv

DESCRIPTION GUIDELINES:
- Use descriptive but concise names
- Avoid spaces (use underscores)
- Include key identifying information
- Keep under 50 characters total

FILE EXTENSIONS:
- Images: .png, .jpg, .jpeg
- Documents: .pdf, .doc, .docx
- Text: .txt, .md
- Data: .csv, .xlsx
- Archives: .zip, .7z
- Audio: .mp3, .wav
- Video: .mp4, .mov

IMPORTANCE LEVELS:
- Critical: Essential for case
- High: Very important evidence
- Medium: Supporting evidence
- Low: Background information
- Supporting: Additional context
"""
    
    with open(file_path, 'w') as f:
        f.write(guide_content)

if __name__ == "__main__":
    import sys
    
    # Allow command line arguments
    case_id = sys.argv[1] if len(sys.argv) > 1 else None
    user_initials = sys.argv[2] if len(sys.argv) > 2 else "USER"
    
    # Create the case directory
    directory_path = create_case_directory(case_id, user_initials)
    
    print(f"\n📋 Case directory created successfully!")
    print(f"📁 Location: {directory_path}")
    print(f"📖 Check the README.md files in each folder for guidance")
    print(f"📊 Use evidence_log.csv to track all collected evidence")
    print(f"📝 Follow FILE_NAMING_GUIDE.txt for consistent naming")
    print(f"\n🚀 You're ready to start collecting evidence!")