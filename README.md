# Optimal-NoC-Design
Project for Google Girl Hackathon 2024 - Silicon Engineering

**Project Name:** Optimal NoC Design (OptiNoC)

**Brief Summary of the Solution:**
As per the problem, the pseudocode used to measure average latency and bandwidth can be written as
```
Initialize read_latency_sum, write_latency_sum, total_reads, total_writes to 0
Initialize bandwidth_sum, total_transactions to 0
Initialize last_read_timestamp, last_write_timestamp to -1

For each entry in the interface monitor output:
    If TxnType is Read:
        If last_read_timestamp is not -1:
            read_latency_sum += current_timestamp - last_read_timestamp
            total_reads += 1
        last_read_timestamp = current_timestamp
    Else if TxnType is Write:
        If last_write_timestamp is not -1:
            write_latency_sum += current_timestamp - last_write_timestamp
            total_writes += 1
        last_write_timestamp = current_timestamp
    bandwidth_sum += size_of(Data)
    total_transactions += 1

Calculate average_read_latency = read_latency_sum / total_reads
Calculate average_write_latency = write_latency_sum / total_writes
Calculate average_bandwidth = bandwidth_sum / total_transactions
```

**Reinforcement Learning Framework Used for OptiNoC:**
- States/Behaviors: The state space will include the buffer occupancy levels, arbitration rates, current power consumption, and current latency and bandwidth measurements.
- Actions: Possible actions will involve adjusting buffer sizes, arbitration weights, and throttling frequency.
- Rewards: The reward function will be designed to maximize bandwidth and minimize latency, while keeping buffer occupancy at the desired level and throttling within the specified limit.

**Recommended RL Algorithm:** An Actor-Critic algorithm would be suitable as it can handle the continuous state space and provide a balance between value-based and policy-based methods, which is beneficial for fine-tuning the NOC parameters to achieve the desired performance metrics.
