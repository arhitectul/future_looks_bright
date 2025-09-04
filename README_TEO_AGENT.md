# Teo AI Agent - TruthRise Case Intake System

## Overview

Teo is an empathetic AI assistant designed to help victims of online fraud, scams, and bad actors document their experiences and organize evidence for potential legal action. The system provides a structured, compassionate approach to case intake that follows professional standards used by law enforcement and legal teams.

## System Components

### 1. Agent Configuration (`teo-agent-config.json`)
- Complete AI agent personality and behavior configuration
- Conversational flow definitions
- Evidence collection guidelines for all major platforms and services
- Case organization structure
- Safety and security considerations

### 2. Conversational Prompts (`teo-agent-prompts.md`)
- Ready-to-use prompts for AI implementation
- Empathetic conversation starters
- Detailed questioning sequences
- Evidence collection scripts
- Support and reassurance messaging

### 3. Case Directory Creator (`case-directory-template.py`)
- Python script to automatically create organized folder structures
- Template files for case documentation
- Evidence tracking spreadsheets
- File naming convention guides

## Key Features

### 🤝 Empathetic Approach
- Non-judgmental, supportive tone
- Recognition that victims may be distressed or embarrassed
- Patient, user-paced interaction
- Regular reassurance and validation

### 🔍 Comprehensive Evidence Collection
- **Communications**: WhatsApp, email, phone calls, social media
- **Financial**: Bank statements, crypto exchanges, transfer services
- **Documents**: Contracts, fake IDs, website screenshots
- **Technical**: Remote access logs, system activity, installed software

### 📱 Multi-Platform Support
- Specific instructions for different devices (mobile, desktop, tablet)
- Platform-specific guidance (Binance, Kraken, Crypto.com, etc.)
- Cross-platform evidence correlation

### 📂 Professional Organization
- Standardized directory structure
- Consistent file naming conventions
- Evidence tracking and categorization
- Chain of custody documentation

## Usage Instructions

### For AI System Integration

1. **Load Configuration**: Import `teo-agent-config.json` into your AI system
2. **Implement Prompts**: Use `teo-agent-prompts.md` as conversation templates
3. **Directory Creation**: Integrate `case-directory-template.py` for case organization

### For Manual Case Management

1. **Run Directory Creator**:
   ```bash
   python case-directory-template.py [case_id] [user_initials]
   ```

2. **Follow Evidence Collection Guide**:
   - Use prompts from `teo-agent-prompts.md`
   - Organize files according to created directory structure
   - Track evidence using the generated CSV log

## Evidence Collection Process

### Phase 1: Initial Story Collection
- User describes experience in their own words
- Agent listens empathetically and validates feelings
- Basic timeline and key facts established

### Phase 2: Detailed Information Extraction
- Chronological reconstruction of events
- Identification of communication methods
- Financial impact assessment
- Technical compromise evaluation

### Phase 3: Evidence Gathering
- Systematic collection from all platforms
- Device-specific instructions provided
- Security and safety considerations addressed
- Proper documentation and organization

### Phase 4: Case Organization
- All evidence categorized and filed
- Timeline documented comprehensively
- Case summary and analysis prepared
- Evidence quality assessed

## Supported Platforms and Services

### Communication Platforms
- **WhatsApp**: Full conversation export with media
- **Email**: Complete thread preservation with headers
- **Phone**: Call logs, recordings, number analysis
- **Social Media**: Profile capture, message threads, media

### Financial Services
- **Banks**: Statement downloads, transaction highlighting
- **Crypto Exchanges**: Binance, Kraken, Crypto.com, others
- **Transfer Services**: Western Union, Wise, MoneyGram
- **Payment Platforms**: PayPal, Venmo, Cash App

### Technical Evidence
- **Remote Access**: TeamViewer, AnyDesk, Chrome Remote Desktop
- **System Logs**: Windows Event Viewer, Mac Console
- **Browser Data**: History, downloads, saved data
- **Network Activity**: Connection logs, IP tracking

## Directory Structure

```
Case_[CASE_ID]_[USER_INITIALS]/
├── 01_Communications/
│   ├── WhatsApp/
│   ├── Email/
│   ├── Phone_Calls/
│   ├── Social_Media/
│   └── Other/
├── 02_Financial_Evidence/
│   ├── Bank_Statements/
│   ├── Crypto_Exchanges/
│   ├── Transfer_Services/
│   └── Receipts/
├── 03_Documents/
│   ├── Contracts/
│   ├── Identity_Documents/
│   ├── Websites/
│   └── Screenshots/
├── 04_Technical_Evidence/
│   ├── Remote_Access_Logs/
│   ├── System_Logs/
│   ├── Installed_Software/
│   └── Network_Activity/
├── 05_Timeline/
│   ├── timeline.md
│   ├── key_dates.txt
│   └── sequence_of_events.md
├── 06_Analysis/
│   ├── case_summary.md
│   ├── modus_operandi.md
│   ├── financial_impact.md
│   └── evidence_checklist.md
├── case_info.json
├── evidence_log.csv
└── FILE_NAMING_GUIDE.txt
```

## Security and Privacy Considerations

### Data Protection
- Secure storage recommendations
- Backup and redundancy planning
- Access control guidance
- Chain of custody maintenance

### User Safety
- Ongoing scam protection advice
- Password and account security
- Emotional support resources
- Legal disclaimer and boundaries

### Evidence Integrity
- Original file preservation
- Metadata retention
- Timestamp verification
- Audit trail maintenance

## Integration with TruthRise Platform

This system is designed to complement the TruthRise platform's existing infrastructure:

- **TR-Intake**: Structured evidence submission
- **TR-Verify**: Multi-layer validation process
- **TR-Casebook**: Legal documentation preparation
- **TR-Solvability**: Risk assessment integration

## Legal and Compliance Notes

- Evidence collection follows law enforcement standards
- Chain of custody documentation included
- GDPR and privacy compliance considerations
- Professional legal disclaimer provided
- Multi-jurisdictional considerations addressed

## Next Steps for Implementation

1. **AI System Integration**: Configure your AI platform with Teo's personality and prompts
2. **Workflow Automation**: Integrate directory creation with case management systems
3. **Training Data**: Use collected cases to improve AI responses and evidence collection
4. **Legal Integration**: Connect with law enforcement and legal professional workflows
5. **Platform Expansion**: Extend support for new platforms and evidence types

## Support and Maintenance

- Regular updates for new scam techniques
- Platform-specific instruction updates
- Legal requirement compliance updates
- User feedback integration
- Security enhancement implementation

---

**For questions or support, contact the TruthRise team at hello@truthrise.io**

This system represents a comprehensive approach to empathetic, professional case intake that prioritizes both victim support and evidence quality for successful legal outcomes.