#!/usr/bin/env python3
import os
import json
import re
from datetime import datetime

class TokenAnalyzer:
    def __init__(self, memory_dir='/home/ubuntu/clawd/memory'):
        self.memory_dir = memory_dir
        self.session_tokens = {}
    
    def parse_session_logs(self):
        """
        Parse daily memory logs to extract token usage
        """
        for filename in os.listdir(self.memory_dir):
            if filename.endswith('.md'):
                full_path = os.path.join(self.memory_dir, filename)
                with open(full_path, 'r') as f:
                    content = f.read()
                    # Extract token usage markers (customize based on actual log format)
                    token_matches = re.findall(r'Tokens Used: (\d+)', content)
                    if token_matches:
                        self.session_tokens[filename] = [int(match) for match in token_matches]
    
    def analyze_token_patterns(self):
        """
        Analyze token usage patterns
        """
        results = {
            'total_sessions': len(self.session_tokens),
            'token_stats': {
                'min': float('inf'),
                'max': 0,
                'average': 0,
                'total': 0
            },
            'daily_breakdown': {}
        }
        
        for date, tokens in self.session_tokens.items():
            daily_total = sum(tokens)
            results['token_stats']['total'] += daily_total
            results['token_stats']['min'] = min(results['token_stats']['min'], daily_total)
            results['token_stats']['max'] = max(results['token_stats']['max'], daily_total)
            results['daily_breakdown'][date] = {
                'total_tokens': daily_total,
                'token_count': len(tokens)
            }
        
        if results['total_sessions'] > 0:
            results['token_stats']['average'] = results['token_stats']['total'] / results['total_sessions']
        
        return results
    
    def generate_report(self):
        """
        Generate a comprehensive token usage report
        """
        self.parse_session_logs()
        analysis = self.analyze_token_patterns()
        
        report_path = os.path.join(self.memory_dir, f'token_usage_report_{datetime.now().strftime("%Y-%m-%d")}.json')
        with open(report_path, 'w') as f:
            json.dump(analysis, f, indent=2)
        
        return report_path

def main():
    analyzer = TokenAnalyzer()
    report_location = analyzer.generate_report()
    print(f"Token usage report generated: {report_location}")

if __name__ == '__main__':
    main()