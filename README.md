# Pyhton Script to use when primary monitor has changed
- This happens when you are using DisplayLink Manager


1. Open /Users/your_user_here/.zshrc"
2. define the swapDisplay() function

swapDisplay() {
    local displayInfo=$(displayplacer list)
    python3 /Users/your_user_here/repositories/private_repos/swap_display/main.py "$displayInfo"
}
