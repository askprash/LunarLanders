# Publish architecture walkthrough as standalone HTML

The interactive architecture walkthrough will be built first as a standalone static HTML page, separate from `lunar_redteam_demo.html`. It should be polished enough for academic/domain-expert onboarding and should not be entangled with the product demo UI until the walkthrough stabilizes.

The page should be published by a GitHub Actions workflow, ideally through GitHub Pages or a generated static artifact, so collaborators and reviewers can open a stable web page without running local tooling. This reinforces the expert-handoff goal: make the pipeline understandable through a shareable, clickable walkthrough before asking reviewers to inspect the whole repository.
