import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [150, 200, 180, 220, 240, 210]
proj_sales = [140, 190, 170, 210, 230, 200]  # projected sales

# Create figure and axes with custom size
fig, ax = plt.subplots(figsize=(10, 6))  # 10x6 inches

# Plot actual sales
ax.plot(months, sales, color="green", marker='o', linestyle='--', linewidth=2, label='Actual Sales')

# Plot projected sales
ax.plot(months, proj_sales, color="orange", marker='^', linestyle='-.', linewidth=2, label='Projected Sales')

# Set axis limits
ax.set_ylim(100, 260)  # y-axis limits
ax.set_xlim(-0.5, len(months)-0.5)  # x-axis limits based on index range

# Customize ticks
ax.set_yticks(range(100, 261, 20))  # y ticks every 20 units
ax.set_xticks(range(len(months)))   # ticks at each month index
ax.set_xticklabels(months, rotation=45, color='blue')  # month labels rotated

# Minor ticks for y-axis
ax.minorticks_on()
ax.tick_params(axis='y', which='major', length=7, color='red')
ax.tick_params(axis='y', which='minor', length=4, color='pink')

# Title and labels with custom fonts and colors
ax.set_title("Monthly Sales Report", fontsize=18, color="navy", pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Sales ($)", fontsize=14)

# Grid style for major and minor ticks
ax.grid(which='major', linestyle=':', linewidth=0.8, color='gray')
ax.grid(which='minor', linestyle='--', linewidth=0.5, color='lightgray')

# Annotation example pointing to peak sales
max_idx = sales.index(max(sales))
ax.annotate('Peak Sales',
            xy=(max_idx, sales[max_idx]),
            xytext=(max_idx-1, sales[max_idx]+30),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='darkgreen')

# Legend
ax.legend(loc='upper left', fontsize=12)


# Tight layout for clean spacing
plt.tight_layout()

# Save figure before showing
plt.savefig("complete_sales_report.png", dpi=300, bbox_inches='tight')

# Show plot
plt.show()
