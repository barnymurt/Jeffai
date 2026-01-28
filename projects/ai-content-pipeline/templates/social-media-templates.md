# Social Media Templates

## Template Structure
Each template contains:
- **Platform**: Target social media platform
- **Format**: Content structure and style
- **Variables**: Dynamic content insertion points
- **Constraints**: Platform-specific limitations
- **Examples**: Sample outputs

---

## Twitter Thread Template

### Structure
```
{{hook_tweet}}

{{#thread_tweets}}
{{thread_number}}/ {{content_chunk}}
{{/thread_tweets}}

{{cta_tweet}}
{{hashtags}} {{blog_link}}
```

### Variables
- `hook_tweet`: Engaging opening (max 280 chars)
- `thread_tweets`: Array of main content points
- `thread_number`: Sequential numbering (1/, 2/, etc.)
- `content_chunk`: Key insight or point (max 250 chars)
- `cta_tweet`: Call to action and closing
- `hashtags`: Relevant hashtags (2-4 max)
- `blog_link`: Original content URL

### Constraints
- Max 25 tweets per thread
- 280 characters per tweet
- Include thread indicators
- End with engagement CTA

---

## LinkedIn Post Template

### Structure
```
{{professional_hook}}

{{value_proposition}}

{{main_insights}}
{{#insights}}
→ {{insight_title}}: {{insight_description}}
{{/insights}}

{{professional_conclusion}}

{{engagement_question}}

{{blog_link}}

{{hashtags}}
```

### Variables
- `professional_hook`: Business-focused opening
- `value_proposition`: Why this matters professionally
- `insights`: Key takeaways (3-5 points)
- `professional_conclusion`: Summary and next steps
- `engagement_question`: Encourage comments
- `hashtags`: Industry-specific tags (5-10)

### Constraints
- 3000 character limit
- Professional tone required
- Include industry context
- End with engagement question

---

## Instagram Caption Template

### Structure
```
{{visual_hook}} {{emoji_string}}

{{story_opener}}

{{personal_angle}}

{{value_delivery}}
{{#tips}}
{{tip_number}}. {{tip_content}} {{tip_emoji}}
{{/tips}}

{{personal_conclusion}}

{{engagement_cta}}

{{visual_suggestion}}

{{hashtags}}
```

### Variables
- `visual_hook`: Eye-catching opening line
- `emoji_string`: Relevant emojis (3-5)
- `story_opener`: Personal/narrative beginning
- `personal_angle`: Individual perspective
- `tips`: Actionable takeaways
- `engagement_cta`: Ask for comments/shares
- `visual_suggestion`: Image/video recommendation
- `hashtags`: Mix of niche and broad tags (20-30)

### Constraints
- 2200 character limit
- High emoji usage encouraged
- Personal/story tone
- Include visual content suggestion

---

## Platform-Specific Adaptations

### Tone Adjustments
- **Twitter**: Conversational, punchy, debate-friendly
- **LinkedIn**: Professional, authoritative, industry-focused  
- **Instagram**: Personal, visual, story-driven
- **Facebook**: Community-oriented, discussion-focused

### Hashtag Strategies
- **Twitter**: 2-4 trending/relevant tags
- **LinkedIn**: 5-10 industry-specific tags
- **Instagram**: 20-30 mix of niche and broad tags
- **Facebook**: 1-3 broad community tags

### Content Length
- **Twitter**: Multiple short chunks (threads)
- **LinkedIn**: Medium-form professional insights
- **Instagram**: Longer storytelling format
- **Facebook**: Community discussion starters

---

## Dynamic Template Selection

### Factors
- Blog post topic and industry
- Target audience demographics
- Historical performance data
- Current trending topics
- Brand voice guidelines

### Template Variations
- **Educational**: How-to, tips, tutorials
- **Thought Leadership**: Industry insights, predictions
- **Personal**: Behind-scenes, stories, experiences  
- **Promotional**: Product features, announcements
- **Interactive**: Questions, polls, challenges

---

## Template Customization Variables

### Brand Variables
- `brand_voice`: Casual, professional, authoritative, friendly
- `brand_personality`: Innovative, traditional, disruptive, supportive
- `industry_context`: Tech, marketing, healthcare, finance, etc.
- `target_audience`: Beginners, experts, decision-makers, practitioners

### Performance Variables
- `engagement_history`: Previous post performance data
- `optimal_timing`: Platform-specific best posting times  
- `trending_topics`: Current industry conversations
- `competitor_analysis`: What's working for similar accounts

---

*These templates serve as the foundation for automated content generation across platforms*