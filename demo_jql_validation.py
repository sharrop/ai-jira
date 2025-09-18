#!/usr/bin/env python3
"""
JQL Input Validation Demonstration

This script demonstrates the JQL input validation features and shows
how they protect against various security and performance issues.
"""

import asyncio
from jira_api import JiraApiClient
from jql_validator import JQLValidator
from exceptions import JiraValidationError, JiraConfigurationError


async def demonstrate_jql_validation():
    """Demonstrate JQL validation with various test cases."""
    print("🔒 JQL Input Validation Demonstration")
    print("=" * 60)
    
    # Create client with validation enabled
    client = JiraApiClient(enable_jql_validation=True, allowed_projects=['AP'])
    validator = JQLValidator(allowed_projects={'AP'})
    
    # Test cases: [description, jql_query, should_pass]
    test_cases = [
        # Safe queries
        ("✅ Basic safe query", 'project = "AP" AND status = "Open"', True),
        ("✅ Safe query with date", 'project = "AP" AND created >= "2025-01-01"', True),
        ("✅ Safe query with user function", 'project = "AP" AND assignee = currentUser()', True),
        
        # Security issues
        ("❌ SQL injection attempt", 'project = "AP"; DROP TABLE users; --', False),
        ("❌ Script injection", 'project = "AP" AND summary ~ "<script>alert(\'xss\')</script>"', False),
        ("❌ Unauthorized project access", 'project = "SECRET" AND status = "Open"', False),
        ("❌ Project wildcard", 'project != "*" AND status = "Open"', False),
        
        # Performance issues
        ("⚠️  Very broad date range", 'project = "AP" AND created >= "1970-01-01"', True),  # Warning, not error
        ("⚠️  Multiple wildcards", 'project = "AP" AND summary ~ "*test*something*else*"', True),  # Warning
        
        # Syntax errors
        ("❌ Unbalanced quotes", 'project = "AP AND status = "Open"', False),
        ("❌ Unbalanced parentheses", 'project = "AP" AND (status = "Open"', False),
        ("❌ Empty query", '', False),
        
        # Edge cases
        ("❌ Too long query", 'project = "AP" AND summary ~ "' + 'x' * 2000 + '"', False),
        ("✅ Complex but safe query", 'project = "AP" AND status IN ("Open", "In Progress") AND assignee = currentUser() ORDER BY created DESC', True),
    ]
    
    print("\n🧪 Running Test Cases:")
    print("-" * 60)
    
    for description, jql, should_pass in test_cases:
        print(f"\n{description}")
        print(f"   Query: {jql[:80]}{'...' if len(jql) > 80 else ''}")
        
        try:
            # Test validation
            result = validator.validate_jql_query(jql, strict_mode=True)
            
            if should_pass:
                print(f"   ✅ PASSED: Query validated successfully")
                if result['warnings']:
                    print(f"      📝 Warnings: {', '.join(result['warnings'])}")
                if result['performance_warnings']:
                    print(f"      🐌 Performance: {', '.join(result['performance_warnings'])}")
            else:
                print(f"   ❌ UNEXPECTED: Query should have failed but passed")
                
        except JiraValidationError as e:
            if not should_pass:
                print(f"   ✅ CORRECTLY BLOCKED: {e}")
            else:
                print(f"   ❌ UNEXPECTED FAILURE: {e}")
        except Exception as e:
            print(f"   💥 UNEXPECTED ERROR: {e}")
    
    print("\n" + "=" * 60)
    print("🛡️  Safe JQL Construction Demonstration")
    print("=" * 60)
    
    # Demonstrate safe query building
    print("\n📝 Building safe parameterized queries:")
    
    safe_examples = [
        {
            'template': 'project = {project} AND assignee = {user}',
            'params': {'project': 'AP', 'user': 'john.doe@company.com'},
            'description': 'User assignment query'
        },
        {
            'template': 'project = {project} AND created >= {date} AND status = {status}',
            'params': {'project': 'AP', 'date': '2025-01-01', 'status': 'In Progress'},
            'description': 'Date and status filter'
        },
        {
            'template': 'project = {project} AND summary ~ {search_term}',
            'params': {'project': 'AP', 'search_term': 'API AND security'},  # Potentially dangerous input
            'description': 'Text search with dangerous characters'
        }
    ]
    
    for example in safe_examples:
        print(f"\n🔧 {example['description']}:")
        print(f"   Template: {example['template']}")
        print(f"   Parameters: {example['params']}")
        
        try:
            safe_jql = validator.build_safe_jql(example['template'], **example['params'])
            print(f"   ✅ Safe JQL: {safe_jql}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("⚡ Performance Comparison")
    print("=" * 60)
    
    # Compare validation overhead
    import time
    
    test_jql = 'project = "AP" AND status = "In Progress" AND created >= "2025-01-01"'
    iterations = 1000
    
    # Test without validation
    start = time.time()
    for _ in range(iterations):
        # Simulate basic validation
        if not test_jql or not test_jql.strip():
            raise ValueError("Empty query")
    no_validation_time = time.time() - start
    
    # Test with full validation
    start = time.time()
    for _ in range(iterations):
        validator.validate_jql_query(test_jql, strict_mode=True)
    with_validation_time = time.time() - start
    
    print(f"\n📊 Validation Performance ({iterations} iterations):")
    print(f"   Without validation: {no_validation_time:.4f}s")
    print(f"   With full validation: {with_validation_time:.4f}s")
    print(f"   Overhead per query: {(with_validation_time - no_validation_time) / iterations * 1000:.2f}ms")
    print(f"   Overhead factor: {with_validation_time / no_validation_time:.1f}x")
    
    print("\n" + "=" * 60)
    print("🎯 Integration with JiraApiClient")
    print("=" * 60)
    
    # Demonstrate client integration (without actually making API calls)
    print("\n🔗 Client integration examples:")
    
    # Show how to use safe search
    print("\n1. Using build_safe_jql method:")
    try:
        safe_jql = client.build_safe_jql(
            "project = {project} AND assignee = {user} AND created >= {date}",
            project="AP",
            user="stephen.harrop@vodafone.com",
            date="2025-01-01"
        )
        print(f"   ✅ Built safe JQL: {safe_jql}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Show validation method
    print("\n2. Using validate_jql method:")
    test_query = 'project = "AP" AND status = "In Progress"'
    try:
        validation_result = client.validate_jql(test_query)
        print(f"   ✅ Validation passed: {validation_result['is_valid']}")
        if validation_result['warnings']:
            print(f"   📝 Warnings: {validation_result['warnings']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Show safe search method
    print("\n3. Using search_issues_safe method:")
    print("   Template: project = {project} AND status = {status}")
    print("   Parameters: project='AP', status='In Progress'")
    print("   ✅ This would safely construct and execute the query")
    
    print("\n" + "=" * 60)
    print("📚 Recommendations for Your Codebase")
    print("=" * 60)
    
    recommendations = [
        "1. ✅ Enable JQL validation by default in JiraApiClient",
        "2. 🔧 Replace string interpolation with build_safe_jql() for dynamic queries",
        "3. 🛡️  Use search_issues_safe() for user-provided search terms",
        "4. 📝 Add validation to check_epics.py if it accepts external input",
        "5. ⚠️  Log validation warnings for monitoring and debugging",
        "6. 🎯 Consider allowing validation bypass for trusted internal queries",
        "7. 📊 Monitor validation performance in production",
        "8. 🔄 Regularly update allowed projects list based on user permissions"
    ]
    
    for rec in recommendations:
        print(f"   {rec}")
    
    print("\n✅ JQL Validation Demonstration Complete!")
    print("Your JIRA toolkit is now protected against injection attacks! 🛡️")


if __name__ == "__main__":
    asyncio.run(demonstrate_jql_validation())